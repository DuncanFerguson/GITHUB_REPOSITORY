from shapely.geometry import Point, LineString, Polygon
from shapely.geometry import box
import numpy as np
pt1 = Point(0,0)
print(Point(0,0).distance(Point(3,4)))
poly1 = Polygon([(0,0),(1,1),(1,0)]) # list of tuples
print(poly1.area, poly1.length)
print(poly1.geom_type)
print(poly1.bounds)
line1 = LineString([(0,0),(3,4),(6,0)]) # list of tuples
poly2 = box(-3,-3,-2,-2)
