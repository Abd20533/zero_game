
from state import map_state
import state as maf
import numpy as np
import queue as queue


def dfs(state, visited=None, max_depth=1000, path=None):
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


initial_state = maf. map_state(8, 16)
initial_state.parent = "root"
initial_state. row_printer_black(1, 1, 5)
initial_state. row_printer_black(1, 8, 11)
initial_state. row_printer_black(1, 12, 14)

initial_state.printer(2, 6, "black", "⬛️", False, False)
initial_state.printer(3, 12, "black", "⬛️", False, False)

initial_state. row_printer_black(4, 1, 5)
initial_state. row_printer_black(4, 6, 8)
initial_state. row_printer_black(4, 9, 15)
initial_state. row_printer_black(5, 1, 8)
initial_state. row_printer_black(5, 9, 15)
initial_state. row_printer_black(6, 1, 15)


initial_state.printer(3, 1, "orange", "🟧", False, False)
initial_state.printer(2, 2, "blue", "🟦", False, False)
initial_state.printer(2, 1, "red", "🟥", False, False)
initial_state.printer(2, 3, "green", "🟩", False, False)
initial_state.printer(3, 2, "yelow", "🟨", False, False)


initial_state.printer(4, 5, "white", "⚪️", True, False)
initial_state.printer(1, 7, "yelow", "🟡", True, False)
initial_state.printer(4, 8, "blue", "🔵", True, False)
initial_state.printer(1, 11, "orange", "🟠", True, False)

initial_state.printer(1, 14, "green", "🟢", True, False)
initial_state.printer(5, 8, "black", "⚫️", True, False)


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
