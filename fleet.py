class Fleet(list):
    def __init__(self, car):
        super().__init__()

        self._car = car
        self._car_count = 8

        self._create_fleet()

    # PRIVATE METHODS
    def _create_fleet(self):
        for _ in range(self._car_count):
            self.append(self._car())

    # PRIVATE METHODS
    def update_car_count(self, count):
        self._car_count = count
