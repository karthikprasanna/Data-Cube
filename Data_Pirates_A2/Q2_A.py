from itertools import count
import pandas as pd
import numpy as np
from pandasql import sqldf

data=pd.read_csv("master.csv")

Dims=['country','age','generation']
numDims=len(Dims)
Cardinality=[]
dist_values=[]
Data_count=[]

p="SELECT * FROM data ORDER BY country,age,generation;"
data=sqldf(p,globals())


for i in range(numDims):
    dist_values.append(data[Dims[i]].unique())
    Cardinality.append(len(dist_values[i]))
    K=np.unique(data[Dims[i]], return_counts=True)
    Data_count.append(K[1])


output_dim=['ALL','ALL','ALL']

def aggregate(input):
    i=0
    q="SELECT "
    if(output_dim[0]!='ALL'):
        i=1
        q=q+"country"

    if(output_dim[1]!='ALL'):
        if(i==1):
            q=q+","
        q=q+"age"
        i=1

    if(output_dim[2]!='ALL'):
        if(i==1):
            q=q+","
        q=q+"generation"
        i=1

    if(i==1):
        q=q+","

    q=q+"COUNT(*),SUM(suicides_no),SUM(population) FROM input"
    if(i==1):
        q=q+" WHERE "
        i=0
        if(output_dim[0]!='ALL'):
            i=1
            q=q+"country='"+output_dim[0]+"'"

        if(output_dim[1]!='ALL'):
            if(i==1):
                q=q+" AND "
            q=q+"age='"+output_dim[1]+"'"
            i=1

        if(output_dim[2]!='ALL'):
            if(i==1):
                q=q+" AND "
            q=q+"generation='"+output_dim[2]+"'"
            i=1

    if(i==1):
        q=q+" GROUP BY "
        i=0
        if(output_dim[0]!='ALL'):
            i=1
            q=q+"country"

        if(output_dim[1]!='ALL'):
            if(i==1):
                q=q+","
            q=q+"age"
            i=1

        if(output_dim[2]!='ALL'):
            if(i==1):
                q=q+","
            q=q+"generation"
            i==1
    q=q+";"
    x=sqldf(q,globals())
    return x

def Partition(input,d,C):
    q="SELECT * FROM input ORDER BY "
    q=q+Dims[d]
    q=q+";"
    x=sqldf(q,globals())
    


    return x

def paging(d):
    for i in range(Cardinality[d]):
        data[[data[Dims[d]]]==dist_values[d][i]].to_csv("./"+d+"_"+i+".csv")

# def print_values(out):
#     pol=out.values[0].astype(str)
#     n=len(pol)
#     for m in range(n):

#     f.write()

def BUC(input,dimen,min_sup):
    output=aggregate(input)
    # output.to_csv("./output.csv")
    # print_values(output)
    # print(output)
    # np.savetxt(r'./output.txt', output.values, fmt='%s')
    # f.write(output.astype(str))

    for d in range(dimen,numDims):
        C=Cardinality[d]
        K=np.unique(input[Dims[d]], return_counts=True)
        Data_count[d]=K[1]
        dist_values[d]=K[0]
        C=len(dist_values[d])
        data1=Partition(input,d,C)
        k=0
        
        for i in range(C):
            sup_count=Data_count[d][i]
            if(sup_count>=min_sup):
                output_dim[d]=dist_values[d][i]
                input=data1[k:k+sup_count]
                input=input.copy()
                BUC(input,d+1,min_sup)
            k+=sup_count
        output_dim[d]='ALL'
    pass

input=data.copy()

import time
min_sup_values = []
execution_time = []
for i in range(100, 5000, 500):
    f = open('output.csv', 'w')
    start_time = time.time()
    BUC(input, 0, i)
    time_taken = time.time() - start_time
    min_sup_values.append(i)
    execution_time.append(time_taken)
    f.close()

import matplotlib.pyplot as plt
plt.plot(min_sup_values, execution_time)
plt.xlabel('Minimum Support')
plt.ylabel('Execution Time')
plt.show()

# q="SELECT * FROM data WHERE country='"+dist_values[0][8]+"'"
# print(sqldf(q,globals()))

# print(Data_count)

# print(dist_values)

# print(data.groupby('age').size())

# print(Cardinality)

# print(len(data['country'].unique()))

# print(len(data['age'].unique()))

# print(len(data['generation'].unique()))

