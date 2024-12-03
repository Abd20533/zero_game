import state as sta
import numpy as np


def simple_hill_climbing(start_state):
    current = start_state
    visited_array = np.array([])

    while not current.you_win():
        visited_array = np.append(visited_array, current)
        next_states = current.all_next_state_move()
        if len(next_states) == 0:
            break

        best_state = None

        if next_states[0].heuristic() < current.heuristic():
            print("funtiones")
            best_state = next_states[0]

        if best_state is None:
            break

        best_state.parent1 = current
        current = best_state

    if current.you_win():
        path = []
        while current.parent1 is not None:
            path.append(current.parent)
            current = current.parent1
        path.reverse()
        return path, len(path), len(visited_array),

    return [], 0, len(visited_array),


initial_state = sta. map_state(6)
initial_state.parent = "root"
initial_state.printer(1, 1, "red", "🔴", True, False)
initial_state.printer(1, 4, "red", "🟥", False, False)
initial_state.printer(3, 4, "red", "🔴", True, False)
initial_state.printer(3, 1, "red", "🟥", False, False)
initial_state.print_map()
path, path_len, visited_len = simple_hill_climbing(initial_state)
print(path)
print(path_len)
print(visited_len)
