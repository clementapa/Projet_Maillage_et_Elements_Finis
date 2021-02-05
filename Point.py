from itertools import count
from math import sqrt

class Point:
    _ids = count(0)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = next(self._ids)
     
    def __str__(self):
        return "Point "+ str(self.id)+ " : ("+str(self.x)+"," + str(self.y)+")"

p1 = Point(1,1)
print(p1)
p2 = Point(1,2)
print(p2)
p3 = Point(2,1)
print(p3)

class Segment:
    _ids = count(0)
    def __init__(self, p, tag):
        self.p = p
        self.tag = tag
        self.id = next(self._ids)
     
    def __str__(self):
        pts_id = ""
        for i in self.p:
            pts_id += " " +str(i.id)
        return "Segment "+ str(self.id)+ " :" + pts_id

    def area(self):
        return sqrt(pow((p2.x-p1.x),2)+pow((p2.y-p1.y),2))
    
    def jac(self):
        return self.area()

list_pts = [p1, p2]
s1 = Segment(list_pts,0)
print(s1)
print(s1.area())
print(s1.jac())


class Triangle:
    _ids = count(0)
    def __init__(self, p, tag):
        self.p = p
        self.tag = tag
        self.id = next(self._ids)

    def __str__(self):
        pts_id = ""
        for i in self.p:
            pts_id += " " +str(i.id)
        return "Triangle "+ str(self.id)+ " :" + pts_id

    def area(self):
        return 0.5*abs((self.p[1].x-self.p[0].x)*(self.p[2].y-self.p[0].y)-(self.p[2].x-self.p[0].x)*(self.p[1].y-self.p[0].y))
    
    def jac(self):
        return 2*self.area()

list_pts = [p1, p2, p3]
t1 = Triangle(list_pts,0)
print(t1.p[1].x)
print(t1.area())
print(t1.jac())

class Mesh :
    def __init__(self, points, segments, triangles, Npts):
        self.points = points
        self.segments = segments
        self.triangles = triangles
        self.Npts = Npts

    def __str__(self):
        return

    def getElements(self, dim, physical_tag):
        elem = []
        if (dim == 1):
            for s in self.segments:
                if(s.tag == physical_tag):
                    elem.append(s.id) 
        else :
            for t in self.triangles:
                if(t.tag == physical_tag):
                    elem.append(t.id) 
        return elem

    def getPoints(self, dim, physical_tag):
        elem = self.getElements(dim,physical_tag)
        index_pts = []
        if(dim == 1):
            for s in self.segments :
                if (s.id in elem): 
                    for pt in s.p:
                        index_pts.append(pt)
        else :
            for t in self.triangles :
                if (t.id in elem): 
                    for pt in t.p:
                        index_pts.append(pt)
        return index_pts 
    
    def GmshToMesh(self, filename):
        file_msh = open(filename, "r")
        
        return 

m = Mesh(list_pts,[s1],[t1],len(list_pts))
print(m.getPoints(1,0)[1])