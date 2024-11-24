
from map_and_func import map_state
import map_and_func as maf
import numpy as np
import queue as queue


def dfs(state, visited=None, max_depth=100, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = np.array([])
        path = np.array([state.parent])
    for item_state in visited:
        if maf.my_equals.equals(item_state, state):
            # if (item_state.parent != state.parent):
            return False, path[:path.size-1], []

    visited.add(state)

    if state.you_win():
        len_visited = len(visited)
        return True, path, len_visited
    if max_depth <= 0:
        return False, None

    for next_state in state.all_next_state_move():
        if next_state not in visited:
            len_visited = len(visited)

            path = np.append(path, next_state.parent)
            if (next_state.you_win() == True):
                print("%"*20)
                len_visited = len(visited)
                return True, path, len_visited
            if maf.my_equals.equals(next_state, state) == False:

                found, path, len_visited = dfs(next_state, visited,
                                               (max_depth - 1), path)

            if found:

                return found, path, len_visited

    return False, path, []


initial_state = maf. map_state(11)
initial_state.parent = "root"
initial_state.printer(1, 1, "black", "⬛️", False, False)
initial_state.printer(1, 6, "black", "⬛️", False, False)
initial_state.printer(1, 5, "black", "⬛️", False, False)
initial_state.printer(1, 7, "black", "⬛️", False, False)
initial_state.printer(2, 5, "black", "⬛️", False, False)
initial_state.printer(1, 8, "black", "⬛️", False, False)
initial_state.printer(1, 9, "black", "⬛️", False, False)
initial_state.printer(2, 6, "black", "⬛️", False, False)
initial_state.printer(2, 9, "black", "⬛️", False, False)
initial_state.printer(3, 9, "black", "⬛️", False, False)
initial_state.printer(5, 9, "black", "⬛️", False, False)
initial_state.printer(6, 1, "black", "⬛️", False, False)
initial_state.printer(6, 4, "black", "⬛️", False, False)
initial_state.printer(6, 5, "black", "⬛️", False, False)
initial_state.printer(6, 6, "black", "⬛️", False, False)
initial_state.printer(6, 7, "black", "⬛️", False, False)
initial_state.printer(6, 8, "black", "⬛️", False, False)
initial_state.printer(6, 9, "black", "⬛️", False, False)
initial_state.printer(7, 1, "black", "⬛️", False, False)
initial_state.printer(7, 2, "black", "⬛️", False, False)
initial_state.printer(7, 3, "black", "⬛️", False, False)
initial_state.printer(7, 4, "black", "⬛️", False, False)
initial_state.printer(4, 4, "black", "⬛️", False, False)
initial_state.printer(4, 6, "black", "⬛️", False, False)
initial_state.printer(4, 5, "black", "⬛️", False, False)


initial_state.printer(4, 9, "red", "🔴", True, False)

initial_state.printer(1, 2, "red", "🟥", False, False)
initial_state.printer(2, 7, "blue", "🔵", True, False)
initial_state.printer(6, 2, "blue", "🟦", False, False)
initial_state.print_map()
found, path, len_visited = dfs(initial_state)

if found:
    print("تم العثور على حل!")
    print("خطوات الحل:")
    print(path)
    print(len(path))

    print(len_visited)
else:
    print("لم يتم العثور على حل.")
