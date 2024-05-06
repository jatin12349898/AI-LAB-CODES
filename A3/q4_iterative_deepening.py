import copy
openl = []
closed = []

initial_state = [
  ['A'],
  ['B','C'],
  []
]

goal_state = [
  ['A','B','C'],
  [],
  []  
]

def compare(s):
  return s==goal_state

def generate_child_dfs(s):
  global openl
  child = []
  for i in range(len(s)):
    if s[i]:
      top_block = s[i][-1]
      state = copy.deepcopy(s)
      state[i].pop()
      for j in range(len(state)):
        if i!=j:
          new_state = copy.deepcopy(state)
          new_state[j].append(top_block)
          if new_state not in child and new_state not in closed:
              child.append(new_state)
    
    return child
            
def depth_limit(s,limit):
    if limit < 0:
        return False

    openl = [s]
    while openl:
        current_state = openl.pop(0)
        
        if compare(current_state):
            return True
        
        if limit > 0:
            new_state = generate_child_dfs(current_state)
            openl = new_state + openl
        
        closed.append(current_state)
    
    return False            

def iterative_deep(s):
    limit = 0
    while True:
        found = depth_limit(s,limit)
        
        if found :
            print(f"Found at depth {limit}")
            return True

        limit += 1
        
        if limit > 100:
            print("Maximum depth limit reached")
            return False
    
  
def main():
    solution = iterative_deep(initial_state)
    if solution:
        print("Goal found.")
    else:
        print("No solution found")

main()
