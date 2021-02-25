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

def resolution(path, save_path):

  # Paramètres
  Tc = 25 # temperature radiateur
  Tf = -10 # temperature fenêtre

  physical_tag_surface = 1
  physical_tag_radiateurs = 2
  physical_tag_fenetres = 3

  gmsh.initialize(sys.argv)

  print("Résolution en cours ...")

  msh = Mesh()

  msh.GmshToMesh(path)

  # test_mass(msh,1)
  # test_rigi(msh,1)

  t = Triplets()

  Algo_assemblage(msh, physical_tag_surface, t, Masse = False, Rigi = True)

  B = np.zeros((msh.Npts,))
  
  # Bords radiateurs
  print("Dirichlet 1 en cours ...")
  Dirichlet(msh, physical_tag_radiateurs, Tc, t, B)
  # Bords fenêtres
  print("Dirichlet 2 en cours ...")
  Dirichlet(msh, physical_tag_fenetres, Tf, t, B)

  # Résolution
  print("Résolution sur système AU = B en cours ...")
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
  plt.savefig(save_path)

  gmsh.finalize()

# Appartement de l'énoncé
resolution(path = "Immobilier/appartement.msh", save_path = "Figures/appartement.png")

# Appartement d'Arthur (3 configurations)
for i in range(1,3):
  resolution(path = "Immobilier/appartement_arthur/fichier_msh/config_"+str(i+1)+".msh" , save_path = "Figures/config_"+str(i+1)+".png")