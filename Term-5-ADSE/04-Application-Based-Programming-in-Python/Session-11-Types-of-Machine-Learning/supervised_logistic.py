# supervised_logistic.py - SUPERVISED learning: predict pass/fail with Logistic Regression
# Install once:  pip install scikit-learn

from sklearn.linear_model import LogisticRegression

# Training examples: [study hours, attendance %]  ->  label (1 = pass, 0 = fail)
X = [[1, 40], [2, 55], [2, 70], [3, 50], [4, 65],
     [5, 80], [6, 75], [7, 90], [8, 85], [9, 95]]
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# Step 1: create the model
model = LogisticRegression()

# Step 2: train (fit) - the model learns from examples WITH answers (labels)
model.fit(X, y)

# Step 3: predict for new students it has never seen
new_students = [[2, 45], [5, 70], [8, 92]]
predictions = model.predict(new_students)
probabilities = model.predict_proba(new_students)   # [chance of 0, chance of 1]

for student, result, prob in zip(new_students, predictions, probabilities):
    label = "PASS" if result == 1 else "FAIL"
    print(f"Hours={student[0]}, Attendance={student[1]}% -> {label} "
          f"(pass chance {prob[1]:.0%})")
