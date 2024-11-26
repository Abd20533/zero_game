
from collections import deque
import queue as qu
import state as maf
import dfs as d
import heapq
import numpy as np



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


def UCS(initial_state):
    priority_queue = []
    heapq.heappush(priority_queue, (initial_state.cost,
                   initial_state)
                   )  # (cost, state)
    visited = set()
    print(priority_queue[0])
    while priority_queue:

        _, current = heapq.heappop(priority_queue)
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

def UCStest(initial_state):
    priority_queue = []
    heapq.heappush(priority_queue, (initial_state.cost,
                   initial_state))  # (cost, state)
    visited = set()

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        visited.add(current.get_hash())

        if current.you_win():

            win_path = []
            path = []
            while current:
                win_path.append(current)
                path.append(current.parent)

                current = current.parent1
            path.reverse()
            win_path.reverse()
            len_visited = len(visited)
            return win_path
           # win_path = []
           # while current is not None:
           #     win_path.append(current)
           #     current = current.parent
           # return win_path
        # [::-1]

        for move in current.all_next_state_move():
            if move.get_hash() not in visited:
                move.parent = current
                heapq.heappush(priority_queue, (move.cost, move))

    return None


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
