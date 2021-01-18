class Fleet(list):
    def __init__(self, count, car):
        super().__init__()

        self.count = count
        self.car = car

        self._create_fleet()

    # PRIVATE METHODS
    def _create_fleet(self):
        for _ in range(self.count):
            self.append(self.car())
