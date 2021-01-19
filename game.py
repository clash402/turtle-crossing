import time


class Game:
    def __init__(self, ui, player, fleet, scoreboard):
        self._ui = ui
        self._player = player(self._ui)
        self._fleet = fleet
        self._scoreboard = scoreboard

        self._level = 1

    # PRIVATE METHODS
    def _increment_level(self):  # Possibly move to Game or Level class
        self._level += 1

    # PUBLIC METHODS
    def play(self):
        game_is_in_progress = True

        while game_is_in_progress:
            self._ui.update()
            time.sleep(0.1)

            for car in self._fleet:
                car.move_left()
                car.has_crossed_finish_line()

                if self._player.has_touched(car):
                    game_is_in_progress = False
                    self._scoreboard.display_game_over()

                if self._player.has_crossed_finish_line():
                    self._increment_level()
                    self._scoreboard.update_display(self._level)
                    car.increase_speed()

        self._ui.exitonclick()
