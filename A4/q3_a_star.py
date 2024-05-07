import copy

openl = []
closed = []
g = [[1,2,3],[8,0,4],[7,6,5]]

def heuristic(s):
    x = 0
    global g
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == g[i][j]:
                x+=1
    return x

def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j]==0:
                return [i,j]
 
def up(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if x>0:
        s1[x][y] = s1[x-1][y]
        s1[x-1][y] = 0
    return s1    
 
def down(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if x<2:
        s1[x][y] = s1[x+1][y]
        s1[x+1][y] = 0
    return s1
 
def left(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if y>0:
        s1[x][y] = s1[x][y-1]
        s1[x][y-1] = 0
    return s1    
 
def right(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if y<2:
        s1[x][y] = s1[x][y+1]
        s1[x][y+1] = 0
    return s1  
 
def generate_child(s):
    global openl
    global closed
    global g
    
    new_state = up(s)
    state = heuristic(new_state)
    if [state,new_state,s] not in openl and [state,new_state] not in closed and new_state != s:
        openl.append([state,new_state,s]) 
        
    new_state = down(s)
    state = heuristic(new_state)
    if [state,new_state,s] not in openl and [state,new_state] not in closed and new_state != s:
        openl.append([state,new_state,s])   
          
    new_state = left(s)
    state = heuristic(new_state)
    if [state,new_state,s] not in openl and [state,new_state] not in closed and new_state != s:
        openl.append([state,new_state,s]) 
            
    new_state = right(s)
    state = heuristic(new_state)
    if [state,new_state,s] not in openl and [state,new_state] not in closed and new_state != s:
        openl.append([state,new_state,s])   
 
def search(g):
    global openl
    global closed
    c = 0
 
    while openl:
        openl.sort()
        
        _, best_state, parent = openl.pop()
        
        if best_state == g:
            print(f"Found in {c} steps")
            exit()
            
        c += 1
        generate_child(best_state)
        closed.append([heuristic(best_state),best_state,parent])
        
    print("Cannot Find Solution")
    exit()

def main():
    global openl
    global g
    s = [[2,0,3],[1,8,4],[7,6,5]]        
    
    openl.append([heuristic(s),s,None])
    search(g)
 
main()
