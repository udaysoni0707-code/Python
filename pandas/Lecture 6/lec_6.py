import pandas as pd
df = pd.read_csv('cleaned_student_performance.csv')
# print(df.head())
# print(df.tail())

print(f"Total students: {len(df)}")

print(f"Rows and columns :\n{df.shape}")

print(f"Average math score: {df['FinalMarks'].mean()}")

print(f"Average attendance: {df['Attendance'].mean()}")

# Count pass and fail students
print("=" * 50)
print("Pass and Fail Students Count")
print("=" * 50)

print(df["Result"].value_counts())

# Count male and female students

print("=" * 50)
print("Male and Female Students")
print("=" * 50)

print(df["Gender"].value_counts())

# Count students by course
print("=" * 50)
print("Students by Course")
print("=" * 50)

print(df["Course"].value_counts())

# Percentage of pass and fail students
print("=" * 50)
print("Percentage of Pass and Fail Students")
print("=" * 50)

result_precentage = df["Result"].value_counts(normalize=True) * 100
print(result_precentage)

gender_percentage = df["Gender"].value_counts(normalize=True) * 100
print("=" * 50)
print("Percentage of Male and Female Students")
print("=" * 50)
print(gender_percentage)

# Now we learn groupby function in pandas

# average Marks by course 

course_avg_marks = df.groupby("Course")["FinalMarks"].mean()
print("=" * 50)
print("Average Marks by Course")
print("=" * 50)
print(course_avg_marks)

# marks between 50 and 80 using between function
# syntax: df[df["column_name"].between(Starting_value, Ending_value)]
marks_between_50_80 = df[df["FinalMarks"].between(50, 80)]
print("=" * 50)
print("Students with Marks between 50 and 80")
print("=" * 50)
print(marks_between_50_80)

# Hours is between 1 and 5
print(df[df["Hours"].between(1, 5)])
# Marks are between 60 and 85
print(df[df["FinalMarks"].between(60, 85)])

# parctice on query function in pandas
# syntax: df.query("column_name operator value")
print(df.query("FinalMarks > 80"))
print(df.query("Age >= 21 and Course == 'BSc'"))

print(df["Course"].value_counts())
print(df["Name"].value_counts())
print(df["Gender"].value_counts())
print(df["Age"].value_counts())

# what is the precentage of students pass and fail 
print("=" * 50)
print("Percentage of Pass and Fail Students")
print("=" * 50)
print(df["Result"].value_counts(normalize=True).mul(100).round(2))

# print the gender precentage of students 
print("=" * 50)
print("Percentage of Male and Female Students")
print("=" * 50)
print(df["Gender"].value_counts(normalize=True) * 100)

# print the course percentage of students
print("=" * 50)
print("Percentage of Students by Course")
print("=" * 50)
print(df["Course"].value_counts(normalize=True)*100)

# find the average marks of students by course
print("=" * 50)
print("Average Marks by Course")
print("=" * 50)
print(df.groupby("Course")["FinalMarks"].mean())

# average marks by gender using groupby function 
# syntax : df.groupby("Column_name")["target_column"].mean()
print("=" * 50) 
print("Average Marks by Gender")
print("=" * 50)
print(df.groupby("Gender")["FinalMarks"].mean())

# practice 1 : Find the average attendance by Course.
print("=" * 50 )
print("Average Attendance by Course")
print("=" * 50)
print(df.groupby("Course")["Attendance"].mean())

# practice 2 : Find the average FinalMarks by Gender.
print("=" * 50 )
print("Average FinalMarks by Gender")
print("=" * 50)
print(df.groupby("Gender")["FinalMarks"].mean())

# practice 3 : Find the average Attendance by Gender.
print("=" * 50 )
print("Average Attendance by Gender")
print("=" * 50)
print(df.groupby("Gender")["Attendance"].mean())

# practice 4 : Find the average FinalMarks by Result.
print("=" * 50 )
print("Average FinalMarks by Result")
print("=" * 50)
print(df.groupby("Result")["FinalMarks"].mean())

# practice 5 : Find the average FinalMatks by Course
print(df.groupby("Course")["FinalMarks"].mean())

# practice 6 : Find the total FinalMarks by Course.
print(df.groupby("Course")["FinalMarks"].sum())

