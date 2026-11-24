from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


iris = load_iris()

X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = DecisionTreeClassifier(random_state=42)


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Actual Values:", y_test)
print("Predicted Values:", y_pred)


accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy * 100, "%")


new_sample = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_sample)

print("New Sample Prediction:",
      iris.target_names[prediction[0]])
