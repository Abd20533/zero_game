
from map_and_func import map_state
import map_and_func as maf
import numpy as np
import queue as queue

def dfs(state, visited=None, max_depth=100, path=None):
    print(path)
    
    if visited is None:
        visited = set()
    if path is None:
        path = np.array([])
        path = np.array([state.parent])
    for item_state in visited:
        if maf.my_equals.equals(item_state, state):
            # if (item_state.parent != state.parent):
            return False, path[:path.size-1]

    visited.add(state)

    if state.you_win():
        return True, path
    if max_depth <= 0:
        return False, None

    for next_state in state.all_next_state_move():
        if next_state not in visited:
            path = np.append(path, next_state.parent)
            if (next_state.you_win() == True):
                print("%"*20)
                return True, path
            found, path = dfs(next_state, visited,
                              max_depth - 1, path)
            if found:

                return found, path

    return False, path


initial_state = map_state(8)
initial_state.parent = "root"
# initial_state.printer(6, 5, "blue", "🔵", True, False)
# initial_state.printer(4, 1, "blue", "🔵", True, False)

initial_state.printer(6, 1, "white", "⚪️", True, False)
# initial_state.printer(5, 3, "black", "⬛️", False, False)

initial_state.printer(5, 1, "blue", "🟦", False, False)

initial_state.printer(1, 1, "red", "🔴", True, False)
initial_state.printer(1, 5, "red", "🟥", False, False)
# initial_state.printer(4, 5, "blue", "🟦", False, False)
initial_state.print_map()
found, path = dfs(initial_state)

if found:
    print("تم العثور على حل!")
    print("خطوات الحل:")
    print(path)
else:
    print("لم يتم العثور على حل.")
# initial_state.printer(3, 1, "red", "🔴", True, False)
# initial_state.printer(3, 2, "red", "🔴", True, False)
# initial_state.printer(3, 3, "red", "🟥", False, False)
# initial_state.printer(4, 5, "white", "⚪️", True, False)
# initial_state.printer(4, 4, "red", "🟥", False, False)
# def dfs1(state, visited=None):

#     if visited is None:
#         visited = []

#     visited.append(state)

#     if state.you_win():
#         return True, visited

#     for next_state in state.all_next_state_move():
#         if next_state not in visited:
#             found, path = dfs(next_state, visited)
#             if found:
#                 return found, path

#     return False, None
############################

# def dfs(state, visited=None, max_depth=100):
#     if visited is None:
#         visited = set()
#         # []
#     # visited.append(state)

#     visited.add(state)

#     if state.you_win():
#         return True, visited
#     if max_depth <= 0:
#         return False, None

#     for next_state in state.all_next_state_move():
#         if next_state not in visited:
#             found, path = dfs(next_state, visited, max_depth - 1)
#             if found:
#                 return found, path

#     return False, None
# 333333333333333333333333333

# def dfs1(state, visited=None, max_depth=100):
#     if visited is None:
#         visited = set()

#     for item_state in visited:

#         if (maf.my_equals.equals(item_state, state)):
#             return False, None

#     visited.add(state)

#     if state.you_win():
#         return True, visited
#     if max_depth <= 0:
#         return False, None

#     for next_state in state.all_next_state_move():
#         if next_state not in visited:
#             found, path = dfs(next_state, visited, max_depth - 1)
#             if found:
#                 return found, path

#     return False, None
