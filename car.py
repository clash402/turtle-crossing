from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()

        self._MOVE_INCREMENT = 10
        self._FINISH_LINE_X = -340
        self._COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(self._COLORS))

        self._reset_pos()

    # PRIVATE METHODS
    def _reset_pos(self):
        ran_x = random.randint(320, 800)
        ran_y = random.randint(-200, 200)
        self.goto(ran_x, ran_y)

    # PUBLIC METHODS
    def move_left(self):
        pos_x = self.xcor() - self._MOVE_INCREMENT
        self.goto(pos_x, self.ycor())

    def has_crossed_finish_line(self):
        if self.xcor() < self._FINISH_LINE_X:
            self._reset_pos()
            return True

    def increase_speed(self):
        self._MOVE_INCREMENT += 2
