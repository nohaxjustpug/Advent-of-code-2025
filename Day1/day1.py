class Dial:
    def __init__(self):
        self.number = 50
        self.zeros = 0

    def rotate(self, direction, rotations):
        for i in range(int(rotations)):
            if direction == "L":
                self.number -= 1
                if self.number < 0:
                    self.number = 99
            else:
                self.number += 1
                if self.number > 99:
                    self.number = 0
        
            if self.number == 0:
                self.zeros += 1

if __name__ == "__main__":
    dial = Dial()

    with open("input.txt", "r") as f:
        inputs = f.readlines()
        for input in inputs:
            dir = input[0]
            rots = input[1:]
            print(f"#0: {dial.zeros:05d} | {dial.number}\t->\t{dir}:{rots}")
            dial.rotate(dir, str(rots))
