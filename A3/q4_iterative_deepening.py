import copy

openl=[]
closed=[]
count=0

goal_state=[
  [],
  [],
  ['A','B','C']
]

initial_state =[
  [],
  ['A'],
  ['B','C']
]

def compare(s,g):
  global count
  count+=1
  s[0].sort()
  g.sort()
  return s[0]==g

def generate_child(s,depth):
  global openl
  global closed
  global g
  if(s==[]):
    return
  s[0].sort()

  if(s[1]==depth):
    generate_child(s[2], depth)
    return

  for i in range(len(s[0])):
    if len(s[0][i])>0:
      new_state=copy.deepcopy(s)
      new_state[2]=s
      pick_element=new_state[0][i][-1]
      del new_state[0][i][-1]

      for j in range(len(new_state[0])):
        if i!=j:
          new_state[0][j].append(pick_element)
          new_state[1]+=1
          final_state=copy.deepcopy(new_state)
          final_state[0].sort()
          if final_state not in openl and final_state[0] not in closed:
            openl.append(final_state)
            return
          del final_state
          del new_state[0][j][-1]
          new_state[1]-=1
  generate_child(s[2], depth)

def search(g, depth):
  global openl
  global closed
  while 1:
    if(openl==[]):
      print("Search was incomplete")
      return []
    openl[0][0].sort()
    current_state=openl[0]
    del openl[0]
    if compare(current_state,g):
      print("Found\n")
      return current_state
    else:
      closed.append(current_state[0])
      generate_child(current_state, depth)

def main():
  global openl
  global closed
  global goal_state
  global initial_state
  global count

  openl.append([initial_state,0,[]])
  depth=1
  while 1:
    sol=search(goal_state,depth)
    if sol==[]:
      depth += 1
      openl.append([initial_state,0,[]])
      closed=[]
    else:
      break
    
  print("The depth at which the goal state is found is: ",sol[1])
  print("The number of states it visited is: ",count)

if __name__=="__main__":
  main()
