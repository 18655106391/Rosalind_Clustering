import math

class Point:
    def __init__(self,n):
        self.dimension=n

    def values(self,coordinates):
        self.coordinates=coordinates

    def get(self,n):
        return self.coordinates[n]

    def __str__(self):
        return "("+",".join(self.coordinates)+")"

    def distance(self,point2):
        squared_distance=0
        for i in range(self.dimension):
            squared_distance+=(self.get(i)-point2.get(i))**2
        return math.sqrt(squared_distance)

class Cluster:
    def __init__(self,centers,data):
        self.centers=centers
        self.data=data

    def center_num(self):
        return len(self.centers)

    def data_num(self):
        return len(self.data)

    def DC_distance(self,point):
        dlist=[]
        for center in self.centers:
            dlist.append(center.distance(point))
        return min(dlist)

    def farthest_data(self):
        distance=[]
        for point in self.data:
            distance.append(self.DC_distance(point))
        max_d=max(distance)
        return self.data[distance.index(max_d)]

    def listify_centers(self):
        listed=[]
        for point in self.centers:
            listed.append((point.get_x(),point.get_y()))
        return listed

    def squared_error_distortion(self):
        distortion=0
        for point in self.data:
            distortion+=(self.DC_distance(point))**2
        distortion/=self.data_num()
        return distortion


with open("dataset_10927_3.txt","r") as f:
    lines=f.read().split("\n")
if "" in lines:
    lines.remove("")

k,m=list(map(int,lines[0].split(" ")))
center_list=[]
data_list=[]
line_count=len(lines)
i=1

while lines[i][0].isdigit(): 
    temp=lines[i].split(" ")
    if "" in temp:
        temp.remove("")
    point=Point(m)
    point.values(list(map(float,temp)))
    center_list.append(point)
    i+=1
i+=1
while i<line_count and lines[i][0].isdigit():
    temp=lines[i].split(" ")
    if "" in temp:
        temp.remove("")
    point=Point(m)
    point.values(list(map(float,temp)))
    data_list.append(point)
    i+=1


cluster=Cluster(center_list,data_list)
print(cluster.squared_error_distortion())

   

