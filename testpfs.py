
from collections import deque
import state as sta
import numpy as np
import time as ti


def bfs(start_state):
    queue = deque([start_state])
    visited = {}
    visited_new = np.array([])

    print(start_state.you_loser_new())
    if (start_state.you_loser_new()):

        return None, [], []

    while queue:
        # if (len(visited_new) % 100 == 0):
        print("len(visited_new) is :", len(visited_new))
        current_state = queue.popleft()
        current_hash = current_state.get_hash()
        v = False
        if current_state.you_win():

            win_path = []
            path = []
            while current_state:
                win_path.append(current_state)
                path.append(current_state.parent)

                current_state = current_state.parent1
            path.reverse()
            win_path.reverse()
            len_visited = len(visited_new)
            return win_path, path, len_visited

        if current_hash in visited_new:
            v = True

        if (v == False):
            visited_new = np.append(visited_new, current_hash)

        possible_states = current_state.all_next_state_move()

        for next_state in possible_states:

            if ((current_state.equals(next_state) == False) and ((next_state.you_loser() == False) or (next_state. you_loser_new() == False))):
                next_hash = next_state.get_hash()
                if next_hash not in visited_new:
                    next_state.parent1 = current_state
                    queue.append(next_state)

    return None, [], []


initial_state = sta. map_state(8, 16)
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


print("#"*40)

initial_state.print_map()
print("#"*40)
t_e = ti.time()

state1, path1, len_visited1 = bfs(initial_state)
t_f = ti.time()

print(f"{t_f-t_e:.4f}")
print("len_visited:", len_visited1)
print(" len path :", len(path1))
print(path1)
for item in state1:
    item.print_map()
# initial_state = sta. map_state(5, 7)

# initial_state.printer(3, 1, "orange", "🟧", False, False)
# initial_state.printer(2, 2, "blue", "🟦", False, False)
# initial_state.printer(2, 3, "red", "🟥", False, False)
# # # initial_state.printer(2, 1, "green", "🟩", False, False)
# # initial_state.printer(1, 1, "yelow", "🟨", False, False)

# initial_state.printer(3, 4, "white", "⚪️", True, False)
# # initial_state.printer(1, 4, "yelow", "🟡", True, False)
# initial_state.printer(2, 4, "blue", "🔵", True, False)
# initial_state.printer(1, 3, "orange", "🟠", True, False)

# initial_state.printer(1, 1, "green", "🟢", True, False)
# initial_state.printer(5, 8, "black", "⚫️", True, False)
