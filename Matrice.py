from triplets import *
import numpy as np

def mass_elem(element, alpha =1.):
    M_e = np.zeros((3,3))
    coeff = element.area()/12
    for i in range(3):
        M_e[i,i] = 2*coeff
        for j in range(3):
            if(i!=j):
                M_e[i,j] = coeff
    return M_e

def rigi_elem(element, alpha =1.):
    D_e = np.zeros((3,3))
    coeff = element.area()
    Bp_t_Bp_ = np.matmul(np.transpose(B_p(element)), B_p(element))
    for i in range(3):
        for j in range(3):
            D_e[i,j] = coeff*np.matmul(np.matmul(np.transpose(gradPhi(element,j)),Bp_t_Bp_),gradPhi(element,i))
    return D_e

def Algo_assemblage(msh, physical_tag, Rigi = True, Masse = True):
    t = Triplets()
    for p in (msh.triangles):
        if p.tag == physical_tag : 
            if (Rigi and Masse):
                Mp = mass_elem(p)
                Dp = rigi_elem(p)
            elif (Masse):
                Mp = mass_elem(p)
                Dp = np.zeros((3,3))
            elif (Rigi):
                Dp = rigi_elem(p)
                Mp = np.zeros((3,3))
            for i in range(3):
                I = Loc2Glob(p, i)
                for j in range(3):
                    J = Loc2Glob(p, j)
                    t.append(I,J,Mp[i,j]+Dp[i,j])
    print("Fin algo assemblage")
    return t

def gradPhi (element, i) :
    if(i == 0):
        return np.array([-1,-1])
    elif (i == 1):
        return np.array([1,0])
    return np.array([0,1])
    
def B_p(triangle):
    if(triangle.jac()==0):
        print(triangle.p[0])
        print(triangle.p[1])
        print(triangle.p[2])

    coeff = 1/triangle.jac()
    B = np.zeros((2,2))
    B[0,0] = coeff*(triangle.p[2].y - triangle.p[0].y)
    B[0,1] = coeff*(triangle.p[0].y - triangle.p[1].y)
    B[1,0] = coeff*(triangle.p[0].x - triangle.p[2].x)
    B[1,1] = coeff*(triangle.p[1].x - triangle.p[0].x)
    return B


def Loc2Glob(triangle,indice_loc):
    return triangle.p[indice_loc].id

def test_mass(msh,dim,physical_tag):
	mass = Mass(msh,dim,physical_tag).data
	M = coo_matrix(mass).tocsr()    
	U = np.ones(len(M))
	gama_area = 0
	for i in mesh.triangles:
		gama_area += i.area()
	assert(np.matmul((np.matmul(np.transpose(U),M),U)) == gama_area )

def test_rigi(msh,dim,physical_tag):
	mass = Mass(msh,dim,physical_tag).data
	M = coo_matrix(mass).tocsr()    
	U = np.ones(len(M))
	gama_area = 0
	for i in mesh.triangles:
		gama_area += i.area()
	assert(np.matmul((np.matmul(np.transpose(U),M),U)) == gama_area )

def Dirichlet(msh, physical_tag, g, T, B):
    """ @triplet représente un triplet de la matrice A possiblement à modifier
        @B est le vecteur B qu'il faut modifier
    """
    Indexes_to_nullify = []
    # pour maillage 3D 
    # for t in msh.triangles:
    #     if(t.tag == physical_tag):
    #         for p in t:
    #             Indexes_to_nullify.append(p.id)

    for s in msh.segments:
        if(s.tag == physical_tag):
            for p in s.p:
                Indexes_to_nullify.append(p.id)
    # print(Indexes_to_nullify)
    for i in Indexes_to_nullify:
        for indx in range(len(T.data[0])) :
            if(T.data[1][0][indx] == i):
                T.data[0][indx] = 0
            elif(T.data[1][1][indx] == i):
                T.data[0][indx] *= g 
        T.append(i,i,1)
        B[i] = g
    return T


