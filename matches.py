###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################
from config import db_connect


class Match (object):
    def __init__(self, match_team_1=None, match_team_2=None, match_league=None,
                 match_stadium=None, match_referee=None, match_date=None,
                 match_team1_score=None, match_team2_score=None, match_id=None):
        self.id = match_id
        self.name1 = match_team_1
        self.name2 = match_team_2
        self.league = match_league
        self.stadium = match_stadium
        self.referee = match_referee
        self.date = match_date
        self.score1 = match_team1_score
        self.score2 = match_team2_score

    def get_match_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            query = """SELECT * FROM matches
                                JOIN team ON matches.match_team_1 = team.team_id
                                JOIN team AS t ON matches.match_team_2 = t.team_id
                                JOIN league ON matches.match_league = league.league_id
                                JOIN stadium ON matches.match_stadium = stadium.stadium_id
                                JOIN person ON matches.match_referee = person.person_id
                                WHERE match_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()

                data = cursor.fetchone()
                if data is not None:
                    self.id = data[0]
                    self.name1 = data[10]
                    self.name2 = data[13]
                    self.league = data[16]
                    self.stadium = data[20]
                    self.referee = data[25]
                    self.score1 = data[7]
                    self.score2 = data[8]
                    self.date = data[6]

                    cursor.close()
                    connection.close()
                    return self

                else:
                    cursor.close()
                    connection.close()
                    return None

            except connection.Error as error:
                print(error)
                connection.rollback()

        else:
            query = """SELECT * FROM matches
                                JOIN team ON matches.match_team_1 = team.team_id
                                JOIN team AS t ON matches.match_team_2 = t.team_id
                                JOIN league ON matches.match_league = league.league_id
                                JOIN stadium ON matches.match_stadium = stadium.stadium_id
                                JOIN person ON matches.match_referee = person.person_id"""
            try:
                cursor.execute(query)
                connection.commit()

                array = []
                data = cursor.fetchall()
                for match in data:
                    array.append(
                        {
                            'id': match[0],
                            'name1': match[10],
                            'name2': match[13],
                            'league': match[16],
                            'stadium': match[20],
                            'referee': match[25],
                            'score1': match[7],
                            'score2': match[8],
                            'date': match[6].strftime("%d %B %Y")
                        }
                    )

                cursor.close()
                connection.close()
                return array

            except connection.Error as error:
                print(error)
                connection.rollback()

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        query_team = """SELECT team_id FROM team
                                WHERE team_name = %s"""

        query_league = """SELECT league_id FROM league
                                WHERE league_name = %s"""

        query_stadium = """SELECT stadium_id FROM stadium
                                WHERE stadium_name = %s"""

        query_referee = """SELECT person_id FROM person
                                WHERE person_name = %s"""

        query = """INSERT INTO matches (match_team_1, match_team_2, match_league,
                                        match_stadium, match_referee, match_date,
                                        match_team1_score, match_team2_score)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        try:
            cursor.execute(query_team, (self.name1,))
            connection.commit()
            team1_id = cursor.fetchone()

            cursor.execute(query_team, (self.name2,))
            connection.commit()
            team2_id = cursor.fetchone()

            cursor.execute(query_league, (self.league,))
            connection.commit()
            league_id = cursor.fetchone()

            cursor.execute(query_stadium, (self.stadium,))
            connection.commit()
            stadium_id = cursor.fetchone()

            cursor.execute(query_referee, (self.referee,))
            connection.commit()
            referee_id = cursor.fetchone()

            cursor.execute(query, (team1_id, team2_id, league_id, stadium_id,
                                   referee_id, self.date, self.score1, self.score2,))
            connection.commit()
            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

    def delete_from_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        query = """DELETE FROM matches WHERE match_id = %s"""

        try:
            cursor.execute(query, (self.id, ))
            connection.commit()
            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

    def update_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        query_team = """SELECT team_id FROM team
                                WHERE team_name = %s"""

        query_league = """SELECT league_id FROM league
                                WHERE league_name = %s"""

        query_stadium = """SELECT stadium_id FROM stadium
                                WHERE stadium_name = %s"""

        query_referee = """SELECT person_id FROM person
                                WHERE person_name = %s"""

        query = """UPDATE matches
                   SET match_team_1=%s, match_team_2=%s, match_league=%s,
                            match_stadium=%s, match_referee=%s, match_date=%s,
                            match_team1_score=%s, match_team2_score=%s
                   WHERE match_id=%s"""

        try:
            cursor.execute(query_team, (self.name1,))
            connection.commit()
            team1_id = cursor.fetchone()

            cursor.execute(query_team, (self.name2,))
            connection.commit()
            team2_id = cursor.fetchone()

            cursor.execute(query_league, (self.league,))
            connection.commit()
            league_id = cursor.fetchone()

            cursor.execute(query_stadium, (self.stadium,))
            connection.commit()
            stadium_id = cursor.fetchone()

            cursor.execute(query_referee, (self.referee,))
            connection.commit()
            referee_id = cursor.fetchone()

            cursor.execute(query, (team1_id, team2_id, league_id, stadium_id,
                                   referee_id, self.date, self.score1, self.score2, self.id,))
            connection.commit()
            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

    @staticmethod
    def home_stats():
        connection = db_connect()
        cursor = connection.cursor()

        query_home = """SELECT team_name AS Team, COUNT(match_id) AS home_played,
                          COUNT(case when(match_team1_score > match_team2_score) then 1 else null end) AS home_wins,
                          COUNT(case when(match_team1_score < match_team2_score) then 1 else null end) AS home_loses,
                          COUNT(case when(match_team1_score = match_team2_score) then 1 else null end) AS home_draw,
                          (3*COUNT(case when(match_team1_score > match_team2_score) then 1 else null end)+
                          COUNT(case when(match_team1_score = match_team2_score) then 1 else null end)) AS home_points,
                          league_name
                            FROM team
                          JOIN matches ON team_id = match_team_1
                          JOIN league ON match_league = league_id
                          GROUP BY team_id, league_name
                          ORDER BY home_points DESC"""

        try:
            cursor.execute(query_home)
            connection.commit()

            array = []
            data = cursor.fetchall()
            for x in data:
                array.append(
                    {
                        'team': x[0],
                        'home_played': x[1],
                        'home_wins': x[2],
                        'home_loses': x[3],
                        'home_draw': x[4],
                        'home_points': x[5],
                        'league': x[6]
                    }
                )

            cursor.close()
            connection.close()
            return array

        except connection.Error as error:
            print(error)
            connection.rollback()

    @staticmethod
    def away_stats():
        connection = db_connect()
        cursor = connection.cursor()

        query_away = """SELECT team_name AS Team, COUNT(match_id) AS away_played,
                          COUNT(case when(match_team2_score > match_team1_score) then 1 else null end) AS away_wins,
                          COUNT(case when(match_team2_score < match_team1_score) then 1 else null end) AS away_loses,
                          COUNT(case when(match_team1_score = match_team2_score) then 1 else null end) AS away_draw,
                          (3*COUNT(case when(match_team2_score > match_team1_score) then 1 else null end)+
                          COUNT(case when(match_team1_score = match_team2_score) then 1 else null end)) AS away_points,
                          league_name
                            FROM team
                          JOIN matches ON team_id = match_team_2
                          JOIN league ON match_league = league_id
                          GROUP BY team_id, league_name
                          ORDER BY away_points DESC"""

        try:
            cursor.execute(query_away)
            connection.commit()

            array = []
            data = cursor.fetchall()
            for x in data:
                array.append(
                    {
                        'team': x[0],
                        'away_played': x[1],
                        'away_wins': x[2],
                        'away_loses': x[3],
                        'away_draw': x[4],
                        'away_points': x[5],
                        'league': x[6]
                    }
                )

            cursor.close()
            connection.close()
            return array

        except connection.Error as error:
            print(error)
            connection.rollback()

