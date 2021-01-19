from turtle import Turtle


class Player(Turtle):
    def __init__(self, ui):
        super().__init__()

        self.ui = ui

        self._STARTING_POS = (0, -260)
        self._MOVE_INCREMENT = 10
        self._FINISH_LINE_Y = 270

        self.penup()
        self.shape("turtle")
        self.shapesize(1.5)
        self.color("blue")
        self.setheading(90)

        self._reset_pos()
        self._listen_for_key_press()

    # PRIVATE METHODS
    def _reset_pos(self):
        self.goto(self._STARTING_POS)

    def _listen_for_key_press(self):
        self.ui.listen()
        self.ui.onkey(self._move_up, "Up")

    def _move_up(self):
        self.forward(self._MOVE_INCREMENT)

    # PUBLIC METHODS
    def has_crossed_finish_line(self):
        if self.ycor() > self._FINISH_LINE_Y:
            self._reset_pos()
            return True

    def has_touched(self, obj):
        if self.distance(obj) < 35:
            return True
