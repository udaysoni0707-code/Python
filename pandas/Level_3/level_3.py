import pandas as pd

df = pd.read_csv("student_filter.csv")

# # its give boolean value True or False based on the condition
# print(df)
# print(df["Marks"]>80)
# print(f"Age is greater than 21 :{df['Age']>21}")
# print(f"City is delhi :{df['City']=='Delhi'}")

# # Filter rows where Marks is greater than 80
# print(f"Marks is greater than 80:\n {df[df['Marks']>80]}")
# print(f"Age is greater than 21 :\n{df[df['Age']>21]}")
# print(f"City is delhi :\n{df[df['City']=='Delhi']}")

# # use AND (&) operator to filter rows where Marks is greater than 80 and Age is greater than 21
# print(f"Marks is greater than 80 and Age is greater than 21 :\n{df[(df['Marks']>80) & (df['Age']>21)]}")


# # practice 1
# print(f"Marks is greater than 80 and City is Delhi :\n{df[(df['Marks']>80) & (df['City']=="Delhi")]}")

# # practice 2
# print(f"Age is greater than 21 and City is Hisar :\n{df[(df['Age']>21) & (df['City']=="Hisar")]}")

# # practice 3
# print(f"Marks is greater than 85 and Age is less than 22 :\n{df[(df['Marks']>85) & (df['Age']<22)]}")

# print("=" * 50)
# print("Students with Marks > 80 AND City = Delhi")
# print("=" * 50)

# print(df[(df["Marks"] > 80) & (df["City"] == "Delhi")])

# # practice 4 using or (|) operator

# print("=" * 50)
# print("Students from Delhi OR Hisar")
# print("=" * 50)

# print(df[(df["City"] == "Delhi") | (df["City"] == "Hisar")])

# # practice 5 using or (|) operator
# print("=" * 50)
# print("Students with Marks >90 OR Age < 20")
# print("=" * 50)

# print(df[(df["Marks"] > 90) | (df["Age"] < 20)])

# # practice 6 using or (|) operator
# print("=" * 50)
# print("Students with City = Jaipur OR Marks < 70")
# print("=" * 50)

# print(df[(df["City"] == "Jaipur") | (df["Marks"] < 70)])

# use isin operator to filter rows where City is in the list of cities
print("=" * 50)
print("Students from Delhi, Hisar, Jaipur")
print("=" * 50)

print(df[df["City"].isin(["Delhi", "Pune", "Jaipur", "Chandigarh"])])
