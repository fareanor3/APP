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
    print(gps[0],distance(home,[float(coords[0]),float(coords[1])]))

    #num_list = [1,2,3,4]
    #name_list = ["one","two","three","four"]
    #print ({name_list[i]:num_list[i] for i in range(len(num_list))

    #villes(zip