class Dial:
    def __init__(self):
        self.number = 50

    def rotate(self, direction):
        if direction == "L":
            self.number -= 1
            if self.number < 0:
                self.number = 99
        else:
            self.number += 1
            if self.number > 99:
                self.number = 0
