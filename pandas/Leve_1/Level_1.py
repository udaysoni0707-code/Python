import pandas as pd

# # # check pandas version 
# # print(pd.__version__)

# marks = pd.Series([78,98,88,79,83,95,89])

# print(marks)

# # series of  strings

# name = pd.Series([
#     "Uday",
#     "Rahual",
#     "Aman",
#     "Rohit"
# ])

# print(name)



# print("Series of decimal numbers")

# price = pd.Series([99.5, 125.75, 89.99])

# print(price)


# print("Create a Series from a dictionary.")

# dictionary = pd.Series({
#     "Uday":95,
#     "Rohit":88,
#     "Aman":91
# })

# print(dictionary)


# print("DataFrame")
# # internally it is create a dictionary in python
# student = {
#     "Name": ["Rahul","Aman","Priya"],
#     "Age": [20,21,19],
#     "Marks": [78,90,85]
# }

# # then pandas converts the dictionary into a DataFrame.
# dataframe_df = pd.DataFrame(student)

# # pandas print the table 
# print(f"It is your dataframe :-\n {dataframe_df}")


print("Task 1")

info = {
    "Name": ["Uday","Rahul","Aman"],
    "Age": [21,22,20],
    "City": ["Hisar","Delhi","Jaipur"]
}

df = pd.DataFrame(info)
print(df["Age"])
print(type(df["Age"]))

print(df["City"])
print(type(df["City"]))

print("diff b/w [] & [[]]")
print(df["Name"])
print(type(df["Name"]))

print()

print(df[["Name"]])
print(type(df[["Name"]]))

print("Second Row\n")
print(df.iloc[1])
print(type(df.iloc[1]))

dataframe = pd.DataFrame(
        info,
        index=["A","B","C"]
)

print(dataframe)

print("\nUsing loc")
print(dataframe.loc["C"])

print("\nUsing iloc")
print(dataframe.iloc[2])