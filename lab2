"""
Missionaries and Cannibals Problem (DFS)

Args:
    num_missionaries: Number of missionaries on the starting side
    num_cannibals: Number of cannibals on the starting side

Returns:
    List of states representing steps to reach the goal state
"""

def missionaries_and_cannibals(num_missionaries, num_cannibals):

    visited = set()   # Keep track of visited states

    # State representation: (missionaries_left, cannibals_left, boat)
    # boat = 0 (left side), 1 (right side)

    def state(m, c, b):
        return (m, c, b)
     
    initial_state = state(num_missionaries, num_cannibals, 0)

    # Check if a state is valid
    def is_valid(m1, c1, m2, c2):
        if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0:
            return False
        if m1 > 0 and m1 < c1:
            return False
        if m2 > 0 and m2 < c2:
            return False
        return True

    # Generate successor states
    def generate_successors(current_state):
        successors = []

        m1, c1, boat = current_state
        m2 = num_missionaries - m1
        c2 = num_cannibals - c1

        location = boat

        # Move 1 or 2  people
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2: #Boat carries 1 or 2 people

                    if location == 0:  # boat on left
                        new_m1 = m1 - m
                        new_c1 = c1 - c
                        new_boat = 1
                    else:  # boat on right
                        new_m1 = m1 + m
                        new_c1 = c1 + c
                        new_boat = 0

                    new_m2 = num_missionaries - new_m1
                    new_c2 = num_cannibals - new_c1

                    if is_valid(new_m1, new_c1, new_m2, new_c2):
                        successors.append(state(new_m1, new_c1, new_boat))

        return successors

    # DFS
    stack = [(initial_state, [])]

    while stack:
        current_state, path = stack.pop()

        if current_state in visited:
            continue

        visited.add(current_state)
        path = path + [current_state]

        if current_state == state(0, 0, 1):   # Goal state
            return path

        for successor in generate_successors(current_state):
            stack.append((successor, path))

    return None


# Example usage
num_missionaries = 3
num_cannibals = 3

solution = missionaries_and_cannibals(num_missionaries, num_cannibals)

if solution:
    print("Solution found in", len(solution) - 1, "steps:\n")

    for step, state in enumerate(solution):
        m, c, boat = state
        side = "Left" if boat == 0 else "Right"
        print(f"Step {step}: {m} missionaries, {c} cannibals on Left | Boat: {side}")

else:
    print("No solution found.")
