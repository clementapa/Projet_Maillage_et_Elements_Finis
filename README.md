# Projet_Maillage_et_Elements_Finis

## Structure 
```
├── Classe            
│   ├── Matrice.py              # Fonctions pour assemblage des matrices A et B du système AU = B
│   ├── Mesh.py                 # Classes Mesh, Triangle, Segment et Point 
│   ├── triplets.py             # Classe Triplets necessaire pour le format CSR
├── Figure                      # Contient les rendus 
│   ├── appartement.png         # Appartement énoncé
│   ├── config_1.png            # Appartement d'Arthur : configuration 1 
│   ├── config_2.png            # Appartement d'Arthur : configuration 2
│   ├── config_3.png            # Appartement d'Arthur : configuration 3
├── immobilier       
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
├── 2020-2021-flat.svg          # Image de l'appartement de l'énoncé
├── python_librairies_pip.bat   # fichier permettant d'installer les librairies python necessaires 
├── resolution.py               # fichier permettant de résoudre le problème à l'aide des élements finis P1
└── README.md
```
## Installation des librairies python via pip

Lancer la commande 'sh python_librairies_pip.bat' \\
Les librairies qui vont être installées sont: 
* alive-progress
* numpy
* scipy
* matplotlib

## 

