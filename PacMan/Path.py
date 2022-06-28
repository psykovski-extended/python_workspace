class Path:

    def __init__(self, points: list):
        self.points = points

    def getNext(self):
        for i in self.points:
            yield i
