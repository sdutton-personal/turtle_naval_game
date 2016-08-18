import math
import turtle


class GraphicPoint(object):
    """
    This class is to be initialized with an x and a y coordinate that represent the initial offset of this point from
    (0,0).  This GraphicPoint would represent one point of a line, of a shape of a Turtle object or for our purposes
    some sort of Naval Ship.
    Naval Ship (Turtle)
        Contains 1 or Many StructureShapes()
            Contains 1 or Many GraphicLines()
                Contains 2 GraphicPoints()
                    Contains 2 Coordinates()
    """

    def __init__(self, x, y):
        self.__init_x = x
        self.__init_y = y
        self.__init_angle_offset = None
        self.__init_distance = math.sqrt(abs(y) ** 2 + abs(x) ** 2)

        self.quadrant_adjustment_tup = None
        self.zero_adjusted_angle = None
        self.current_pos = (x, y)
        self.x = x
        self.y = y

        self.set_init_angle_offset()
        self.update_point_position((0, 0), 0)

    @property
    def init_angle_offset(self):
        """
        Returns the init_angle_offset, this is used by this object to calculate the x and y values when the heading of
        the main object has changed.  It probably does not need to be accessed externally, but it is made available for
        read only access if needed.
        :return:
        """
        return self.__init_angle_offset

    @property
    def init_distance(self):
        """
        Returns the init_distance, this is used by this object to calculate the x and y values when the heading of the
        main object has changed.  It probably does not need to be accessed externally, but it is made available for
        read only access if needed.
        :return:
        """
        return self.__init_distance

    def set_init_angle_offset(self):
        """
        Finds and sets the initial angle offset of the point from (0,0), this is used for calculating the position
        of the point when updating point position.
        :return:
        """
        angle = math.degrees(math.asin(abs(self.__init_y) / self.__init_distance))
        if self.__init_x >= 0 and self.__init_y >= 0:
            self.__init_angle_offset = angle
            self.quadrant_adjustment_tup = (1, 1)
        elif self.__init_x < 0 <= self.__init_y:
            self.__init_angle_offset = 90 + (90 - angle)
            self.quadrant_adjustment_tup = (-1, 1)
        elif self.__init_x < 0 and self.__init_y < 0:
            self.__init_angle_offset = 180 + angle
            self.quadrant_adjustment_tup = (-1, -1)
        elif self.__init_y < 0 <= self.__init_x:
            self.__init_angle_offset = 270 + (90 - angle)
            self.quadrant_adjustment_tup = (1, -1)
        else:
            self.__init_angle_offset = None

    def update_point_position(self, current_center_location_tup, current_heading):
        """
        Uses the current location of the main object and the current objects overall heading and calculates this points
        current location and stores it in the self.current_pos variable.
        :param current_center_location_tup: Tuple containing the (x,y) coordinates of the object
        :param current_heading: degree heading from 0-360 representing the direction of the overall objects orientation.
        :return: A tuple containing the (x,y) coordinates of the object.
        """
        self.set_heading_adjustment(current_heading)
        sin = math.sin
        to_rads = math.radians
        x = (sin(to_rads(90 - self.zero_adjusted_angle)) * self.__init_distance) * self.quadrant_adjustment_tup[0]
        y = (sin(to_rads(self.zero_adjusted_angle)) * self.__init_distance) * self.quadrant_adjustment_tup[1]
        self.current_pos = (current_center_location_tup[0] + x, current_center_location_tup[1] + y)
        return self.current_pos

    def set_heading_adjustment(self, current_heading):
        """
        This function will take the current heading, or angle of movement of the turtle object, and set a zero
        adjusted heading, that represents the angle from point (0,0) that the point would be rotated to.  This angle is
        adjusted to max of 90 degrees at both x zero planes, and 0 degrees at both y zero planes.  This angle is used
        only to calculate the new x and y positions.
        :param current_heading: The current direction and or heading in degrees from 0-360 of the object that this
        point is part of.
        :return:
        """
        last_heading = current_heading + self.__init_angle_offset
        if last_heading > 360:
            last_heading -= 360
        if last_heading <= 90:
            # this is quadrant_1, x positive, y positive
            self.zero_adjusted_angle = last_heading
            self.quadrant_adjustment_tup = (1, 1)
        elif 90 < last_heading <= 180:
            # this is quadrant_2, x negative, y positive
            self.zero_adjusted_angle = 90 - (last_heading - 90)
            self.quadrant_adjustment_tup = (-1, 1)
        elif 180 < last_heading <= 270:
            # this is quadrant_3, x negative, y negative
            self.zero_adjusted_angle = last_heading - 180
            self.quadrant_adjustment_tup = (-1, -1)
        else:
            # else quadrant_4
            self.zero_adjusted_angle = 90 - (last_heading - 270)
            self.quadrant_adjustment_tup = (1, -1)
