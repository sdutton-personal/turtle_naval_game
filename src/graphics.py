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
        if not isinstance(x, (int, float)):
            raise Exception('x must be supplied as an integer or a float')
        if not isinstance(y, (int, float)):
            raise Exception('y must be supplied as an integer or a float')
        self.__init_x = x
        self.__init_y = y
        self.__init_angle_offset = None
        self.__init_distance = math.sqrt(y ** 2 + x ** 2)

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
        try:
            angle = math.degrees(math.asin(abs(self.__init_y) / self.__init_distance))
        except ZeroDivisionError:
            angle = 0
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


class GraphicLine(object):

    def __init__(self, start_point, end_point, is_drawn=True, test_for_intersection=True):
        if not isinstance(start_point, (tuple, GraphicPoint)):
            # start_point is invalid, it must either be a tuple or a GraphicPoint
            raise Exception('start_point must either be a tuple or a GraphicPoint')
        if isinstance(start_point, tuple):
            if len(start_point) != 2:
                raise Exception('start_point tuple must contain 2 and only integer or floats Ex (15, 23.5)')
            self.start_point = GraphicPoint(*start_point)
        else:
            self.start_point = start_point
        if not isinstance(end_point, (tuple, GraphicPoint)):
            raise Exception('end_point must be either a tuple or a GraphicPoint')
        if isinstance(end_point, tuple):
            if len(end_point) != 2:
                raise Exception('start_point tuple must contain 2 and only integer or floats Ex (15, 23.5)')
            self.end_point = GraphicPoint(*end_point)
        else:
            self.end_point = end_point

        self.is_drawn = is_drawn
        self.__test_for_intersection = test_for_intersection
        self.start_point_cur_loc = None
        self.end_point_cur_loc = None
        self.intersection_ind = 0
        self.update_line_position((0, 0), 0)
        self.hyp_distance = math.hypot(self.start_point_cur_loc[0] - self.end_point_cur_loc[0], self.start_point_cur_loc[1] - self.end_point_cur_loc[1])

    def update_line_position(self, cur_ref_point_loc_tup, heading):
        """
        Updates the line position by taking in the current reference point location tuple, and the current heading, and
        calling each graphic point object to find its new position.  These new positions will be stored in:
        self.start_point_cur_loc, and self.end_Point_cur_loc
        :param cur_ref_point_loc_tup: The current location of the center point that this line was created from.
        :param heading: The new heading in degrees of the parent object.
        :return:
        """
        self.start_point_cur_loc = self.start_point.update_point_position(cur_ref_point_loc_tup, heading)
        self.end_point_cur_loc = self.end_point.update_point_position(cur_ref_point_loc_tup, heading)

    def is_intersected_by(self, intersection_point_tup):
        """
        This function will determine if the given intersection_point_tup would intersect our line on the x axis, and if
        so which side of the line the intersection point will reside on. If the point would not intersect our line, we
        will return 0.  If it intersects on the left side or is exactly on our line we will return 1.  If it intersects
        on the right side we will return 2.
        :param intersection_point_tup: A tuple representing a point on an (x,y) axis.
        :return:
        0 for No intersection
        1 for intersection on the left
        2 for intersection on the right
        """
        if self.__test_for_intersection:
            # Added in the below rounding of the points to the 5th decimal place.  This will prevent what would seem to
            # be "unpredictable" behaviour when comparing points that actually exist on the line, or are the same as
            # the end or the start point.  If the rounding was left out, a point on the line may show up as right of
            # the line if the y value was negative on a positive slope line, or positive on a negative slope line.  This
            # would happen because the start and end values when re calculated would come in as something like:
            # 12.0000000000001 , or -12.000000000001, and would not be equal to the test value of 12.0, or -12.0 when as
            # far as we are concerned those values should be equal.
            start_x = round(self.start_point_cur_loc[0], 5)
            start_y = round(self.start_point_cur_loc[1], 5)
            end_x = round(self.end_point_cur_loc[0], 5)
            end_y = round(self.end_point_cur_loc[1], 5)
            intersect_x = round(intersection_point_tup[0], 5)
            intersect_y = round(intersection_point_tup[1], 5)

            if start_y > intersect_y:
                if end_y > intersect_y:
                    # intersection point is below our line return 0
                    return 0
            if start_y < intersect_y:
                if end_y < intersect_y:
                    # intersection point is above our line return 0
                    return 0
            # at this point the point must be in between our line, as if it were above or below we would have returned.
            # now test to see if the point is to the left or the right of both x points.
            if start_x > intersect_x:
                if end_x > intersect_x:
                    # intersection point is to the left, or less than both of our points.
                    return 1
            if start_x < intersect_x:
                if end_x < intersect_x:
                    # intersection point is the to right, or greater than both of our points.
                    return 2
            # the intersection point is now between both x's and both y's, so we will do some geometry to find out its
            # exact location in reference to our line.  The below function will give us the y value on the line that
            # the x of the point in question would intersect on.
            line_y = self.find_y_given_x_on_two_points(start_x, start_y, end_x, end_y, intersect_x)

            # find the slope of the line, this is used for determining if points are on the left or the right.
            slope = 1
            if end_x > start_x:
                slope *= -1
            if end_y > start_y:
                slope *= -1

            if slope > 0:
                # logic for positive slope
                if intersect_y >= line_y:
                    # if the line orientation is positive, and our intersect_y is greater than or = to the y where the x
                    # intersects then we are on the left side of the line, or on the line, so return 1
                    return 1
                else:
                    # orientation is positive, yet our intersect y is smaller, so we are on the right side of the line.
                    return 2
            else:
                # logic for negative slope
                if intersect_y <= line_y:
                    # if the line orientation is negative, and or intersect_y is less than or = to the y where the x
                    # intersects then we are on the left side of the line, or on the line, so return 1
                    return 1
                else:
                    # orientation is negative, and our intersect y is greater than the y on the line, so we are on the
                    # right side.
                    return 2
        else:
            # this line should not be tested for intersection, so return 0
            return 0

    def find_y_given_x_on_two_points(self, x_1, y_1, x_2, y_2, x_to_find):
        """
        This function will take x values and y values from two points and use them to find the y value on the line where
        the provided x_to_find value would intersect the line.
        :param x_1: x of the start point
        :param y_1: y of the start point
        :param x_2: x of the end point
        :param y_2: y of the end point
        :param x_to_find: x value of the point to find the y value where the line is intersected.
        :return: y value where the x value intersects the line.
        """
        # get the angle
        try:
            angle = math.degrees(math.asin(abs(y_1 - y_2) / self.hyp_distance))
        except ZeroDivisionError:
            angle = 0

        # get the slope, this is used to determine how to correct the y and also to shift the y value positive or
        # negative
        slope = 1
        if x_2 > x_1:
            slope *= -1
        if y_2 > y_1:
            slope *= -1

        # subtract the x of the 2nd point, this will "zero" out the x value
        x_to_find -= x_2

        # get the y of the point, note this is an "absolute" y from a 0,0 point
        y_to_find = math.tan(math.radians(angle)) * x_to_find

        if slope > 0:
            # if the slope is positive, add the y back in
            y_to_find += y_2
        else:
            # if the slope is negative, subtract the y and then multiply the y to find by -1 correcting its slope
            y_to_find -= y_2
            y_to_find *= -1

        # round to 5th decimal place, as our use only needs accuracy to the 2nd decimal place, so the extra three are
        # just over kill and for good measure.  This will help to make sure equality tests that may be performed would
        # not fail on something like 25.0000000000001 == 25.0.  For our purposes 25.000000000001 is == to 25.0.
        return round(y_to_find, 5)


