"""
Missionaries and Cannibals Problem Solver
-----------------------------------------
This script solves the classic "Missionaries and Cannibals" problem using 
the Breadth-First Search (BFS) algorithm. It finds the shortest sequence 
of moves to transport all missionaries and cannibals safely across the river.

State representation:
(missionaries left, cannibals left, missionaries right, cannibals right, boat position)
boat position: 0 = left, 1 = right

At all times, missionaries must be >= cannibals
"""

# Possible moves (missionaries, cannibals)
MOVES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

# Initial state and Goal
INITIAL = (3, 3, 0, 0, 0)
GOAL = (0, 0, 3, 3, 1)

# Check constraints
def check_valid(state):
    missionaries_left, cannibals_left, missionaries_right, cannibals_right, boat = state
    
    # Negative numbers check
    if (missionaries_left < 0 or cannibals_left < 0 or 
        missionaries_right < 0 or cannibals_right < 0):
        return False
    
    # Cannibals > Missionaries left
    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False
    
    # Cannibals > Missionaries right
    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False
    
    return True

# Check if goal is achieved
def check_goal(state):
    return state == GOAL

# Find next states
def get_next(state):
    missionaries_left, cannibals_left, missionaries_right, cannibals_right, boat = state
    next_states = []
    
    # If boat is left
    if boat == 0:
        for m, c in MOVES:
            # Move from left to right
            if m <= missionaries_left and c <= cannibals_left:
                new_state = (
                    missionaries_left - m,
                    cannibals_left - c,
                    missionaries_right + m,
                    cannibals_right + c,
                    1
                )
                if check_valid(new_state):
                    next_states.append(new_state)

    # If boat is right
    else:
        for m, c in MOVES:
            # Move from right to left
            if m <= missionaries_right and c <= cannibals_right:
                new_state = (
                    missionaries_left + m,
                    cannibals_left + c,
                    missionaries_right - m,
                    cannibals_right - c,
                    0
                )
                if check_valid(new_state):
                    next_states.append(new_state)
                    
    return next_states

# BFS search algorithm
def bfs_search():
    visited = set()
    queue = [[INITIAL]]
    
    while queue:
        path = queue.pop(0)
        current_state = path[-1]
        
        if check_goal(current_state):
            return path
            
        if current_state not in visited:
            visited.add(current_state)
            
            for successor in get_next(current_state):
                if successor not in visited:
                    new_path = list(path)
                    new_path.append(successor)
                    queue.append(new_path)
                    
# Print step-by-step solution
def print_solution(solution):        
    for i, state in enumerate(solution):
        missionaries_left, cannibals_left, missionaries_right, cannibals_right, boat = state

        left_side = f"Left Bank: {missionaries_left}M, {cannibals_left}C"
        right_side = f"Right Bank: {missionaries_right}M, {cannibals_right}C"

        if boat == 1:
            boat_position = "Boat: Right"
        else:
            boat_position = "Boat: Left"

        print(f"Step {i}: {left_side} | {right_side} | {boat_position}")

    print(f"Total Steps: {len(solution) - 1}")


solution = bfs_search()
print_solution(solution)