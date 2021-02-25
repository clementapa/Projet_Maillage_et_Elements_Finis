"""
@credits : Apavou Clément & Zucker Arthur
@date : 12/03/21
"""

import gmsh
import sys
import math

# Init GMSH
gmsh.initialize(sys.argv)

# Ask GMSH to display information in the terminal
gmsh.option.setNumber("General.Terminal", 1)

# Création de l'appartement
model = gmsh.model
model.add("appartement")

# Paramètres
h = 0.3; # finesse du maillage                   
L = 5; # Longueur appartement
l = 10; # Largeur appartement
d = 0.3; # Épaisseur des murs 
Lf = 2; # Longueur d’une fenêtre
Lr = 2; # Longueur d’une radiateur

points_radiateur = [(L, l/5), (L,l/1.4), (0, L/2)]

points = []
points.append(model.geo.addPoint(0, 0, 0, h))
points.append(model.geo.addPoint(L, 0, 0, h))

points.append(model.geo.addPoint(L, l/5, 0, h))
points.append(model.geo.addPoint(L, l/5 + Lr, 0, h))

points.append(model.geo.addPoint(L, l/2.2, 0, h))

points.append(model.geo.addPoint(L/1.4, l/2.2, 0, h))
points.append(model.geo.addPoint(L/1.4, l/2.2 + d, 0, h))

points.append(model.geo.addPoint(L, l/2.2 + d, 0, h))

points.append(model.geo.addPoint(L, l/1.6, 0, h))

points.append(model.geo.addPoint(L/3 + d, l/1.6, 0, h))
points.append(model.geo.addPoint(L/3 + d, l/2.2, 0, h))
points.append(model.geo.addPoint(L/3, l/2.2, 0, h))

points.append(model.geo.addPoint(L/3, l, 0, h))
points.append(model.geo.addPoint(0, l, 0, h))

points.append(model.geo.addPoint(0, l/5 + Lf, 0, h))
points.append(model.geo.addPoint(0, l/5, 0, h))

lines = []
for i in range(1,len(points)):
    lines.append(model.geo.addLine(i,i+1))

lines.append(model.geo.addLine(len(points),1))

# Curveloop and Surface
curveloop = model.geo.addCurveLoop([i for i in range(1,len(lines)+1)])
L = model.geo.addPlaneSurface([curveloop])

# Physical groups
# gmsh.model.addPhysicalGroup(dim, list of tags, physical tag)
gmsh.model.addPhysicalGroup(2, lines, 1)
gmsh.model.addPhysicalGroup(1, [3,4], 2)
gmsh.model.addPhysicalGroup(1, [len(points)-1,len(points)], 3)

# This command is mandatory and synchronize CAD with GMSH Model. The less you launch it, the better it is for performance purpose
gmsh.model.geo.synchronize()

# Mesh (2D)
model.mesh.generate(2)

# Write on disk
gmsh.write("fichier_msh/config_1.msh")

# Launch the GUI (not mandatory at all)
gmsh.fltk.run();

# Finalize GMSH
gmsh.finalize()