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


t = Triplets()           
print(t) # ([], ([], []))
t.append(0, 1 ,2.)  
print(t) # ([2.], ([0], [1]))
t.append(3, 4 ,5.2) 
print(t) # ([2., 5.2], ([0, 3], [1, 4]))

# Format COO
A = coo_matrix(t.data)    
print(A)
print(A.toarray())

t2 = Triplets()
t2.append(0,0,1.1)
t2.append(0,3,2)
t2.append(1,1,1)
t2.append(2,2,2.3)
t2.append(3,0,0.5)
t2.append(3,1,2)
t2.append(3,3,2)

A = coo_matrix(t2.data)    
print(A)
print(A.toarray())

# Format CSR
A = coo_matrix(t2.data).tocsr()
print(A)