### Tri par insertion

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
        print(array)
    return array

array_insertion = insertion_sort([76,32,65,2,80,11,7])

### Tri par sélection

def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab

liste_triee= tri_selection([34, 52, 1, 7, 40])

###Tri fusion

def tri_fusion(m):
    if len(m) <= 1:
        return m
    milieu = len(m) // 2
    #on prend le mid 
    gauche = m[:milieu]
    droite = m[milieu:]
    #on le refait encore et encore 
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    #"créer une liste avec la fonction fusion 
    return list(fusion(gauche,droite))

def fusion(gauche,droite):
    resultat = []
    #on definie la position de recherche 
    index_gauche=0
    index_droite=0
    #boucle qui a pour condition que la position de recherche soit inferieur a la taille de la liste
    while index_gauche < len(gauche) and index_droite < len(droite): 
        #si la liste1[i] et inferieur ou egale a la liste2[i]
        if gauche[index_gauche] <= droite[index_droite]:
            #alors a liste final aprend l'element liste[i]
            resultat.append(gauche[index_gauche])
            #i1=i1+1
            index_gauche += 1
        else:
            #alors la liste final aprend l'element liste2[i]
            resultat.append(droite[index_droite])
            #i2=i2+1
            index_droite += 1
    #si liste existe alors liste final aprend les "elements" (exemple gauche=[1,2,3,4,5,6]
    #sera egale gauche[2:]=[3,4,5,6] avec extend on fait enleve chaque element et donc on 
    # obtiens liste_final=[3,4,5,6] et non liste_final=[[3,4,5,6]])
    if gauche:
        resultat.extend(gauche[index_gauche:])
    if droite:
        resultat.extend(droite[index_droite:])
    return resultat

L=[3,4,6,2,5,1,8,7]
print(tri_fusion(L))

###Tri à bulles

def tri_bulle(tab):
    n = len(tab)
    # Parcourir tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1 ):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
            print(tab)
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]

tri_bulle(tab)