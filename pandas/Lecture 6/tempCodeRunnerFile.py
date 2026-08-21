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