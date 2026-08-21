import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("cleaned_student_performance.csv")

features = [
"Attendance",
"StudyHours",
"PreviousMarks"
]
X = df[features]
y = df["FinalMarks"]

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42
)
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))



model = LinearRegression()
model.fit(X_train, y_train)
print("Model training completed")


# Make Predictions

y_pred = model.predict(X_test)
print("Actual Marks:")
print(y_test.values)
print("Predicted Marks:")
print(y_pred)

# Actual vs Predicted Table

result_df = pd.DataFrame({
"ActualMarks": y_test.values,
"PredictedMarks": y_pred
})
print(result_df)