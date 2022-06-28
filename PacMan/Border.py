from PacMan.Point2D import Point2D


class Border:

    def __init__(self, p1: Point2D, p2: Point2D):
        self.p1 = p1
        self.p2 = p2
        try:
            self.k = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        except ZeroDivisionError:
            self.k = None

    def isOnLineSegment(self, item: Point2D):
        return self.isOn(item) and self.isBetween(item)

    def isBetween(self, item):
        return min(self.p1.x, self.p2.x) <= item.x <= max(self.p1.x, self.p2.x) and \
               min(self.p1.y, self.p2.y) <= item.y <= max(self.p1.y, self.p2.y)

    def isOn(self, item):
        if self.k is None:
            return self.p1.x == item.x
        else:
            return self.k * (item.x - self.p1.x) == (item.y - self.p1.y)
