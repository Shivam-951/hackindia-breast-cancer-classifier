"""
Train and evaluate a Random Forest classifier on scikit-learn's
Wisconsin Diagnostic Breast Cancer dataset.

Educational use only; not for clinical diagnosis.
"""
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split


def main():
    dataset = load_breast_cancer(as_frame=True)
    X = dataset.data
    y = dataset.target

    print(f"Dataset: {dataset.DESCR.splitlines()[0]}")
    print(f"Features: {X.shape[1]}")
    print(f"Samples: {X.shape[0]}")
    print("Target labels:", dict(enumerate(dataset.target_names)))

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("\nEvaluation results")
    print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall   : {recall_score(y_test, y_pred):.4f}")
    print(f"F1-score : {f1_score(y_test, y_pred):.4f}")
    print("\nConfusion matrix (rows=true labels, columns=predicted labels):")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification report:")
    print(classification_report(y_test, y_pred, target_names=dataset.target_names))


if __name__ == "__main__":
    main()
