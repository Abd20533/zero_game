
import cell_const as CC


class my_color_Squres:
    def __init__(self, x, y, name_color, shape, state, covered, state_true_or_false):
        self.square_zero_info = CC.Const_cell(x,  y,
                                              name_color,  shape, state, covered).square_zero_info
        self.square_zero_info.update({"state": state_true_or_false})