class GraphicShape(object):

    graphic_lines_lst = []
    points_to_draw_lst = []
    scale = 0
    shape_fill_color = 'gray'
    shape_line_color = 'black'

    __overall_length = None
    __overall_width = None
    __shape_to_overall_scale = None
    __scale = None
    base_points_lst = []

    def __init__(self, overall_length, overall_width, shape_to_overall_scale, scale=0):
        self.__overall_length = overall_length
        self.__overall_width = overall_width
        self.__shape_to_overall_scale = shape_to_overall_scale
        self.__scale = scale
        self.__scale_width = self.__overall_width + (self.__overall_width * self.__scale / 100)
        self.__scale_length = self.__overall_length + (self.__overall_length * self.__scale / 100)

        self.load_graphic_lines()
        self.load_points_to_draw()

    def load_graphic_lines(self):
        """
        Over write this method when inheriting this class
        :return:
        """
        pass

    def load_points_to_draw(self):
        last_point = None
        for line in self.graphic_lines_lst:
            if line.is_drawn:
                if line.start_point_cur_loc != last_point:
                    self.points_to_draw_lst.append(line.start_point_cur_loc)
                self.points_to_draw_lst.append(line.end_point_cur_loc)
                last_point = line.end_point_cur_loc

    def update_shape_position(self, cur_ref_point_loc_tup, heading):
        for line in self.graphic_lines_lst:
            line.update_line_position(cur_ref_point_loc_tup, heading)

    def is_point_inside_shape(self, point_in_question_tup):

        intersection_reference_total = 0
        for line in self.graphic_lines_lst:
            intersection_reference_total += line.is_intersected_by(point_in_question_tup)

        if intersection_reference_total == 3:
            return True
        else:
            return False


class BowShape(GraphicShape):

    def load_graphic_lines(self):
        point_1_tup = (self.__scale_width / 2, self.__scale_length / self.__shape_to_overall_scale)
        point_2_tup = (0, self.__scale_length / 2)
        point_3_tup = (-self.__scale_width / 2, self.__scale_length / self.__shape_to_overall_scale)

        self.graphic_lines_lst.append(GraphicLine(point_1_tup, point_2_tup))
        self.graphic_lines_lst.append(GraphicLine(point_2_tup, point_3_tup))
        self.graphic_lines_lst.append(GraphicLine(point_3_tup, point_1_tup, is_drawn=False))
