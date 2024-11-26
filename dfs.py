import queue as qe
import state as maf
from collections import deque

import numpy as np


def dfs(initial_state):
    stack = [initial_state]
    visited = {initial_state.get_hash(): True}

    while stack:
        current_state = stack.pop()
        if current_state.you_loser():
            return [], [], []
        if current_state.you_win():
            win_path = []
            path = []
            while current_state:
                path.append(current_state.parent)
                win_path.append(current_state)
                current_state = current_state.parent1
            path.reverse()
            len_visited = len(visited)
            return win_path[::-1], path, len_visited

        for move in current_state.all_next_state_move():
            move_hash = move.get_hash()
            if move_hash not in visited:
                visited[move_hash] = True

                stack.append(move)
            move.parent1 = current_state

    return [], [], []


# initial_state = maf. map_state(11)
# initial_state.parent = "root"
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
# initial_state.printer(2, 7, "blue", "🔵", True, False)
# initial_state.printer(4, 2, "blue", "🟦", False, False)
# initial_state.printer(4, 3, "red", "🟥", False, False)
# initial_state.printer(1, 3, "red", "🔴", True, False)
# initial_state.print_map()
# state, path, len_visited = dfs(initial_state)
# print("len_visited:", len_visited)
# print(" len path :", len(path))

# print(path)
# for item in state:
#     item.print_map()
