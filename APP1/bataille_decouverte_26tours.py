# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:23:45 2021

@author: loris
"""

import random

def jeu_cartes():

    jeu=[]

    couleurs=["Pique","Coeur","Carreau","Trefle"]

    valeurs=[(2,"Deux"),(3,"Trois"),(4,"Quatre"),(5,"Cinq"),(6,"Six"),(7,"Sept"),(8,"Huit"),(9,"Neuf"),(10,"Dix"),(11,"Valet"),(12,"Dame"),(13,"Roi"),(14,"As")]

    for c in couleurs:

        for v in valeurs:

            jeu.append((c,)+v)

    return jeu

jeu=jeu_cartes()
random.shuffle(jeu)
joueur1=[]
joueur2=[]

###distribution###
for i in range(0,52,2):
    joueur1.append(jeu[i])
for i in range(1,52,2):
    joueur2.append(jeu[i])
    

###jeu###
random.shuffle(joueur1)
random.shuffle(joueur2)
cj1 = []
cj2 = []
n=0

while n<26:

    cj1.append(joueur1[0])
    cj2.append(joueur2[0])
    n+=1
    print(n)

    if cj1[-1][1]>cj2[-1][1]: #joueur 1 gagne

        joueur2.pop(0)   # ajoute l'elment de la liste à la fin
        joueur1.pop(0)
        joueur1.append(cj2)
        joueur1.append(cj1)
        
        print("joueur 1 gagne")

    elif cj1[-1][1]<cj2[-1][1]: # joueur 2 gagne

        joueur1.pop(0)   # ajoute l'elment de la liste à la fin
        joueur2.pop(0)
        joueur2.append(cj1)
        joueur2.append(cj2)
        
        print("joueur 2 gagne")
        
    elif cj1[-1][1]==cj2[-1][1]:
        print("bataille")
        
        cj1.append(joueur1[1])
        cj2.append(joueur2[1])

        joueur1.pop(0)
        joueur1.pop(0)
        joueur2.pop(0)
        joueur2.pop(0)

        if cj1[-1][1]>cj2[-1][1]: #joueur 1 gagne

            joueur1.append(cj2[-2])
            joueur1.append(cj2[-1])
            joueur1.append(cj1[-2])
            joueur1.append(cj1[-1])
        
        elif cj1[-1][1]<cj2[-1][1]: # joueur 2 gagne

            joueur2.append(cj1[-2])
            joueur2.append(cj1[-1])
            joueur2.append(cj2[-2])
            joueur2.append(cj2[-1])
        
        while cj1[-1][1]==cj2[-1][1]:
            cj1.append(joueur1[0])
            cj2.append(joueur2[0])
            joueur1.pop(0)
            joueur2.pop(0)

            
            if cj1[-1][1]>cj2[-1][1]: #joueur 1 gagne

                joueur1.append(cj2[-2])
                joueur1.append(cj2[-1])
                joueur1.append(cj1[-2])
                joueur1.append(cj1[-1])
        
            elif cj1[-1][1]<cj2[-1][1]: # joueur 2 gagne

                joueur2.append(cj1[-2])
                joueur2.append(cj1[-1])
                joueur2.append(cj2[-2])
                joueur2.append(cj2[-1])

    print("joueur 1 ", len(joueur1))
    print("joueur 2 ", len(joueur2))


if len(joueur1) > len(joueur2) : 
    print("le joueur 1 a Gagner")

elif len(joueur1) < len(joueur2) :
    print("le joueur 2 a Gagner")