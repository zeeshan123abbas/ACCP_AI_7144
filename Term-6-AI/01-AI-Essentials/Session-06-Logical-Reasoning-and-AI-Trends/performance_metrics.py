"""Session 06 - Measuring an AI system: quality metrics and computational cost.

1) Classification metrics from a confusion matrix (by hand and with sklearn).
2) Regression metrics.
3) Time cost: how runtime grows with input size.
"""
import time
import numpy as np
from sklearn.metrics import (confusion_matrix, accuracy_score, precision_score,
                             recall_score, f1_score, mean_absolute_error,
                             mean_squared_error, r2_score)

# 1) A spam filter's results on 12 emails (1 = spam)
y_true = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0]

tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
print(f"TP={tp} FP={fp} FN={fn} TN={tn}")
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
print(f"By hand -> precision={precision:.2f} recall={recall:.2f} f1={f1:.2f}")
print(f"sklearn -> accuracy={accuracy_score(y_true, y_pred):.2f} "
      f"precision={precision_score(y_true, y_pred):.2f} "
      f"recall={recall_score(y_true, y_pred):.2f} f1={f1_score(y_true, y_pred):.2f}")

# 2) Regression: predicted vs actual house prices (PKR millions)
actual = np.array([12.0, 18.5, 25.0, 9.5, 31.0])
predicted = np.array([13.1, 17.0, 26.5, 10.0, 28.9])
print(f"\nMAE={mean_absolute_error(actual, predicted):.2f}  "
      f"RMSE={np.sqrt(mean_squared_error(actual, predicted)):.2f}  "
      f"R2={r2_score(actual, predicted):.3f}")

# 3) Computational performance: linear search vs set lookup
print("\nn         list search (ms)   set lookup (ms)")
for n in (10_000, 100_000, 1_000_000):
    data = list(range(n)); as_set = set(data); target = n - 1
    t0 = time.perf_counter(); _ = target in data; t1 = time.perf_counter()
    _ = target in as_set; t2 = time.perf_counter()
    print(f"{n:<10}{(t1 - t0) * 1000:>14.3f}{(t2 - t1) * 1000:>18.4f}")
