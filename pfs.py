
from collections import deque
import queue as queue
import map_and_func as maf


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
                # print(path)
            path.reverse()
            win_path.reverse()
            return win_path, path

        possible_states = current_state.all_next_state_move()

        for next_state in possible_states:
            next_hash = next_state.get_hash()
            if next_hash not in visited:
                next_state.parent1 = current_state
                queue.append(next_state)

    return None, []


initial_state = maf. map_state(8)
# initial_state.parent = "root"
# initial_state.printer(6, 5, "blue", "🔵", True, False)
# initial_state.printer(4, 1, "blue", "🔵", True, False)

# initial_state.printer(6, 1, "white", "⚪️", True, False)
# initial_state.printer(5, 3, "black", "⬛️", False, False)

# initial_state.printer(5, 1, "blue", "🟦", False, False)

initial_state.printer(1, 1, "red", "🔴", True, False)
initial_state.printer(5, 5, "red", "🟥", False, False)
# initial_state.printer(4, 5, "blue", "🟦", False, False)
initial_state.print_map()

a, path = bfs(initial_state)
print(path)
for itme in a:
    itme.print_map()
