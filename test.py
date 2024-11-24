import heapq
import map_and_func as maf


def UCS(initial_state):
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


initial_state = maf.map_state(6)
initial_state.parent = "root"
initial_state.printer(1, 1, "red", "🔴", True, False)
initial_state.printer(2, 4, "red", "🟥", False, False)
initial_state.printer(1, 2, "red", "🔴", True, False)
initial_state.printer(2, 3, "red", "🟥", False, False)
solution_path = UCS(initial_state)

if solution_path:
    print("مسار الحل:")
    for state in solution_path: 
        state.print_map()  # قم بطباعة معلومات الحالة كما تريد
else:
    print("لم يتم العثور على حل.")
