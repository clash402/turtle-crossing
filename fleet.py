from car import Car


class Fleet(list):
    def __init__(self, count):
        super().__init__()

        self.count = count
        self._create_fleet()

    # PRIVATE METHODS
    def _create_fleet(self):
        for _ in range(self.count):
            self.append(Car())
