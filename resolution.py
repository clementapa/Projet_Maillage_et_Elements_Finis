"""
@credits : Apavou Clément & Zucker Arthur

Usage:
  resolution.py <name> [options]
  resolution.py appartement  
  resolution.py config_1
  resolution.py config_2
  resolution.py config_3 

Args: 
  <name>        nom de la resolution que l'on veut lancer : appartement/config_1/config_2/config_3

Options:
  -h           Montrer l'en-tête
"""

import gmsh
import sys
from  Classe.Mesh import *
from Classe.Matrice import *
from Classe.triplets import *
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt
import docopt

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
  print("Construction de la visualisation en cours ...")
  x = [pt.x for pt in msh.points]
  y = [pt.y for pt in msh.points]
  connectivity=[]
  for tri in msh.triangles:
    connectivity.append([ p.id for p in tri.p])

  plt.tricontourf(x, y, connectivity, U, 12)
  plt.colorbar()
  plt.savefig(save_path)
  plt.show()
  
  gmsh.finalize()

args = docopt.docopt(__doc__)
name = args['<name>']

# Appartement de l'énoncé
if name == "appartement":
  resolution(path = "Immobilier/appartement.msh", save_path = "Figures/appartement.png")
else: # Appartement d'Arthur
  resolution(path = "Immobilier/appartement_arthur/fichier_msh/"+name+".msh" , save_path = "Figures/"+name+".png")