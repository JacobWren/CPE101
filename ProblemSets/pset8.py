# Name: Jacob Wren
# Course: CPE 101
# Instructor: Irene Humer
# Assignment: Problem set8
# Term: Winter 2020


class Point:
    
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y


    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


    def distance(self, to: 'Point') -> float:
        return ((self.x - to.x) ** 2 + (self.y - to.y) ** 2) ** (1 / 2)
    

    def get_slope_intercept(self, other: 'Point') -> [float, float]:
        slope = (self.y - other.y) / (self.x - other.x)
        return (slope, self.y - (slope * self.x))
        

class Line:

    def __init__(self, p1: Point, p2: Point) -> None:
        if p1.x == p2.x:
            self.m = 0.0
            self.b = p1.y
        else:
            slope = (p1.y - p2.y) / (p1.x - p2.x)
            self.m = slope
            self.b = p1.y - (slope * p1.x)

            
    def __eq__(self, other: 'Line') -> bool:
        return self.m == other.m and self.b == other.b


    def __repr__(self) -> str:
        if self.b >= 0:
            return f"y = {self.m:.1f}x + {self.b:.1f}"
        else:
            return f"y = {self.m:.1f}x - {abs(self.b):.1f}"
            
        
    def to_parallel(self, point: Point) -> 'Line':
        intercept = point.y - (self.m * point.x)
        new_p = (self.m * -1.5) + intercept
        return Line(point, Point(-1.5, new_p))          


    def to_perpendicular(self) -> 'Line':
        slope = -(1 / self.m)
        y = slope * (1 + self.b)
        x = (y - self.b) / slope
        return Line(Point(x, y), Point(0, self.b))


class Circle:

    def __init__(self, center: Point, radius: int) -> None:
        self.center = center
        self.radius = radius


    def __eq__(self, other: 'Circle') -> bool:
        return self.center == other.center and self.radius == other.radius
    

    def __repr__(self) -> str:
        return f"{self.radius}r @ {self.center}"


    def overlaps(self, other: 'Circle') -> bool:
        dist_cent = Point.distance(self.center, other.center)
        radi_sum = self.radius + other.radius
        return dist_cent < radi_sum 

    
    def bisects(self, line: Line) -> bool:
        return self.center.y == (line.m * self.center.x) + line.b
   

def get_point_distances(points: Point) -> float:
    return [i.distance(Point(0, 0)) for i in points] 


def get_circle_distances(circles: Circle) -> float:
    return [i.center.distance(Point(0, 0)) for i in circles] 


def are_in_first_quadrant(points: Point) -> Point:
    return [i for i in points if i.x > 0 and i.y > 0]


def overlaps_unit_circle(circles: Circle) -> Circle:
    return [i for i in circles if Circle(Point(0, 0), 1).overlaps(i)]
