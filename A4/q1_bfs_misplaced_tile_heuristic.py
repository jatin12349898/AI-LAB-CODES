import copy
open = []
closed = []
g = [[1,2,3],[8,0,4],[7,6,5]]

def heuristic(s):
    x = 0
    global g
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != g[i][j]:
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
    global open
    global closed
    global g
    
    new_state = up(s)
    state = heuristic(new_state)
    if [state,new_state] not in open and [state,new_state] not in closed:
        open.append([state,new_state]) 
    new_state = down(s)
    state = heuristic(new_state)
    if [state,new_state] not in open and [state,new_state] not in closed:
        open.append([state,new_state])     
    new_state = left(s)
    state = heuristic(new_state)
    if [state,new_state] not in open and [state,new_state] not in closed:
        open.append([state,new_state])     
    new_state = right(s)
    state = heuristic(new_state)
    if [state,new_state] not in open and [state,new_state] not in closed:
        open.append([state,new_state])    
 
def search(g):
    global open
    global closed
    c = 0
 
    while len(open):
        open.sort()
        curr = open[0][1]
        p = open[0]
        del open[0]
        c+=1

        if curr==g:
            print(f"Found in {c} steps")
            exit()
        
        generate_child(curr)
        closed.append(p)
        print(c)
    print("Cannot Find Solution")
    exit()

def main():
    global open
    global g
    s = [[2,0,3],[1,8,4],[7,6,5]]        
    
    open.append([heuristic(s),s])
    search(g)
 
main()
