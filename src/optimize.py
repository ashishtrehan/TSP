from util import build_matrix
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2



matrix = build_matrix(10,10)
tsp_size = matrix.shape[0]
city_names = [1,2,3,4,5,6,7,8,9,10]
num_routes = 1
depot = 0

#if tsp_size > 0:
routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
# Create the distance callback.
routing.SetArcCostEvaluatorOfAllVehicles(matrix)
# Solve the problem.
assignment = routing.SolveWithParameters(search_parameters)
if assignment:
    print ("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")

    route_number = 0
    index = routing.Start(route_number) # Index of the variable for the starting node.
    route = ''
    while not routing.IsEnd(index):
        # Convert variable indices to node indices in the displayed route.
        route += str(city_names[routing.IndexToNode(index)]) + ' -> '
        index = assignment.Value(routing.NextVar(index))
        route += str(city_names[routing.IndexToNode(index)])
        print ("Route:\n\n" + route)
    else:
        print('No solution found.')



