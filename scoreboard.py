from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()

        self._FONT = ("Courier", 18, "normal")

        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 270)

        self.update_display(level)

    # PUBLIC METHODS
    def update_display(self, level):
        self.clear()
        self.write(f"Level: {level}", align="left", font=self._FONT)

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=self._FONT)
