

import heapq


# FUNCTION TO PERFORM DIJKSTRA'S ALGORITHM AND RETURN SHORTEST PATH AND DISTANCE



def dijkstra(network, origin, destination):



    # INITIALIZE DISTANCE TO ALL NODES AS INFINITY



    cost_tracker = {vertex: float('inf') for vertex in network}
    cost_tracker[origin] = 0



    # INITIALIZE PREVIOUS NODE TRACKER FOR PATH RECONSTRUCTION



    backtrack = {vertex: None for vertex in network}



    # CREATE PRIORITY QUEUE FOR UNVISITED NODES



    to_visit = [(0, origin)]



    # PROCESS NODES UNTIL THE QUEUE IS EMPTY


    while to_visit:
        current_cost, current_vertex = heapq.heappop(to_visit)



        # IF TARGET IS REACHED, REBUILD THE PATH



        if current_vertex == destination:
            route = []
            while current_vertex is not None:
                route.append(current_vertex)
                current_vertex = backtrack[current_vertex]
            route.reverse()
            return cost_tracker[destination], route
        


        # UPDATE DISTANCES TO NEIGHBORS IF SHORTER PATH IS FOUND



        for neighbor_node, edge_cost in network[current_vertex].items():
            alt_path = current_cost + edge_cost
            if alt_path < cost_tracker[neighbor_node]:
                cost_tracker[neighbor_node] = alt_path
                backtrack[neighbor_node] = current_vertex
                heapq.heappush(to_visit, (alt_path, neighbor_node))



    # RETURN NONE IF TARGET IS UNREACHABLE



    return None



# SAMPLE GRAPH FOR TESTING PURPOSES



route_map = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 3},
    'D': {'B': 1, 'C': 4, 'E': 1, 'F': 2},
    'E': {'C': 3, 'D': 1, 'F': 1},
    'F': {'D': 2, 'E': 1, 'G': 3},
    'G': {'F': 3}
}



# RUN TEST CASE FROM A TO F



res1, path1 = dijkstra(route_map, 'A', 'F')
print("SHORTEST PATH FROM A TO F:", path1, "WITH DISTANCE", res1)



# RUN TEST CASE FROM B TO G



res2, path2 = dijkstra(route_map, 'B', 'G')
print("SHORTEST PATH FROM B TO G:", path2, "WITH DISTANCE", res2)
