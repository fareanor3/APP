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
for i in range(0,36,2):
    joueur1.append(jeu[i])
for i in range(1,36,2):
    joueur2.append(jeu[i])

###bataille###
#def face_off():
    #n = 1
    #for i in range (n):
        #if cj1[i+1]>cj2[i+1]:
            #Gjoueur1+=2
        #elif cj1[i+1]<cj2[i+1] :
            #Gjoueur2+=2
        #else :
            #n+=1

###jeu###

pioche=0
Gjoueur1=0
Gjoueur2=0
random.shuffle(joueur1)
random.shuffle(joueur2)
for i in range(0,len(joueur1),2):
    ca1=joueur1[i]
    ca2=joueur2[i]
    cb1=joueur1[i+1]
    cb2=joueur2[i+1]
    score_a1 = ca1[1] # sert a comparer le tuple et donc de ne pas comparer les symboles entre eux
    score_b1 = cb1[1]
    score_a2 = ca2[1]
    score_b2 = cb2[1]

    if score_a1 > score_b1:
        score1 = score_a1*10 + score_b1
    else:
        score1 = score_b1*10 + score_a1
    if score_a2 > score_b2:
        score2 = score_a2*10 + score_b2
    else:
        score2 = score_b2*10 + score_a2
    if score1>score2: #joueur 1 gagne
        Gjoueur1+=2
    elif score1<score2: # joueur 2 gagne
        Gjoueur2+=2
    ##else : #alors bataille 
        ###face_off()


if Gjoueur1 > Gjoueur2 : 
    print("le joueur 1 a Gagner")    
    print("le joueur 1 possède ", Gjoueur1, "  cartes ",sep=(" "))
    print("le joueur 2 possède ", Gjoueur2, "  cartes ",sep=(" "))
elif Gjoueur1 < Gjoueur2 :
    print("le joueur 2 a Gagner")
    print("le joueur 1 possède ", Gjoueur1, "  cartes ",sep=(" "))
    print("le joueur 2 possède ", Gjoueur2, "  cartes ",sep=(" "))
else :
    print("Egualité")
    print("le joueur 1 & 2 possèdent ", Gjoueur1, "  cartes ",sep=(" "))