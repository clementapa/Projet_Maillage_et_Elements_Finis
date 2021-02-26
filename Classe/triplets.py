"""
@credits : Apavou Clément & Zucker Arthur
"""

from scipy.sparse import coo_matrix

class Triplets:
    def __init__(self):
        self.data = ([], ([], []))
    def __str__(self):
        return str(self.data)
    def append(self, I, J, val):
        # Ajoute le triplet [I, J, val] dans self.data
        # (val, (row, col))
        self.data[0].append(val)
        self.data[1][0].append(I)
        self.data[1][1].append(J)
    def get(self, I, J):
        A = coo_matrix(self.data)
        A = A.toarray()
        return A[I][J]