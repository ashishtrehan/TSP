import os
import parameters


class Googlemaps(object):
    def __init__(self):
        self.API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
        self.MODE = 'driving'
        self.LANG = 'en-US'
        self.TRAFFIC_MOD = 'best_guess'
        self.UNITS = 'imperial'


class GoogleResponse(object):
    def __init__(self,dict):
        self.destination_address = dict.get('destination_addresses')
        self.origin_address = dict.get('origin_addresses')
        self.rows = dict.get('rows')
        self.elements = self.rows[0]['elements'][0]
        self.distance_text = self.elements.get('distance').get('text')
        self.distance_value = self.elements.get('distance').get('value')
        self.duration_text = self.elements.get('duration').get('text')
        self.duration_value = self.elements.get('duration').get('value')
        self.duration_traffic_text = self.elements.get('duration_in_traffic').get('text')
        self.duration_traffic_value = self.elements.get('duration_in_traffic').get('value')





