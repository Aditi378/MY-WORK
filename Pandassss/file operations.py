#read data from csv files
import pandas as pd
aditi=pd.read_csv("data.csv")
print(aditi.head(11))

#if we want info about the data
df=pd.read_csv('data.csv')
print(df.info())

#if we want to print whole data in one stroke then use to_string()
print(aditi.to_string())

        ##########CLEANING DATA############
#delete the empty cell return without that empty cell
aditinew=aditi.dropna()
print(aditinew.to_string())

#to fill our desired info in the empty cell
aditinew=aditi.fillna(130)
print(aditinew.to_string())

#we can also replace the cell by mean and mode value
x=aditi["Calories"].mean()
aditinew=aditi["Calories"].fillna(x)
print(aditinew.to_string())

aditi[""]=pd.to_datetime(aditi["Calories"])
aditi.dropna(Subset=["Calories"],inplace=True)
print(aditi.to_string())

aditi.loc[7,"Duration"]=45
print(aditi.to_string())

#if we want to apply any condition then
for i in aditi.index:
    if aditi.loc[i,"Duration"]>120:
        aditi.loc[i,"Duration"]=120
        print(aditi.to_string())

#if we want to remove the whole row we can simply use drop()
for i in aditi.index:
    if aditi.loc[i,"Duration"]>120:
        aditi.drop(i,inplace=True)
        print(aditi.to_string()

#for duplicates return true for every row that is duplicate
aditinew=print(aditi.duplicated())
print(aditinew.to_string())

#for removing duplicates----
aditi.drop_duplicates(inplace=True)
print(aditi.to_string())

       