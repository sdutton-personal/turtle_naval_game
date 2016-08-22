import unittest

from base_test import TurtleNavalTestBase
from src.graphics import GraphicLine


class TestGraphicLines(TurtleNavalTestBase):

    __test__ = True
    expected_line_y_intersect = None

    def test_all_general_operation(self):
        pass

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



if __name__ == '__main__':
    unittest.main()
