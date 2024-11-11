# import map_and_func as maf
from map_and_func import map_state

m = map_state(8)
m.printer(2, 2, "black", "⬛️", False, False)
m.printer(2, 2, "black", "⬛️", False, False)
m.printer(2, 1, "black", "⬛️", False, False)
m.printer(3, 2, "black", "⬛️", False, False)
m.printer(4, 2, "black", "⬛️", False, False)

m.printer(5, 1, "red", "🔴", True, False)
# m.printer(5, 6, "blue", "🔵", True, False)
m.printer(4, 3, "white", "⚪️", True, False)
m.printer(4, 5, "red", "🔴", True, False)

# m.printer(6, 3, "black", "⚫️", True, False)


m.printer(2, 3, "red", "🟥", False, False)
m.printer(4, 1, "red", "🟥", False, False)

# m.printer(2, 4, "blue", "🟦", False, False)
map_state.play(m)
