from gui import GUI
from player import Player
from fleet import Fleet
from scoreboard import Scoreboard
import time


class Game:
    def __init__(self):
        self._gui = GUI()
        self._player = Player(self._gui)
        self._fleet = Fleet(8)
        self._scoreboard = Scoreboard()

    # PUBLIC METHODS
    def play(self):
        game_is_in_progress = True

        while game_is_in_progress:
            self._gui.update()
            time.sleep(0.1)

            for car in self._fleet:
                car.move_left()
                car.has_crossed_finish_line()

                if self._player.has_touched(car):
                    game_is_in_progress = False
                    self._scoreboard.display_game_over()

                if self._player.has_crossed_finish_line():
                    self._scoreboard.increment_level()
                    car.increase_speed()

        self._gui.exitonclick()
