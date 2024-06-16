import math


class Turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0

    def forward(self, distance):
        self.x += distance * math.sin(math.radians(self.direction))
        self.y += distance * math.cos(math.radians(self.direction))

    def right(self, angle):
        self.direction += angle

    def left(self, angle):
        self.right(-angle)

    def draw(self, rows, cols):
        for i in range(cols-1, -1, -1):
            for j in range(rows):
                if int(self.x) == j and int(self.y) == i:
                    print('X', end='')
                else:
                    print('.', end='')
            print()

    def __repr__(self):
        return f'{self.x:.2f} {self.y:.2f} {self.direction}'


t = Turtle()
t.forward(1)
t.right(90)
t.forward(2)

t.draw(20, 10)
