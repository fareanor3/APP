import random

def jeu_cartes():

    jeu=[]
    symbole=["Pique","Coeur","Carreau","Trefle"]
    nombre=[[2,"Deux"],[3,"Trois"],[4,"Quatre"],[5,"Cinq"],[6,"Six"],[7,"Sept"],[8,"Huit"],[9,"Neuf"],[10,"dix"],[11,"valet"],[12,"dame"],[13,"roi"],[14,"as"]]
    for c in symbole:
        for v in nombre:
            jeu.append([c,]+v)
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

###jeu###
random.shuffle(joueur1)
random.shuffle(joueur2)
cj1 = []
cj2 = []
compte1=0
compte2=0
flag = False

while len(joueur1)>0 and len(joueur2)>0:
    cj1.append(joueur1.pop(0))
    cj2.append(joueur2.pop(0))
    if compte1 > 10000 or compte2 > 10000:
        flag = True
        break

    if len(joueur1) == 1 :
        flag1 = True
        break 
    elif len(joueur2) == 1 :
        flag2 = True
        break

    if cj1[-1][1]>cj2[-1][1]: #joueur 1 gagne

        joueur1.extend(cj1)   # ajoute l'elment de la liste à la fin
        joueur1.extend(cj2)
        compte1 += len(cj1)*2
        cj1 = []
        cj2 = []
        
    elif cj1[-1][1]<cj2[-1][1]: # joueur 2 gagne

        joueur2.extend(cj1)   # ajoute l'elment de la liste
        joueur2.extend(cj2)
        compte2 += len(cj2)*2
        cj1 = []
        cj2 = []

if len(joueur1) == len(joueur2) or flag == True : 
    print("Egalité")

elif len(joueur1) < len(joueur2) :
    print("Le joueur 2 a gagné")
    print("score :" ,compte2,"cartes")
    print("à ",compte1,"cartes")

elif len(joueur1) > len(joueur2) :
    print("Le joueur 2 a gagné")
    print("score :" ,compte2,"cartes")
    print("à ",compte1,"cartes")
    

import Interface_graphique
