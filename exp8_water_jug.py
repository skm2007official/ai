from collections import deque

def water_jug(capacity_a, capacity_b, target):
    queue = deque([(0, 0)])
    visited = {(0, 0)}
    parent = {(0, 0): None}

    while queue:
        a, b = queue.popleft()

        if a == target or b == target:
            path = []
            state = (a, b)

            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()

            print("Solution path:")

            for state in path:
                print(state)

            return

        # Possible operations
        next_states = [
            (capacity_a, b),                  # Fill Jug A
            (a, capacity_b),                  # Fill Jug B
            (0, b),                           # Empty Jug A
            (a, 0),                           # Empty Jug B
            (a - min(a, capacity_b - b),
             b + min(a, capacity_b - b)),    # Pour A into B
            (a + min(b, capacity_a - a),
             b - min(b, capacity_a - a))     # Pour B into A
        ]

        for next_state in next_states:
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (a, b)
                queue.append(next_state)

    print("No solution exists.")


# Main program
capacity_a = 4
capacity_b = 3
target = 2

water_jug(capacity_a, capacity_b, target)