# import map_and_func as maf
from state import map_state

m = map_state(7)

m.printer(2, 3, "red", "🔴", True, False)
m.printer(3, 5, "blue", "🔵", True, False)
m.printer(4, 4, "red", "🟥", False, False)
m.printer(2, 4, "blue", "🟦", False, False)
m.printer(3, 2, "black", "⬛️", False, False)
m.printer(3, 3, "black", "⬛️", False, False)

map_state.play(m)
