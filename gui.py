from turtle import Screen


class GUI:
    def __init__(self):
        self._screen = Screen()

        self._screen.setup(600, 600)
        self._screen.title("Turtle Crossing")
        self._screen.tracer(0)

    # PUBLIC METHODS
    def update(self):
        self._screen.update()

    def listen(self):
        self._screen.listen()

    def onkey(self, fn, key):
        self._screen.onkey(fn, key)

    def exitonclick(self):
        self._screen.exitonclick()
