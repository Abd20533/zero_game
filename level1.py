# import map_and_func as maf
from state import map_state

m = map_state(10)
m.printer(2, 2, "black", "⬛️", False, False)
m.printer(2, 2, "black", "⬛️", False, False)
m.printer(2, 1, "black", "⬛️", False, False)
m.printer(3, 2, "black", "⬛️", False, False)
m.printer(4, 2, "black", "⬛️", False, False)
m.printer(5, 2, "black", "⬛️", False, False)
m.printer(6, 2, "black", "⬛️", False, False)
m.printer(6, 2, "black", "⬛️", False, False)
m.printer(6, 3, "black", "⬛️", False, False)
m.printer(6, 4, "black", "⬛️", False, False)
m.printer(6, 5, "black", "⬛️", False, False)
m.printer(6, 6, "black", "⬛️", False, False)
m.printer(6, 7, "black", "⬛️", False, False)
m.printer(6, 8, "black", "⬛️", False, False)
m.printer(5, 7, "red", "🔴", True, False)
m.printer(5, 6, "blue", "🔵", True, False)
m.printer(4, 7, "red", "🟥", False, False)
m.printer(2, 4, "blue", "🟦", False, False)
map_state.play(m)

