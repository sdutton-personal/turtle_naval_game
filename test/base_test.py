import os
import sys
import time
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.interface_control import MainScreen


class TurtleNavalTestBase(unittest.TestCase):

    __test__ = False
    end_threads = False
    screen_obj = None
    results = None
    expected = None
    x_1 = 0
    x_2 = 0
    x_3 = 0
    x_4 = 0
    x_tst_lst = ['x_1', 'x_2', 'x_3', 'x_4']

########################################################################################################################
    # These 4 functions are only used to be passed into a main screen object for testing if needed, they serve no other
    # purpose.
    def fun_1_used_to_test(self):
        self.x_1 += 1

    def fun_2_used_to_test(self):
        self.x_2 += 1

    def fun_3_used_to_test(self):
        self.x_3 += 1

    def fun_4_used_to_test(self):
        self.x_4 += 1
########################################################################################################################

    def check_x_vars(self):
        # checks all of the x_var attributes of this class to see if they are equal to the expected.  Note that this
        # is really only useful if all of the attributes should be the same value (you called all attributes at the
        # same time interval).
        for att_name in self.x_tst_lst:
            self.results = getattr(self, att_name)
            self.run_equality_tst()

    def call_screen_methods(self, delay):
        # calls all of the screen methods at a set delay interval.
        for method in self.screen_obj_method_lst:
            time.sleep(delay)
            method()

    def set_main_screen_object(self, fun_1=None, fun_2=None, fun_3=None, fun_4=None):
        # this will set the self.screen_obj to an instance of MainScreen() with the functions provided, or stub
        # functions if some are not provided.

        # these functions are provided so you don't have to provide every function if you only want to test one
        def stub_fun_1():
            pass

        def stub_fun_2():
            pass

        def stub_fun_3():
            pass

        def stub_fun_4():
            pass

        if not fun_1:
            fun_1 = stub_fun_1
        if not fun_2:
            fun_2 = stub_fun_2
        if not fun_3:
            fun_3 = stub_fun_3
        if not fun_4:
            fun_4 = stub_fun_4

        self.screen_obj = MainScreen(fun_1, fun_2, fun_3, fun_4)

        # adds the methods for the screen_obj to the screen_obj_method_lst for more convenient iteration and testing.
        self.screen_obj_method_lst = [self.screen_obj.left, self.screen_obj.right,
                                      self.screen_obj.speed_up, self.screen_obj.slow_down]

    def run_equality_tst(self, msg=None):
        if not msg:
            msg = '\n\nThe result was not equal to the expected \n' \
                      'result value: *{}* \nresult type: {}\n' \
                      'expected value: *{}* \nexpected type: {}'.format(self.results,
                                                                        type(self.results),
                                                                        self.expected,
                                                                        type(self.expected))
        self.assertTrue(self.results == self.expected, msg=msg)

    def run_non_equality_tst(self, msg=None):
        if not msg:
            msg = '\n\nThe result was equal to the expected when it should not have been \n' \
                      'result value: *{}* \nresult type: {}\n' \
                      'expected value: *{}* \nexpected type: {}'.format(self.results,
                                                                        type(self.results),
                                                                        self.expected,
                                                                        type(self.expected))
        self.assertFalse(self.results == self.expected, msg=msg)
