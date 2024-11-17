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
                print(current_state.parent)
                path.append(current_state.parent)
                win_path.append(current_state)
                current_state = current_state.parent1

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
initial_state.printer(5, 1, "red", "🔴", True, False)
initial_state.printer(1, 5, "red", "🟥", False, False)
initial_state.print_map()
state, path = dfs(initial_state)
print(path)
for item in state:
    item.print_map()


    
# for itme in a:
#     itme.print_map()

# # 2"""""""

# def dfs(start_state):
#     queue = qe.LifoQueue([])
#     queue = qe.LifoQueue([start_state])
#     visited = {}

#     while queue.not_empty:
#         print(1)
#         current_state = queue.get()
#         current_hash = current_state.get_hash()

#         if current_hash in visited:
#             continue

#         visited[current_hash] = True

#         if current_state.you_win():

#             win_path = []
#             path = []
#             while current_state:
#                 win_path.append(current_state)
#                 path.append(current_state.parent)

#                 current_state = current_state.parent1

#             path.reverse()
#             win_path.reverse()
#             return win_path, path

#         possible_states = current_state.all_next_state_move()

#         for next_state in possible_states:
#             next_hash = next_state.get_hash()
#             if next_hash not in visited:
#                 next_state.parent1 = current_state
#                 queue.append(next_state)

#     return None, []

# def dfs(start_state):
#     queue = qe.LifoQueue([])
#     queue = qe.LifoQueue([start_state])
#     visited = {}

#     while queue:
#         current_state = queue.get()
#         current_hash = current_state.get_hash()

#         if current_hash in visited:
#             continue

#         visited[current_hash] = True

#         if current_state.you_win():

#             win_path = []
#             path = []
#             while current_state:
#                 win_path.append(current_state)
#                 path.append(current_state.parent)

#                 current_state = current_state.parent1

#             path.reverse()
#             win_path.reverse()
#             return win_path, path

#         possible_states = current_state.all_next_state_move()

#         for next_state in possible_states:
#             next_hash = next_state.get_hash()
#             if next_hash not in visited:
#                 next_state.parent1 = current_state
#                 queue.append(next_state)

#     return None, []