###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect

class Sponsorship(object):
    def __init__(self, sponsor_name=None, sponshorship_start_date=None, sponsorship_end_date=None,
                 sponshorship_type=None, sponsor_id=None):
        self.id = sponsor_id
        self.name = sponsor_name
        self.start_date = sponsorship_start_date
        self.end_date = sponsorship_end_place
        self.type = sponsorhip_type

    def get_sponsor_by_id(self, get_id=None):
        pass

    def add_to_db(self):
        pass

    def delete_from_db(self):
        pass

    def update_db(self):
        pass



class SponsorshipType(object):
    def __init__(self, sponsorship_type_name=None, sponsorship_type_id=None):
        self.id = sponsorship_type_id
        self.type = sponsorship_type_name

    def get_person_type(self, type_id=None):
        pass

    def add_to_db(self):
        pass