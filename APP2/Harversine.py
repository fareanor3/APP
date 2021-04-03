import math
import statistics as stat
villechosen = ""
Villes=[]

def distance(origin, destination):
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
all_gps = {}
lines = file.readlines()
file.close()
for line in lines:
    data = line.split(";")
    if len (data) > 5 and data[5] != "\n" and data [5] != "":
        gps = data[5]
        all_gps[data[1]] = gps


while villechosen not in all_gps :
    villechosen = input("Entrez une ville : ")

Coordschosen = all_gps[villechosen].split(",")
Coordschosen = [float(Coordschosen[0]),float(Coordschosen[1])]


for Ville in all_gps: # ne change pas la complexité car boucle 1 + 2 car les deux s'execute pour ttes les lignes
    coords = all_gps[Ville].split(",")
    Villes.append((Ville,distance(Coordschosen,[float(coords[0]),float(coords[1])])))

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

def mediane(liste):
    lg = len(liste)
    n = lg//2 
    if lg%2 == 1 :		# cas effectif impair
        return liste[n]
    else :
        return (liste[n-1][1]+liste[n][1])/2

print("mediane : ",mediane(Villes))
print("1er quartile : ")
print("le min :",tri_fusion(Villes)[2])
print("3e quartile: ")
print("le max : ",tri_fusion(Villes)[-1])