###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect


class Popularity(object):
    def __init__(self, team=None, match=None, player=None, supporters=None, popularity_id=None):
        self.id = popularity_id
        self.team = team
        self.match = match
        self.player = player
        self.supporters = supporters

    def get_popularity_by_id(self, get_id=None):
        conn = db_connect()
        cursor = conn.cursor()

        if get_id is not None:
            query = """SELECT * FROM popularity
                                JOIN team ON popularity.team_name = team.team_id
                                JOIN matches ON popularity.most_popular_match = matches.match_id
                                JOIN person ON popularity.most_popular_player = person.person_id
                                WHERE popularity_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                conn.commit()
            except conn.Error as error:
                print(error)
                conn.rollback()

            data = cursor.fetchone()
            print(data)
            if data is not None:
                self.id = data[0]
                self.team = data[6]
                self.match = data[8]
                self.player = data[18]
                self.supporters = data[4]

                cursor.close()
                conn.close()

                return self

            else:
                cursor.close()
                conn.close()

                return None

        else:
            query = """SELECT * FROM popularity
                                JOIN team AS team1 ON popularity.team_name = team1.team_id
                                JOIN matches ON popularity.most_popular_match = matches.match_id
                                JOIN team AS team2 ON matches.match_team_1 = team2.team_id
                                JOIN team AS team3 ON matches.match_team_2 = team3.team_id
                                JOIN person ON popularity.most_popular_player = person.person_id"""
            try:
                cursor.execute(query, (get_id,))
                conn.commit()
            except conn.Error as error:
                print(error)
                conn.rollback()

            data_array = []
            data = cursor.fetchall()
            print(data)
            for popularity in data:
                data_array.append(
                    {
                        'id': popularity[0],
                        'team': popularity[6],
                        'match': popularity[18] + "-" + popularity[21],
                        'player': popularity[24],
                        'supporters':  popularity[4]
                    }
                )

            print(data_array)
            cursor.close()
            conn.close()

            return data_array

    def add_to_db(self):
        conn = db_connect()
        cursor = conn.cursor()

        query = """INSERT INTO popularity(team_name, most_popular_match, most_popular_player, supporters)
                            VALUES (%s, %s, %s, %s)"""

        try:
            cursor.execute(query, (self.team, self.match, self.player, self.supporters))
            conn.commit()
            status = True

        except conn.Error as error:
            print(error)
            conn.rollback()
            status = False

        cursor.close()
        conn.close()
        return status

    def delete_from_db(self):
        conn = db_connect()
        cursor = conn.cursor()

        query = """DELETE FROM popularity WHERE popularity_id = %s"""

        try:
            cursor.execute(query, (self.id, ))
            conn.commit()
            status = True

        except conn.Error as error:
            print(error)
            conn.rollback()
            status = False

        cursor.close()
        conn.close()
        return status

    def update_db(self):
        conn = db_connect()
        cursor = conn.cursor()
        status = False

        query = """UPDATE popularity
                   SET team_name=%s, most_popular_match=%s, most_popular_player=%s, supporters=%s
                   WHERE popularity_id=%s"""

        try:
            cursor.execute(query, (self.team, self.match, self.player, self.supporters, self.id))
            conn.commit()
            # print(cursor.mogrify(query, (self.given_date, self.person, type_id, self.id)))
            status = True
        except conn.Error as error:
            print(error)
            conn.rollback()
            status = False
        finally:
            cursor.close()
            conn.close()
            return status
