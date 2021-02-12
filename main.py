import gmsh
import sys
from Mesh import *
import Matrice

gmsh.initialize(sys.argv)

p1 = Point(1,1,0)
print(p1)
p2 = Point(1,2,0)
print(p2)
p3 = Point(2,1,0)
print(p3)

list_pts = [p1, p2]
s1 = Segment(list_pts,0)
print(s1)
print(s1.area())
print(s1.jac())

list_pts = [p1, p2, p3]
t1 = Triangle(list_pts,0)
print(t1.p[1].x)
print(t1.area())
print(t1.jac())

mass_elem(element, alpha =1.)

# m = Mesh()
# m.GmshToMesh("./MyDisk.msh")
# print(m)

gmsh.finalize()