from PIL import Image, ImageOps
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import time
from timeit import default_timer as timer
#########from IPython.display import display

#Création des fonctions de tri
def triParComptage(Tab):
   # Initialisation des variables
   bSup=max(Tab)
   TabComptage=[]
   x = 0
  # Initialisation du tableau de comptage à 0
   for i in range (max(Tab)+1):
      TabComptage.append(0)
  
   # Création du tableau de comptage
   for i in range (len(Tab)):
      TabComptage[Tab[i]]+=1
  
   # Création du tableau trié
   for i in range (bSup+1):
      for j in range (TabComptage[i]):
         Tab[x] = i
         x+=1
   return Tab
 
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

#Fonction pour calculer la dilatation d'histogramme
    
def dilatation_histo(Pixel,h):        
    #Tri de la liste         
    #triParComptage(Pixel)       
    imin=h[0]
    imax=h[-1]
    l, g = Pixel.size
    for y in range(g):
        for x in range(l):
            c = Pixel.getpixel((x, y))
            dilat = int((c)*(c-imin)/(imax-imin))
            if dilat>255:
                dilat=255
            Pixel.putpixel((x, y), dilat)
    return Pixel

#Fonction pour changer la luminosité de l'image
def lumino(img,lum):
    
    a=input('voulez vous up ou down la lumino \nTape 1 ou Tape 2\nVotre réponse: ')
    h,l = img.size
    if a == '1': # le if doit être avant les deux boucles qui parcours l'image 
        # Sinon après chaque rebouclage le prog attend la valeur a de l'utilisateur  
        for y in range(h-1):
            for x in range(l-1):
                c = img.getpixel((y, x))
                c += lum
                if c > 255:
                    img.putpixel((y,x), 255)
                else:
                    img.putpixel((y, x), c)
    elif a == '2':
        for y in range(h-1):
            for x in range(l-1):
                c = img.getpixel((y, x))
                c -= lum
                if c < 0:
                    img.putpixel((y,x), 0)
                else:
                    img.putpixel((y, x), c)
    return img

#Liste contenant tous les pixels de l'image
def création(Img): 
    Pixel=[]
    (l,h)=Img.size
    for i in range(l):
        for j in range(h):
            p = Img.getpixel((i, j))
            Pixel.append(p)
    return Pixel
  
#Appel de l'image
Img = Image.open("D:\Programe\Python\APP1\APP\APP3\lena_ng.png")
#Menu 
print("\n\nBienvenue,\nvous allez lancer le programme de modification d'image.")
n=int(input("veuillez choisir un programme à lancer: \n1 Tri des couleurs de l'image \n2 modifier la luminosité \n3 Augmenter le contraste \n\n Entrer ici le numéro: "))
if n==1:
    u=int(input("Quel algorithme de tri voulez vous utiliser ?\n\n1 Tri par comptage \n2 Tri par fusion \n3 Tri par séléction \n Entrer ici le numéro: "))
    Pixel = création(Img)
    if u==1:
        start_time = time.time()
        h=triParComptage(Pixel)
        print(h)
        print("Temps d execution : %s secondes ---" % (time.time() - start_time))
    if u==2:
        start_time = time.time()
        h=tri_fusion(Pixel)
        print(h)
        print("Temps d execution : %s secondes ---" % (time.time() - start_time))
        
    if u==3:
        print(" Cela va prendre un peu de temps...")
        start_time = time.time()
        h=tri_selection(Pixel)
        print(h)
        print("Temps d execution : %s secondes ---" % (time.time() - start_time))
        
    plt.hist(h, range = (0, 255), bins = 255, color = 'yellow', edgecolor = 'red')
    plt.xlabel('Niveaux de gris')
    plt.ylabel('Effectif')
    plt.title('Histogramme des différentes valeurs des pixels dans l\'image')
    plt.show

    
if n==2:
    
    Img.show()
    # Appel de la fonction  
    value = int(input("entrer un contraste entre 0 et 255: "))
    img1 = lumino(Img,value)
    # Affichage des images  
    img1.show()
    
if n==3:
    print("\nImage originale :")
    Img.show()
    Pixel = création(Img)
    h=triParComptage(Pixel)
    plt.hist(h, range = (0, 255), bins = 255, color = 'green', edgecolor = 'blue')
    plt.xlabel('Niveaux de gris')
    plt.ylabel('Effectif')
    plt.title('Histogramme des différentes valeurs des pixels dans l\'image')
    plt.show()
    
    dilatation_histo(Img,h)
    m=création(Img)
    Img.show()
    plt.hist(m, range = (0, 255), bins = 255, color = 'yellow', edgecolor = 'red')
    plt.xlabel('Niveaux de gris')
    plt.ylabel('Effectif')
    plt.title('Histogramme des différentes valeurs des pixels dans l\'image')
    plt.show()
    print("\nImage contrastée :")
    print("\nHistogramme de dilatation : en bleu avant la dilatation, en rouge après la dilatation\n")
#Fin du menu 