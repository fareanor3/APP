import math

villes= []
home = [48.86193629481076, 2.330573253789304]

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6378.140 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) **2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d

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
    villes(zip(gps[0],distance(home,[float(coords[0]),float(coords[1])])))
print(villes)