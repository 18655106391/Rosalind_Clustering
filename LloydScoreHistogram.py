import LloydAlgorithm as LA
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def generate_indices(index_range,k):
    center_indices=[]
    for i in range(k):
        temp=random.randint(0,index_range-1)
        if temp not in center_indices:
            center_indices.append(temp)
    return center_indices


with open("dataset.txt","r") as f:
    lines=f.read().split("\n")
if "" in lines:
    lines.remove("")
headers=lines[0].split("\t")
if "" in headers:
    headers.remove("")
data=[]
for line in lines[1:]:
    temp=line.split("\t")[2:]
    if "" in temp:
        temp.remove("")
    data.append(list(map(float,temp)))

k=10
distortion,cluster_d=LA.lloyd(data,generate_indices(len(data),k))



