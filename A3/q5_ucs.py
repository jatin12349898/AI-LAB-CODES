all_path_cost = {}

def uniform_cost_search(graph, start, goal, current_cost=0):
    
    current_node = start[-1]
    if current_node == goal:
        all_path_cost["".join(start)] = current_cost
        return  

    for neighbor, cost in graph[current_node].items():
        new_path = start + [neighbor]
        new_cost = current_cost + cost
        uniform_cost_search(graph, new_path, goal, new_cost)

def optimal_path():
    min_cost = min(all_path_cost.values())
    optimal_paths = []

    for path, cost in all_path_cost.items():
        if cost == min_cost:
            optimal_paths.append((path, cost))
    
    for path, cost in optimal_paths:
        print(f"Optimal path: {path} with cost: {cost}")

def main():

    graph = {
        'S': {'A': 1, 'B': 5, 'C': 15},
        'A': {'G': 10},
        'B': {'G': 5},
        'C': {'G': 1},
    }

    uniform_cost_search(graph, ['S'], 'G')

    print("All paths and their costs:")
    for path, cost in all_path_cost.items():
        print(f"{path}: {cost}")

    optimal_path()

main()
