import turtle

from base_graphics import GraphicPoint
from base_graphics import GraphicLine
from base_graphics import GraphicShape
from base_graphics import BaseBoat


class BowShape(GraphicShape):

    fill_color = 'gray'
    line_color = 'black'

    def load_graphic_lines(self):
        bow_port_point = GraphicPoint(self._scale_length / self._shape_to_overall_scale, self._scale_width / 2)
        bow_point = GraphicPoint(self._scale_length / 2, 0)
        bow_starboard_point = GraphicPoint(self._scale_length / self._shape_to_overall_scale, -self._scale_width / 2)

        self.graphic_lines_lst.append(GraphicLine(bow_port_point, bow_point))
        self.graphic_lines_lst.append(GraphicLine(bow_point, bow_starboard_point))
        self.graphic_lines_lst.append(GraphicLine(bow_starboard_point, bow_port_point, is_drawn=False))


class HullShape(GraphicShape):

    fill_color = 'gray'
    line_color = 'black'

    def load_graphic_lines(self):
        bow_starboard_point = GraphicPoint(self._scale_length / self._shape_to_overall_scale, -self._scale_width / 2)
        stern_st_starboard_point = GraphicPoint(-self._scale_length / self._shape_to_overall_scale, -self._scale_width / 2)
        stern_port_point = GraphicPoint(-self._scale_length / self._shape_to_overall_scale, self._scale_width / 2)
        bow_port_point = GraphicPoint(self._scale_length / self._shape_to_overall_scale, self._scale_width / 2)

        self.graphic_lines_lst.append(GraphicLine(bow_starboard_point, stern_st_starboard_point))
        self.graphic_lines_lst.append(GraphicLine(stern_st_starboard_point, stern_port_point))
        self.graphic_lines_lst.append(GraphicLine(stern_port_point, bow_port_point))
        self.graphic_lines_lst.append(GraphicLine(bow_port_point, bow_starboard_point, is_drawn=False))


class SternShape(GraphicShape):

    fill_color = 'gray'
    line_color = 'black'

    def load_graphic_lines(self):
        stern_hull_port_point = GraphicPoint(-self._scale_length / self._shape_to_overall_scale, self._scale_width / 2)
        stern_end_port_point = GraphicPoint(-self._scale_length / 2.5, self._scale_width / 3)
        stern_end_starboard_point = GraphicPoint(-self._scale_length / 2.5, -self._scale_width / 3)
        stern_hull_starboard_point = GraphicPoint(-self._scale_length / self._shape_to_overall_scale, -self._scale_width / 2)

        self.graphic_lines_lst.append(GraphicLine(stern_hull_port_point, stern_end_port_point))
        self.graphic_lines_lst.append(GraphicLine(stern_end_port_point, stern_end_starboard_point))
        self.graphic_lines_lst.append(GraphicLine(stern_end_starboard_point, stern_hull_starboard_point))
        self.graphic_lines_lst.append(GraphicLine(stern_hull_starboard_point, stern_hull_port_point, is_drawn=False))


class MainBoat(BaseBoat):

    def __init__(self):
        super(MainBoat, self).__init__()
        self.speed = 0
        self.speed_increment = .01
        self.max_speed = .2
        self.turn_increment = 0.02
        self.heading = 0
        self.max_turn_increment = .1

        self.ship_width = 30
        self.ship_length = 200
        self.mb_scale = 5
        self.load_shapes()

    def load_shapes(self):
        bow = BowShape(self.ship_length, self.ship_width, self.mb_scale)
        hull = HullShape(self.ship_length, self.ship_width, self.mb_scale)
        stern = SternShape(self.ship_length, self.ship_width, self.mb_scale)
        self.graphic_shape_lst.extend([bow, hull, stern])
