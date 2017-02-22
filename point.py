# File: point.py


class Point:
    'Represents a point in two-dimensional geometric coordinates'
    def __init__(self, x=0, y=0):
        """
        Initialize the position of a new point. The x and y coordinates can be
        specified. If they are not, the point defaults to the origin.
        """
        self.move(x, y)

    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y

    def rotate(self, beta, other_point):
        'Rotate point around other point'
        dx = self.x - other_point.get_xposition()
        dy = self.y - other_point.get_yposition()
        beta = radians(beta)
        xpoint3 = dx * cos(beta) - dy * sin(beta)
        ypoint3 = dy * cos(beta) + dx * sin(beta)
        xpoint3 = xpoint3 + other_point.get_xposition()
        ypoint3 = ypoint3 + other_point.get_yposition()
        return self.move(xpoint3, ypoint3)

    def get_xposition(self):
        return self.x

    def get_yposition(self):
        return self.y

    def __add__(self, point_q, point_r):
        """
        (self, Point, Point) -> (None)
        Move the point p to the location of sum of points q and r.
        p = q + r # Point. __add__()
        """
        self.move(point_q.get_xposition + point_r.get_xposition,
                  point_q.get_yposition + point_r.get_yposition)

    def __iadd__(self, point_q):
        """
        (self, Point) -> (None)
        Move the point p to the location of sum of points p and q.
        p += q # Point. __iadd__()
        """
        self.move(self.get_xposition + point_q.get_xposition,
                  self.get_yposition + point_q.get_yposition)

    def __sub__(self, point_q, point_r):
        """
        (self, Point) -> (None)
        Move the point p to the location of differance of points p and q.
        p = q - r # Point.
        """
        self.move(point_q.get_xposition - point_r.get_xposition,
                  point_q.get_yposition - point_r.get_yposition)

    def __isub__(self, point_q):
        """
        (self, Point) -> (None)
        Move the point p to the location of differance of points p and q.
        p -= q # Point. __isub__()
        """
        self.move(self.get_xposition - point_q.get_xposition,
                  self.get_yposition - point_q.get_yposition)

    def __mul__(self, point_q, n):
        """
        (self, Point, float) -> (None)
        Move the point p to location of multiplication:coord q and n (float).
        p = q * n # Point.
        """
        self.move(point_q.get_xposition * n, point_q.get_yposition * n)

    def __imul__(self, n):
        """
        (self, float) -> (None)
        Move the point p to location of multiplication: coord p and n(float).
        p *= n # Point.
        """
        self.move(self.get_xposition * n, self.get_yposition * n)

    def __truediv__(self, point_q, n):
        """
        (self, Point, float) -> (None) or (str)
        Precautions: n != 0.
        Move the point p to the location of division of coord q and n(float).
        p = q / n # Point.
        """
        if n == 0:
            return "n can't be equall to 0"
        self.move(point_q.get_xposition / n, point_q.get_yposition / n)

    def __itruediv__(self, n):
        """
        (self, float) -> (None) or (str)
        Precautions: n != 0.
        Move the point p to the location of division of coord q and n(float).
        p /= n
        """
        if n == 0:
            return "n can't be equall to 0"
        self.move(self.get_xposition / n, self.get_yposition / n)

    def __floordiv__(self, point_q, n):
        """
        (self, Point, float) -> (None) or (str)
        Precautions: n != 0.
        Move the point p to location of int(division of coord q and n(float)).
        p = q // n # Point.
        """
        if n == 0:
            return "n can't be equall to 0"
        self.move(point_q.get_xposition // n, point_q.get_yposition // n)

    def __ifloordiv__(self, n):
        """
        (self, float) -> (None) or (str)
        Precautions: n != 0.
        Move the point p to location of int(division of coord q and n(float)).
        p //= n
        """
        if n == 0:
            return "n can't be equall to 0"
        self.move(self.get_xposition // n, self.get_yposition // n)
