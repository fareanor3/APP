# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:12:31 2021

@author: loris
"""

import random

def jeu_cartes():

    jeu=[]
    symbole=["Pique","Coeur","Carreau","Trefle"]
    nombre=[(2,"Deux"),(3,"Trois"),(4,"Quatre"),(5,"Cinq"),(6,"Six"),(7,"Sept"),(8,"Huit"),(9,"Neuf"),(1,"as")]
    for c in symbole:
        for v in nombre:
            jeu.append((c,)+v)
    return jeu

jeu=jeu_cartes()
random.shuffle(jeu)
joueur1=[]
joueur2=[]

###distribution###
for i in range(0,len(jeu),2):
    joueur1.append(jeu[i])
for i in range(1,len(jeu),2):
    joueur2.append(jeu[i])

print(len(joueur1))
print(len(joueur2))
###jeu###
random.shuffle(joueur1)
random.shuffle(joueur2)
cj1 = []
cj2 = []
n=0


while n<26:
    
    n+=1
    
    cj1.append(joueur1.pop(0))
    cj1.append(joueur1.pop(0))
    cj2.append(joueur2.pop(0))
    cj2.append(joueur2.pop(0))
    score_a1 = cj1[-1][1] # sert a comparer le tuple et donc de ne pas comparer les symboles entre eux
    score_b1 = cj1[-2][1]
    score_a2 = cj2[-1][1]
    score_b2 = cj2[-2][1]
    if score_a1 > score_b1:
        score1 = score_a1*10 + score_b1
    else:
        score1 = score_b1*10 + score_a1
    if score_a2 > score_b2:
        score2 = score_a2*10 + score_b2
    else:
        score2 = score_b2*10 + score_a2
    

    if score_a1>score_a2: #joueur 1 gagne

        joueur1.extend(cj1)   # ajoute l'elment de la liste à la fin
        joueur1.extend(cj2)
        cj1 = []
        cj2 = []
        
    elif score_a1<score_a2: # joueur 2 gagne

        joueur2.extend(cj2)   # ajoute l'elment de la liste
        joueur2.extend(cj1)
        cj1 = []
        cj2 = []
        
        
    print("joueur 1 ", len(joueur1))
    print("joueur 2 ", len(joueur2))

if len(joueur1) > len(joueur2) : 
    print("le joueur 1 a Gagner")    

elif len(joueur1) < len(joueur2) :
    print("le joueur 2 a Gagner")
