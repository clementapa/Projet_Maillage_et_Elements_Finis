from .triplets import *
import numpy as np
from alive_progress import alive_bar
import math

def signif(x, digit):
    """
    @x : nombre
    @digit : nombre de chiffes significatifs
    Pour avoir le même nombre de significatif pour le test de calcul 
    de la matrice Masse
    """
    if x == 0:
        return 0
    return round(x, digit - int(math.floor(math.log10(abs(x)))) - 1)

def mass_elem(element):
    """
    Calcule la matrice de masse élémentaire de @element 
    """
    M_e = np.zeros((3,3))
    coeff = element.area()/12
    for i in range(3):
        M_e[i,i] = 2*coeff
        for j in range(3):
            if(i!=j):
                M_e[i,j] = coeff
    return M_e

def rigi_elem(element):
    """
    Calcule la matrice de masse de rigidité élémentaire de @element 
    """
    D_e = np.zeros((3,3))
    coeff = element.area()
    Bp_t_Bp_ = np.matmul(np.transpose(B_p(element)), B_p(element))
    for i in range(3):
        for j in range(3):
            D_e[i,j] = coeff*np.matmul(np.matmul(np.transpose(gradPhi(j)),Bp_t_Bp_),gradPhi(i))
    return D_e

def Algo_assemblage(msh, physical_tag, t, Rigi = True, Masse = True):
    """
    Calcule la matrice A sous la forme d'un triplet @t du système AU = B en calculant les matrices de masse élémentaire 
    et de rigidité élémentaire de chaque triangle du maillage et en les assemblant à l'aide de l'algo d'assemblage
    """
    print("Algo assemblage en cours ...")
    with alive_bar(len(msh.triangles)) as bar:
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
            bar()
    return 

def gradPhi(i) :
    """
    Retourne le gradient de la fonction de forme @i dans le triangle de référence 
    """
    if(i == 0):
        return np.array([-1,-1])
    elif (i == 1):
        return np.array([1,0])
    return np.array([0,1])
    
def B_p(triangle):
    """
    Retourne la matrice de passage de @triangle 
    """
    coeff = 1/triangle.jac()
    B = np.zeros((2,2))
    B[0,0] = coeff*(triangle.p[2].y - triangle.p[0].y)
    B[0,1] = coeff*(triangle.p[0].y - triangle.p[1].y)
    B[1,0] = coeff*(triangle.p[0].x - triangle.p[2].x)
    B[1,1] = coeff*(triangle.p[1].x - triangle.p[0].x)
    return B


def Loc2Glob(triangle,indice_loc):
    """
    Retourne l'indice globale du point d'indice @indice_loc dans @triangle
    """
    return triangle.p[indice_loc].id

def test_mass(msh,physical_tag):
    """
    Permet de s'assurer que la matrice de masse est bien calculé
    """
    mass = Algo_assemblage(msh,physical_tag, Rigi=False)
    M = coo_matrix(mass.data).toarray()    
    U = np.ones(msh.Npts)
    gama_area = 0
    for t in msh.triangles:
        gama_area += t.area()
    print(signif(np.matmul(np.matmul(np.transpose(U),M),U),4))
    print(signif(gama_area,4))
    assert(signif(np.matmul(np.matmul(np.transpose(U),M),U),4) == signif(gama_area,4))

def test_rigi(msh,physical_tag):
    """
    Permet de s'assurer que la matrice de rigidité est bien calculé
    """
    rigi = Algo_assemblage(msh,physical_tag, Masse=False)
    D = coo_matrix(rigi.data).toarray()   
    U = np.ones(msh.Npts)
    assert(np.matmul(D,U).all() == 0)

def Dirichlet(msh, physical_tag, g, T, B):
    """
    Applique la condition de Dirichlet à la matrice B et à la matrice T qui reprèsente A
    dans le système AU = B
    """
    Indexes_to_nullify = []
    with alive_bar(len(msh.segments)) as bar:
        for s in msh.segments:
            if(s.tag == physical_tag):
                for p in s.p:
                    Indexes_to_nullify.append(p.id)
            bar()
    
    with alive_bar(len(Indexes_to_nullify)) as bar:
        for i in Indexes_to_nullify:
            for indx in range(len(T.data[0])) :
                if(T.data[1][0][indx] == i):
                    T.data[0][indx] = 0
                elif(T.data[1][1][indx] == i):
                    T.data[0][indx] *= g 
            T.append(i,i,1)
            B[i] = g
            bar()
    return 


