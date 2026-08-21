import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_student_performance.csv")

sns.set_theme(style="whitegrid")
"""
"darkgrid"
"whitegrid"
"dark"
"white"
"ticks"
"""
plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="Course",
    hue="Result"
)

plt.title("Pass vs Fail Count")
plt.xlabel("Course")
plt.ylabel("Number of student")

plt.show