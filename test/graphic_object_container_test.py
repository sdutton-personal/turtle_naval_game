import unittest

from base_test import TurtleNavalTestBase
import src.base_graphics as bg
from src.base_graphics import GraphicObjectContainer


class TestGraphicShape(TurtleNavalTestBase):

    __test__ = True

    def test_offset_1(self):
        distance_to_boundary, angle = (30, 45)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = 30.0
        self.run_equality_tst(round_to=5)

    def test_offset_2(self):
        distance_to_boundary, angle = (30, 10)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = 5.2898
        self.run_equality_tst(round_to=3)

    def test_offset_3(self):
        distance_to_boundary, angle = (30, 26.565)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = 15
        self.run_equality_tst(round_to=3)

    def test_offset_4(self):
        distance_to_boundary, angle = (30, 63.435)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = 60
        self.run_equality_tst(round_to=3)

    def test_offset_5(self):
        distance_to_boundary, angle = (-30, 10)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = -5.2898
        self.run_equality_tst(round_to=3)

    def test_offset_6(self):
        distance_to_boundary, angle = (30, 0)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = 0
        self.run_equality_tst(round_to=3)

    def test_offset_7(self):
        distance_to_boundary, angle = (10, 5)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = 0.8748
        self.run_equality_tst(round_to=3)

    def test_offset_8(self):
        distance_to_boundary, angle = (50, 80)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = 283.5640
        self.run_equality_tst(round_to=3)

    def test_offset_9(self):
        distance_to_boundary, angle = (100, 40)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = 83.9099
        self.run_equality_tst(round_to=3)

    def test_offset_10(self):
        distance_to_boundary, angle = (100, 90)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = 0
        self.run_equality_tst(round_to=3)

    def test_offset_11(self):
        distance_to_boundary, angle = (0, 89)
        self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)
        self.expected = 0
        self.run_equality_tst(round_to=3)

    def test_offset_12(self):
        distance_to_boundary, angle = (None, 89)
        with self.assertRaises(Exception):
            self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)

    def test_offset_13(self):
        distance_to_boundary, angle = (10, None)
        with self.assertRaises(Exception):
            self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)

    def test_offset_14(self):
        distance_to_boundary, angle = ('abcd', 89)
        with self.assertRaises(Exception):
            self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)

    def test_offset_15(self):
        distance_to_boundary, angle = (12, 'ddff')
        with self.assertRaises(Exception):
            self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)

    def test_offset_16(self):
        distance_to_boundary, angle = ([1], 89)
        with self.assertRaises(Exception):
            self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)

    def test_offset_17(self):
        distance_to_boundary, angle = (32, [2])
        with self.assertRaises(Exception):
            self.results = bg.get_opposite_given_angle_and_adjacent(distance_to_boundary, angle)

if __name__ == '__main__':
    unittest.main()