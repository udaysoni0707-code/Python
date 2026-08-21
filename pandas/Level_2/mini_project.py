import pandas as pd
df = pd.read_csv("student.csv")

# task 1 : Print the first 3 rows.
print("Print the first 3 rows.")
print(df.head(3))
print()

# task 2 : Print the last 2 rows.
print("Print the last 2 rows.")
print(df.tail(2))
print()

# task 3 : Print the shape of the DataFrame.
print("Print the shape of the DataFrame.")
print(df.shape)
print()

# task 4 : Print all column names.
print("Print all column names:-")
print(df.columns)
print()

# task 5 : Print information about the DataFrame.
print("Print information about the DataFrame.")
print()
print(df.info())
print()

# task 6 : Print the statistical summary.
print("Print the statistical summary.")
print()
print(df.describe())
print()

""" task 7 : Save the DataFrame as:

student_backup.csv

without the index."""

df.to_csv("mini_project_bacup.csv", index=False)
