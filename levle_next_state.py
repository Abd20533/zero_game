# import map_and_func as maf
from state import map_state

m = map_state(7)

m.printer(2, 3, "red", "🔴", True, False)
m.printer(3, 4, "blue", "🔵", True, False)
m.printer(4, 5, "red", "🟥", False, False)
m.printer(2, 5, "blue", "🟦", False, False)
# map_state.play(m)

s = map_state.all_next_state_move(m)
print("state old")
m.print_map()
for i in s:
    i.print_map()
    print("#"*50)
