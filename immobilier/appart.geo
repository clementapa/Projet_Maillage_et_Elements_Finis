h = 1; // finesse du maillage                   
L = 10; // Longueur appartement
l = 10; // Largeur appartement
d = 0.5; // Épaisseur des murs 
Lf = 2; // Longueur d’une fenêtre
Lr = 2; // Longueur d’une fenêtre

Point(1) = {0, 0, 0, h};  
Point(2) = {L/3, 0, 0, h};  
Point(3) = {L/3, l/4, 0, h};  
Point(4) = {L/3 + d,l/4, 0, h}; 
Point(5) = {L/3 + d, 0, 0, h}; 

Point(6) = {L/2, 0, 0, h}; 
Point(7) = {L/2, l/4, 0, h}; 
Point(8) = {L/2, l/4 + Lr, 0, h}; 
Point(9) = {L/2, l/2, 0, h}; 
Point(10) = {L/2 + d, l/2, 0, h}; 
Point(11) = {L/2 + d , 0, 0, h}; 

Point(12) = {L, 0, 0, h};

Point(13) = {L, l/4, 0, h};
Point(14) = {L/1.5, l/4, 0, h};
Point(15) = {L/1.5, l/4 + d, 0, h};
Point(16) = {L, l/4 + d, 0, h};

Point(17) = {L, l/2.5, 0, h};
Point(18) = {L, l/2.5 + Lf, 0, h};

Point(19) = {L, l/1.5, 0, h};
Point(20) = {L/1.5 + Lr, l/1.5, 0, h};
Point(21) = {L/1.5, l/1.5, 0, h};
Point(22) = {L/2.5, l/1.5, 0, h};
Point(23) = {L/2.5, l/1.5 + d, 0, h};
Point(24) = {L, l/1.5 + d, 0, h};

Point(25) = {L, l, 0, h};

Point(26) = {L/1.5 + Lf, l, 0, h};
Point(27) = {L/1.5, l, 0, h};

Point(28) = {L/2.5 + d, l, 0, h};
Point(29) = {L/2.5 + d , l/1.2, 0, h};
Point(30) = {L/2.5, l/1.2, 0, h};
Point(31) = {L/2.5, l, 0, h};

Point(32) = {L/7 + Lf, l, 0, h};
Point(33) = {L/7, l, 0, h};

Point(34) = {0, l, 0, h};

Point(35) = {0, l/1.5 + Lr, 0, h};
Point(36) = {0, l/1.5, 0, h};

Point(37) = {0, l/4 + Lf, 0, h};
Point(38) = {0, l/4, 0, h};

Line(1) = {1,2};            
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,5};
Line(5) = {5,6};            
Line(6) = {6,7};
Line(7) = {7,8};
Line(8) = {8,9};
Line(9) = {9,10};            
Line(10) = {10,11};
Line(11) = {11,12};
Line(12) = {12,13};
Line(13) = {13,14};
Line(14) = {14,15};
Line(15) = {15,16};
Line(16) = {16,17};
Line(17) = {17,18};
Line(18) = {18,19};
Line(19) = {19,20};
Line(20) = {20,21};
Line(21) = {21,22};
Line(22) = {22,23};
Line(23) = {23,24};
Line(24) = {24,25};
Line(25) = {25,26};
Line(26) = {26,27};
Line(27) = {27,28};
Line(28) = {28,29};
Line(29) = {29,30};
Line(30) = {30,31};
Line(31) = {31,32};
Line(32) = {32,33};
Line(33) = {33,34};
Line(34) = {34,35};
Line(35) = {35,36};
Line(36) = {36,37};
Line(37) = {37,38};
Line(38) = {38,1};


Curve Loop(1) = {1:38}; 
Plane Surface(1) = {1};     
Physical Surface(1) = {1}; 

// Radiateur 
Physical Line (2) = {7,20,35};
// Fenêtre
Physical Line (3) = {17,26,32,37};
