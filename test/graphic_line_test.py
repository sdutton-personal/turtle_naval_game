import unittest

from base_test import TurtleNavalTestBase
from src.base_graphics import GraphicLine
from src.base_graphics import GraphicPoint


class TestGraphicLines(TurtleNavalTestBase):

    __test__ = True

    def test_all_general_operation(self):
        line_1 = GraphicLine((1, 5), (5, 6))

        self.results = line_1.is_drawn
        self.expected = True
        self.run_equality_tst()

        self.results = line_1.is_intersected_by((1, 5))
        self.expected = 1
        self.run_equality_tst()

        line_2 = GraphicLine((1, 5), (5, 6), True, True)

        self.results = line_2.is_drawn
        self.expected = True
        self.run_equality_tst()

        self.results = line_2.is_intersected_by((1, 5))
        self.expected = 1
        self.run_equality_tst()

        line_3 = GraphicLine((1, 5), (5, 6), False, False)

        self.results = line_3.is_drawn
        self.expected = False
        self.run_equality_tst()

        self.results = line_3.is_intersected_by((1, 5))
        self.expected = 0
        self.run_equality_tst()

        p1 = GraphicPoint(1, 5)
        p2 = GraphicPoint(5, 6)

        line_4 = GraphicLine(p1, p2)

        self.results = line_4.is_drawn
        self.expected = True
        self.run_equality_tst()

        self.results = line_4.is_intersected_by((1, 5))
        self.expected = 1

    def test_error_conditions(self):
        with self.assertRaises(Exception):
            line_1 = GraphicLine((1, 5), 'bacdd')

        with self.assertRaises(Exception):
            line_2 = GraphicLine('bacdd', (1, 5))

        with self.assertRaises(Exception):
            line_3 = GraphicLine((1, 4, 5), (1, 5))

        with self.assertRaises(Exception):
            line_4 = GraphicLine((1, 4), (1, 5, 5))

    def test_point_location_and_expected_side_function_in_q1(self):
        # test line creation and side function in q1, (x and y both positive)
        start_pt = (10, 10)
        end_pt = (45, 45)

        # points on the line
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=start_pt, exp_y=start_pt[1], exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=end_pt, exp_y=end_pt[1], exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(22, 22), exp_y=22, exp_side=1)

        # points that do not intersect our line on the x axis at all ( y point is less than or greater than both the
        # start and the end point y values.
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(30, 9), exp_y=30, exp_side=0)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(start_pt[0], 9), exp_y=start_pt[0], exp_side=0)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(end_pt[0], 46), exp_y=end_pt[0], exp_side=0)

        # points where the x axis would intersect our line, but it is less than or greater than
        # both x points on the line
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(9, 44), exp_y=9, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(9, start_pt[0]), exp_y=9, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(46, end_pt[0]), exp_y=46, exp_side=2)

        # points where the x axis would intersect, and the x is in between our two points.
        # points on the left side
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(11, 12), exp_y=11, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(22.465, 25.507), exp_y=22.465, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(44, 44.001), exp_y=44, exp_side=1)
        # points on the right side
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(12, 11), exp_y=12, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(20, 19), exp_y=20, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(30, 11), exp_y=30, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(44, 29.985), exp_y=44, exp_side=2)

    def test_point_location_and_expected_side_function_in_q2(self):
        # test line creation and side function in q2, (x positive, y negative)
        start_pt = (-10, 10)
        end_pt = (-45, 45)

        # points on the line
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=start_pt, exp_y=start_pt[1], exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=end_pt, exp_y=end_pt[1], exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-22, 22), exp_y=22, exp_side=1)

        # points that do not intersect our line on the x axis at all ( y point is less than or greater than both the
        # start and the end point y values.
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-30, 9), exp_y=30, exp_side=0)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(start_pt[0], 9), exp_y=-start_pt[0], exp_side=0)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(end_pt[0], 46), exp_y=-end_pt[0], exp_side=0)

        # points where the x axis would intersect our line, but it is less than or greater than
        # both x points on the line
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-9, 44), exp_y=9, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-9, start_pt[1]), exp_y=9, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-46, end_pt[1]), exp_y=46, exp_side=1)

        # points where the x axis would intersect, and the x is in between our two points.
        # points on the right
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-11, 12), exp_y=11, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-22.465, 25.507), exp_y=22.465, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-44, 44.001), exp_y=44, exp_side=2)
        # points on the left
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-12, 11), exp_y=12, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-20, 19), exp_y=20, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-30, 11), exp_y=30, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-44, 29.985), exp_y=44, exp_side=1)

    def test_point_location_and_expected_side_function_in_q3(self):
        # test line creation and side function in q3, (x and y both negative)
        start_pt = (-2, -8)
        end_pt = (-12, -38)

        # points on the line
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=start_pt, exp_y=start_pt[1], exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=end_pt, exp_y=end_pt[1], exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-6, -20), exp_y=-20, exp_side=1)

        # points that do not intersect our line on the x axis at all ( y point is less than or greater than both the
        # start and the end point y values.
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-8, -7), exp_y=-26, exp_side=0)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(start_pt[0], -7), exp_y=start_pt[1], exp_side=0)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(end_pt[0], -39), exp_y=end_pt[1], exp_side=0)

        # points where the x axis would intersect our line, but it is less than or greater than
        # both x points on the line
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-1, -30), exp_y=-5, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-1, start_pt[1]), exp_y=-5, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-13, end_pt[1]), exp_y=-41, exp_side=1)

        # points where the x axis would intersect, and the x is in between our two points.
        # points on the left side
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-11, -12), exp_y=-35, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-10.465, -25.507), exp_y=-33.395, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-4, -13.001), exp_y=-14, exp_side=1)
        # points on the right side
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-3, -21), exp_y=-11, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-10, -32.5), exp_y=-32, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-7, -31), exp_y=-23, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(-5, -18), exp_y=-17, exp_side=2)

    def test_point_location_and_expected_side_function_in_q4(self):
        # test line creation and side function in q4, (x positive and y negative)
        start_pt = (5, -75)
        end_pt = (10, -25)

        # points on the line
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=start_pt, exp_y=start_pt[1], exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=end_pt, exp_y=end_pt[1], exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(6, -65), exp_y=-65, exp_side=1)

        # points that do not intersect our line on the x axis at all ( y point is less than or greater than both the
        # start and the end point y values.
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(8, -24), exp_y=-45, exp_side=0)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(start_pt[0], -24.999), exp_y=start_pt[1], exp_side=0)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(end_pt[0], -75.0001), exp_y=end_pt[1], exp_side=0)

        # points where the x axis would intersect our line, but it is less than or greater than
        # both x points on the line
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(4.999, -30), exp_y=-75.01, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(4, start_pt[1]), exp_y=-85, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(11, end_pt[1]), exp_y=-15, exp_side=2)

        # points where the x axis would intersect, and the x is in between our two points.
        # points on the left side
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(6, -64), exp_y=-65, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(7.465, -40), exp_y=-50.35, exp_side=1)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(9, -28), exp_y=-35, exp_side=1)
        # points on the right side
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(8, -50), exp_y=-45, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(9, -36.254), exp_y=-35, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(7, -56), exp_y=-55, exp_side=2)
        self.run_line_tst(start_pt=start_pt, end_pt=end_pt, test_pt=(6, -70), exp_y=-65, exp_side=2)

    def test_line_movement(self):
        start_pt = (5, -75)
        end_pt = (10, -25)
        line_1 = GraphicLine(start_pt, end_pt)

        tst_tup_1 = (7, -50)
        tst_tup_2 = (7, -60)

        self.results = line_1.is_intersected_by(tst_tup_1)
        self.expected = 1
        self.run_equality_tst()

        self.results = line_1.is_intersected_by(tst_tup_2)
        self.expected = 2
        self.run_equality_tst()

        line_1.update_line_position((4, 0), 0)

        self.results = line_1.is_intersected_by(tst_tup_1)
        self.expected = 1
        self.run_equality_tst()

        self.results = line_1.is_intersected_by(tst_tup_2)
        self.expected = 1
        self.run_equality_tst()

        line_1.update_line_position((-4, 0), 0)

        self.results = line_1.is_intersected_by(tst_tup_1)
        self.expected = 2
        self.run_equality_tst()

        self.results = line_1.is_intersected_by(tst_tup_2)
        self.expected = 2
        self.run_equality_tst()

        line_1.update_line_position((-20, 0), 30)

        self.results = line_1.is_intersected_by(tst_tup_1)
        self.expected = 1
        self.run_equality_tst()

        self.results = line_1.is_intersected_by(tst_tup_2)
        self.expected = 1
        self.run_equality_tst()

        line_1.update_line_position((0, 0), 300)

        self.results = line_1.is_intersected_by(tst_tup_1)
        self.expected = 0
        self.run_equality_tst()

        self.results = line_1.is_intersected_by(tst_tup_2)
        self.expected = 0
        self.run_equality_tst()

        line_1.update_line_position((-50, -25), 60)

        self.results = line_1.is_intersected_by(tst_tup_1)
        self.expected = 2
        self.run_equality_tst()

        self.results = line_1.is_intersected_by(tst_tup_2)
        self.expected = 0
        self.run_equality_tst()

    def test_line_movement_positions(self):
        line_1 = GraphicLine((-5, -5), (5, 5))

        self.results = line_1.start_point_cur_loc
        self.expected = (-5, -5)
        self.run_equality_tst(round_lst_tup_to=3)
        self.results = line_1.end_point_cur_loc
        self.expected = (5, 5)
        self.run_equality_tst(round_lst_tup_to=3)

        line_1.update_line_position((0, 0), 90)
        self.results = line_1.start_point_cur_loc
        self.expected = (5, -5)
        self.run_equality_tst(round_lst_tup_to=3)
        self.results = line_1.end_point_cur_loc
        self.expected = (-5, 5)
        self.run_equality_tst(round_lst_tup_to=3)

        line_1.update_line_position((0, 0), 180)
        self.results = line_1.start_point_cur_loc
        self.expected = (5, 5)
        self.run_equality_tst(round_lst_tup_to=3)
        self.results = line_1.end_point_cur_loc
        self.expected = (-5, -5)
        self.run_equality_tst(round_lst_tup_to=3)

        line_1.update_line_position((0, 0), 270)
        self.results = line_1.start_point_cur_loc
        self.expected = (-5, 5)
        self.run_equality_tst(round_lst_tup_to=3)
        self.results = line_1.end_point_cur_loc
        self.expected = (5, -5)
        self.run_equality_tst(round_lst_tup_to=3)

        line_1.update_line_position((0, 0), 360)
        self.results = line_1.start_point_cur_loc
        self.expected = (-5, -5)
        self.run_equality_tst(round_lst_tup_to=3)
        self.results = line_1.end_point_cur_loc
        self.expected = (5, 5)
        self.run_equality_tst(round_lst_tup_to=3)

        line_1.update_line_position((10, -5), 0)
        self.results = line_1.start_point_cur_loc
        self.expected = (5, -10)
        self.run_equality_tst(round_lst_tup_to=3)
        self.results = line_1.end_point_cur_loc
        self.expected = (15, 0)
        self.run_equality_tst(round_lst_tup_to=3)

        line_1.update_line_position((10, 10), 0)
        self.results = line_1.start_point_cur_loc
        self.expected = (5, 5)
        self.run_equality_tst(round_lst_tup_to=3)
        self.results = line_1.end_point_cur_loc
        self.expected = (15, 15)
        self.run_equality_tst(round_lst_tup_to=3)

if __name__ == '__main__':
    unittest.main()