# practice 7 : Find the highest FinalMarks by Course.
print(df.groupby("Course")["FinalMarks"].sum().max())

# practice 8 : Find the lowest FinalMarks by Course.
print(df.groupby("Course")["FinalMarks"].sum().min())

# practice 9 : Find the number of students in each Course.
print(df.groupby("Course")["StudentID"].count())

# agg (aggregation) operation in pandas
# syntax : df.groupby("column_name").agg({"target_column": "aggregation_function"})

# Practice 1 — Basic Summary
summary = df.groupby("Course").agg({
    "FinalMarks": ["mean", "count", "max", "min"]
})

# Practice 2 — Attendance Summary
attendance_summary = df.groupby("Course").agg({
    "Attendance" : ["mean", "max", "min"] 
})

# Practice 3 — FinalMarks Summary by Gender
finalmarks_summary = df.groupby("Gender").agg({
    "FinalMarks": ["mean", "count", "max", "min"]
})

# practice 4 - course wise final marks
print(df.groupby("Course").agg({
    "FinalMarks": ["count", "mean", "max", "min"]
}))

# practice 5 - course wise attendance 
print(df.groupby("Course").agg({
    "Attendance": ["mean", "max", "min"]
}))

# practice 6 - Gender wise final marks
print(df.groupby("Gender").agg({
    "FinalMarks": ["count", "mean", "max", "min"]
}))

# Practice 1 : Create a Course + Gender average marks report:
result = df.groupby(["Course", "Gender"])["FinalMarks"].mean()
result = result.reset_index()
print(result)

# practice 2 Create a Course-wise average attendance report and then use reset_index():
result = df.groupby("Course")["Attendance"].mean()
result = result.reset_index()
print(result)

# practice 3 : Create a Course + Gender summary using agg():
result = df.groupby(["Course", "Gender"]).agg({
    "FinalMarks": ["mean", "count", "max", "min"]
})
result = result.reset_index()
print(result)

# pivot_table function in pandas
# syntax : df.pivot_table(index="column_name", values="target_column", aggfunc="aggregation_function")

pivot = pd.pivot_table(
    df,
    values = "FinalMarks",
    index="Course",
    columns="Gender",
    aggfunc="mean"
)

print(pivot)

# Practice 2 :Create a pivot table showing:
# Average Attendance by Course and Gender
pivot_attendance = pd.pivot_table(
    df,
    values = "Attendance",
    index = "Course",
    columns = "Gender",
    aggfunc = "mean"
)
print(pivot_attendance)

# Practice 3 🔥: Create a pivot table showing:
# Maximum FinalMarks by Course and Gender
pivot_max_marks = pd.pivot_table(
    df,
    values = "FinalMarks",
    index = "Course",
    columns = "Gender",
    aggfunc = "max"
)
print(pivot_max_marks)

# now learn about the idxmax and idxmin functions in pandas
# syntax : df["column_name"].idxmax() or df["column_name"].idxmin

# practice 1 Find the course with the highest average FinalMarks.
print(df.groupby("Course")["FinalMarks"].mean().idxmax())

# practice 2 : Find the course with the lowest average FinalMarks.
print(df.groupby("Course")["FinalMarks"].mean().idxmin())

# practice 3 : Find the course with the highest average Attendance.
print(df.groupby("Course")["Attendance"].mean().idxmax())

# practice 4 : Find the course with the lowest average Attendance.
print(df.groupby("Course")["Attendance"].mean().idxmin())

# practice 5 : Practice 5 — Find Both
print(df.groupby("Course")["FinalMarks"].mean().idxmax())
print(df.groupby("Course")["FinalMarks"].mean().idxmin())


avg_marks = df.groupby("Course")["FinalMarks"].mean()
# What is the highest average marks value?
print(avg_marks.max())
# Which course has that highest average?
print(avg_marks.idxmax())
# What is the lowest average marks value?
print(avg_marks.min())
# Which course has that lowest average?
print(avg_marks.idxmin())

pass_percentage = (
    (df["Result"] == "Pass").sum() / len(df) *100
)
print(f"Pass percentage: {pass_percentage:.2f}%")

# Pass percentage by Course

pass_percentage_by_course = (
    (df["Course"] == "BSc") & (df["Result"] == "Pass").sum() / len(df) * 100
)