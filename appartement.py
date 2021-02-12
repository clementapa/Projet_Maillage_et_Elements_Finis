import gmsh
import sys
import math

# Init GMSH
gmsh.initialize(sys.argv)
# Ask GMSH to display information in the terminal
gmsh.option.setNumber("General.Terminal", 1)

print(gmsh.__version__)

# Create a model and name it "MyL"
model = gmsh.model
model.add("appartement")

# Parameters
h = 10 # Mesh size

# Create 3 Points on the circle
points = []
points.append(model.geo.addPoint(0, 0, 0, h))
points.append(model.geo.addPoint(100, 0, 0, h))
points.append(model.geo.addPoint(100, 30, 0, h))
points.append(model.geo.addPoint(50, 30, 0, h))
points.append(model.geo.addPoint(50, 100, 0, h))
points.append(model.geo.addPoint(0, 100, 0, h))

# Create 6 lines
lines = []
lines.append(model.geo.addLine(1,2))
lines.append(model.geo.addLine(2,3))
lines.append(model.geo.addLine(3,4))
lines.append(model.geo.addLine(4,5))
lines.append(model.geo.addLine(5,6))
lines.append(model.geo.addLine(6,1))

print(lines)
# Curveloop and Surface
curveloop = model.geo.addCurveLoop([1,2,3,4,5,6])
L = model.geo.addPlaneSurface([curveloop])

# Physical groups
# gmsh.model.addPhysicalGroup(dim, list of tags, physical tag)
gmsh.model.addPhysicalGroup(1, lines, 1)
gmsh.model.addPhysicalGroup(2, [L], 10)

# This command is mandatory and synchronize CAD with GMSH Model. The less you launch it, the better it is for performance purpose
gmsh.model.geo.synchronize()
# Mesh (2D)
# model.mesh.generate(2)
# Write on disk
gmsh.write("MyL.msh")
# Launch the GUI (not mandatory at all)
gmsh.fltk.run();
# Finalize GMSH
gmsh.finalize()