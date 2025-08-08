import pandas as pd
#Read data from CSV file into a DataFrames
df = pd.read_csv("data.csv")

#data write 
print("Full Data: ")
print(df)
#only show the city column
print("\n Cities:")
print(df['city'])
#Filter : whoom Age >20
print("\n Age>20:")
print(df[df['Age']>20])
