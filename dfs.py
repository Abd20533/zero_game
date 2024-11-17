import queue as qe
import map_and_func as maf


def dfs(initial_state):
    stack = [initial_state]
    visited = {initial_state.get_hash(): True}

    while stack:
        current_state = stack.pop()

        if current_state.you_win():
            win_path = []
            path = []
            while current_state:
                path.append(current_state.parent)
                win_path.append(current_state)
                current_state = current_state.parent1
            path.reverse()
            return win_path[::-1], path

        for move in current_state.all_next_state_move():
            move_hash = move.get_hash()
            if move_hash not in visited:  # Check if already visited
                visited[move_hash] = True

                stack.append(move)
            move.parent1 = current_state
            # move.parent = current_state

    return None


initial_state = maf. map_state(8)
initial_state.parent = "root"
initial_state.printer(1, 1, "red", "🔴", True, False)
initial_state.printer(5, 1, "white", "⚪️", True, False)

initial_state.printer(1, 5, "red", "🟥", False, False)
initial_state.printer(5, 5, "red", "🟥", False, False)

initial_state.print_map()
state, path = dfs(initial_state)
print(path)
for item in state:
    item.print_map()
