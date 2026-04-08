import heapq


def heuristic(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
            
def generate_moves(state):
    moves = []
    x, y = find_blank(state)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
            
    return moves

def best_first_search(start, goal):
    pq = []
    visited = set()

    heapq.heappush(pq, (heuristic(start, goal), start))

    while pq:
        h, current=heapq.heappop(pq)
        
        if current == goal:
            print("\nGoal state Reached!")
            return
        visited.add(tuple(map(tuple, current)))
        print("\ncurrent state(Heuristic=", h ,"):")
        
        for row in current:
            print(row)
            
        for move in generate_moves(current):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
               heapq.heappush(pq, (heuristic(move, goal), move))

    print("\nGoal not reached.")
                              
print("Enter initial state (use 0 for blank):")
initial = [list(map(int, input().split())) for _ in range(3)]

                              
print("Enter goal state")
goal = [list(map(int, input().split())) for _ in range(3)]
                              
best_first_search(initial, goal)                                               
                                               
           
                                
                   
                   
                   
            
