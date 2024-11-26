import heapq
import state as maf
# import numpy as np


def UCS(initial_state):
    priority_queue = []
    heapq.heappush(priority_queue, (initial_state.cost,
                   initial_state)
                   )  # (cost, state)
    # visited = np.array([])
    visited = set()
    print(priority_queue[0])
    while priority_queue:
        print(len(visited))

        _, current = heapq.heappop(priority_queue)

        # visited = np.append(visited, current.get_hash1())
        visited.add(current.get_hash())
        if current.you_win():
            cost = current.cost
            win_path = []
            path = []
            while current:
                win_path.append(current)
                path.append(current.parent)

                current = current.parent1
            path.reverse()
            win_path.reverse()
            len_visited = len(visited)

            return win_path, path, len_visited, cost

        for move in current.all_next_state_move():
            if move.get_hash() not in visited:
                move.parent1 = current
                heapq.heappush(priority_queue, (move.cost, move))

    return None, None, None


# class my_set:

#     def equals(state1, state2):
#         for i in range(len(state1.mymap)):
#             for j in range(len(state1.mymap)):
#                 if (state1.mymap[i][j] == state2.mymap[i][j]):
#                     continue
#                 else:
#                     return False

#         return True

# initial_state = maf. map_state(6)
# initial_state.parent = "root"


# initial_state.printer(1, 4, "red", "🔴", True, False)
# initial_state.printer(4, 1, "red", "🔴", True, False)
# initial_state.printer(4, 4, "red", "🟥", False, False)

# initial_state.printer(1, 1, "red", "🟥", False, False)
# # initial_state.printer(1, 2, "blue", "🔵", True, False)
# # initial_state.printer(2, 4, "blue", "🟦", False, False)
# initial_state.print_map()


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

# initial_state.printer(4, 9, "red", "🔴", True, False)
# initial_state.printer(1, 2, "red", "🟥", False, False)
# initial_state.printer(2, 7, "blue", "🔵", True, False)
# initial_state.printer(6, 2, "blue", "🟦", False, False)
# initial_state.printer(4, 2, "red", "🟥", False, False)
# initial_state.printer(1, 4, "red", "🔴", True, False)

initial_state.printer(4, 9, "red", "🔴", True, False)

initial_state.printer(1, 2, "red", "🟥", False, False)
initial_state.printer(2, 7, "blue", "🔵", True, False)
initial_state.printer(6, 2, "blue", "🟦", False, False)
initial_state.print_map()
solution_path, path, len_visited, cost = UCS(initial_state)
print(path)
print("cost:  ", cost)

print(len_visited)

if solution_path:
    print("مسار الحل:")
    for state in solution_path:
        state.print_map()  # قم بطباعة معلومات الحالة كما تريد
else:
    print("لم يتم العثور على حل.")
