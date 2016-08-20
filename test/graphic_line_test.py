import unittest

from base_test import TurtleNavalTestBase
from src.graphics import GraphicLine


class TestGraphicLines(TurtleNavalTestBase):

    __test__ = True
    expected_line_y_intersect = None

    def test_all_general_operation(self):
        pass

    def test_point_location_and_expected_side_function_in_q1(self):
        # this is basically a smoke test to see if the functions given will be called.
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


