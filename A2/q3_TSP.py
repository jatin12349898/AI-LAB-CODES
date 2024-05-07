def next_city(graph):
    visited_cities = []
    travel_order = []

    while True:
        start_city = input("Enter starting city: ")
        if start_city == 'q':# q is quit command
            exit()
        elif start_city in graph:
            break
        else:
            print(f"Invalid city '{start_city}'. Please choose from: {', '.join(graph.keys())}")

    visited_cities.append(start_city)
    travel_order.append(start_city)
    current_city = start_city
    while len(visited_cities) != len(graph):
        nearest_city = None
        min_distance = float('inf')# inf is infinity

        for city, distance in graph[current_city].items():
            if city not in visited_cities and distance < min_distance:
                min_distance = distance
                nearest_city = city
                
        visited_cities.append(nearest_city)
        travel_order.append(nearest_city)
        current_city = nearest_city

    travel_order.append(start_city)
    return travel_order

my_graph = {
    '1': {'2': 10, '3': 15, '4': 20}, 
    '2': {'1': 10, '3': 35, '4': 25},
    '3': {'1': 15, '2': 35, '4': 30},
    '4': {'1': 20, '2': 25, '3': 30}
}

path = next_city(my_graph)
total_travel_cost = 0

for i in range(len(path) - 1):
    city1 = path[i]
    city2 = path[i+1]
    total_travel_cost += my_graph[city1][city2]
    
print(f"Travel Path: {' -> '.join(path)}")
print(f"Total Travel Cost: {total_travel_cost}")

