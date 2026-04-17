"""
Logistics Routing Optimizer
Solves the basics of the Traveling Salesperson Problem (TSP) using a Nearest Neighbor Heuristic.
"""
import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def nearest_neighbor_tsp(nodes):
    """
    Finds a suboptimal tour passing through all nodes exactly once using nearest neighbor.
    nodes: dictionary of {node_id: (x, y)}
    """
    if not nodes:
        return [], 0.0

    unvisited = list(nodes.keys())
    current_node = unvisited[0]
    tour = [current_node]
    unvisited.remove(current_node)
    
    total_distance = 0.0
    
    while unvisited:
        next_node = None
        min_dist = float('inf')
        
        for candidate in unvisited:
            dist = calculate_distance(nodes[current_node], nodes[candidate])
            if dist < min_dist:
                min_dist = dist
                next_node = candidate
                
        tour.append(next_node)
        total_distance += min_dist
        unvisited.remove(next_node)
        current_node = next_node
        
    # Return to start node to complete the cycle
    total_distance += calculate_distance(nodes[current_node], nodes[tour[0]])
    tour.append(tour[0])
    
    return tour, round(total_distance, 2)

if __name__ == "__main__":
    locations = {
        'Depot': (0, 0),
        'Customer A': (2, 4),
        'Customer B': (5, 2),
        'Customer C': (7, 5),
        'Customer D': (1, 8)
    }
    
    optimized_tour, total_dist = nearest_neighbor_tsp(locations)
    print(f"Optimized Route: {' -> '.join(optimized_tour)}")
    print(f"Total Distance: {total_dist} units")
