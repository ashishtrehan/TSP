from util import distance_matrix
from datetime import datetime as dt
from util import loc_lookup,neighbors,combo,pooling,reverse_lookup
from py_geohash_any import geohash as gh
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="specify_your_app_name_here")


b = loc_lookup("1673 McLendon Avenue Northeast, Atlanta, GA",False)
print (b)
print (combo(neighbors(b,8,6)))
print (gh.decode('ZSAAO54u'))
print (geolocator.reverse("33.764768, -84.332588"))
print (reverse_lookup(33.765449, -84.334487))
# date_index = dt.now()
#
# print (distance_matrix(b,date_index,'1 AMB Drive Northwest, Atlanta, GA 30313'))

