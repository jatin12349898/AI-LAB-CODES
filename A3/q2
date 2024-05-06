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
  for i in range(len(s)):
    if s[i]:
      top_block = s[i][-1]
      state = copy.deepcopy(s)
      state[i].pop()
      for j in range(len(state)):
        if i!=j:
          new_state = copy.deepcopy(state)
          new_state[j].append(top_block)
          
          if new_state not in openl and new_state not in closed:
            openl.append(new_state)
            
def bfs(s):
  global openl
  global closed
  
  openl = [s]
  closed = []
  count = 0
  while openl:
    current_state = openl.pop(0)
    count += 1
    
    print(f"Current state : {current_state}")
    
    if compare(current_state):
      print(f"Found in {count} steps")
      return
    
    generate_child_dfs(current_state)
    closed.append(current_state)
  
  print("No solution found.")
  
def main():
  bfs(initial_state)
  
main()
