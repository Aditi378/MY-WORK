import pandas as pd
aditi=[1,2,3]
aditinew=pd.Series(aditi,index=['x','y','z'])
print(aditinew) 

cal={"day1":420,"day2":380,"day3":390}
aditinew=pd.Series(cal)
print(aditinew)