###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect


class Team_stat(object):
    def __init__(self, team_stat_name=None, team_stat_run=None, team_stat_hit=None,
                 team_stat_save=None, team_stat_win=None, team_stat_draw=None,
                 team_stat_loss=None, team_stat_id=None):
        self.id = team_stat_id
        self.name = team_stat_name
        self.run = team_stat_run
        self.hit = team_stat_hit
        self.save = team_stat_save
        self.win = team_stat_win
        self.draw = team_stat_draw
        self.loss = team_stat_loss

    def get_team_stat_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            statement = """SELECT team_stat.team_stat_id, team_stat.team_stat_name, team_stat.team_stat_run,
                            team_stat.team_stat_hit, team_stat.team_stat_save, team_stat.team_stat_win,
                            team_stat.team_stat_draw, team_stat.team_stat_loss
                            FROM team_stat
                            WHERE team_stat_id = %s"""
            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            data = cursor.fetchone()
            if data is not None:
                self.id = data[0]
                self.name = data[1]
                self.run = data[2]
                self.hit = data[3]
                self.save = data[4]
                self.win = data[5]
                self.draw = data[6]
                self.loss = data[7]

                cursor.close()
                connection.close()
                return self
            else:
                cursor.close()
                connection.close()
                return None

        else:
            statement = """SELECT team_stat.team_stat_id, team_stat.team_stat_name, team_stat.team_stat_run,
                            team_stat.team_stat_hit, team_stat.team_stat_save, team_stat.team_stat_win,
                            team_stat.team_stat_draw, team_stat.team_stat_loss,
                            team.team_id, team.team_name
                            FROM team_stat
                            LEFT OUTER JOIN team ON team.team_id = team_stat.team_stat_name"""
            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            team_stat_array = []
            data = cursor.fetchall()
            for team_stat in data:
                team_stat_array.append(
                    {
                        'id': team_stat[0],
                        'name': team_stat[9],
                        'run': team_stat[2],
                        'hit': team_stat[3],
                        'save': team_stat[4],
                        'win': team_stat[5],
                        'draw': team_stat[6],
                        'loss': team_stat[7]
                    }
                )
            #print(team_stat_array)
            cursor.close()
            connection.close()
            return team_stat_array

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        new_team = None

        select_team = """SELECT team_id FROM team WHERE team_name = %s"""


        count_win1 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_1
                    WHERE (matches.match_team1_score > matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_win2 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_2
                    WHERE (matches.match_team1_score < matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_draw1 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_1
                    WHERE (matches.match_team1_score = matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_draw2 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_2
                    WHERE (matches.match_team1_score = matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_loss1 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_1
                    WHERE (matches.match_team1_score < matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_loss2 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_2
                    WHERE (matches.match_team1_score > matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        statement = """INSERT INTO team_stat (team_stat_name, team_stat_run,
                        team_stat_hit, team_stat_save, team_stat_win,
                        team_stat_draw, team_stat_loss )
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        count_matches = """SELECT count(match_id) FROM matches"""

        try:
            cursor.execute(select_team, (self.name,))
            connection.commit()
            new_name = cursor.fetchone()

            cursor.execute(count_win1, (self.name,))
            connection.commit()
            total_win1 = cursor.fetchone()
            if total_win1 is None:
                total_win1 = (0,)

            cursor.execute(count_win2, (self.name,))
            connection.commit()
            total_win2 = cursor.fetchone()
            if total_win2 is None:
                total_win2 = (0,)

            cursor.execute(count_draw1, (self.name,))
            connection.commit()
            total_draw1 = cursor.fetchone()
            if total_draw1 is None:
                total_draw1 = (0,)

            cursor.execute(count_draw2, (self.name,))
            connection.commit()
            total_draw2 = cursor.fetchone()
            if total_draw2 is None:
                total_draw2 = (0,)

            cursor.execute(count_loss1, (self.name,))
            connection.commit()
            total_loss1 = cursor.fetchone()
            if total_loss1 is None:
                total_loss1 = (0,)

            cursor.execute(count_loss2, (self.name,))
            connection.commit()
            total_loss2 = cursor.fetchone()
            if total_loss2 is None:
                total_loss2 = (0,)

            cursor.execute(statement, (new_name, self.hit, self.run, self.save,
                                       total_win1[0]+total_win2[0], total_draw1[0]+total_draw2[0],
                                       total_loss1[0]+total_loss2[0]))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status


    def delete_from_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        statement = """DELETE FROM team_stat WHERE team_stat_id = %s"""

        try:
            cursor.execute(statement, (self.id,))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

    def update_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        new_name = None

        select_team = """SELECT team_id FROM team WHERE team_name = %s"""

        count_win1 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_1
                    WHERE (matches.match_team1_score > matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_win2 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_2
                    WHERE (matches.match_team1_score < matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_draw1 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_1
                    WHERE (matches.match_team1_score = matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_draw2 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_2
                    WHERE (matches.match_team1_score = matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_loss1 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_1
                    WHERE (matches.match_team1_score < matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_loss2 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_2
                    WHERE (matches.match_team1_score > matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

        count_matches = """SELECT count(match_id) FROM matches"""

        statement = """UPDATE team_stat
                       SET team_stat_name=%s, team_stat_run=%s, team_stat_hit=%s, team_stat_save=%s,
                       team_stat_win=%s, team_stat_draw=%s, team_stat_loss=%s
                       WHERE team_stat_id=%s"""

        try:
            cursor.execute(select_team, (self.name,))
            connection.commit()
            new_name = cursor.fetchone()

            cursor.execute(count_win1, (self.name,))
            connection.commit()
            total_win1 = cursor.fetchone()
            if total_win1 is None:
                total_win1 = (0,)

            cursor.execute(count_win2, (self.name,))
            connection.commit()
            total_win2 = cursor.fetchone()
            if total_win2 is None:
                total_win2 = (0,)

            cursor.execute(count_draw1, (self.name,))
            connection.commit()
            total_draw1 = cursor.fetchone()
            if total_draw1 is None:
                total_draw1 = (0,)

            cursor.execute(count_draw2, (self.name,))
            connection.commit()
            total_draw2 = cursor.fetchone()
            if total_draw2 is None:
                total_draw2 = (0,)

            cursor.execute(count_loss1, (self.name,))
            connection.commit()
            total_loss1 = cursor.fetchone()
            if total_loss1 is None:
                total_loss1 = (0,)

            cursor.execute(count_loss2, (self.name,))
            connection.commit()
            total_loss2 = cursor.fetchone()
            if total_loss2 is None:
                total_loss2 = (0,)

            cursor.execute(statement, (new_name, self.hit, self.run, self.save, total_win1[0]+total_win2[0], total_draw1[0]+total_draw2[0],
                                       total_loss1[0]+total_loss2[0], self.id))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status
