import unittest

from base_test import TurtleNavalTestBase
from src.graphics import GraphicPoint


class TestGraphicPoints(TurtleNavalTestBase):

    __test__ = True

    def test_all_general_operation(self):
        # this is basically a smoke test to see if the functions given will be called.
        point_1 = GraphicPoint(45, 45)

        self.expected = 45.0
        self.results = point_1.init_angle_offset
        self.run_equality_tst(round_to=3)

        self.expected = 63.64
        self.results = point_1.init_distance
        self.run_equality_tst(round_to=3)

        self.expected = 45.0
        self.results = point_1.zero_adjusted_angle
        self.run_equality_tst(round_to=3)

        self.expected = (1, 1)
        self.results = point_1.quadrant_adjustment_tup
        self.run_equality_tst()

        self.expected = (45, 45)
        self.results = point_1.current_pos
        self.run_equality_tst(round_lst_tup_to=3)

    def test_check_heading_at_all_4_quadrants(self):
        # tests the heading calculation only, no movement
        point_1 = GraphicPoint(100, 100)

        self.expected = (-100, 100)
        self.results = point_1.update_point_position((0, 0), 90)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-100, -100)
        self.results = point_1.update_point_position((0, 0), 180)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (100, -100)
        self.results = point_1.update_point_position((0, 0), 270)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (100, 100)
        self.results = point_1.update_point_position((0, 0), 360)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_movement_change_only_no_heading_change(self):
        point_1 = GraphicPoint(100, 100)

        self.expected = (110, 115)
        self.results = point_1.update_point_position((10, 15), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (200, 80)
        self.results = point_1.update_point_position((100, -20), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (100, -100)
        self.results = point_1.update_point_position((0, -200), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (50, 0)
        self.results = point_1.update_point_position((-50, -100), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (95, 99)
        self.results = point_1.update_point_position((-5, -1), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (100, 100)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_heading_and_movement_change(self):
        point_1 = GraphicPoint(10, 10)

        self.expected = (10, 10)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (58.112, 61.585)
        self.results = point_1.update_point_position((50, 50), 10)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (1.888, 61.585)
        self.results = point_1.update_point_position((10, 50), 80)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-12.817, 95.977)
        self.results = point_1.update_point_position((0, 90), 110)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (21.585, -21.888)
        self.results = point_1.update_point_position((10, -30), 350)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-51.233, -64.088)
        self.results = point_1.update_point_position((-50, -50), 220)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_non_equal_starting_points_init_q1(self):
        point_1 = GraphicPoint(11, 3)

        self.expected = 15.255
        self.results = point_1.init_angle_offset
        self.run_equality_tst(round_to=3)

        self.expected = 11.402
        self.results = point_1.init_distance
        self.run_equality_tst(round_to=3)

        self.expected = 15.255
        self.results = point_1.zero_adjusted_angle
        self.run_equality_tst(round_to=3)

        self.expected = (1, 1)
        self.results = point_1.quadrant_adjustment_tup
        self.run_equality_tst()

        self.expected = (11, 3)
        self.results = point_1.current_pos
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (11, 3)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        point_2 = GraphicPoint(4, 80)

        self.expected = 87.138
        self.results = point_2.init_angle_offset
        self.run_equality_tst(round_to=3)

        self.expected = 80.1
        self.results = point_2.init_distance
        self.run_equality_tst(round_to=3)

        self.expected = 87.138
        self.results = point_2.zero_adjusted_angle
        self.run_equality_tst(round_to=3)

        self.expected = (1, 1)
        self.results = point_2.quadrant_adjustment_tup
        self.run_equality_tst()

        self.expected = (4, 80)
        self.results = point_2.current_pos
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (4, 80)
        self.results = point_2.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_non_equal_starting_points_init_q2(self):
        point_1 = GraphicPoint(-11, 3)

        self.expected = 164.745
        self.results = point_1.init_angle_offset
        self.run_equality_tst(round_to=3)

        self.expected = 11.402
        self.results = point_1.init_distance
        self.run_equality_tst(round_to=3)

        self.expected = 15.255
        self.results = point_1.zero_adjusted_angle
        self.run_equality_tst(round_to=3)

        self.expected = (-1, 1)
        self.results = point_1.quadrant_adjustment_tup
        self.run_equality_tst()

        self.expected = (-11, 3)
        self.results = point_1.current_pos
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-11, 3)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        point_2 = GraphicPoint(-3, 11)

        self.expected = 105.255
        self.results = point_2.init_angle_offset
        self.run_equality_tst(round_to=3)

        self.expected = 11.402
        self.results = point_2.init_distance
        self.run_equality_tst(round_to=3)

        self.expected = 74.745
        self.results = point_2.zero_adjusted_angle
        self.run_equality_tst(round_to=3)

        self.expected = (-1, 1)
        self.results = point_2.quadrant_adjustment_tup
        self.run_equality_tst()

        self.expected = (-3, 11)
        self.results = point_2.current_pos
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-3, 11)
        self.results = point_2.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_non_equal_starting_points_init_q3(self):
        point_1 = GraphicPoint(-20, -6)

        self.expected = 196.699
        self.results = point_1.init_angle_offset
        self.run_equality_tst(round_to=3)

        self.expected = 20.881
        self.results = point_1.init_distance
        self.run_equality_tst(round_to=3)

        self.expected = 16.699
        self.results = point_1.zero_adjusted_angle
        self.run_equality_tst(round_to=3)

        self.expected = (-1, -1)
        self.results = point_1.quadrant_adjustment_tup
        self.run_equality_tst()

        self.expected = (-20, -6)
        self.results = point_1.current_pos
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-20, -6)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        point_2 = GraphicPoint(-5, -20)

        self.expected = 255.964
        self.results = point_2.init_angle_offset
        self.run_equality_tst(round_to=3)

        self.expected = 20.616
        self.results = point_2.init_distance
        self.run_equality_tst(round_to=3)

        self.expected = 75.964
        self.results = point_2.zero_adjusted_angle
        self.run_equality_tst(round_to=3)

        self.expected = (-1, -1)
        self.results = point_2.quadrant_adjustment_tup
        self.run_equality_tst()

        self.expected = (-5, -20)
        self.results = point_2.current_pos
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-5, -20)
        self.results = point_2.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_non_equal_starting_points_init_q4(self):
        point_1 = GraphicPoint(2, -10)

        self.expected = 281.310
        self.results = point_1.init_angle_offset
        self.run_equality_tst(round_to=3)

        self.expected = 10.198
        self.results = point_1.init_distance
        self.run_equality_tst(round_to=3)

        self.expected = 78.69
        self.results = point_1.zero_adjusted_angle
        self.run_equality_tst(round_to=3)

        self.expected = (1, -1)
        self.results = point_1.quadrant_adjustment_tup
        self.run_equality_tst()

        self.expected = (2, -10)
        self.results = point_1.current_pos
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (2, -10)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        point_2 = GraphicPoint(9, -.056)

        self.expected = 359.643
        self.results = point_2.init_angle_offset
        self.run_equality_tst(round_to=3)

        self.expected = 9.0001
        self.results = point_2.init_distance
        self.run_equality_tst(round_to=3)

        self.expected = .357
        self.results = point_2.zero_adjusted_angle
        self.run_equality_tst(round_to=3)

        self.expected = (1, -1)
        self.results = point_2.quadrant_adjustment_tup
        self.run_equality_tst()

        self.expected = (9, -.056)
        self.results = point_2.current_pos
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (9, -.056)
        self.results = point_2.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_heading_and_movement_change_q1(self):
        point_1 = GraphicPoint(3, 15)

        self.expected = (3, 15)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (6.38, 44.862)
        self.results = point_1.update_point_position((10, 30), 25)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-25.293, 1.35)
        self.results = point_1.update_point_position((-10, 1), 100)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-15.681, -115.204)
        self.results = point_1.update_point_position((-14, -100), 185)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (34.204, -51.681)
        self.results = point_1.update_point_position((19, -50), 275)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_heading_and_movement_change_q2(self):
        point_1 = GraphicPoint(-13, 15)

        self.expected = (-13, 15)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-8.121, 38.101)
        self.results = point_1.update_point_position((10, 30), 25)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-22.515, -14.407)
        self.results = point_1.update_point_position((-10, 1), 100)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (0.258, -127.62)
        self.results = point_1.update_point_position((-14, -113.81), 185)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (32.81, -35.742)
        self.results = point_1.update_point_position((19, -50), 275)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_heading_and_movement_change_q3(self):
        point_1 = GraphicPoint(-1, -3)

        self.expected = (-1, -3)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (7.362, 28.858)
        self.results = point_1.update_point_position((7, 32), 25)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-6.872, 0.536)
        self.results = point_1.update_point_position((-10, 1), 100)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-13.265, -110.734)
        self.results = point_1.update_point_position((-14, -113.81), 185)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (15.924, -49.265)
        self.results = point_1.update_point_position((19, -50), 275)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_heading_and_movement_change_q4(self):
        point_1 = GraphicPoint(1, -2)

        self.expected = (1, -2)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (8.752, 30.61)
        self.results = point_1.update_point_position((7, 32), 25)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-8.204, 2.332)
        self.results = point_1.update_point_position((-10, 1), 100)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-15.171, -111.905)
        self.results = point_1.update_point_position((-14, -113.81), 185)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (17.095, -51.171)
        self.results = point_1.update_point_position((19, -50), 275)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_0_0(self):
        point_1 = GraphicPoint(0, 0)
        self.expected = (0, 0)
        self.results = point_1.update_point_position((0, 0), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (10, -140)
        self.results = point_1.update_point_position((10, -140), 60)
        self.run_equality_tst(round_lst_tup_to=3)

    def test_0_points(self):
        point_1 = GraphicPoint(15, 0)
        self.expected = (25, 20)
        self.results = point_1.update_point_position((10, 20), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (20.607, 30.607)
        self.results = point_1.update_point_position((10, 20), 45)
        self.run_equality_tst(round_lst_tup_to=3)

        point_2 = GraphicPoint(0, -20)
        self.expected = (10, -40)
        self.results = point_2.update_point_position((10, -20), 0)
        self.run_equality_tst(round_lst_tup_to=3)

        self.expected = (-5.176, -39.319)
        self.results = point_2.update_point_position((0, -20), 345)
        self.run_equality_tst(round_lst_tup_to=3)


if __name__ == '__main__':
    unittest.main()
