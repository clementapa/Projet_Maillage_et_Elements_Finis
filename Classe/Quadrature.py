"""
@credits : Apavou Clément & Zucker Arthur
@date : 12/03/21
"""
import numpy as np

def phiRef(element, i:int, param:[float]):
    # to do includen https://bthierry.pages.math.cnrs.fr/course/fem/condition_fourier/ : 
    case = {0 : 1 - param[0]-param[1],
            1 : param[0],
            2 : param[1]}
    return case[i]
    
# def Integrale(msh:Mesh, dim:int, physical_tag:int, f, B:np.array, order=2):
    
#     return