import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_student_performance.csv")

plt.figure(figsize=(8, 5))

plt.bar(
    df["Name"],
    df["FinalMarks"],
    color = 'orange'
)

plt.title("Student Marks comparision")
plt.xlabel("Student Name ")
plt.ylabel("FinalMarks")
plt.xticks(rotation=45)
plt.show()

# bar chart by group by function 