import pandas as pd

df = pd.read_csv("student.csv")

print(df)

print()
print("head command")
print(df.head()) # print all rows
print(df.head(1)) # print 1st row only 
print(df.head(2)) # print 1st two rows only

# tail ()
#  It returns the last 5 rows of the DataFrame by default.
print(df.tail())

# shape :- it tells us : How many rows and columns are present in a DataFrame.
print("shape command :-")
print(df.shape)

# columns ?? It returns the names of all columns in the DataFrame.
print(df.columns)
print(df.columns[0])
print(df.columns[2])

# info :- it gives a summary of the DataFrame.
print("The info student.csv")
df = pd.read_csv("student.csv")
df.info()

# describe() :- It gives statistical information about numeric columns.
print("Describe method is called :-\n")
print(df.describe())

# to_csv() :- It saves a DataFrame into a CSV file.
df.to_csv("back_up.csv", index=False)