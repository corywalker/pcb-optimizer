class Space:
    def __init__(self, points, width, height):
        self.points = points
        self.w = width
        self.h = height
        assert len(self.points) == self.h
        for row in self.points:
            assert len(row) == self.w
