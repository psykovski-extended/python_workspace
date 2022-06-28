import math
from dataclasses import dataclass


@dataclass
class Point2D:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
