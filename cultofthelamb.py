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
        """
        Initialisation plateaux + numéros de player , plateaux[player][ligne (bas --> haut)][case (gauche --> droite)] 
        """
        self.plateaux=[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
        self.P1=int(0)
        self.P2=int(1)
        self.scores = [0, 0]
        
    def tirage_de(self):
        #Nombre random int entre 1 et 6
        self.devalue=random.randint(1, 6)
        return self.devalue
        
    def play(self, player):
        #Input player choix colonne
        self.playedColums=0
        while True:
            self.playedColums = int(input("Choix de la colonne entre 1 et 3 : "))
            self.playedColums -= 1 #Pour correspondre aux tableaux
            if self.playedColums <= 2 and self.playedColums >= 0:
                break
        #Calcul position vertical (gravité)
        self.playable = True
        self.ligne = 0
        while True:
            self.val_ligne = self.plateaux[player][self.ligne][self.playedColums]
            if self.val_ligne != 0 and self.ligne < 2:
                self.ligne += 1
            elif self.val_ligne == 0:
                break
            else:
                self.playable = False
                break
        #Mise à jour plateaux (nplayer, ligne, colonne)
        if self.playable == True:
            self.plateaux[player][self.ligne][self.playedColums]=self.tirage_de()
        else:
            print("La colonne est deja pleine")
            self.play(player)
     

    def enemyVerif(self, player):
        enemy = 1 - player
        for i in range(0,3):
            if self.plateaux[enemy][self.playedColums][i] == self.devalue: 
                self.plateaux[enemy][self.playedColums][i] = 0
        """for _ in range(2):
            for z in range(0,2):
                if self.plateaux[enemy][self.playedColums][z] == 0 and self.plateaux[enemy][self.playedColums][z+1] != 0:
                    self.plateaux[enemy][self.playedColums][z] = self.plateaux[enemy][self.playedColums][z+1]
            """
        

        
    def point(self, player):
        colonne = [0, 0, 0]
        score = [0, 0, 0]
        for i in range(0,3):
            for y in range(0,3):
                colonne[y] = self.plateaux[player][y][i]
            for x in range(1,7):
                score[i] += (colonne.count(x)**2)*x
        self.scores[player] = sum(score)
            
            
    def printPlate(self):
        #Affiche plateau P1
        for i in reversed(range(0,3)):
            for j in range(0,3):
                print("|", end="")
                if (self.plateaux[0][i][j]) == 0:
                    print(" ", end="")
                else:
                    print(self.plateaux[0][i][j], end="")
            print("|")
        print("-------")
        #Affiche plateau P2
        for i in range(0,3):
            for j in range(0,3):
                print("|", end="")
                if (self.plateaux[1][i][j]) == 0:
                    print(" ", end="")
                else:
                    print(self.plateaux[1][i][j], end="")
            print("|")
            
            
    def endGame(self):
        for player in range(0,2):
            for i in range(0,3):
                if self.plateaux[player][i].count(0) == 0:
                    return True
        return False

    def game(self):
        player = 1
        while not(self.endGame()):
            player = 1 - player
            self.printPlate()
            self.play(player)
            self.enemyVerif(player)
            self.point(player)
             
             
         
         
         