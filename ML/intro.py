import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("cleaned_student_performance.csv")
# print(df.head())
# print(df.info())
# print(df.describe())

# Select Features and Target
features = [
"Attendance",
"StudyHours",
"PreviousMarks"
]
X = df[features]
y = df["FinalMarks"]
print(X.head())
print(y.head())