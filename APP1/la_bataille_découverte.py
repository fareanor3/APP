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

while len(joueur1)>0 and len(joueur2)>0:
    cj1.append(joueur1.pop(0))
    cj2.append(joueur2.pop(0))
    print(joueur1)
    print(joueur2)
    if cj1[-1][1]>cj2[-1][1]: #joueur 1 gagne

        joueur1.extend(cj1)   # ajoute l'elment de la liste à la fin
        joueur1.extend(cj2)
        cj1 = []
        cj2 = []
        compte1 += 1
        
    elif cj1[-1][1]<cj2[-1][1]: # joueur 2 gagne

        joueur2.extend(cj1)   # ajoute l'elment de la liste
        joueur2.extend(cj2)
        cj1 = []
        cj2 = []
        compte2 += 1

if len(joueur1) > len(joueur2) : 
    print("Le joueur 1 a gagné")
    print("score :" compte1)
    print("à ",compte2)

elif len(joueur1) < len(joueur2) :
    print("Le joueur 2 a gagné")
    print("score :" compte2)
    print("à ",compte1)

else :
    print("Egalité")
    print("score : "compte2)
    print("à ",compte1)
