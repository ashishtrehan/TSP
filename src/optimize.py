from util import distance_matrix
from datetime import datetime as dt
from util import loc_lookup,neighbors


b = loc_lookup("1673 McLendon Avenue Northeast, Atlanta, GA",False)
print (b)

print (neighbors(b,8,8))

date_index = dt.now()

print (distance_matrix(b,date_index,'1 AMB Drive Northwest, Atlanta, GA 30313'))

