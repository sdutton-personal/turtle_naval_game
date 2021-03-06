import math
import turtle


def get_opposite_given_angle_and_adjacent(adjacent_side, angle_in_degrees):
    if round(angle_in_degrees, 1) == 90:
        return 0
    return math.tan(math.radians(angle_in_degrees)) * adjacent_side


class GraphicPoint(object):
    """
    This class is to be initialized with an x and a y coordinate that represent the initial offset of this point from
    (0,0).  This GraphicPoint would represent one point of a line, of a shape of a Turtle object or for our purposes
    some sort of Naval Ship.
    Naval Ship (Turtle)
        Contains 1 or Many GraphicShapes()
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
        self.last_heading = None
        self.last_location = None

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
        if current_heading != self.last_heading:
            # adding this block to prevent needless calls to calculate the zero_adjusted_angle and the quadrant
            # adjustment if the heading has not changed.
            self.set_heading_adjustment(current_heading)
            self.last_heading = current_heading
        else:
            if current_center_location_tup == self.last_location:
                # if the heading has not changed, and the location has not changed, return the current position.
                return self.current_pos
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
        adjusted_heading = current_heading + self.__init_angle_offset
        if adjusted_heading > 360:
            adjusted_heading -= 360
        if adjusted_heading <= 90:
            # this is quadrant_1, x positive, y positive
            self.zero_adjusted_angle = adjusted_heading
            self.quadrant_adjustment_tup = (1, 1)
        elif 90 < adjusted_heading <= 180:
            # this is quadrant_2, x negative, y positive
            self.zero_adjusted_angle = 90 - (adjusted_heading - 90)
            self.quadrant_adjustment_tup = (-1, 1)
        elif 180 < adjusted_heading <= 270:
            # this is quadrant_3, x negative, y negative
            self.zero_adjusted_angle = adjusted_heading - 180
            self.quadrant_adjustment_tup = (-1, -1)
        else:
            # else quadrant_4
            self.zero_adjusted_angle = 90 - (adjusted_heading - 270)
            self.quadrant_adjustment_tup = (1, -1)


class GraphicLine(object):
    """
    This class is to be initialized with two points, either GraphicPoint objects as defined in this file, or tuples
    consisting of two integers each.  These two points or tuples will represent a GraphicLine that is this object.
    This GraphicLine will consist of two GraphicPoints.  Multiple GraphicLines will make a GraphicShape, and multiple
    GraphicShapes will make a Turtle object or for our purposes some sort of Naval Ship.
    Naval Ship (Turtle)
        Contains 1 or Many GraphicShapes()
            Contains 1 or Many GraphicLines()
                Contains 2 GraphicPoints()
                    Contains 2 Coordinates()
    Optional Arguments:
    is_drawn: sets an attribute with this value, either True or False to represent if this line should be drawn.  This
    attribute will not affect anything in this class, but is used by the parent class GraphicShape when loading points
    to draw.
    test_for_intersection: sets an attribute with this value, either True or False.  If True will run the intersection
    test, if False, will always return False for line intersecting.
    """

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
        except ValueError as err:
            if 1 < abs(y_1 - y_2) / self.hyp_distance < 1.0001:
                # due to rounding issues it is possible that this number may end up larger than 1, and that would
                # generate a rounding error.  If the Value error is deemed to be caused by a rounding issue,
                # we will set the angle to 90, as math.degrees(math.asin(1)) would generate a result of 90.
                angle = 90
            else:
                # if the value error was not found to be caused by rounding in the range of tolerance, we will
                # re raise the exception.
                raise Exception('ValueError:  {}'.format(err))

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
    """
    This is a base class, it should be inherited and used to create a custom GraphicShape.  When inheriting and
    creating the new graphic shape make sure to overwrite the load_graphic_lines method with a method to load the
    GraphicLine Objects that will make up the custom shape.  Multiple GraphicLines will make a GraphicShape, and
    multiple GraphicShapes will make a Turtle object or for our purposes some sort of Naval Ship.
    Naval Ship (Turtle)
        Contains 1 or Many GraphicShapes()
            Contains 1 or Many GraphicLines()
                Contains 2 GraphicPoints()
                    Contains 2 Coordinates()
    Required args:
    overall_length: The length of the Turtle object
    overall_width: The width of the turtle object
    shape_to_overall_scale: A number representing the size of this Shape to the overall Turtle.
    scale: A number representing the scale of the object in general.  if scale is negative the object will shrink,
    and if scale is positive, it will become larger.
    x_boundary: the x point that if any point in this shape crosses, the shape will be considered out of bounds for
    that axis.  If set or left to 0, shape will never be out of bounds.
    y_boundary: the y point that if any point in this shape crosses, the shape will be considered out of bounds for that
    axis.  If set or left to 0, shape will never be out of bounds.
    """

    _shape_to_overall_scale = None
    _scale = None
    _scale_width = None
    _scale_length = None

    def __init__(self, overall_length, overall_width, shape_to_overall_scale, scale=0, x_boundary=0, y_boundary=0):
        self.graphic_lines_lst = []
        self.points_to_draw_lst = []
        self._overall_length = overall_length
        self._overall_width = overall_width
        self._shape_to_overall_scale = shape_to_overall_scale
        self._scale = scale
        self._scale_width = self._overall_width + (self._overall_width * self._scale / float(100))
        self._scale_length = self._overall_length + (self._overall_length * self._scale / float(100))
        self.shape_out_of_bounds = False
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary

        self.load_graphic_lines()
        self.load_points_to_draw()

    def load_graphic_lines(self):
        """
        Over write this method when inheriting this class
        :return:
        """
        pass

    def load_points_to_draw(self):
        """
        This method will load up the points needed for drawing from the self.graphic_lines_lst.  If the line.is_drawn
        attribute is false, lines will not be drawn.
        :return:
        """
        last_point = None
        for line in self.graphic_lines_lst:
            if line.is_drawn:
                start_point_tup = (round(line.start_point_cur_loc[1], 5), round(line.start_point_cur_loc[0], 5))
                end_point_tup = (round(line.end_point_cur_loc[1], 5), round(line.end_point_cur_loc[0], 5))
                if start_point_tup != last_point:
                    self.points_to_draw_lst.append(start_point_tup)
                self.points_to_draw_lst.append(end_point_tup)
                last_point = end_point_tup

    def update_shape_position(self, cur_ref_point_loc_tup, heading):
        """
        This method is called to update the current shapes position in reference to the center tuple location.
        :param cur_ref_point_loc_tup: The center reference point of the containing turtle object.
        :param heading: The heading or direction in degrees of the turtle object.
        :return:
        """
        for line in self.graphic_lines_lst:
            line.update_line_position(cur_ref_point_loc_tup, heading)

    def is_point_inside_shape(self, point_in_question_tup):
        """
        This method can be called to see if the point_in_question_tup is inside the GraphicShape object.  If
        point_in_question is in the shape, this method will return True, if not, will return False
        """
        to_left = False
        to_right = False
        for line in self.graphic_lines_lst:
            point_location = line.is_intersected_by(point_in_question_tup)
            if point_location == 1:
                to_left = True
            elif point_location == 2:
                to_right = True
            if to_right and to_left:
                return True
        return False

    def is_shape_out_of_bounds(self):
        """
        This method can be called to determine if any part of this shape is out of bounds.  If all of the shape is
        in bounds this method will return False.  If part of the shape is out of bounds a list will be returned
        with two integers, the first representing if the shape is out of bounds on the x axis and the second if
        the shape is out of bounds on the y axis.  If the shape is out of bounds on the positive x axis but
        in bounds on the y axis the returned result would be [1,0].  If the shape is out of bounds on both the
        x and y positive axis the result would be [1,1], and if the shape is out of bounds on the positive x axis
        and the negative y axis the result would be [1,-1].
        :return:
        """
        x_max = self.x_boundary
        y_max = self.y_boundary
        x_min = x_max * -1
        y_min = y_max * -1
        if sum([x_max, y_max]) == 0:
            return False
        result_lst = [0, 0]
        for line in self.graphic_lines_lst:
            if line.start_point_cur_loc[0] > x_max or line.end_point_cur_loc[0] > x_max:
                result_lst[0] = 1
            if line.end_point_cur_loc[0] < x_min or line.end_point_cur_loc[0] < x_min:
                result_lst[0] = -1
            if line.start_point_cur_loc[1] > y_max or line.end_point_cur_loc[1] > y_max:
                result_lst[1] = 1
            if line.start_point_cur_loc[1] < y_min or line.end_point_cur_loc[1] < y_min:
                result_lst[1] = -1
        if result_lst[0] or result_lst[1]:
            return result_lst
        else:
            return False


class BaseBoat(object):
    """
    This is the base class for boats and possibly all moving objects.  When this class is inherited, the sub class
    should overwrite the below attributes with the desired settings.  The sub class MUST also have an __init__ that
    will define self.boat as an instance of turtle.Turtle()

    Example:
    def __init__(self):
        self.boat = turtle.Turtle(shape='circle')
    """
    def __init__(self, x_boundary, y_boundary):
        self.speed = 0  # overwrite this to change initial speed
        self.speed_increment = .01  # overwrite this to change the incremental rate of speed change
        self.max_speed = .5  # overwrite this to change the maximum speed of movement allowed
        self.turn_increment = 0.01  # overwrite this to change the increment of turning
        self.heading = 0  # overwrite this to change the initial heading.
        self.max_turn_increment = .05  # overwrite this to change the maximum rate that the object can turn.
        self.shape_name = None

        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.boat = turtle.Turtle()
        self.graphic_shape_lst = []
        self.out_of_bounds_lst = []

    def load_shapes(self):
        """
        overwrite this method to append graphic shapes to the graphic_shape_lst. Then call this method from the
        extended __init__ of the child class.
        :return:
        """
        pass

    def move(self):
        """
        Moves forward (or backward) at the current speed setting, should be called regularly in a loop with a slight
        sleep timer in between calls
        """
        self.update_object_position_points()
        self.set_out_of_bounds_lst()
        self.boat.forward(self.speed)
        if self.heading > 0:
            self.boat.left(self.heading)
        elif self.heading < 0:
            self.boat.right(self.heading * -1)

    def right(self):
        """
        Alters the direction to the right by turn increment degrees
        """
        self.heading -= self.turn_increment
        if self.heading < self.max_turn_increment * -1:
            self.heading = self.max_turn_increment * -1

    def left(self):
        """
        Alters the direction to the left by turn increment degrees
        """
        self.heading += self.turn_increment
        if self.heading > self.max_turn_increment:
            self.heading = self.max_turn_increment

    def speed_up(self):
        """
        Increases the current speed by the speed increment, unless that speed is greater than max speed, if so speed
        is set to max speed.
        """
        self.speed += self.speed_increment
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def slow_down(self):
        """
        Decreases the current speed (or increases to reverse speed) unless that reverse speed is faster in reverse than
        1/2 of the max speed.
        """
        self.speed -= self.speed_increment
        if self.speed < self.max_speed * -1 / float(2):
            self.speed = self.max_speed * -1 / float(2)

    def return_shape(self):
        # (y,x)
        master_shape = turtle.Shape("compound")
        for shape in self.graphic_shape_lst:
            sub_shape = tuple(shape.points_to_draw_lst)
            master_shape.addcomponent(sub_shape, shape.fill_color, shape.line_color)
        return master_shape

    def update_object_position_points(self):
        current_pos_tup = self.boat.pos()
        heading = self.boat.heading()
        for shape in self.graphic_shape_lst:
            shape.update_shape_position(current_pos_tup, heading)

    def set_out_of_bounds_lst(self):
        self.out_of_bounds_lst = []
        for shape in self.graphic_shape_lst:
            shape_bounds_lst = shape.is_shape_out_of_bounds()
            if shape_bounds_lst:
                # if the shape is out of bounds ..
                if not self.out_of_bounds_lst:
                    # if no other shapes have been out of bounds, the boat out of bounds list is the shapes out of
                    # bounds list
                    self.out_of_bounds_lst = shape_bounds_lst
                else:
                    # if another shape in this object has been out of bounds, we will need to merge both of lists, by
                    # favoring any value that is not 0.
                    if not self.out_of_bounds_lst[0]:
                        self.out_of_bounds_lst[0] = shape_bounds_lst[0]
                    if not self.out_of_bounds_lst[1]:
                        self.out_of_bounds_lst[1] = shape_bounds_lst[1]

    def copy_settings_from_clone(self, clone_instance_obj):
        self.speed = clone_instance_obj.speed
        self.boat.setheading(clone_instance_obj.boat.heading())
        self.turn_increment = clone_instance_obj.turn_increment
        self.shape_name = clone_instance_obj.shape_name
        self.boat.shape(self.shape_name)

    def register_shape(self, shape_name):
        self.shape_name = shape_name
        self.boat.shape(shape_name)


class GraphicObjectContainer(object):

    def __init__(self, sub_instance_of_base_boat_class):
        self.primary_object = sub_instance_of_base_boat_class
        self.object_clone = None

    def move(self):
        self.clone_management()
        self.primary_object.move()
        if self.object_clone:
            self.object_clone.move()

    def right(self):
        self.primary_object.right()
        if self.object_clone:
            self.object_clone.right()

    def left(self):
        self.primary_object.left()
        if self.object_clone:
            self.object_clone.left()

    def speed_up(self):
        self.primary_object.speed_up()
        if self.object_clone:
            self.object_clone.speed_up()

    def slow_down(self):
        self.primary_object.slow_down()
        if self.object_clone:
            self.object_clone.slow_down()

    def clone_management(self):
        if not self.object_clone:
            # no clone currently present, check if one is needed, if so create it.
            if self.primary_object.out_of_bounds_lst:
                # clone is needed, create it
                obj_class = self.primary_object.__class__
                self.object_clone = obj_class(self.primary_object.x_boundary, self.primary_object.y_boundary)
                if self.primary_object.out_of_bounds_lst[0]:
                    # if the x position is not 0, then set the x position to 2 times the boundary * -1 + the current x
                    clone_x_pos = self.primary_object.x_boundary * 2 * self.primary_object.out_of_bounds_lst[0] * -1
                    clone_x_pos += self.primary_object.boat.pos()[0]
                else:
                    # if the x position is 0 set its x to the opposite of the current x
                    clone_x_pos = self.primary_object.boat.pos()[0] * -1
                if self.primary_object.out_of_bounds_lst[1]:
                    # if the y position is not 0, the y of the clone will be 2 times the boundary * -1 + the current y
                    clone_y_pos = self.primary_object.y_boundary * 2 * self.primary_object.out_of_bounds_lst[1] * -1
                    clone_y_pos += self.primary_object.boat.pos()[1]
                else:
                    clone_y_pos = self.primary_object.boat.pos()[1] * -1
                self.object_clone.boat.setposition(clone_x_pos, clone_y_pos)
                self.object_clone.copy_settings_from_clone(self.primary_object)
        else:
            # clone is active, check to see if the clone is either 1 not needed anymore, or 2 the clone is the primary
            # and the primary is not needed anymore.
            if not self.primary_object.out_of_bounds_lst:
                # primary object is no longer out of bounds, kill the clone
                self.object_clone.boat.clear()
                self.object_clone.boat.ht()
                del self.object_clone
                self.object_clone = None
            else:
                # primary object is still out of bounds, check to see if the clone is out of bounds as well, if not, the
                # primary object is completely out of bounds and the clone is now our active and primary object.
                if not self.object_clone.out_of_bounds_lst:
                    self.primary_object.boat.clear()
                    self.primary_object.boat.ht()
                    del self.primary_object
                    self.primary_object = self.object_clone
                    self.object_clone = None
