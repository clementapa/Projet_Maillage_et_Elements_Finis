"""
@credits : Apavou Clément & Zucker Arthur
"""

import gmsh
import sys
from  Classe.Mesh import *
from Classe.Matrice import *
from Classe.triplets import *
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

# Paramètres
Tc = 25 # temperature radiateur
Tf = -10 # temperature fenêtre

physical_tag_surface = 1
physical_tag_radiateurs = 2
physical_tag_fenetres = 3

# Initialise gmsh
gmsh.initialize(sys.argv)

# Maillage appartement projet
print("Maillage de l'appartement du projet en cours ...")

msh = Mesh()

msh.GmshToMesh("Immobilier/appartement.msh")

# test_mass(msh,1)
# test_rigi(msh,1)

t = Triplets()
Algo_assemblage(msh, physical_tag_surface, t, Masse = False, Rigi = True)

B = np.zeros((msh.Npts))

# Bords radiateurs
print("Dirichlet 1 en cours ...")
Dirichlet(msh, physical_tag_radiateurs, Tc, t, B)
# Bords fenêtres
print("Dirichlet 2 en cours ...")
Dirichlet(msh, physical_tag_fenetres, Tf, t, B)

# Résolution
print("Résolution en cours ...")
A = coo_matrix(t.data).tocsr()
U = spsolve(A, B) # solve avec scipy

# Visualisation
print("Visualisation en cours ...")
x = [pt.x for pt in msh.points]
y = [pt.y for pt in msh.points]
connectivity=[]
for tri in msh.triangles:
  connectivity.append([ p.id for p in tri.p])

plt.tricontourf(x, y, connectivity, U, 12)
plt.colorbar()
plt.savefig("Figures/appartement.png")

gmsh.finalize()

# Maillage de l'appartement d'arthur
# Initialise gmsh
# gmsh.initialize(sys.argv)

# for i in range(3):
#   print("Maillage de l'appartement d'arthur en cours ...")

#   msh = Mesh()

#   msh.GmshToMesh("Immobilier/appartement_arthur/fichier_msh/config_"+str(i+1)+".msh")

#   # test_mass(msh,1)
#   # test_rigi(msh,1)

#   t = Triplets()
#   Algo_assemblage(msh, physical_tag_surface, t, Masse = False, Rigi = True)

#   B = np.zeros((msh.Npts))

#   # Bords radiateurs
#   print("Dirichlet 1 en cours ...")
#   Dirichlet(msh, physical_tag_radiateurs, Tc, t, B)
#   # Bords fenêtres
#   print("Dirichlet 2 en cours ...")
#   Dirichlet(msh, physical_tag_fenetres, Tf, t, B)

#   # Résolution
#   print("Résolution en cours ...")
#   A = coo_matrix(t.data).tocsr()
#   U = spsolve(A, B) # solve avec scipy

#   # Visualisation
#   print("Visualisation en cours ...")
#   x = [pt.x for pt in msh.points]
#   y = [pt.y for pt in msh.points]
#   connectivity=[]
#   for tri in msh.triangles:
#     connectivity.append([ p.id for p in tri.p])

#   plt.tricontourf(x, y, connectivity, U, 12)
#   plt.colorbar()
#   plt.savefig("Figures/config_"+str(i+1)+".png")

#   break

# gmsh.finalize()