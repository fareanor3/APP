import math
villechosen = ""
Villes=[]

def distance(origin, destination): # code de la distance
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6378.140 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    calcul1 = math.sin(dlat/2) **2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    calcul2 = 2 * math.atan2(math.sqrt(calcul1), math.sqrt(1-calcul1))
    result = radius * calcul2
    return result

file = open("villes.csv", "r")
lines = file.readlines()
file.close()
all_gps = {}

for line in lines:
    data = line.split(";")
    if len (data) > 5 and data[5] != "\n" and data [5] != "":
        gps = data[5]
        all_gps[data[1]] = gps # recuperation d'une liste de ville et coordonnée

while villechosen not in all_gps :
    villechosen = input("Entrez une ville : ") # demande a l'utiliateur de recuperer 

Coordschosen = all_gps[villechosen].split(",")
Coordschosen = [float(Coordschosen[0]),float(Coordschosen[1])]

for Ville in all_gps: # ne change pas la complexité car boucle 1 + 2 car les deux s'execute pour ttes les lignes
    coords = all_gps[Ville].split(",")
    Villes.append((Ville,distance(Coordschosen,[float(coords[0]),float(coords[1])])))

 ### ALGO DE TRIE FUSION ###

def fusion(liste1,liste2):
    liste=[]
    i,j=0,0
    while i<len(liste1)and j<len(liste2):
        if liste1[i][1]<=liste2[j][1]:
            liste.append(liste1[i])
            i+=1
        else:
            liste.append(liste2[j])
            j+=1
    while i<len(liste1):
        liste.append(liste1[i])
        i+=1
    while j<len(liste2):
        liste.append(liste2[j])
        j+=1
    return liste

def tri_fusion(liste):
    if len(liste)<2:
        return liste[:]
    else:
        milieu=len(liste)//2
        liste1=tri_fusion(liste[:milieu])
        liste2=tri_fusion(liste[milieu:])
        return fusion(liste1,liste2)

### FIN ALGO TRIE ###

def mediane(liste):
    lg = len(liste)-1
    n = lg//2 
    return liste[n]

def quartile1(liste):
    lg = len(liste)-1
    n = lg//4
    return liste[n]

def quartile3(liste):
    lg = len(liste)-1
    n = 3*(lg//4)
    return liste[n]

Villes_triees = tri_fusion(Villes)

print("Le Min :         ",Villes_triees[1][0]," pour : ",Villes_triees[1][1],"km")
print("1er Quartile :   ",quartile1(Villes_triees)[0]," pour : ",quartile1(Villes_triees)[1]," km")
print("Mediane :        ",mediane(Villes_triees)[0]," pour : ",mediane(Villes_triees)[1]," km")
print("3e Quartile :    ",quartile3(Villes_triees)[0]," pour : ",quartile3(Villes_triees)[1]," km")
print("Le Max :         ",Villes_triees[-1][0]," pour : ",Villes_triees[-1][1]," km")