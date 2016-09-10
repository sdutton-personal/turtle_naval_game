import unittest

from base_test import TurtleNavalTestBase
from src.graphics import GraphicLine
from src.graphics import GraphicPoint
from src.graphics import GraphicShape
from src.graphics import HullShape
from src.graphics import BowShape
from src.graphics import SternShape


class TestGraphicShape(TurtleNavalTestBase):

    __test__ = True

    def setUp(self):
        self.length = 100
        self.width = 20
        self.hull_to_bow_scale = 5
        self.x_max = 500
        self.y_max = 300

    def test_general_operation(self):
        # smoke test

        bow = BowShape(self.length, self.width, self.hull_to_bow_scale)
        stern = SternShape(self.length, self.width, self.hull_to_bow_scale)
        hull = HullShape(self.length, self.width, self.hull_to_bow_scale)

        self.width = float(self.width)
        self.length = float(self.length)
        self.hull_to_bow_scale = float(self.hull_to_bow_scale)

        self.expected = [(self.width / 2, self.length / self.hull_to_bow_scale),
                         (0, self.length / 2),
                         (-self.width / 2, self.length / self.hull_to_bow_scale)]
        self.results = bow.points_to_draw_lst
        self.run_equality_tst()

        self.expected = [(-self.width / 2, self.length / self.hull_to_bow_scale),
                         (-self.width / 2, -self.length / self.hull_to_bow_scale),
                         (self.width / 2, -self.length / self.hull_to_bow_scale),
                         (self.width / 2, self.length / self.hull_to_bow_scale)]

        self.results = hull.points_to_draw_lst
        self.run_equality_tst()

        self.expected = [(self.width / 2, -self.length / self.hull_to_bow_scale),
                         (round(self.width / 3, 5), -self.length / 2.5),
                         (round(-self.width / 3, 5), -self.length / 2.5),
                         (-self.width / 2, -self.length / self.hull_to_bow_scale)]

        self.results = stern.points_to_draw_lst
        self.run_equality_tst()

        self.expected = False
        self.results = bow.is_shape_out_of_bounds()
        self.run_equality_tst()

        self.expected = False
        self.results = hull.is_shape_out_of_bounds()
        self.run_equality_tst()

        self.expected = False
        self.results = stern.is_shape_out_of_bounds()
        self.run_equality_tst()

        self.results = bow.is_point_inside_shape((1, 1))
        self.expected = False
        self.run_equality_tst()

        self.results = hull.is_point_inside_shape((1, 1))
        self.expected = True
        self.run_equality_tst()

        self.results = stern.is_point_inside_shape((1, 1))
        self.expected = False
        self.run_equality_tst()

        bow.update_shape_position((10, 10), 40)
        hull.update_shape_position((10, 10), 40)
        stern.update_shape_position((10, 10), 40)

    def test_scale_args(self):
        hull_to_bow_scale = 2

        # scale is default, so it is 0, hull to bow scale is 2
        bow = BowShape(self.length, self.width, hull_to_bow_scale)
        hull = HullShape(self.length, self.width, hull_to_bow_scale)
        stern = SternShape(self.length, self.width, hull_to_bow_scale)

        self.results = bow.points_to_draw_lst
        self.expected = [(10.0, 50.0), (0.0, 50.0), (-10.0, 50.0)]
        self.run_equality_tst()

        self.results = hull.points_to_draw_lst
        self.expected = [(-10.0, 50.0), (-10.0, -50.0), (10.0, -50.0), (10.0, 50.0)]
        self.run_equality_tst()

        self.results = stern.points_to_draw_lst
        self.expected = [(10.0, -50.0), (6.66667, -40.0), (-6.66667, -40.0), (-10.0, -50.0)]
        self.run_equality_tst()

        scale = 50
        # scale is 50, so shape will be 50 larger
        bow = BowShape(self.length, self.width, hull_to_bow_scale, scale)
        hull = HullShape(self.length, self.width, hull_to_bow_scale, scale)
        stern = SternShape(self.length, self.width, hull_to_bow_scale, scale)

        self.results = bow.points_to_draw_lst
        self.expected = [(15.0, 75.0), (0.0, 75.0), (-15.0, 75.0)]
        self.run_equality_tst()

        self.results = hull.points_to_draw_lst
        self.expected = [(-15.0, 75.0), (-15.0, -75.0), (15.0, -75.0), (15.0, 75.0)]
        self.run_equality_tst()

        self.results = stern.points_to_draw_lst
        self.expected = [(15.0, -75.0), (10.0, -60.0), (-10.0, -60.0), (-15.0, -75.0)]
        self.run_equality_tst()

        scale = -50
        # scale is -50, so shape will be 50% smaller
        bow = BowShape(self.length, self.width, hull_to_bow_scale, scale)
        hull = HullShape(self.length, self.width, hull_to_bow_scale, scale)
        stern = SternShape(self.length, self.width, hull_to_bow_scale, scale)

        self.results = bow.points_to_draw_lst
        self.expected = [(5.0, 25.0), (0.0, 25.0), (-5.0, 25.0)]
        self.run_equality_tst()

        self.results = hull.points_to_draw_lst
        self.expected = [(-5.0, 25.0), (-5.0, -25.0), (5.0, -25.0), (5.0, 25.0)]
        self.run_equality_tst()

        self.results = stern.points_to_draw_lst
        self.expected = [(5.0, -25.0), (3.33333, -20.0), (-3.33333, -20.0), (-5.0, -25.0)]
        self.run_equality_tst()

        hull_to_bow_scale = 10

        # scale is default, so it is 0, hull to bow scale is 10.  This increases the size of the bow and decreases the
        # size of the hull
        bow = BowShape(self.length, self.width, hull_to_bow_scale)
        hull = HullShape(self.length, self.width, hull_to_bow_scale)
        stern = SternShape(self.length, self.width, hull_to_bow_scale)

        self.results = bow.points_to_draw_lst
        self.expected = [(10.0, 10.0), (0.0, 50.0), (-10.0, 10.0)]
        self.run_equality_tst()

        self.results = hull.points_to_draw_lst
        self.expected = [(-10.0, 10.0), (-10.0, -10.0), (10.0, -10.0), (10.0, 10.0)]
        self.run_equality_tst()

        self.results = stern.points_to_draw_lst
        self.expected = [(10.0, -10.0), (6.66667, -40.0), (-6.66667, -40.0), (-10.0, -10.0)]
        self.run_equality_tst()

    def test_boundary_args(self):
        x_max = 200
        y_max = 200
        bow = BowShape(self.length, self.width, self.hull_to_bow_scale)
        hull = HullShape(self.length, self.width, self.hull_to_bow_scale)
        stern = SternShape(self.length, self.width, self.hull_to_bow_scale)

        # no boundary set, boundary will always be 0
        self.results = bow.x_boundary
        self.expected = 0
        self.run_equality_tst()

        self.results = bow.y_boundary
        self.expected = 0
        self.run_equality_tst()

        self.results = hull.x_boundary
        self.expected = 0
        self.run_equality_tst()

        self.results = hull.y_boundary
        self.expected = 0
        self.run_equality_tst()

        self.results = stern.x_boundary
        self.expected = 0
        self.run_equality_tst()

        self.results = stern.y_boundary
        self.expected = 0
        self.run_equality_tst()

        bow = BowShape(self.length, self.width, self.hull_to_bow_scale, x_boundary=x_max)
        hull = HullShape(self.length, self.width, self.hull_to_bow_scale, x_boundary=x_max)
        stern = SternShape(self.length, self.width, self.hull_to_bow_scale, x_boundary=x_max)

        # x boundary should be x max
        self.results = bow.x_boundary
        self.expected = x_max
        self.run_equality_tst()

        self.results = bow.y_boundary
        self.expected = 0
        self.run_equality_tst()

        self.results = hull.x_boundary
        self.expected = x_max
        self.run_equality_tst()

        self.results = hull.y_boundary
        self.expected = 0
        self.run_equality_tst()

        self.results = stern.x_boundary
        self.expected = x_max
        self.run_equality_tst()

        self.results = stern.y_boundary
        self.expected = 0
        self.run_equality_tst()

        bow = BowShape(self.length, self.width, self.hull_to_bow_scale, x_boundary=x_max, y_boundary=y_max)
        hull = HullShape(self.length, self.width, self.hull_to_bow_scale, x_boundary=x_max, y_boundary=y_max)
        stern = SternShape(self.length, self.width, self.hull_to_bow_scale, x_boundary=x_max, y_boundary=y_max)

        # x boundary should be x max, y boundary should be y max
        self.results = bow.x_boundary
        self.expected = x_max
        self.run_equality_tst()

        self.results = bow.y_boundary
        self.expected = y_max
        self.run_equality_tst()

        self.results = hull.x_boundary
        self.expected = x_max
        self.run_equality_tst()

        self.results = hull.y_boundary
        self.expected = y_max
        self.run_equality_tst()

        self.results = stern.x_boundary
        self.expected = x_max
        self.run_equality_tst()

        self.results = stern.y_boundary
        self.expected = y_max
        self.run_equality_tst()

        bow = BowShape(self.length, self.width, self.hull_to_bow_scale, y_boundary=y_max)
        hull = HullShape(self.length, self.width, self.hull_to_bow_scale, y_boundary=y_max)
        stern = SternShape(self.length, self.width, self.hull_to_bow_scale, y_boundary=y_max)

        # x boundary should be x max, y boundary should be y max
        self.results = bow.x_boundary
        self.expected = 0
        self.run_equality_tst()

        self.results = bow.y_boundary
        self.expected = y_max
        self.run_equality_tst()

        self.results = hull.x_boundary
        self.expected = 0
        self.run_equality_tst()

        self.results = hull.y_boundary
        self.expected = y_max
        self.run_equality_tst()

        self.results = stern.x_boundary
        self.expected = 0
        self.run_equality_tst()

        self.results = stern.y_boundary
        self.expected = y_max
        self.run_equality_tst()

    def test_is_point_inside_shape_bow(self):
        points_in_shape_lst = [(21, 9), (20.01111, 9.955), (20.01111, -9.955), (40, 0), (35, 4), (35, -2)]
        points_out_of_shape_lst = [(19.99, 0), (19.99, 9), (19.99, -9), (35, 8), (35, -8), (51, 0)]
        bow = BowShape(self.length, self.width, self.hull_to_bow_scale)
        self.tst_points_for_existence_in_shape(bow, points_in_shape_lst, points_out_of_shape_lst)

        bow.update_shape_position((-10, -10), 0)
        points_in_shape_lst = [(11, -1), (10.01111, -.045), (10.01111, -19.955), (30, -10)]
        points_out_of_shape_lst = [(9.99, -10), (9.99, -1), (9.99, -19), (25, -2), (25, -18), (41, -10)]
        self.tst_points_for_existence_in_shape(bow, points_in_shape_lst, points_out_of_shape_lst)

        bow.update_shape_position((0, 0), 90)
        points_in_shape_lst = [(9, 21), (9.955, 20.01111), (-9.955, 20.01111), (0, 40)]
        points_out_of_shape_lst = [(0, 19.99), (9, 19.99), (-9, 19.99), (8, 35), (-8, 35), (0, 51)]
        self.tst_points_for_existence_in_shape(bow, points_in_shape_lst, points_out_of_shape_lst)

    def test_is_point_inside_shape_hull(self):
        points_in_shape_lst = [(19.99, 9.99), (19.99, -9.99), (-19.99, 9.99), (-19.99, -9.99), (0, 0), (0, 5), (19.99, 0)]
        points_out_of_shape_lst = [(20.1, 0), (0, 10.4), (23, 4), (3, -12), (-30, -8), (-5, -29), (-6, 13)]
        hull = HullShape(self.length, self.width, self.hull_to_bow_scale)
        self.tst_points_for_existence_in_shape(hull, points_in_shape_lst, points_out_of_shape_lst)

        hull.update_shape_position((20, -10), 90)
        points_in_shape_lst = [(10.1, 9.99), (29.99, 9.99), (10.1, -29.99), (29.99, -29.99), (20, 0), (30, 10), (20, -10)]
        points_out_of_shape_lst = [(0, 0), (9, 9), (11, 11), (9, 0), (31, 0), (20, -31), (31, -20), (-20, -10)]
        self.tst_points_for_existence_in_shape(hull, points_in_shape_lst, points_out_of_shape_lst)

        hull.update_shape_position((2, 2), 63.4)
        points_in_shape_lst = [(2, 23), (19, 15.4), (1.98, -20), (-15.8, -11.4), (0, 0), (-5, 0), (0, 5), (10, 12), (-10, -13), (-6, 7), (4, -2)]
        points_out_of_shape_lst = [(-10.5, 0), (12.5, 0), (-8, 10), (-12, -18), (10, -5), (4, 23.5), (0, 24), (0, -20)]
        self.tst_points_for_existence_in_shape(hull, points_in_shape_lst, points_out_of_shape_lst)

if __name__ == '__main__':
    unittest.main()
