# Projet_Maillage_et_Elements_Finis

Projet de Maillage et Éléments Finis, implémenté par `Clément Apavou` et `Arthur Zucker`.

## Structure 
```
├── Classe            
│   ├── Matrice.py              # Fonctions pour assemblage des matrices A et B du système AU = B
│   ├── Mesh.py                 # Classes Mesh, Triangle, Segment et Point 
│   ├── triplets.py             # Classe Triplets necessaire pour le format CSR
├── Figures                     # Contient les rendus 
│   ├── appartement.png         # Appartement énoncé
│   ├── config_1.png            # Appartement d'Arthur : configuration 1 
│   ├── config_2.png            # Appartement d'Arthur : configuration 2
│   ├── config_3.png            # Appartement d'Arthur : configuration 3
├── Images                       
|   ├── 2020-2021-flat.svg      # Image de l'appartement de l'énoncé
│   ├── equation1.svg           # Équation de l'énoncé
│   ├── equation2.svg           # a(u,v) = l(v)
├── Immobilier       
│   ├── appartement_arthur      # Essaie de dfférentes position du radiateur dans l'appartement d'Arthur
|   |   |── fichier_msh
|   │   |   ├── config_1.msh    # Configuration 1
|   │   |   ├── config_2.msh    # Configuration 2
|   │   |   ├── config_3.msh    # Configuration 3
│   |   ├── config_1.png        # Appartement d'Arthur : configuration 1 
│   |   ├── config_2.png        # Appartement d'Arthur : configuration 2
│   |   ├── config_3.png        # Appartement d'Arthur : configuration 3
│   ├── appartement.geo         # Fichier .geo permettant de générer l'appartement de l'énoncé 
│   ├── appartement.msh         # Fichier .msh : maillage de l'appartement de l'énoncé   
│   ├── appartement.py          # Fichier .py permettant de générer l'appartement de l'énoncé    
├── python_librairies_pip.bat   # fichier permettant d'installer les librairies python necessaires 
├── resolution.py               # fichier permettant de résoudre le problème à l'aide des élements finis P1
└── README.md
```
## Installation des librairies python via pip

Lancer la commande `sh python_librairies_pip.bat`<br/>
Les librairies qui vont être installées sont: 
* alive-progress
* numpy
* scipy
* matplotlib

##  Énoncé

![](Images/2020-2021-flat.svg=400x)
<br/>
![](Images/equation1.svg)
<br/>
Une condition de Neumann homogène et deux conditions de Dirichlet hétérogène.

## a(u,v) = l(v)
![](Images/equation2.svg)

Dans le système AU = B, il n'y aura donc pas de matrice de masse à calculer pour A et pas de méthode de quadrature à faire pour le calcul de B.

## Utilisation du code
Pour résoudre le problème il faut lancer le code resolution.py via la commande `python resolution.py`, la figure de la solution sera alors créée dans le repertoire `Figures`.

## Appartement énoncé

### Les paramètres : 
* La finesse du maillage `h = 0.5`                   
* Longueur appartement `L = 10`
* Largeur appartement `l = 10`
* Épaisseur des murs `d = 0.5`
* Longueur d’une fenêtre `Lf = 2`
* Longueur d’une radiateur `Lr = 2`
* `Tc = 25`
* `Tf = -10`

![](Figures/appartement.png)


## Détermination de la position du radiateur dans l'appartement d'Arthur

Arthur a très froid en ce moment il ne sait pas où mettre le radiateur dans son appartement. À l'aide de la méthode des élements finis P1 pour résoudre l'équation nous allons determiner où est ce que Arthur mettra son radiateur. 
Nous avons essayé trois configurations différentes.

### Configuration 1 : à côté de son lit 

![](Figures/config_1.png)

### Configuration 2 : dans la salle de bain

![](Figures/config_2.png)

### Configuration 3 : dans le couloir de l'entrée à côté de la fenêtre
![](Figures/config_3.png)