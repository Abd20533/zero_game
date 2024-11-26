import numpy as np
import cell_const as CC
import copy

# ⚪️


class map_state:
    parent = "root"
    cost = 0
    parent1 = None
    dim = 0
    map_not_goal = []
    # ❤️🔲
    square_white_goal = {"🟦": "🔵", "🟥": "🔴"}

    def printer(self, x, y, name_color, shape, state, covered):
        self.mymap[x][y] = CC.Const_cell(
            x, y, name_color, shape, state, covered).square_zero_info

    def rename_parent(self, name):
        self.parent = name

    def __lt__(self, other):
        # print("__lt__")
        return self.cost < other.cost

    def recost_parent(self, cost):
        self.cost = cost

    def get_hash(self):
        return hash(tuple(
            tuple((cell["name_color"], cell["shape"]) for cell in row)
            for row in self.mymap
        ))

    def get_hash1(self):
        return hash((tuple(
            (tuple((cell["name_color"], cell["shape"]) for cell in row)
             for row in self.mymap)
        )))

    def __init__(self, dim):
        self.dim = dim
        self.mymap = np.full((dim, dim), fill_value="⬜️", dtype=object)
        for i in range(0, dim):
            for j in range(0, dim):
                self.mymap[i][j] = CC.Const_cell(
                    i, j, "white", "⬜️", False, False).square_zero_info
        self. black_wall()

    def black_wall(self):

        for y in range(self.dim):
            for x in range(self.dim):

                if (x == 0):
                    self.mymap[x][y] = CC.Const_cell(
                        x, y, "black", "⬛️", False, False).square_zero_info
                if (x == self.dim-1):
                    self.mymap[x][y] = CC.Const_cell(
                        x, y, "black", "⬛️", False, False).square_zero_info
                if (y == 0):
                    self.mymap[x][y] = CC.Const_cell(
                        x, y, "black", "⬛️", False, False).square_zero_info
                if (y == self.dim-1):
                    self.mymap[x][y] = CC.Const_cell(
                        x, y, "black", "⬛️", False, False).square_zero_info

    def print_map(self):
        for row in self.mymap:
            print("".join(str(col["shape"]) for col in row))

    def print_square_white(self, x, y):
        self.mymap[x][y]["name_color"] = "white"
        self.mymap[x][y]["shape"] = "⬜️"
        self.mymap[x][y]["state"] = False
        self.mymap[x][y]["covered"] = False

    def add_square_white_to_map_not_goal_append(self, x, y, name_color, shape):
        self.map_not_goal.append(
            [x, y, name_color, shape, True, self.mymap[x][y]["covered"]])

    def add_to_map_not_goal_append(self, x, y):

        self.map_not_goal.append(
            [x, y, self.mymap[x][y]["name_color"], self.mymap[x][y]["shape"], self.mymap[x][y]["state"], self.mymap[x][y]["covered"]])

    def change_tow_squres_in_map_and_white(self, xn, xo, yn, yo):
        self.mymap[xn][yn]["name_color"] = self.mymap[xo][yo]["name_color"]
        self.mymap[xn][yn]["covered"] = True
        self.mymap[xn][yn]["state"] = False
        self.mymap[xn][yn]["shape"] = self.mymap[xo][yo]["shape"]
        self.mymap[xo][yo]["name_color"] = "white"
        self.mymap[xo][yo]["shape"] = "⬜️"
        self.mymap[xo][yo]["state"] = False
        self.mymap[xo][yo]["covered"] = False

    def is_empty_map_not_goal_append(self, x, y):
        if (len(self.map_not_goal) == 0):
            return -1
        for i in range(len(self.map_not_goal)):
            if (self.map_not_goal[i][0] == x):
                if (self.map_not_goal[i][1] == y):
                    return i
        return -1

    def squres_return_to_map(self, x, y):
        self.ind = self.is_empty_map_not_goal_append(x, y)
        if (self.ind != -1):
            # print(self.ind, "#"*40)
            self.mymap[x][y]["name_color"] = self.map_not_goal[self.ind][2]
            self.mymap[x][y]["shape"] = self.map_not_goal[self.ind][3]
            self.mymap[x][y]["state"] = True
            self.mymap[x][y]["covered"] = self.map_not_goal[self.ind][5]
            self.map_not_goal.pop(self.ind)

    def inside_map(self, i):
        if (i < self.dim and i > 0):
            return True
        else:
            return False

    def color_square(self, x, y):
        return self.mymap[x][y]["name_color"]

    def shape_square(self, x, y):
        return self.mymap[x][y]["shape"]

    def state_square(self, x, y):
        return self.mymap[x][y]["state"]

    def covered_square(self, x, y):
        return self.mymap[x][y]["covered"]

    def true_move(self, x, y, i):
        if (self.inside_map(i) and ((self.color_square(x, y) == "white") or (self.state_square(x, y) == True))):
            return True
        else:
            return False

    def condition_equle_goal_with_square(self, x1, x2, y1, y2):
        if ((self.color_square(x1, y1) == self.color_square(x2, y2)) and (self.state_square(x1, y1) != self.state_square(x2, y2))):
            return True
        else:
            return False

    def covered_to_true_or_false(self, x, y, T):
        self.mymap[x][y]["covered"] = T

    def condition_for_moving_the_previous_box(self, x, y, i):
        if (self.covered_square(x, y) == True and self.inside_map(i) and self.color_square(x, y) != "white" and self.state_square(x, y) == False):
            return True
        else:
            return False

    def move_to_down(self, x, y):
        self . i = x+1
        while (self.true_move(self.i, y, self.i)):
            if (self.state_square(self.i, y) == True):
                if ((self.shape_square(self.i, y) == "⚫️") and (self.color_square(self.i, y) == "black")):
                    self.print_square_white(self.i-1, y)
                    if (self.is_empty_map_not_goal_append(self . i-1, y) != -1):
                        self.squres_return_to_map(self . i-1, y)
                    if (self.condition_for_moving_the_previous_box(self.i-2, y, self.i-2)):
                        self.move_to_down(self.i-2, y)
                    break
                if (self.condition_equle_goal_with_square(self.i-1, self.i, y, y)):
                    self.delet_and_to_white(self.i, y, self.i-1, y)
                    if (self.is_empty_map_not_goal_append(self.i-1, y) != -1):
                        self.squres_return_to_map(self.i-1, y)
                    if (self.condition_for_moving_the_previous_box(self.i-2, y, self.i-2)):
                        self.move_to_down(self.i-2, y)
                    self.i = self.i+1

                    break
                elif ((self.shape_square(self.i, y) == "⚪️")):
                    self. add_square_white_to_map_not_goal_append(
                        self.i, y, self.mymap[self.i-1][y]["name_color"], self.square_white_goal[self.mymap[self.i-1][y]["shape"]])
                    self.change_tow_squres_in_map_and_white(
                        self . i, (self.i)-1, y, y)
                    if (self.is_empty_map_not_goal_append(self . i-1, y) != -1):
                        self.squres_return_to_map(self . i-1, y)
                    if (self.condition_for_moving_the_previous_box(self.i-2, y, self.i-2)):
                        self.move_to_down(self.i-2, y)
                    self.i = self.i+1
                else:
                    self. add_to_map_not_goal_append(self.i, y)
                    self.change_tow_squres_in_map_and_white(
                        self.i, self.i-1, y, y)

                    if (self.is_empty_map_not_goal_append((self.i)-1, y) != -1):
                        self.squres_return_to_map((self.i)-1, y)
                    self.i = self.i+1
            if ((self.shape_square(self.i, y) == "⬜️")):
                self.change_tow_squres_in_map_and_white(
                    self.i, self.i-1, y, y)
                if (self.is_empty_map_not_goal_append(self.i-1, y) != -1):
                    self.squres_return_to_map(self.i-1, y)
                if (self.condition_for_moving_the_previous_box(self.i-2, y, self.i-2)):
                    self.move_to_down(self.i-2, y)
                self.i = self.i+1
        if (self.mymap[self.i][y]["name_color"] == "black"):
            self.covered_to_true_or_false(self . i - 1, y, False)

    def move_to_Top(self, x, y):
        self . i_top = x-1
        while (self.true_move(self.i_top, y, self.i_top)):
            if (self.state_square(self.i_top, y) == True):
                if ((self.shape_square(self.i_top, y) == "⚫️") and (self.color_square(self.i_top, y) == "black")):
                    self.print_square_white(self.i_top+1, y)
                    if (self.is_empty_map_not_goal_append(self . i_top+1, y) != -1):
                        self.squres_return_to_map(self . i_top+1, y)

                    if (self.condition_for_moving_the_previous_box(self.i_top+2, y, self.i_top+2)):
                        self.move_to_Top(self.i_top+2, y)
                    break
                if ((self.shape_square(self.i_top, y) == "⚪️") and (self.color_square(self.i_top, y) == "white")):
                    self. add_square_white_to_map_not_goal_append(
                        self.i_top, y, self.mymap[self.i_top+1][y]["name_color"], self.square_white_goal[self.mymap[self.i_top+1][y]["shape"]])
                    self.change_tow_squres_in_map_and_white(
                        self . i_top, self . i_top+1, y, y)
                    if (self.is_empty_map_not_goal_append(self . i_top+1, y) != -1):
                        self.squres_return_to_map(self . i_top+1, y)

                    if (self.condition_for_moving_the_previous_box(self.i_top+2, y, self.i_top+2)):
                        self.move_to_Top(self.i_top+2, y)

                    self.i_top = self.i_top-1
                elif (self.condition_equle_goal_with_square(self.i_top+1, self.i_top, y, y)):
                    self.delet_and_to_white(self.i_top, y, self.i_top+1, y)
                    if (self.is_empty_map_not_goal_append(self.i_top+1, y) != -1):
                        self.squres_return_to_map(self.i_top+1, y)

                    if (self.condition_for_moving_the_previous_box(self.i_top+2, y, self.i_top+2)):
                        self.move_to_Top(self.i_top+2, y)
                    self.i_top = self.i_top-1
                    break
                else:
                    self. add_to_map_not_goal_append(self.i_top, y)
                    self.change_tow_squres_in_map_and_white(
                        self.i_top, self.i_top+1, y, y)

                    if (self.is_empty_map_not_goal_append((self.i_top)+1, y) != -1):
                        self.squres_return_to_map((self.i_top)+1, y)
                    if (self.condition_for_moving_the_previous_box(self.i_top+2, y, self.i_top+2)):
                        self.move_to_Top(self.i_top+2, y)
                    self.i_top = self.i_top-1
            if ((self.shape_square(self.i_top, y) == "⬜️") and (self.state_square(self.i_top, y) != True)):
                self.change_tow_squres_in_map_and_white(
                    self.i_top, self.i_top+1, y, y)
                if (self.is_empty_map_not_goal_append(self.i_top+1, y) != -1):
                    self.squres_return_to_map(self.i_top+1, y)

                if (self.condition_for_moving_the_previous_box(self.i_top+2, y, self.i_top+2)):
                    self.move_to_Top(self.i_top+2, y)
                self.i_top = self.i_top-1
        if (self.mymap[self.i_top][y]["name_color"] == "black"):
            self.covered_to_true_or_false(self . i_top + 1, y, False)

    def move_to_Right(self, x, y):
        self . i_right = y+1
        while (self.true_move(x, self.i_right, self.i_right)):
            if (self.state_square(x, self.i_right) == True):
                if ((self.shape_square(x, self.i_right) == "⚫️") and (self.color_square(x, self.i_right) == "black")):
                    self.print_square_white(x, self.i_right-1)
                    if (self.is_empty_map_not_goal_append(x, self.i_right-1) != -1):
                        self.squres_return_to_map(x, self.i_right-1)
                    if (self.condition_for_moving_the_previous_box(x, self.i_right-2, self.i_right-2)):
                        self.move_to_Right(x, self.i_right-2)
                    break
                if ((self.shape_square(x, self.i_right) == "⚪️") and (self.color_square(x, self.i_right) == "white")):
                    self. add_square_white_to_map_not_goal_append(
                        x, self.i_right, self.mymap[x][self.i_right-1]["name_color"], self.square_white_goal[self.mymap[x][self.i_right-1]["shape"]])
                    self.change_tow_squres_in_map_and_white(
                        x, x, self.i_right, self.i_right-1)

                    if (self.is_empty_map_not_goal_append(x, (self.i_right)-1) != -1):
                        self.squres_return_to_map(x, self.i_right-1)
                    if (self.condition_for_moving_the_previous_box(x, self.i_right-2, self.i_right-2)):
                        self.move_to_Right(x, self.i_right-2)
                    self.i_right = self.i_right+1
                elif (self.condition_equle_goal_with_square(x, x, self.i_right-1, self.i_right)):
                    self.delet_and_to_white(x, self.i_right, x, self.i_right-1)
                    if (self.is_empty_map_not_goal_append(x, self.i_right-1) != -1):
                        self.squres_return_to_map(x, self.i_right-1)
                    if (self.condition_for_moving_the_previous_box(x, self.i_right-2, self.i_right-2)):
                        self.move_to_Right(x, self.i_right-2)
                    self.i_right = self.i_right+1
                    break

                else:
                    self. add_to_map_not_goal_append(x, self.i_right)
                    self.change_tow_squres_in_map_and_white(
                        x, x, self.i_right, self.i_right-1)

                    if (self.is_empty_map_not_goal_append(x, (self.i_right)-1) != -1):
                        self.squres_return_to_map(x, self.i_right-1)
                    if (self.condition_for_moving_the_previous_box(x, self.i_right-2, self.i_right-2)):
                        self.move_to_Right(x, self.i_right-2)
                    self.i_right = self.i_right+1
            if (((self.shape_square(x, self.i_right) == "⬜️"))):
                self.change_tow_squres_in_map_and_white(
                    x, x, self.i_right, self.i_right-1)
                if (self.is_empty_map_not_goal_append(x, self.i_right-1) != -1):
                    self.squres_return_to_map(x, self.i_right-1)
                if (self.condition_for_moving_the_previous_box(x, self.i_right-2, self.i_right-2)):
                    self.move_to_Right(x, self.i_right-2)
                self.i_right = self.i_right+1

        if (self.mymap[x][self . i_right]["name_color"] == "black"):
            self.covered_to_true_or_false(x, self . i_right - 1, False)

    def move_to_Left(self, x, y):
        self . i_left = y-1
        self.true_move(x, self.i_left, self.i_left)
        while (self.true_move(x, self.i_left, self.i_left)):
            if (self. state_square(x, self.i_left) == True):
                if ((self.shape_square(x, self.i_left) == "⚫️") and (self.color_square(x, self.i_left) == "black")):
                    self.print_square_white(x, self.i_left+1)

                    if (self.is_empty_map_not_goal_append(x, self.i_left+1) != -1):
                        self.squres_return_to_map(x, self.i_left+1)

                    if (self.condition_for_moving_the_previous_box(x, self.i_left+2, self.i_left+2)):
                        self.move_to_Left(x, self.i_left+2)

                    break
                if ((self.shape_square(x, self.i_left) == "⚪️") and (self. color_square(x, self.i_left) == "white")):
                    self. add_square_white_to_map_not_goal_append(
                        x, self.i_left, self.mymap[x][self.i_left+1]["name_color"], self.square_white_goal[self.mymap[x][self.i_left+1]["shape"]])
                    self.change_tow_squres_in_map_and_white(
                        x, x, self.i_left, self.i_left+1)

                    if (self.is_empty_map_not_goal_append(x, (self.i_left)+1) != -1):
                        self.squres_return_to_map(x, self.i_left+1)

                    if (self.condition_for_moving_the_previous_box(x, self.i_left+2, self.i_left+2)):
                        self.move_to_Left(x, self.i_left+2)
                    self.i_left = self.i_left-1

                elif (self.condition_equle_goal_with_square(x, x, self.i_left, self.i_left+1)):
                    self.delet_and_to_white(x, self.i_left, x, self.i_left+1)

                    if (self.is_empty_map_not_goal_append(x, self.i_left+1) != -1):
                        self.squres_return_to_map(x, self.i_left+1)
                    if (self.condition_for_moving_the_previous_box(x, self.i_left+2, self.i_left+2)):
                        self.move_to_Left(x, self.i_left+2)
                    self.i_left = self.i_left-1

                    break

                else:
                    self. add_to_map_not_goal_append(x, self.i_left)
                    self.change_tow_squres_in_map_and_white(
                        x, x, self.i_left, self.i_left+1)
                    if (self.condition_for_moving_the_previous_box(x, self.i_left+2, self.i_left+2)):
                        self.move_to_Left(x, self.i_left+2)

                    if (self.is_empty_map_not_goal_append(x, (self.i_left)+1) != -1):
                        self.squres_return_to_map(x, self.i_left+1)
                    self.i_left = self.i_left-1
            if ((self.shape_square(x, self.i_left) == "⬜️") and (self.state_square(x, self.i_left) == False)):
                self.change_tow_squres_in_map_and_white(
                    x, x, self.i_left, self.i_left+1)
                if (self.is_empty_map_not_goal_append(x, self.i_left+1) != -1):
                    self.squres_return_to_map(x, self.i_left+1)
                if (self.condition_for_moving_the_previous_box(x, self.i_left+2, self.i_left+2)):
                    self.move_to_Left(x, self.i_left+2)
                self.i_left = self.i_left-1
        if (self.mymap[x][self . i_left]["name_color"] == "black"):
            self.covered_to_true_or_false(x, self . i_left + 1, False)

    def move_state(axis, state):
        next_state = copy.deepcopy(state)

        if (axis == "w"):
            next_state. rename_parent("w")
            next_state. recost_parent(state.cost+1)

            next_state .Top = next_state.all_cell_moveable()
            next_state .Top.reverse()
            for i in next_state.Top:
                next_state.move_to_Top(i[0], i[1])

        if (axis == "s"):
            next_state. rename_parent("s")
            next_state. recost_parent(state.cost+1)

            next_state .down = next_state.all_cell_moveable()
            for i in next_state.down:

                next_state.move_to_down(i[0], i[1])

        if (axis == "a"):
            next_state. rename_parent("a")
            next_state. recost_parent(state.cost+1)

            next_state .left = next_state.all_cell_moveable()
            next_state .left.reverse()
            for i in next_state.left:
                next_state.move_to_Left(i[0], i[1])

        if (axis == "d"):
            next_state. rename_parent("d")
            next_state. recost_parent(state.cost+1)

            next_state .down = next_state.all_cell_moveable()
            for i in next_state.down:
                next_state.move_to_Right(i[0], i[1])

        return next_state

    def all_next_state_move(state):
        all_next_state = np.array([])

        right = map_state.move_state("d", state)
        if (my_equals.equals(right, state) == False):
            all_next_state = np.append(all_next_state, right)

        left = map_state.move_state("a", state)
        if (my_equals.equals(state, left) == False):
            all_next_state = np.append(all_next_state, left)
        top = map_state.move_state("w", state)
        if (my_equals.equals(state, top) == False):
            all_next_state = np.append(all_next_state, top)
        down = map_state.move_state("s", state)
        if (my_equals.equals(state, down) == False):
            all_next_state = np.append(all_next_state, down)

        return all_next_state

    def move(self, axis):

        if (axis == "w"):
            self .Top = self.all_cell_moveable()
            for i in self.Top:
                self.move_to_Top(i[0], i[1])
            self.print_map()

        if (axis == "s"):
            self .down = self.all_cell_moveable()
            self .down.reverse()
            for i in self.down:

                self.move_to_down(i[0], i[1])
            self.print_map()

        if (axis == "a"):
            self .left = self.all_cell_moveable()
            self .left.reverse()
            for i in self.left:
                self.move_to_Left(i[0], i[1])
            self.print_map()

        if (axis == "d"):
            self .down = self.all_cell_moveable()
            for i in self.down:
                self.move_to_Right(i[0], i[1])
            self.print_map()

        return self.mymap

    def delet_and_to_white(self, x, y, x1, y1):
        self.mymap[x][y]["shape"] = "⬜️"
        self.mymap[x1][y1]["shape"] = "⬜️"
        self.mymap[x][y]["name_color"] = "white"
        self.mymap[x1][y1]["name_color"] = "white"
        self.mymap[x][y]["state"] = False
        self.mymap[x1][y1]["state"] = False
        self.mymap[x][y]["covered"] = False
        self.mymap[x1][y1]["covered"] = False

    def play(state):

        state.print_map()
        print("#"*50)
        if (state.you_win()):
            print("congratulations you win ")
        elif (state.you_loser()):
            print("congratulations you loser hhhhhhh")

        else:
            print(state.all_cell_moveable())
            print("please enter q to stop game:")
            print("move to left please enter a")
            print("move to right please enter d")
            print("move to top please enter w")
            print("move to down please enter s")

            move_location = str(input(" please  enter move_location  : "))
            if (move_location != "q"):
                next = map_state.move_state(move_location, state)
                map_state.play(next)

    def you_win(self):
        if (self.all_cell_gaol() == [] and self.all_cell_moveable() == []):
            return True

        else:
            return False

    def you_loser(self):
        if (self.all_cell_gaol() != [] and self.all_cell_moveable() == []):
            return True
        elif (self.all_cell_gaol() == [] and self.all_cell_moveable() != []):
            if (self.map_not_goal == []):
                return True
            if (len(self.map_not_goal) != 0):
                return False

        else:
            return False

    def all_cell_moveable(self):
        self.moveable = []
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                if ((self.mymap[i][j]["name_color"] != "white") and (self.mymap[i][j]["name_color"] != "black") and (self.mymap[i][j]["state"] == False)):
                    self.moveable.append((i, j))

        return self.moveable

    def all_cell_gaol(self):
        self.gaol = []
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                if ((self.mymap[i][j]["name_color"] != "black" and self.mymap[i][j]["state"] == True)):
                    self.gaol.append((i, j))

        return self.gaol


class my_equals:

    def equals(state1, state2):
        for i in range(len(state1.mymap)):
            for j in range(len(state1.mymap)):
                if (state1.mymap[i][j] == state2.mymap[i][j]):
                    continue
                else:
                    return False

        return True
