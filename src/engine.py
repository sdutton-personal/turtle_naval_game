
import time
import graphics
from base_graphics import GraphicObjectContainer

from interface_control import MainScreen


class MainEngine(object):

    exit_now = False
    shape_1_name = 'battleship'

    def __init__(self):
        self.shape_dct = {}
        user_boat = graphics.BattleShip(MainScreen.screen_width, MainScreen.screen_height)
        self.user_obj = GraphicObjectContainer(user_boat)

        self.main_screen = MainScreen(left_fun=self.user_obj.left,
                                      right_fun=self.user_obj.right,
                                      speed_up_fun=self.user_obj.speed_up,
                                      slow_down_fun=self.user_obj.slow_down)
        self.register_shapes_to_screen()
        self.user_obj.primary_object.register_shape(self.shape_1_name)

        self.run_engine()

    def run_engine(self):
        while True:
            self.user_obj.move()
            time.sleep(.02)
            self.main_screen.get_input()
            if self.main_screen.exit_now:
                self.main_screen.screen.bye()
                break

    def register_shapes_to_screen(self):
        # list all shapes used
        self.shape_dct[self.shape_1_name] = graphics.BattleShip(MainScreen.screen_width, MainScreen.screen_height)

        # register, then hide and delete these objects, we are only using these for shape registration.
        for shape_name, shape_obj in self.shape_dct.iteritems():
            self.main_screen.screen.register_shape(shape_name, shape_obj.return_shape())
            shape_obj.boat.clear()
            shape_obj.boat.ht()
            del shape_obj
            self.shape_dct[self.shape_1_name] = None

eng = MainEngine()
