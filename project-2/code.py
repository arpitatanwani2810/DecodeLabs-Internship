import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    f1_score
)

iris = load_iris()

X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = y

print("\nDATASET OVERVIEW")
print("=" * 50)
print(df.head())

print("\nDATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\nFEATURE STATISTICS")
print("=" * 50)
print(df.describe())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

k_values = range(1, 16)

accuracies = []

best_accuracy = 0
best_k = 1
best_model = None

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    accuracies.append(accuracy)

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k
        best_model = model

print("\nK VALUE COMPARISON")
print("=" * 50)

for k, acc in zip(k_values, accuracies):
    print(f"K = {k:<2} Accuracy = {acc:.4f}")

plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracies, marker="o")
plt.title("KNN Accuracy vs K Value")
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.grid(True)
plt.tight_layout()
plt.savefig("accuracy_comparison.png")

predictions = best_model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average="weighted")

print("\nBEST MODEL")
print("=" * 50)
print(f"Best K Value : {best_k}")
print(f"Accuracy     : {accuracy:.4f}")
print(f"F1 Score     : {f1:.4f}")

print("\nCLASSIFICATION REPORT")
print("=" * 50)
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))

cm = confusion_matrix(y_test, predictions)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()
plt.savefig("confusion_matrix.png")

feature_importance = pd.DataFrame(
    {
        "Feature": iris.feature_names,
        "Mean Value": np.mean(X, axis=0)
    }
)

plt.figure(figsize=(8, 5))
plt.bar(feature_importance["Feature"],
        feature_importance["Mean Value"])
plt.xticks(rotation=20)
plt.title("Average Feature Values")
plt.tight_layout()
plt.savefig("feature_analysis.png")

print("\nFILES GENERATED")
print("=" * 50)
print("accuracy_comparison.png")
print("confusion_matrix.png")
print("feature_analysis.png")

print("\nPROJECT COMPLETED SUCCESSFULLY")
