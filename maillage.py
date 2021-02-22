import gmsh
import sys
from  Mesh import *
from Matrice import *
from triplets import *
from scipy.sparse.linalg import spsolve

# Paramètres
Tc = 25
Tf = -10

# Initialise gmsh
gmsh.initialize(sys.argv)

# Maillage
print("Maillage en cours ...")

msh = Mesh()

msh.GmshToMesh("appartement.msh")

print("Algo assemblage en cours ...")
t = Algo_assemblage(msh, 1, Masse = False)

b = np.zeros((msh.Npts))
print(len(b))

# # Bords radiateurs
# print("Dirichlet 1 en cours ...")
# t = Dirichlet(msh, 2, Tc, t, b)
# # Bords fenêtres
# print("Dirichlet 2 en cours ...")
# t = Dirichlet(msh, 3, Tf, t, b)

gmsh.finalize()

# Résolution
print("Résolution en cours ...")
A = coo_matrix(t.data).tocsr()
U = spsolve(A, b) # solve avec scipy

# Visualisation
print("Visiualisation en cours ...")
x = [pt.x for pt in msh.points]
y = [pt.y for pt in msh.points]
connectivity=[]
for tri in msh.triangles:
  connectivity.append([ p.id for p in tri.p])

plt.tricontourf(x, y, connectivity, U, 12)
plt.colorbar()
plt.show()

### U de référence
# print("Phase U de référence en cours ...")
# Uref = np.zeros((msh.Npts,))
# for pt in msh.points:
#   I = int(pt.id)
#   Uref[I] = g(pt.x, pt.y)

# plt.tricontourf(x, y, connectivity, Uref, 12)
# plt.colorbar()
# plt.show()