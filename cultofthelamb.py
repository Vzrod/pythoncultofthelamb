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
        
        self.plateauJ1=[[0,1,0],[0,2,0],[0,0,0]]
        self.plateauJ2=[[0,1,0],[0,3,0],[0,0,0]]
        self.J1='J1'
        self.J2='J2'
        
    def tirage_de(self):
        self.devalue=random.randint(1, 6)
        return self.devalue
        
    def jouer(self):
        while True:
            y = int(input("Entrez la colonne entre 1 et 3"))
            if y < 3 and y > 1:
                break
            
    def afficher_plateau(self):
        for i in reversed(range(0,3)):
            for j in range(0,3):
                print("|", end="")
                if (self.plateauJ1[i][j]) == 0:
                    print(" ", end="")
                else:
                    print(self.plateauJ1[i][j], end="")
            print("|")
        print("-------")
        for i in range(0,3):
            for j in range(0,3):
               print("|", end="")
               if (self.plateauJ2[i][j]) == 0:
                   print(" ", end="")
               else:
                   print(self.plateauJ2[i][j], end="")
            print("|")                
        
    
        


