import unittest

from base_test import TurtleNavalBase


class TestInterfaceControl(TurtleNavalBase):

    __test__ = True

    def setUp(self):
        self.x_1 = 0
        self.x_2 = 0
        self.x_3 = 0
        self.x_4 = 0
        self.x_tst_lst = [self.x_1, self.x_2, self.x_3, self.x_4]

    def tearDown(self):
        del self.screen_obj

    def test_general_operation(self):
        # this is basically a smoke test to see if the functions given will be called.
        self.set_main_screen_object(fun_1=self.fun_1_used_to_test, fun_2=self.fun_2_used_to_test,
                                    fun_3=self.fun_3_used_to_test, fun_4=self.fun_4_used_to_test)

        self.expected = 0
        self.check_x_vars()

        self.call_screen_methods(.25)
        self.expected = 1
        self.check_x_vars()

    def test_de_bounce(self):
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

unittest.main()
