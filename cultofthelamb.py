# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:47:09 2022
@author: arthu
"""
#Permet de copier n'importe quel objet
import copy
#Importation d'un perceptron Multi-Couche
from sklearn.neural_network import MLPClassifier
import numpy as np
#Génère des nombres aléatoires
import random
#Importation des fonctions de prétraitement des données
from sklearn import preprocessing
#Importation d'une forêt d'arbre décisionnels
from sklearn.ensemble import RandomForestClassifier
#Importation des arbres de décisions
from sklearn import tree


import os

clear = lambda: os.system("cls")


class Game:
    def __init__(self):
        """
        Initialisation plateaux + numéros de player , plateaux[player][ligne (bas --> haut)][case (gauche --> droite)]
        """
        self.plateaux = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        ]
        self.P1 = int(0)
        self.P2 = int(1)
        self.scores = [0, 0]
        self.game_base = [] #Historique partie jouée
        self.game_results = [] #Base de résultat qui contient les résultats des parties jouées
        #self.clf = tree.DecisionTreeClassifier() #Classifier Arbre de Décision
        self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(6, 2), random_state=1)
        #self.clf = RandomForestClassifier(n_estimators=50, max_depth=2,random_state=0)
        
        

    def tirage_de(self):
        # Nombre random int entre 1 et 6
        self.devalue = random.randint(1, 6)
        return self.devalue

    def play(self, player):
        # Input player choix colonne
        self.playedColums = 0
        de = self.tirage_de()
        print("")
        print("Dé :", de)
        while True:
            print("Joueur ", player + 1, ", ",end="", sep="")
            self.playedColums = int(input("choix de la colonne entre 1 et 3 : "))
            print("")
            self.playedColums -= 1  # Pour correspondre aux tableaux
            if self.playedColums <= 2 and self.playedColums >= 0:
                break
        # Calcul position vertical (gravité)
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
        # Mise à jour plateaux (nplayer, ligne, colonne)
        if self.playable == True:
            self.plateaux[player][self.ligne][self.playedColums] = de
        else:
            print("La colonne est deja pleine")
            self.play(player)

    def enemyVerif(self, player):
        enemy = 1 - player
        for i in range(0, 3):
            if self.plateaux[enemy][i][self.playedColums] == self.devalue:
                self.plateaux[enemy][i][self.playedColums] = 0
        for _ in range(2):
            for z in range(0, 2):
                if (
                    self.plateaux[enemy][z][self.playedColums] == 0
                    and self.plateaux[enemy][z + 1][self.playedColums] != 0
                ):
                    self.plateaux[enemy][z][self.playedColums] = self.plateaux[enemy][
                        z + 1
                    ][self.playedColums]
                    self.plateaux[enemy][z+1][self.playedColums] = 0

    def point(self, player):
        colonne = [0, 0, 0]
        score = [0, 0, 0]
        for i in range(0, 3):
            for y in range(0, 3):
                colonne[y] = self.plateaux[player][y][i]
            for x in range(1, 7):
                score[i] += (colonne.count(x) ** 2) * x
        self.scores[player] = sum(score)


    def printPoint(self):
        print("")
        print("Player 1 :", self.scores[self.P1], "     Player 2 :", self.scores[self.P2])
        print("")
        

    def printPlate(self):
        # Affiche plateau P1
        for i in reversed(range(0, 3)):
            for j in range(0, 3):
                print("|", end="")
                if (self.plateaux[0][i][j]) == 0:
                    print(" ", end="")
                else:
                    print(self.plateaux[0][i][j], end="")
            print("|")
        print("-------")
        # Affiche plateau P2
        for i in range(0, 3):
            for j in range(0, 3):
                print("|", end="")
                if (self.plateaux[1][i][j]) == 0:
                    print(" ", end="")
                else:
                    print(self.plateaux[1][i][j], end="")
            print("|")

    def endGame(self):
        for player in range(0, 2):
            if self.plateaux[player][0].count(0) == 0 and self.plateaux[player][1].count(0) == 0 and self.plateaux[player][2].count(0) == 0:
                return True
        return False
    
    ################################# AI #########################################
    
    def initPlate(self):
        self.plateaux = [c
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        ]
    def ai_play(self, i):
    
    def convert_plate(self, plateau):
        
    def train_ai_game(self):
        for i in range(0, 10):
            victoire_J1 = 0
            victoire_J2 = 0
            egalite = 0
        
    def player_mov(self, player):
    
    def train_ai_player(self):
        
    def player_ai_play(self, mvt_possible):
    
    def ai_play(self, mvt_possible):
    
    
    
    
    
    
    
    
    
    

    def game(self):
        player = 1
        while not (self.endGame()):
            player = 1 - player
            self.point(1 - player)
            self.point(player)
            self.printPoint()
            self.printPlate()
            self.play(player)
            self.enemyVerif(player)
        self.printPlate()
        