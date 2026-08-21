import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_student_performance.csv")

plt.figure(figsize=(8,6))

plt.hist(
    df["FinalMarks"],
    bins=5,
    color="green",
    edgecolor="black"
)

plt.title("Distribution of final marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of students")
plt.show()