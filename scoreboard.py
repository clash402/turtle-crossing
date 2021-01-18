from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self._FONT = ("Courier", 18, "normal")
        self._level = 1

        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 270)

        self._update_display()

    # PRIVATE METHODS
    def _update_display(self):
        self.clear()
        self.write(f"Level: {self._level}", align="left", font=self._FONT)

    # PUBLIC METHODS
    def increment_level(self):  # Possibly move to Game or Level class
        self._level += 1
        self._update_display()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=self._FONT)
