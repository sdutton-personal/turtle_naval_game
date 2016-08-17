
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

        self.expected = 63.6396
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
        self.round_list_or_tup_of_results_and_expected(5)
        self.run_equality_tst()
