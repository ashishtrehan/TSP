from util import distance_matrix
from datetime import datetime as dt
from util import loc_lookup,neighbors,combo,pooling,reverse_lookup,build_destinations
from py_geohash_any import geohash as gh





b = loc_lookup("1673 McLendon Avenue Northeast, Atlanta, GA",False)
print (b)
a = combo(neighbors(b,8,4))
print (reverse_lookup(33.765449, -84.334487))
build_destinations(a)
# date_index = dt.now()
#
# print (distance_matrix(b,date_index,'1 AMB Drive Northwest, Atlanta, GA 30313'))

