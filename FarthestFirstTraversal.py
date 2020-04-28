import math

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return "({},{})".format(self.x,self.y)

    def distance(self,point2):
        diff_x=self.x-point2.x
        diff_y=self.y-point2.y
        return math.sqrt(diff_x**2+diff_y**2) 

class Cluster:
    def __init__(self,centers,data):
        self.centers=centers
        self.data=data

    def center_num(self):
        return len(self.centers)

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

def farthest_first_traversal(data,k):
    cluster=Cluster([data[0]],data)
    while cluster.center_num()<k:
        new_center=cluster.farthest_data()
        cluster.centers.append(new_center)
    return cluster.listify_centers()

with open("dataset_38039_2.txt","r") as f:
    lines=f.read().split("\n")
if "" in lines:
    lines.remove("")
k,m=list(map(int,lines[0].split(" ")))
point_list=[]
for line in lines[1:]:
    temp=line.split(" ")
    if "" in temp:
        temp.remove("")
    x,y=list(map(float,temp))
    point_list.append(Point(x,y))

centers=farthest_first_traversal(point_list,k)

with open("answer.txt","w+") as f:
    for x,y in centers:
        f.write("{} {}\n".format(x,y))

