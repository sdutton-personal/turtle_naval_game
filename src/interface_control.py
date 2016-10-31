# @ Shawn Dutton 8-12-2016

import time
import turtle


class MainScreen(object):
    """
    This class creates and contains a turtle.Screen().  In addition to providing access to this, this class will
    provide wrapper functions to sanitize the input from the turtle.Screen() instance.  This object must be provided
    with the movement functions desired for the turtle, then this object will call those movement functions if input is
    deemed sanitized.

    For the purpose of this application "non sanitized" input is input that is determined to come from holding down a
    key.  For our purposes, 1 key press no matter how long it is held should result in only 1 instruction.

    The de bounce limit is set to .1, however it could be adjusted if needed, though a higher number may result in the
    muffling of real key presses.

    A very simple example of use:

    ## begin example

    # movement functions - note this example does not move anything, it will simply print the instruction
    def mv_left():
        print 'moving left'
    def mv_right():
        print 'moving right'
    def spd_up():
        print 'speeding up'
    def slw_dwn():
        print 'slowing down'

    # initialize the object passing in these movement functions
    obj = MainScreen(mv_left, mv_right, spd_up, slw_dwn)
    while True:
        # a loop of some sort is required to keep listening for input, obj.get_input() must be called in the loop.
        time.sleep(.01)
        obj.get_input()
        if obj.exit_now:
            # this is optional, though useful to be able to quit easily.
            break

    ## end example

    """

    de_bounce_limit = .1
    last_input = time.time()
    exit_now = False
    screen_height = 245
    screen_width = 335

    def __init__(self, left_fun, right_fun, speed_up_fun, slow_down_fun):
        self.screen = turtle.Screen()
        self.screen.bgcolor("yellow")
        self.screen.screensize(self.screen_width, self.screen_height)

        # these attributes should be functions to be called after the input is sanitized.
        self.move_left_fun = left_fun
        self.move_right_fun = right_fun
        self.speed_up_fun = speed_up_fun
        self.slow_down_fun = slow_down_fun

        # these are the current keybindings
        self.screen.onkey(self.left, 'a')
        self.screen.onkey(self.right, 'd')
        self.screen.onkey(self.speed_up, 'w')
        self.screen.onkey(self.slow_down, 's')
        self.screen.onkey(self.exit, 'q')
        self.screen.tracer(0, 0)

    def left(self):
        """
        Check for de bounce, if input is valid, call the left function supplied, and update.
        """
        if self.de_bounce():
            self.move_left_fun()
        self.screen.update()

    def right(self):
        """
        Check for de bounce, if input is valid, call the right function supplied, and update.
        """
        if self.de_bounce():
            self.move_right_fun()
        self.screen.update()

    def speed_up(self):
        """
        Check for de bounce, if input is valid, call the speedup function supplied, and update.
        """
        if self.de_bounce():
            self.speed_up_fun()
        self.screen.update()

    def slow_down(self):
        """
        Check for de bounce, if input is valid, call the slowdown function supplied, and update.
        """
        if self.de_bounce():
            self.slow_down_fun()
        self.screen.update()

    def exit(self):
        """
        This method sets the exit_now attribute, that can be read in order to see that a clean exit is desired.
        """
        self.exit_now = True
        self.screen.update()

    def de_bounce(self):
        """
        This method exists in order to ensure than 1 press of a key results in only 1 command for that key.  Without
        a call to this function, holding a key down would result in many actions for one press of that key.
        :return True if the input was not a held key and false if the input was determined to be a held key:
        """
        current_time = time.time()
        if current_time < self.last_input + self.de_bounce_limit:
            # if new input has been detected in less time than the de bounce limit, then we want to ignore
            # this input, as it is most likely caused by key mashing.
            valid_input = False
        else:
            # valid input
            valid_input = True
        self.last_input = current_time
        return valid_input

    def get_input(self):
        """
        Calls both listen, and update from turtle.Screen().  With out both of these calls, we can not check for our
        next input.  Note that that one could call obj.screen.listen() and obj.screen.update() without using this
        method if desired.
        """
        self.screen.listen()
        self.screen.update()
