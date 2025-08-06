import pandas as pd 
data ={
 "Name":['Ram','seeta','Ramesh','Pinki','Punam']
 "Age":[10,20,30,26,,34]
 "City":['Patna','Lucknow','Goa','mumbai','Rajsthan']
}
df =pd.DataFrame(data)
print(df)
#
df.to.csv("Output.csv",indexFalse)
