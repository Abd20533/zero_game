# import map_and_func as maf
from state import map_state
initial_state = map_state(7, 16)
initial_state.parent = "root"
initial_state. row_printer_black(1, 1, 5)
initial_state. row_printer_black(1, 8, 11)
initial_state. row_printer_black(1, 12, 14)

initial_state.printer(2, 6, "black", "⬛️", False, False)
initial_state.printer(3, 12, "black", "⬛️", False, False)

initial_state. row_printer_black(4, 1, 5)
initial_state. row_printer_black(4, 6, 8)
initial_state. row_printer_black(4, 9, 15)
initial_state. row_printer_black(5, 1, 8)
initial_state. row_printer_black(5, 9, 15)
initial_state. row_printer_black(6, 1, 15)


initial_state.printer(3, 1, "orange", "🟧", False, False)
initial_state.printer(2, 2, "blue", "🟦", False, False)
initial_state.printer(2, 1, "red", "🟥", False, False)
initial_state.printer(2, 3, "green", "🟩", False, False)
initial_state.printer(3, 2, "yelow", "🟨", False, False)


initial_state.printer(4, 5, "red", "🔴", True, False)
initial_state.printer(1, 7, "yelow", "🟡", True, False)
initial_state.printer(4, 8, "blue", "🔵", True, False)
initial_state.printer(1, 11, "orange", "🟠", True, False)

initial_state.printer(1, 14, "green", "🟢", True, False)
initial_state.printer(5, 8, "black", "⚫️", True, False)

map_state.play(initial_state)
