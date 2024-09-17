import pandas as pd
aditi={"cal":[420,380,390],"duration":[50,40,45]}
aditinew=pd.DataFrame(aditi)
print(aditinew)

#use loc for specified row
print(aditinew.loc[0])

#use loc for returning in a table
print(aditinew.loc[[0,1]])