import pandas as pd
df= pd.read_json("Sample_Data.son")
print('Display 10 rows of first')
print(df.head(10)) # head() is use to display the first rows 
print('Display 10rows of last')
print(df.tail(10)) # tail() is use to display the last rows
