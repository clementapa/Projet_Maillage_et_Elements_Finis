
from itertools import count
from math import sqrt
import gmsh

class Point:
    _ids = count(0)
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.id = next(self._ids)
     
    def __str__(self):
        return "Point "+ str(self.id)+ " : ("+str(self.x)+ "," + str(self.y)+ "," +str(self.z)+")"

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
        return sqrt(pow((self.p[1].x-self.p[0].x),2)+pow((self.p[1].y-self.p[0].y),2)+pow((self.p[1].z-self.p[0].z),2))
    
    def jac(self):
        return self.area()

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
        return "Triangle {} : {}".format(self.id,pts_id)

    def area(self):
        return 0.5*abs((self.p[1].x-self.p[0].x)*(self.p[2].y-self.p[0].y)-(self.p[2].x-self.p[0].x)*(self.p[1].y-self.p[0].y))
    
    def jac(self):
        return 2*self.area()

class Mesh :
    def __init__(self):
        pass
        self.points = []
        self.segments = []
        self.triangles = []
        self.Npts = []

    def __str__(self):
        return "Points : {},\nSegments : {},\nTriangles : {},\nNpts = {}".format(self.points,self.segments,self.triangles,self.Npts)

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
        gmsh.merge(filename)
        all_nodes =  gmsh.model.mesh.getNodes()
        # print(all_nodes)
        self.Npts = len(all_nodes[0])
        # print(self.Npts)
        # print(len(all_nodes[1]))

        for i in range(self.Npts):
            self.points.append(Point(all_nodes[1][i*3],all_nodes[1][i*3+1],all_nodes[1][i*3+2]))
        
        # print("gmsh.model.getPhysicalGroups() : {}".format(gmsh.model.getPhysicalGroups()))
        for temp in gmsh.model.getPhysicalGroups():
            dim = temp[0]
            physical_tag = temp[1]
            # print("gmsh.model.getEntitiesForPhysicalGroup({},{}) : {}".format(dim,physical_tag,gmsh.model.getEntitiesForPhysicalGroup(dim, physical_tag)))
            for entity in gmsh.model.getEntitiesForPhysicalGroup(dim, physical_tag):
                # print("entity : ",entity," tag : ",physical_tag)
                elements = gmsh.model.mesh.getElements(dim, entity)
                # print(elements)
                for i in range(len(elements[1][0])):
                    list_pts = []
                    for k in range(dim):
                        # print(elements[2])
                        # print(int(elements[2][0][i*dim+k]-1))
                        # print(self.points[int(elements[2][0][i*dim+k]-1)])
                        list_pts.append(self.points[int(elements[2][0][i*dim+k]-1)])
                    if(dim == 2):
                        self.triangles.append(Triangle(list_pts,physical_tag))
                    else : 
                        self.segments.append(Segment(list_pts,physical_tag))
            # print("Next")
        return 
    

