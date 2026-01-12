#Pandas for Data Analyst – Complete Guide
---------------------------------------------------------------------------
#1️ What is Pandas?
Pandas is a Python library used for:
Data cleaning
Data analysis
Data manipulation
Handling large datasets (CSV, Excel, SQL, JSON)
Used by Data Analysts, Data Scientists, ML Engineers
---------------------------------------------------------------------------------
#Core Data Structures in Pandas
1. Series (1D Data)
s = pd.Series([10, 20, 30, 40])
print(s)
With index:
s = pd.Series([10, 20, 30], index=['a','b','c'])
# Use case: Single column data
--------------------------------------------------------------------------------------
DataFrame (2D Data – most important)
data = {
    'Name': ['Aman', 'Ravi', 'Neha'],
    'Age': [22, 25, 21],
    'Salary': [30000, 40000, 35000]
}
df = pd.DataFrame(data)
print(df)
-----------------------------------------------------------------------------------------
# Rows + Columns = Excel-like table
------------------------------------------------------------------------------------------
#Reading & Writing Data (VERY IMPORTANT)
Read CSV
df = pd.read_csv('data.csv')

Read Excel
df = pd.read_excel('data.xlsx')

Save Data
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)

# Interview Question:
index=False → removes index column

5️⃣ Basic Data Exploration (Daily Use)
df.head()        # first 5 rows
df.tail()        # last 5 rows
df.shape         # rows, columns
df.columns       # column names
df.info()        # data types & nulls
df.describe()    # statistical summary
