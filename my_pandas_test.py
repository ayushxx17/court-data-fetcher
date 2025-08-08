# series -> it is 1D array like object which can hold  any type.It is similar to colomn in table.

import pandas as pd
"""
data = [1,2,3,4,5]
series = pd.Series(data)
print("series: \n", series)
print(type(data))


# create series data dict

data = {'a':1, 'b':2, 'c':3}
series_dict = pd.Series(data)
print(series_dict)
print(type(data))


data1 = [10, 20, 30]
index = ['a','b','c']
print(pd.Series(data1, index=index))
print(type(data1))
"""

# Data Frame --> It has multiple rows and coloumn. (2D array) 

# Creating DataFrame
"""
data = {
    'Name': ['Ayush', 'John', 'Krish'],
    'Age': ['21', '27', '35'],
    'City': ['Noida', 'Pune', 'Delhi']
}

df = pd.DataFrame(data)
print(df)
print(type(df))

import numpy as np   # We can also import numpy here.
print(np.array(df))"""


# Creating Data Frame from list of dictionary (2nd Method)
"""
data1 = [
    {'Name':'Ayush', 'Age':'21', 'City':'Noida'},
    {'Name':'Harsh', 'Age':'21', 'City':'Pune'},
    {'Name':'Alok', 'Age':'22', 'City':'Delhi'},
    {'Name':'Ansh', 'Age':'23', 'City':'Gurgoan'}

]

df = pd.DataFrame(data1)
print(df)
print(type(df))"""

"""
df = pd.read_csv('data(1).csv')
print(df.head(5))   # print top 5 records
print(df.tail(5))   # print bottom 5 records


"""

#Accessing data from dataframe

data = {
    'Name': ['Ayush', 'John', 'Krish'],
    'Age': ['21', '27', '35'],
    'City': ['Noida', 'Pune', 'Delhi']
}

df = pd.DataFrame(data)
print(df['Name'])
print(type(df['Name'])) 
print(df.loc[0][0])        # use for accesing the row.
print(df.iloc[0])       # index location.
print(df)               # print whole data frame.

# Acessing Specified element

print(df.at[1,'Age'])     # print Age at index 1.
print(df.at[0,'Name'])
print(df.iat[2,2])        # we can access both rows & column index

# Data manipulation with data frame

df['Salary'] = [70000,60000,55000]    # Addiing a new column.
print(df)

df.drop('Salary', axis=1)   # it temprory drop a column again it will show when we give command(print(df))
print(df)

df.drop('Salary', axis=1, inplace=True)  # it permantely drop the column, axis=1 it means accesing of colmn not row whwn axis=0 it means rows.
print(df)

df.drop(0,inplace=True)   # drop column permanetly.
print(df)

