import googlemaps
import concurrent.futures
from datetime import datetime as dt
from models import Googlemaps, GoogleResponse,GeocodeResponse
from geopy.geocoders import Nominatim
from py_geohash_any import geohash as gh
from itertools import permutations,combinations



def initialize_google():
    g = Googlemaps()
    apiKey = g.API_KEY
    client = googlemaps.Client(apiKey)
    return client,g


def distance_matrix(location, departureTime,home_address):
    client,g = initialize_google()
    matrix = client.distance_matrix(origins=home_address, destinations=location,
                                        mode=g.MODE,
                                        language=g.LANG,
                                        departure_time=departureTime,
                                        traffic_model=g.TRAFFIC_MOD,
                                        units=g.UNITS)
    return matrix

def pooling(addresses,date_index,home_address):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_matrix = {executor.submit(distance_matrix, address, date_index,home_address): address for address
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


def loc_lookup(address,reverse=False):
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    if reverse==False:
        location = geolocator.geocode(str(address))
        return (location.latitude,location.longitude)
    else:
        location = geolocator.reverse(address)
        return location.address

def geohash(data,precision):
    lat = float(data[0])
    long = float(data[1])
    return gh.encode(lat,long,precision)

def decoder(x):
    a = gh.decode(x)
    return [a['lat'],a['lon']]

def neighbors(data,precision,range):
    hash = geohash(data,precision)
    n = list(gh.neighbors(hash,range).values())
    l = [decoder(x) for x in n]
    return l

def combo(l):
    a = list(combinations(l,2))
    return a

def reverse_lookup(x,y):
    client, g = initialize_google()
    destination = client.reverse_geocode((x,y))
    return GeocodeResponse(destination[0]).formatted_address

def build_destinations(combo):
    dm = distance_matrix
    date_index = dt.now()
    for x in combo:
        depatureAddress = tuple(x[1])
        depatureAddress_lat = depatureAddress[0]
        depatureAddress_long = depatureAddress[1]
        home_address = tuple(x[0])
        home_address_lat = home_address[0]
        home_address_long = home_address[1]
        distance = GoogleResponse(dm(depatureAddress,date_index,home_address))
        print ({'departure':reverse_lookup(depatureAddress_lat,depatureAddress_long),
                'home':reverse_lookup(home_address_lat,home_address_long),
                'distance':distance.distance_value})

