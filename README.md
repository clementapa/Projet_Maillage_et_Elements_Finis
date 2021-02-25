<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

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
<img src="https://render.githubusercontent.com/render/math?math=
\begin{align}
-\int_{\Omega}\Delta uv &= 0 \\
\int_{\Omega}\nabla u \nabla v  -\int_{\Omega}(\partial_{n}u)v &= 0 \\
\int_{\Omega}\nabla u \nabla v &= \int_{\Omega}(\partial_{n}u)v \\
&=  \int_{\Gamma_{radiateur}}(\partial_{n}u)v +  \int_{\Gamma_{fenêtre}}(\partial_{n}u)v +  \int_{\Gamma_{mur}}(\partial_{n}u)v \\
&=  \underbrace{\int_{\Gamma_{radiateur}}(\partial_{n}u)v +  \int_{\Gamma_{fenêtre}}(\partial_{n}u)v + 0 }_\textrm{Dirichlet homogène}
\end{align}">
