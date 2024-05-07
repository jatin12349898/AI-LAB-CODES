import copy
q = []
visited = []

def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return [i , j];

def up(s):
    pos = find_pos(s);
    row = pos[0] # finding position of row in the source
    col = pos[1]
    new_state = [[0 , 0 , 0] , [ 0 , 0 , 0] , [0 , 0 , 0]];
    
    # new copy banane ke liye new state banayi hai maine
    
    for i in range(len(s)):
        for j in range(len(s[0])):
            new_state[i][j] = s[i][j]
            
    if row > 0: # row 0 se kam nai ho skti
        new_state[row][col] = new_state[row - 1][col]
        new_state[row - 1][col] = 0
    return new_state

def down(s):
    pos = find_pos(s);
    row = pos[0]
    col = pos[1]
    
    new_state = copy.deepcopy(s)
    
    if row < 2: # sirf 3 hi row hai 0 1 2 so 2 se aage nai ja skti apni rows
        new_state[row][col] = new_state[row + 1][col]
        new_state[row + 1][col] = 0;
    return new_state

def left(s):
    pos = find_pos(s);
    row = pos[0]
    col = pos[1]
    new_state = copy.deepcopy(s)
    
    if col > 0: # sirf 3 hi row hai 0 1 2 so 2 se aage nai ja skti apni rows
        new_state[row][col] = new_state[row][col - 1];
        new_state[row][col - 1] = 0;
    return new_state
        
def generate_children(s):
    global q;
    global visited;
    
    newstate = up(s);
    if newstate not in q and newstate not in visited:
        q.append(newstate);     
       
    newstate = down(s);
    if newstate not in q and newstate not in visited:
        q.append(newstate);         
    
    newstate = left(s);
    if newstate not in q and newstate not in visited:
        q.append(newstate);         

    newstate = right(s);
    if newstate not in q and newstate not in visited:
        q.append(newstate);         

def search(g):
    count=0
    global q;
    global visited
    print(q);
    while(1):
        s=q[0];
        del q[0];
    
    
        if compare(s , g) == 1:
            count=count+1
            #print(s);
            print("found")
            print(count)
            exit();     
        else:
            count=count+1
            print(s)
            generate_children(s);
            visited.append(s);
    
    print("------");
    print(q);
        
def right(s):
    pos = find_pos(s);
    row = pos[0]
    col = pos[1]
    new_state = copy.deepcopy(s)
    
    if col < 2: # sirf 3 hi row hai 0 1 2 so 2 se aage nai ja skti apni rows
        new_state[row][col] = new_state[row][col + 1];
        new_state[row][col + 1] = 0;
    return new_state
        
def compare(s , g):#compairing both the list
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != g[i][j]:
                return 0;
    return 1;   
    
def main():
    global q;
    source =[[1 , 2 , 3] , [8 , 0 , 4] , [7 , 6 , 5]]
    goal = [[2 , 8 , 1] , [0 , 4 , 3] , [7 , 6 , 5]]
    q.append(source);
    search(goal);
    
main()
