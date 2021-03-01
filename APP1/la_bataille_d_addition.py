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
compte1=0
compte2=0

while len(joueur1)>0 and len(joueur2)>0:
    cj1.append(joueur1.pop(0))
    cj1.append(joueur1.pop(0))
    cj2.append(joueur2.pop(0))
    cj2.append(joueur2.pop(0))
    score_a1 = cj1[-1][1] + cj1[-2][1] 
    score_a2 = cj2[-1][1] + cj2[-2][1]
    

    if score_a1>score_a2: #joueur 1 gagne

        joueur1.extend(cj1)   # ajoute l'elment de la liste à la fin
        joueur1.extend(cj2)
        cj1 = []
        cj2 = []
        compte1 += 1
        
    elif score_a1<score_a2: # joueur 2 gagne

        joueur2.extend(cj2)   # ajoute l'elment de la liste
        joueur2.extend(cj1)
        cj1 = []
        cj2 = []
        compte2 += 1
        
    print("joueur 1 ", len(joueur1))
    print("joueur 2 ", len(joueur2))

if len(joueur1) > len(joueur2) : 
    print("Le joueur 1 a gagné")
    print("score :" compte1)
    print("à ",compte2)

elif len(joueur1) < len(joueur2) :
    print("Le joueur 2 a gagné")
    print("score :" compte2)
    print("à ",compte1)
