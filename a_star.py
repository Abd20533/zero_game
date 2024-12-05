
import state as sta
import numpy as np
import queue
import time as ti


def A_star(start_state):
    priority_queue = queue.PriorityQueue()
    start_cost = start_state.heuristic()
    priority_queue.put((start_cost, 0, start_state))
    visited_array = np.array([])

    while not priority_queue.empty():
        _, current_cost, current = priority_queue.get()

        if current.you_win():
            path = []
            path_win = []

            while current is not None:
                path .append(current.parent)
                path_win.append(current)

                current = current.parent1
            path.reverse()
            path_win.reverse()
            return path, path_win, len(path)-1, len(visited_array),

        visited = False
        for item in visited_array:
            if sta.my_equals. equals(item, current) and item.cost == current.cost:
                visited = True
                break

        if not visited:
            if (current.you_loser() == False or current.you_loser_new() == False):

                visited_array = np.append(visited_array, current)

                next_states = current.all_next_state_move()
                for item in next_states:
                    if (item.you_loser() == False or item. you_loser_new() == False):
                        if current.parent1 is None or not sta.map_state. equals(item, current):
                            item.parent1 = current
                            g_cost = current_cost + 1
                            f_cost = g_cost + item.heuristic()

                            priority_queue.put((f_cost, g_cost, item))

    return [], [], [], len(visited_array),


# initial_state = sta. map_state(16)
# initial_state.parent = "root"
# initial_state. row_printer_black(1, 1, 5)
# initial_state. row_printer_black(1, 8, 11)
# initial_state. row_printer_black(1, 12, 14)

# initial_state.printer(2, 6, "black", "⬛️", False, False)
# initial_state.printer(3, 12, "black", "⬛️", False, False)

# initial_state. row_printer_black(4, 1, 5)
# initial_state. row_printer_black(4, 6, 8)
# initial_state. row_printer_black(4, 9, 15)
# initial_state. row_printer_black(5, 1, 8)
# initial_state. row_printer_black(5, 9, 15)
# initial_state. row_printer_black(6, 1, 15)


# initial_state.printer(3, 1, "orange", "🟧", False, False)
# initial_state.printer(2, 2, "blue", "🟦", False, False)
# initial_state.printer(2, 1, "red", "🟥", False, False)
# initial_state.printer(2, 3, "green", "🟩", False, False)
# initial_state.printer(3, 2, "yelow", "🟨", False, False)


# initial_state.printer(4, 5, "white", "⚪️", True, False)
# initial_state.printer(1, 7, "yelow", "🟡", True, False)
# initial_state.printer(4, 8, "blue", "🔵", True, False)
# initial_state.printer(1, 11, "orange", "🟠", True, False)

# initial_state.printer(1, 14, "green", "🟢", True, False)
# initial_state.printer(5, 8, "black", "⚫️", True, False)


# initial_state.print_map()


initial_state = sta. map_state(9)
initial_state.parent = "root"

initial_state.row_printer_black(4, 1, 8)
initial_state.row_printer_black(1, 1, 4)
initial_state.row_printer_black(1, 6, 8)
initial_state.printer(3, 3, "black", "⬛️", False, False)
initial_state.printer(3, 6, "black", "⬛️", False, False)
initial_state.add_to_map_not_goal(3, 7, "green", "🟢")
# initial_state.printer(3, 1, "green", "🟩", False, False)

initial_state.printer(1, 4, "red", "🟥", False, False)
initial_state.printer(3, 4, "red", "🔴", True, False)
initial_state.printer(2, 1, "blue", "🔵", True, False)
initial_state.printer(2, 3, "blue", "🟦", False, False)
initial_state.printer(3, 7, "yelow", "🟨", False, False)
initial_state.printer(1, 5, "yelow", "🟡", True, False)

# initial_state.printer(1, 1, "black", "⬛️", False, False)
# initial_state.printer(1, 6, "black", "⬛️", False, False)
# initial_state.printer(1, 5, "black", "⬛️", False, False)
# initial_state.printer(1, 7, "black", "⬛️", False, False)
# initial_state.printer(2, 5, "black", "⬛️", False, False)
# initial_state.printer(1, 8, "black", "⬛️", False, False)
# initial_state.printer(1, 9, "black", "⬛️", False, False)
# initial_state.printer(2, 6, "black", "⬛️", False, False)
# initial_state.printer(2, 9, "black", "⬛️", False, False)
# initial_state.printer(3, 9, "black", "⬛️", False, False)
# initial_state.printer(5, 9, "black", "⬛️", False, False)
# initial_state.printer(6, 1, "black", "⬛️", False, False)
# initial_state.printer(6, 4, "black", "⬛️", False, False)
# initial_state.printer(6, 5, "black", "⬛️", False, False)
# initial_state.printer(6, 6, "black", "⬛️", False, False)
# initial_state.printer(6, 7, "black", "⬛️", False, False)
# initial_state.printer(6, 8, "black", "⬛️", False, False)
# initial_state.printer(6, 9, "black", "⬛️", False, False)
# initial_state.printer(7, 1, "black", "⬛️", False, False)
# initial_state.printer(7, 2, "black", "⬛️", False, False)
# initial_state.printer(7, 3, "black", "⬛️", False, False)
# initial_state.printer(7, 4, "black", "⬛️", False, False)
# initial_state.printer(4, 4, "black", "⬛️", False, False)
# initial_state.printer(4, 6, "black", "⬛️", False, False)
# initial_state.printer(4, 5, "black", "⬛️", False, False)

# # initial_state.printer(4, 9, "red", "🔴", True, False)
# # initial_state.printer(1, 2, "red", "🟥", False, False)
# # initial_state.printer(2, 7, "blue", "🔵", True, False)
# # initial_state.printer(6, 2, "blue", "🟦", False, False)
# initial_state.printer(2, 2, "red", "🟥", False, False)
# initial_state.printer(5, 8, "red", "🔴", True, False)

# initial_state.printer(4, 9, "red", "🔴", True, False)

# initial_state.printer(2, 8, "green", "🟢", True, False)
# initial_state.printer(2, 1, "green", "🟩", False, False)


# initial_state.printer(1, 2, "red", "🟥", False, False)
# initial_state.printer(2, 7, "blue", "🔵", True, False)
# initial_state.printer(6, 2, "blue", "🟦", False, False)
initial_state.print_map()
t_f = ti.time()
path, path_win, path_len, visited_len = A_star(initial_state)
t_e = ti.time()

print(f"{t_e-t_f:.4f}")

print(path)
for state in path_win:
    state.print_map()
print(path_len)
print(visited_len)
