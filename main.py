import gmsh
import sys
from Mesh import *
import Matrice
from triplets import *

t = Triplets()           
print(t) # ([], ([], []))
t.append(0, 1 ,2.)  
print(t) # ([2.], ([0], [1]))
t.append(3, 4 ,5.2) 
print(t) # ([2., 5.2], ([0, 3], [1, 4]))

print(t.data[0])

print(t.get(3,4))

# Format COO
A = coo_matrix(t.data)    
print(A)
print(A.toarray())

t2 = Triplets()
t2.append(0,0,1.1)
t2.append(0,3,2)
t2.append(1,1,1)
t2.append(2,2,2.3)
t2.append(3,0,0.5)
t2.append(3,1,2)
t2.append(3,3,2)

print('ici')
print(t2.get(3,3))

A = coo_matrix(t2.data)    
print(A)
print(A.toarray())

# Format CSR
A = coo_matrix(t2.data).tocsr()
print(A)

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