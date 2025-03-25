# Missionaries and Cannibals Problem Solver

## Problem Description

This is a Python implementation of the classic Missionaries and Cannibals river crossing puzzle. The goal is to transport 3 missionaries and 3 cannibals across a river using a boat, with the following constraints:

- The boat can carry at most 2 people at a time
- At no point can the number of cannibals exceed the number of missionaries on either side of the river (unless there are no missionaries present)
- The boat must be used to transport people across the river

## Problem Representation

The state is represented as a tuple: `(missionaries_left, cannibals_left, missionaries_right, cannibals_right, boat_position)`

- `missionaries_left`: Number of missionaries on the left side
- `cannibals_left`: Number of cannibals on the left side
- `missionaries_right`: Number of missionaries on the right side
- `cannibals_right`: Number of cannibals on the right side
- `boat_position`: 0 = left side, 1 = right side

## Solution Method

The solution uses Breadth-First Search (BFS) to find the shortest path from the initial state to the goal state.

### Key Functions

- `check_valid()`: Validates each state to ensure the game rules are not violated
- `check_goal()`: Checks if the current state is the goal state
- `get_next()`: Generates possible next states based on current state
- `bfs_search()`: Implements the breadth-first search algorithm
- `print_solution()`: Prints the step-by-step solution

## Initial and Goal States

- Initial State: 3 missionaries and 3 cannibals on the left side
- Goal State: 3 missionaries and 3 cannibals on the right side

## How to Run

1. Ensure you have Python installed
2. Clone the repository
3. Run:
   ```
   python missionaries_cannibals.py
   ```

## Output

The program will print out each step of the solution, showing:
- Missionaries and cannibals on the left side
- Missionaries and cannibals on the right side
- Boat position
- Total number of steps to solve the puzzle

## Possible Moves

The boat can transport the following combinations:
- 1 missionary
- 2 missionaries
- 1 cannibal
- 2 cannibals
- 1 missionary and 1 cannibal

## License

This project is licensed under the MIT License.

## Author

Alkinoos Mavrofyllidis
