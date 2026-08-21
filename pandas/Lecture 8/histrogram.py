import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_student_performance.csv")

plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x="FinalMarks",
    bins=5,
    kde=True,
    color="green"
)
plt.title("Final Marks Distribution")
plt.xlabel("Final Marks")
plt.ylabel("Number of students")
plt.show()