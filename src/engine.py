
import time
import graphics

from interface_control import MainScreen


class MainEngine(object):

    exit_now = False
    shape_1_name = 'battleship'

    shape_dct = {}

    def __init__(self):
        self.main_boat = graphics.MainBoat()
        self.main_screen = MainScreen(left_fun=self.main_boat.left,
                                      right_fun=self.main_boat.right,
                                      speed_up_fun=self.main_boat.speed_up,
                                      slow_down_fun=self.main_boat.slow_down)

        self.shape_dct[self.shape_1_name] = self.main_boat.return_shape
        self.register_shapes_to_screen()

        self.main_boat.boat.shape(self.shape_1_name)
        self.run_engine()

    def run_engine(self):
        while True:
            self.main_boat.move()
            self.main_boat.update_object_position_points()
            time.sleep(.02)
            self.main_screen.get_input()
            if self.main_screen.exit_now:
                self.main_screen.screen.bye()
                break

    def register_shapes_to_screen(self):
        for shape_name, shape_mtd in self.shape_dct.iteritems():
            self.main_screen.screen.register_shape(shape_name, shape_mtd())

eng = MainEngine()
