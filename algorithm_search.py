
from collections import deque
import queue as qu
import map_and_func as maf
import dfs as d


def bfs(start_state):
    queue = deque([start_state])
    visited = {}

    while queue:
        current_state = queue.popleft()
        current_hash = current_state.get_hash()

        if current_hash in visited:
            continue

        visited[current_hash] = True

        if current_state.you_win():

            win_path = []
            path = []
            while current_state:
                win_path.append(current_state)
                path.append(current_state.parent)

                current_state = current_state.parent1
            path.reverse()
            win_path.reverse()
            len_visited = len(visited)
            return win_path, path, len_visited

        possible_states = current_state.all_next_state_move()

        for next_state in possible_states:
            next_hash = next_state.get_hash()
            if next_hash not in visited:
                next_state.parent1 = current_state
                queue.append(next_state)

    return None, []


def dfs(start_state):
    queue = deque([start_state])
    visited = {}

    while queue:
        current_state = queue.pop()
        current_hash = current_state.get_hash()

        if current_hash in visited:
            continue

        visited[current_hash] = True

        if current_state.you_win():

            win_path = []
            path = []
            while current_state:
                win_path.append(current_state)
                path.append(current_state.parent)

                current_state = current_state.parent1
            path.reverse()
            win_path.reverse()
            len_visited = len(visited)
            return win_path, path, len_visited

        possible_states = current_state.all_next_state_move()

        for next_state in possible_states:
            next_hash = next_state.get_hash()
            if next_hash not in visited:
                next_state.parent1 = current_state
                queue.append(next_state)

    return None, [], []


def ucs(start_state):










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

initial_state.printer(2, 8, "blue", "🔵", True, False)
initial_state.printer(6, 2, "blue", "🟦", False, False)
initial_state.printer(4, 3, "red", "🟥", False, False)
initial_state.printer(1, 4, "red", "🔴", True, False)
initial_state.printer(2, 7, "red", "🟥", False, False)
initial_state.printer(5, 7, "red", "🔴", True, False)
initial_state.print_map()

print("dfs")
state, path, len_visited = d.dfs(initial_state)
print("len_visited:", len_visited)
print(" len path :", len(path))
print(path)
print("#"*40)

print("dfs1")
state, path, len_visited = dfs(initial_state)
print("len_visited:", len_visited)
print(" len path :", len(path))
print(path)
print("pfs")
print("#"*40)

state1, path1, len_visited1 = bfs(initial_state)
print("len_visited:", len_visited1)
print(" len path :", len(path1))
print(path1)
# for item in state:
#     item.print_map()
