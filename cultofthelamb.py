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
            y -= 1 #Pour correspondre aux tableaux
            if y <= 2 and y >= 0:
                break
        #Calcul position vertical (gravité)
        self.playable = True
        self.ligne = 0
        while True:
            self.val_ligne = self.plateaux[joueur][self.ligne][y]
            if self.val_ligne != 0 and self.ligne < 2:
                self.ligne += 1
            elif self.val_ligne == 0:
                break
            else:
                self.playable = False
                break
        #Mise à jour plateaux (nJoueur, ligne, colonne)
        if self.playable == True:
            self.plateaux[joueur][self.ligne][y]=self.tirage_de()
        else:
            print("La colonne est deja pleine")
            self.jouer(joueur)
        y=0
            
        
    def calcul_point(self, joueur):
         
        
        
        
        joueur.point=int()
            
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