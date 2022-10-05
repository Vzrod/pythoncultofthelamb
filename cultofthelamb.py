# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:47:09 2022

@author: arthu
"""

import random
import os
clear = lambda: os.system('cls')

class Game:
    
    def __init__(self):
        #Initialisation plateaux + numéros de joueur
        self.plateaux=[[[0,1,0],[0,2,0],[0,0,0]],[[0,1,0],[0,3,0],[0,0,0]]]
        self.J1=int(0)
        self.J2=int(1)
        
    def tirage_de(self):
        #Nombre random int entre 1 et 6
        self.devalue=random.randint(1, 6)
        return self.devalue
        
    def jouer(self, joueur):
        #Input joueur choix colonne
        while True:
            y = int(input("Choix de la colonne entre 1 et 3 : "))
            if y <= 3 and y >= 1:
                break
        #Calcul position vertical (gravité)
        
        
        
        
        #Mise à jour plateaux (nJoueur, ligne, colonne)
        self.plateaux[joueur][1][y]=self.tirage_de()
        y=0
            
    def afficher_plateau(self):
        #Affiche plateau J1
        for i in reversed(range(0,3)):
            for j in range(0,3):
                print("|", end="")
                if (self.plateaux[0][i][j]) == 0:
                    print(" ", end="")
                else:
                    print(self.plateaux[0][i][j], end="")
            print("|")
        print("-------")
        #Affiche plateau J2
        for i in range(0,3):
            for j in range(0,3):
               print("|", end="")
               if (self.plateaux[1][i][j]) == 0:
                   print(" ", end="")
               else:
                   print(self.plateaux[1][i][j], end="")
            print("|")
        
    
        


