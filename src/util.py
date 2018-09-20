import googlemaps
import concurrent.futures
import numpy as np
import json
import datetime
from Util import date_index,obtain_concierge_trips
from classes import Googlemaps, Request, Trips, GoogleResponse


def initialize_google():
    g = Googlemaps()
    apiKey = g.API_KEY
    client = googlemaps.Client(apiKey)
    return client,g


def distance_matrix(flipLocation, departureTime):
    client,g = initialize_google()
    matrix = client.distance_matrix(origins=g.HQ, destinations=flipLocation,
                                        mode=g.MODE,
                                        language=g.LANG,
                                        departure_time=departureTime,
                                        traffic_model=g.TRAFFIC_MOD,
                                        units=g.UNITS)
    return matrix

def pooling(addresses,date_index):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_matrix = {executor.submit(distance_matrix, address, date_index()): address for address
                            in addresses}
        a = []
        for future in concurrent.futures.as_completed(future_to_matrix):
            address = future_to_matrix[future]
            try:
                request = future.result()
                a.append({'response':GoogleResponse(request)})
            except Exception as exc:
                print('generated an exception: {0}'.format(address, exc))
            else:
                print('{0} response is {1} bytes'.format(address, len(request)))
        return a