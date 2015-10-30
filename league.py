###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect

class League (object):
    def __init__(self, league_name=None, league_country=None, league_team_number=None,
                league_start_date=None, league_id=None):
        self.id = league_id
        self.name = league_name
        self.start_date = league_start_date
        self.country = league_country
        self.team_count = league_team_number

    def get_league_by_id(self, get_id=None):
        pass

    def add_to_db(self):
        pass

    def delete_from_db(self):
        pass

    def update_db(self):
        pass
