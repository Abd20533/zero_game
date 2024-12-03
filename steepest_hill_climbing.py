
import state as sta
import numpy as np


def steepest_hill_climbing(start_state):
    current = start_state
    visited_array = np.array([])

    while not current.you_win():
        visited_array = np.append(visited_array, current)
        next_states = current.all_next_state_move()

        if len(next_states) == 0:
            break

        best_next_state = min(next_states, key=sta.map_state.heuristic)
        if best_next_state.heuristic() >= current.heuristic():
            break

        best_next_state.parent1 = current
        current = best_next_state

    if current.you_win():
        print("you_win")
        path = []

        while current.parent1:
            path.append(current.parent)
            current = current.parent1
        path.reverse()
        return path, len(path), len(visited_array)
    print(" not you_win")

    return [], 0, visited_array


initial_state = sta. map_state(12)
initial_state.parent = "root"
initial_state.printer(10, 1, "red", "🔴", True, False)
initial_state.printer(1, 1, "red", "🟥", False, False)
# initial_state.printer(3, 4, "red", "🔴", True, False)
# initial_state.printer(3, 1, "red", "🟥", False, False)
# initial_state.printer(1, 8, "red", "🔴", True, False)
# initial_state.printer(8, 8, "red", "🟥", False, False)
initial_state.print_map()
# path, len(path), len(visited_array)
# path, path_win, path_len, visited_len
path, path_len, visited_len = steepest_hill_climbing(initial_state)
print("path: ", path)
print("path_len: ", path_len)
print("visited_len: ", visited_len)
