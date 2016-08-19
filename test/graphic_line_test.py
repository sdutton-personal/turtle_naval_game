import unittest

from base_test import TurtleNavalTestBase
from src.graphics import GraphicLine


class TestGraphicLines(TurtleNavalTestBase):

    __test__ = True

    def test_all_general_operation(self):
        # this is basically a smoke test to see if the functions given will be called.
        line_1 = GraphicLine((10, 10), (45, 45), is_drawn=True)

        self.expected = 1
        self.results = line_1.is_intersected_by(15, 20)

        self.expected = 2
        self.results = line_1.is_intersected_by(30, 15)

        self.expected = 0
        self.results = line_1.is_intersected_by(30, 9)

        self.expected = 0
        self.results = line_1.is_intersected_by(30, 46)
