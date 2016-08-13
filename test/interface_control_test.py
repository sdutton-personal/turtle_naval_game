import time
import unittest

from base_test import TurtleNavalTestBase


class TestInterfaceControl(TurtleNavalTestBase):

    __test__ = True

    def setUp(self):
        self.x_1 = 0
        self.x_2 = 0
        self.x_3 = 0
        self.x_4 = 0

    def tearDown(self):
        del self.screen_obj

    def test_all_general_operation(self):
        # this is basically a smoke test to see if the functions given will be called.
        self.set_main_screen_object(fun_1=self.fun_1_used_to_test, fun_2=self.fun_2_used_to_test,
                                    fun_3=self.fun_3_used_to_test, fun_4=self.fun_4_used_to_test)

        self.expected = 0
        self.check_x_vars()

        self.call_screen_methods(.25)
        self.expected = 1
        self.check_x_vars()

    def test_all_de_bounce(self):
        # This will call all methods 1 time to setup valid inputs, then will hit all 4 methods 3 times each
        # all under the de bounce.  Only the initial valid inputs should count.
        self.set_main_screen_object(fun_1=self.fun_1_used_to_test, fun_2=self.fun_2_used_to_test,
                                    fun_3=self.fun_3_used_to_test, fun_4=self.fun_4_used_to_test)

        self.expected = 0
        self.check_x_vars()

        self.call_screen_methods(.2)
        self.expected = 1
        self.check_x_vars()

        for x in range(10):
            # all of these inputs should be under the de bounce limit and should be ignored.
            self.call_screen_methods(0)
            self.call_screen_methods(.01)
            self.call_screen_methods(.05)
        self.expected = 1
        self.check_x_vars()

    def test_multiple_inputs_some_de_bounce_some_not(self):
        # this test will loop over all of the methods, focusing on one method at a time, calling that one method at
        # various intervals.  Making sure the de bounce ignores calls when it should and accepts them when it should.

        self.set_main_screen_object(fun_1=self.fun_1_used_to_test, fun_2=self.fun_2_used_to_test,
                                    fun_3=self.fun_3_used_to_test, fun_4=self.fun_4_used_to_test)

        for idx, method in enumerate(self.screen_obj_method_lst):
            att_name = self.x_tst_lst[idx]

            # sleep to make sure that each loop for each method starts fresh
            time.sleep(.2)
            # test that the function has not been called yet and the var is 0.
            self.expected = 0
            self.results = getattr(self, att_name)
            self.run_equality_tst()

            for x in range(1000):
                # call the function 1000 times, very quickly, note that only the first call should be counted,
                # all others should trigger the de_bounce.
                method()
            self.expected = 1
            self.results = getattr(self, att_name)
            self.run_equality_tst()

            # wait .15 seconds this should be longer than the de bounce, then trigger the left again, this should not
            # trigger the de bounce.
            time.sleep(.15)
            method()
            self.expected = 2
            self.results = getattr(self, att_name)
            self.run_equality_tst()

            # now wait for the de bounce to expire again then we will simulate holding the key down for 10 triggers.
            # Only the first should count.
            time.sleep(.15)
            for x in range(10):
                method()
            self.expected = 3
            self.results = getattr(self, att_name)
            self.run_equality_tst()

            # now trigger the function 10 times in a row, but wait long enough in between each trigger that the de
            # bounce is not triggered.  All of these calls should count.
            for x in range(10):
                time.sleep(.15)
                method()
            self.expected = 13
            self.results = getattr(self, att_name)
            self.run_equality_tst()

unittest.main()
