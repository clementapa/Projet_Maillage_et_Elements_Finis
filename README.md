# Projet_Maillage_et_Elements_Finis


# To do later : 
- [ ]  Implementer les méthodes de quadratures 
- [ ] Calculs à faire en 3D 

lancer sh python_librairies_pip.bat

## Structure 
```
├── Classe            
│   ├── Matrice.py              # Fonctions pour assemblage des matrices 
│   ├── Mesh.py                 # Classe Mesh, Triangle, Segment et Point 
│   ├── Quadrature.py           # Méthode de quadrature
│   ├── triplets.py             # Classe Triplets necessaire pour le format CSR
├── immobilier           
│   ├── appart.geo              # 
│   ├── appartement.py          # Static Gesture
│   ├── appartement.geo
│   ├── appartement.msh         # classe Triplets necessaire pour le format CSR
├── indications.txt             # indication du professeur
├── master-paper-rev6.5.pdf     # research article based on the project
├── projet.pdf                  # subject of the project 
└── README.md
```
<img src="https://render.githubusercontent.com/render/math?math=-\int_{\Omega}\Delta uv = 0 ">
<img src="https://render.githubusercontent.com/render/math?math=-\int_{\Omega}\Delta uv = 0 ">
<img src="https://render.githubusercontent.com/render/math?math=\int_{\Omega}\nabla u \nabla v  -\int_{\Omega}(\partial_{n}u)v = 0 ">
<img src="https://render.githubusercontent.com/render/math?math=\int_{\Omega}\nabla u \nabla v = \int_{\Omega}(\partial_{n}u)v ">
<img src="https://render.githubusercontent.com/render/math?math==\int_{\Gamma_{rad}}(\partial_{n}u)v %2B  \int_{\Gamma_{fen}}(\partial_{n}u)v %2B  \int_{\Gamma_{mur}}(\partial_{n}u)v ">
<img src="https://render.githubusercontent.com/render/math?math==\underbrace{\int_{\Gamma_{rad}}(\partial_{n}u)v %2B  \int_{\Gamma_{fen}}(\partial_{n}u)v %2B 0 }_\textrm{Dirichlet homogène}">




