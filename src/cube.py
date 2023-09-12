# %%
import pandas as pd
import numpy as np

data = pd.read_excel('../data/master.xlsx')

# %%
data.columns

# %%
data.head()

# %%
# get the number of unique values in each column
unique_counts = data.nunique()

# create a dictionary with column names as keys and number of unique values as values
col_dict = dict(zip(unique_counts.index, unique_counts.values))

# sort the dictionary by values in descending order
sorted_cols = sorted(col_dict, key=col_dict.get, reverse=True)

# rearrange the columns in the data based on the sorted column names
data = data[sorted_cols]

# %%
data.head()

# %%
print(len(data.columns))
print(data['country'].unique())
print(len(data['country'].unique()))
print(len(data))

# %%
numDims = len(data.columns)
cardinality = [len(data[attribute].unique()) for attribute in data.columns]
minSup = 100
outputRec = pd.DataFrame({
    "Combination": [],
    "Count": []
})
dataCount = [[] for _ in range(numDims)]

# %%
print(numDims)
print(cardinality)
print(outputRec)
print(dataCount)

# %%
def Aggregate(input):
    # sort the input dataframe based on first column
    input.sort_values(by=input.columns[5], inplace=True)

    


# %%
def BottomUpCube(input, dim):
    Aggregate(input)
    

# %%
BottomUpCube(data, 0)
data.head()


