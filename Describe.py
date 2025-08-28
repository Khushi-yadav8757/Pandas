import pandas as pd 
data ={
"Name":['Ram','seeta','Radha','Krishna']
"Age":[10,11,15,16]
"Salary":[10000,50000,190000,80000]
"Performance_Score":[85,90,94,98]
}
df=pd.Dataframe(data)
print("Sample_Dataframe")
print (df.describe())
