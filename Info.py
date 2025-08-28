import pandas as pd
df= pd.read_json('sample_data.json')
print ('Displaying the info of data set ')
print(df.info())

#info() is use to find 
the no. of rows and columns 
data types
column name 
non null count
means rows,columns,what types of data & misssing data.
