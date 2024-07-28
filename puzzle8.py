import heapq

def get_neighbors(state):
    neighbors = []
    zero_pos = [(i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0][0]
    i, j = zero_pos

    def swap_and_clone(a, b, c, d):
        new_state = [list(row) for row in state]
        new_state[a][b], new_state[c][d] = new_state[c][d], new_state[a][b]
        return new_state

    if i > 0:
        neighbors.append(swap_and_clone(i, j, i - 1, j))
    if i < 2:
        neighbors.append(swap_and_clone(i, j, i + 1, j))
    if j > 0:
        neighbors.append(swap_and_clone(i, j, i, j - 1))
    if j < 2:
        neighbors.append(swap_and_clone(i, j, i, j + 1))

    return neighbors

def print_state(state):
    for row in state:
        print(" ".join(str(val) for val in row))
    print()

def a_star_search(initial_state, goal_state):
    goal = [val for row in goal_state for val in row]
    initial_tuple = tuple(tuple(row) for row in initial_state)
    goal_tuple = tuple(tuple(row) for row in goal_state)

    frontier = []
    heapq.heappush(frontier, (0, 0, initial_tuple, [])) 
    explored = set()

    while frontier:
        cost, mismatches, state, path = heapq.heappop(frontier)

        if state == goal_tuple:
            return path

        explored.add(state)

        for neighbor in get_neighbors([list(row) for row in state]):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple not in explored:
                new_cost = cost + 1  
                new_mismatches = sum(1 for val in neighbor_tuple if val != goal[neighbor_tuple.index(val)])
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_cost + new_mismatches, new_mismatches, neighbor_tuple, new_path))

    return None

print("Enter the initial state (use 0 for the empty space):")
initial_state = []
for i in range(3):
    row = input(f"Enter row {i + 1} (space-separated numbers): ").split()
    initial_state.append([int(val) for val in row])

print("Enter the goal state (use 0 for the empty space):")
goal_state = []
for i in range(3):
    row = input(f"Enter row {i + 1} (space-separated numbers): ").split()
    goal_state.append([int(val) for val in row])

path = a_star_search(initial_state, goal_state)

if path is not None:
    print("Solution found!")
    print("Initial state:")
    print_state(initial_state)
    for step, state in enumerate(path):
        print(f"Step {step + 1}:")
        print_state(state)
else:
    print("No solution found.")