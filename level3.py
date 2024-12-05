# import map_and_func as maf
from state import map_state

m = map_state(10, 10)

# m.printer(1, 3, "red", "🔴", True, False)
# m.printer(3, 5, "blue", "🔵", True, False)
m.printer(3, 4, "blue", "🔵", True, False)

# m.printer(2, 4, "red", "🟥", False, False)
# m.printer(2, 4, "blue", "🟦", False, False)

m.printer(1, 1, "blue", "🟦", False, False)
m.printer(2, 1, "blue", "🟦", False, False)
m.printer(3, 1, "blue", "🟦", False, False)

# m.printer(1, 1, "blue", "🟦", False, False)
# m.printer(1, 2, "blue", "🟦", False, False)
# m.printer(1, 4, "blue", "🟦", False, False)
print("num is : ", m.all_cell_moveable_in_Row(1, 0))
# m.row_printer_black(4, 1, 9)
# m.printer(3, 2, "black", "⬛️", False, False)
# m.printer(3, 3, "black", "⬛️", False, False)

map_state.play(m)
