import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_student_performance.csv")
# print(df.head(10))

# plt.figure(figsize=(8,5))

# plt.plot(
#     df["Name"],
#     df["FinalMarks"],
#     marker = 'o',
#     color='Green'
# )

# plt.title("Student Performance")

# plt.xlabel("Student")
# plt.ylabel("Final Marks")
# plt.xticks(rotation=45)
# plt.grid(True)

# plt.show()

# Practice 1 : StudentName ke according Attendance ka line chart banao.

plt.figure(figsize=(8,8))

plt.plot(
    df["Name"],
    df["Attendance"],
    marker = 'o',
    color = 'Red',
    linewidth = 2,
    linestyle = '-'
)

plt.title("Student Attendance" , fontsize = 16)

plt.xlabel("Student Name")
plt.ylabel("Attendance")
plt.xticks(rotation=45)
plt.grid(
    axis = 'y',
    linestyle = '--',
    alpha = 0.5
)
plt.show()

# Practice 2 🔥:- Attendanc ka dashed line banao:

plt.figure(figsize=(8,6))

plt.plot(    
    df["Name"],
    df["Attendance"],
    marker = '*',
    linewidth = 2,
    linestyle = '--'
    )

plt.title("Students Attendance", fontsize = 12)

plt.xlabel("Student Name")
plt.ylabel("Attendance")
plt.xticks(rotation=45)
plt.gird(True)
plt.show()


# Practice 3:- Same chart mein :
plt.figure(figsize=(8,8))

plt.plot(
    df["Name"],
    df["Attendance"],
    marker = 'o',
    color = 'Red',
    linewidth = 2,
    linestyle = '-'
)

plt.title("Student Attendance" , fontsize = 18)

plt.xlabel("Student Name")
plt.ylabel("Attendance")
plt.xticks(rotation=45)
plt.grid(
    axis = 'y',
    linestyle = '--',
    alpha = 0.5
)
plt.show()