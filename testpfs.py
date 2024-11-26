

from state import map_state
import state as maf
import numpy as np
import queue as queue


def pfs(state, q):

    visited = set()
    queue = q
    queue.put(state)
    path = np.array([])
    path = np.array([state.parent])

    while not queue.empty():
        current_state = queue.get()
        if (current_state in visited):
            continue
        visited.add(current_state)
        if (current_state.you_loser()):
            return False, path
        if (current_state.you_win()):
            path = np.append(path, current_state.parent)
            return True, path

        for next_state in current_state.all_next_state_move():
            if (next_state not in visited):

                if (maf.my_equals.equals(next_state, current_state) == False):
                    print("-"*40)
                    if (next_state.you_win()):
                        path = np.append(path, next_state.parent)
                        return True, path
                    queue.put(next_state)
                    path = np.append(path, next_state.parent)

    return False, path


initial_state = map_state(8)
initial_state.parent = "root"
initial_state.printer(1, 1, "red", "🔴", True, False)
initial_state.printer(1, 5, "red", "🟥", False, False)
initial_state.printer(5, 5, "red", "🔴", True, False)
initial_state.printer(5, 1, "red", "🟥", False, False)
# initial_state.printer(1, 6, "white", "⚪️", True, False)

# initial_state.printer(1, 5, "red", "🟥", False, False)
initial_state.print_map()

q = queue.Queue()
result, path = pfs(initial_state, q)
print(path)
if (result):
    print(path)
