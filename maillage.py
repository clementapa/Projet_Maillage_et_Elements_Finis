import gmsh
import sys
from  Mesh import *
import Matrice
import triplets

# Paramètres
Tc = 25
Tf = -10

# Maillage
msh = Mesh()

t = Algo_assemblage(msh)
b = np.zeros((msh.Npts,))
t = Dirichlet(msh, 1, Tc, t, b)
t = Dirichlet(msh, 2, Tf, t, b)

# Résolution
A = coo_matrix(t.data).tocsr()
U = spsolve(A, b) # solve avec scipy

# # Visualisation
# x= [pt.x for pt in msh.points]
# y= [pt.y for pt in msh.points]
# connectivity=[]
# for tri in msh.triangles:
#   connectivity.append([ p.id for p in tri.p])

# plt.tricontourf(x, y, connectivity, U, 12)
# plt.colorbar()
# plt.show()

# ### U de référence
# Uref = np.zeros((msh.Npts,))
# for pt in msh.points:
#   I = int(pt.id)
#   Uref[I] = g(pt.x, pt.y)
# plt.tricontourf(x, y, connectivity, Uref, 12)
# plt.colorbar()
# plt.show()