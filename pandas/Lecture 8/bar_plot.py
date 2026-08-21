import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_student_performance.csv")
plt.figure(figsize=(8, 5))
sns.barplot(
data=df,
x="Course",
y="FinalMarks",
estimator="mean",
palette="viridis"
)
plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("Average Marks")
plt.show()