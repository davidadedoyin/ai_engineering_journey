# Precision, recall, F1 and confusion matrix are metrics for classification.
# This is a tiny teaching example, not a full model training workflow.

from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

# Real labels: 1 means positive class.
y_true = [1, 0, 1, 1, 0, 1]
y_pred = [1, 0, 0, 1, 0, 1]

print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1:", f1_score(y_true, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_true, y_pred))
