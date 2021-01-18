from turtle import Turtle


class Player(Turtle):
    def __init__(self, gui):
        super().__init__()

        self.gui = gui

        self._STARTING_POS = (0, -260)
        self._MOVE_INCREMENT = 10
        self._FINISH_LINE_Y = 270

        self.penup()
        self.shape("turtle")
        self.shapesize(1.5)
        self.color("blue")
        self.setheading(90)

        self._reset_pos()
        self.listen_for_key_press()

    # PRIVATE METHODS
    def _reset_pos(self):
        self.goto(self._STARTING_POS)

    # PUBLIC METHODS
    def listen_for_key_press(self):
        self.gui.listen()
        self.gui.onkey(self.move_up, "Up")

    def move_up(self):
        self.forward(self._MOVE_INCREMENT)

    def has_crossed_finish_line(self):
        if self.ycor() > self._FINISH_LINE_Y:
            self._reset_pos()
            return True

    def has_touched(self, obj):
        if self.distance(obj) < 35:
            return True
