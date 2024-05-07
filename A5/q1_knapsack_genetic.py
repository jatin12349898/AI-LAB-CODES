
initial_population = ["1111","1000","1010","1001"]

items = {
    'A': {'weight': 45, 'value': 3},
    'B': {'weight': 40, 'value': 5},
    'C': {'weight': 50, 'value': 8},
    'D': {'weight': 90, 'value': 10}
}

max_weight = 100
mutation_order = [3,2,1,0]

def fitness_value(chromosome):
    total_weight = 0
    total_value = 0
    for i,j in enumerate(chromosome):
        if j == '1':
            key = list(items.keys())[i]
            total_weight += items[key]['weight']
            total_value += items[key]['value']
    if total_weight <= max_weight:
        fitness = total_value
    else:
        fitness = 0
    return total_weight, total_value, fitness

def crossover(parent1,parent2):
    crossover_point = len(parent1)//2
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(chromosome, pos):
    mut_chromosome = list(chromosome)
    if chromosome[pos] == '0':
        mut_chromosome[pos] = '1'
    else:
        mut_chromosome[pos] = '0'
        
    return "".join(mut_chromosome)

def get(entry):
    return entry[1]

def genetic(initial_population, mutation_order, crossover, mutation ):
    population = initial_population
    
    for i in range(10):
        population_fitness = [(chromosome, fitness_value(chromosome)[2]) for chromosome in population]
        population_fitness.sort(key=get, reverse=True)
        
        top_two = [entry[0] for entry in population_fitness[:2]]
        
        last_two = [entry[0] for entry in population_fitness[2:]]
        
        child1, child2 = crossover(last_two[0], last_two[1])
        
        mut_pos = mutation_order[(i)%len(mutation_order)]
        
        child1 = mutation(child1, mut_pos)
        
        population = top_two + [child1, child2]

        print(f"Iteration {i+1}: ")
        for chromosome in population:
            _, _, fitness = fitness_value(chromosome)
            print(f"Chromosome : {chromosome}, Fitness : {fitness}")
        print("\n")
    
    return population

final_population = genetic(initial_population, mutation_order, crossover, mutation)

print("\nFinal population : ")
for chromosome in final_population:
    _, _, fitness = fitness_value(chromosome)
    print(f"Chromosome: {chromosome}, Fitness: {fitness}")
