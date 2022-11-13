class Adder:
    count = 0

    def __init__(self):
        Adder.count += 1

    def addMyStuff(self, a, b):
        return a + b