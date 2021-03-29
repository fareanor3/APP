import math

villes= []
home = [48.86193629481076, 2.330573253789304]

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
all_gps = []
lines = file.readlines()
for line in lines:
    data = line.split(";")
    if len (data) > 5 and data[5] != "\n":
        gps = data[5]
        all_gps.append((data[1], gps))

for gps in all_gps: # ne change pas la complexité car boucle 1 + 2 car les deux s'execute pour ttes les lignes
    coords = gps[1].split(",")
    print(gps[0],distance(home,[float(coords[0]),float(coords[1])])) # passer sous la forme d'un dico ( tuple )
    d = {k:v for k, v in iterable}
    #num_list = [1,2,3,4]
    #name_list = ["one","two","three","four"]
    #print ({name_list[i]:num_list[i] for i in range(len(num_list))

    #villes(zip

def fusion(liste1,liste2):
    liste=[]
    i,j=0,0
    while i<len(liste1)and j<len(liste2):
        if liste1[i]<=liste2[j]:
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

L=[3,4,6,2,5,1,8,7]
print(tri_fusion(L))