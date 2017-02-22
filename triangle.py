# File: triangle.py
from point import Point
from math import sqrt


class Triangle(object):
    def __init__(self, point_A, point_B, point_C):
        """
        This method initializes a new Triangle instance with params:
        (Point) - the first point
        (Point) - the second point
        (Point) - the third point

        >>> triangle = Triangle(Point(1,1), Point(3,1), Point(2,3))
        """
        self.point_A = point_A
        self.point_B = point_B
        self.point_C = point_C

    def get_sides(self):
        """
        This method returns triangle's sides.
        """
        def segment(point1, point2):
            """
            (Point), (Point) -> (float)
            This method returns a length of segment between the two points.
            """
            return sqrt((point1.get_xposition() - point2.get_xposition())**2+(
                point1.get_yposition() - point2.get_yposition())**2)
        return [segment(self.point_B, self.point_C), segment(self.point_A, self.point_C), segment(self.point_A, self.point_B)]

    def is_triangle(self):
        """
        This method checks if the triangle is valid.

        >>> triangle = Triangle(Point(1,1), Point(3,1), Point(2,3))
        >>> triangle.is_triangle()
        True
        """
        sides = self.get_sides()
        if (sides[0] < (sides[1]+sides[2])) and (sides[1] < (sides[0]+sides[2])) and (sides[2] < (sides[0]+sides[1])):
            return True
        else:
            return False

    def perimeter(self):
        """
        This method calculates the perimetr of triangle.

        >>> triangle = Triangle(Point(1,1), Point(3,1), Point(2,3))
        >>> triangle.perimeter()
        6.47213595499958
        """
        return sum(self.get_sides())

    def area(self):
        """
        This method calculates the area of triangle.

        >>> triangle = Triangle(Point(1,1), Point(3,1), Point(2,3))
        >>> triangle.area()
        2.0
        """
        p = self.perimeter()/2
        sides = self.get_sides()
        a, b, c = sides[0], sides[1], sides[2]
        return sqrt((p*(p-a)*(p-b)*(p-c)))
