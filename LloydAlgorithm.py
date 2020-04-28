import math

def insert_dict(d,key,value):
    if key in d:
        if value not in d[key]:
            d[key].append(value)
    else:
        d[key]=[value]

class Point:
    def __init__(self,n,coordinates):
        self.dimension=n
        self.coordinates=coordinates

    def get(self,n):
        return self.coordinates[n]

    def __str__(self):
        return "("+",".join(list(map(str,self.coordinates)))+")"

    def distance(self,point2):
        squared_distance=0
        for i in range(self.dimension):
            squared_distance+=(self.get(i)-point2.get(i))**2
        return math.sqrt(squared_distance)

    def equals(self,point2):
        for i in range(self.dimension):
            if self.get(i)!=point2.get(i):
                return False
        return True


class Cluster:
    def __init__(self,centers,data):
        self.centers=centers
        self.data=data
        d={}
        for point in self.data:
            min_dis,assigned_center=self.DC_distance(point)
            insert_dict(d,assigned_center,point)
        self.dict=d
               
    def DC_distance(self,point):
        dlist=[]
        for center in self.centers:
            dlist.append(center.distance(point))
        min_dis=min(dlist)
        assigned_center=self.centers[dlist.index(min_dis)]
        return min_dis,assigned_center

    def data_num(self):
        return len(self.data)

    def squared_error_distortion(self):
        distortion=0
        for point in self.data:
            min_dis,assigned_center=self.DC_distance(point)
            distortion+=(min_dis)**2
        distortion/=self.data_num()
        return distortion

    def new_centers(self):
        new_dict={}
        for center in self.dict:
            new_dict[gravity_point(self.dict[center])]=self.dict[center]
        new_cluster=Cluster(list(new_dict.keys()),self.data)
        return new_cluster

    def __str__(self):
        s=""
        for center in self.dict:
            s+="("+",".join(list(map(str,center.coordinates)))+"):"
            for point in self.dict[center]:
                s+="("+",".join(list(map(str,point.coordinates)))+")"
            s+="\n"
        return s

def point_to_tuple(point):
    coordinate=[]
    for i in range(point.dimension):
        coordinate.append(point.get(i))
    return tuple(coordinate)

def not_equal(list1,list2):
    sorted1=sorted(list1,key=point_to_tuple)
    sorted2=sorted(list2,key=point_to_tuple)
    for i in range(len(list1)):
        if not sorted1[i].equals(sorted2[i]):
            return True
    return False

def gravity_point(point_list):
    gravity_coordinate=[]
    length=len(point_list)
    dimension=point_list[0].dimension
    for i in range(dimension):
        sum=0
        for point in point_list:
            sum+=point.get(i)
        gravity_coordinate.append(sum/length)
    gravity_point=Point(dimension,gravity_coordinate)
    return gravity_point

def change_format(list_of_list,center_indices):
    dimension=len(list_of_list[0])
    data=[]
    centers=[]
    for coordinates in list_of_list:
        data.append(Point(dimension,coordinates))
    for index in center_indices:
        centers.append(data[index])
    return Cluster(centers,data)

def lloyd(list_of_list,center_indices):
    """input a list_of_list and indices of center,output the cluster after iteration and distortion"""
    cluster=change_format(list_of_list,center_indices)
    new_cluster=cluster.new_centers()
    while not_equal(new_cluster.centers,cluster.centers):
        cluster=new_cluster
        new_cluster=cluster.new_centers()
    return new_cluster.squared_error_distortion(),new_cluster.dict


