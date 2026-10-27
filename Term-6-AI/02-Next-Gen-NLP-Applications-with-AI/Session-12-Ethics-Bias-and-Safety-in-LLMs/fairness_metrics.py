"""Session 12 - Example 4: measure fairness of a classifier's decisions.

Demographic parity: does each group get a "yes" at a similar rate?
Equal opportunity : among people who truly qualify, does each group get
                    a "yes" at a similar rate (true positive rate)?
Run: python fairness_metrics.py
"""

# Step 1: toy results of a loan-approval model
# Each row: (group, truly_qualified, model_approved)   1 = yes, 0 = no
results = [
    ("A", 1, 1), ("A", 1, 1), ("A", 0, 0), ("A", 1, 1), ("A", 0, 1), ("A", 1, 1),
    ("B", 1, 0), ("B", 1, 1), ("B", 0, 0), ("B", 1, 0), ("B", 0, 0), ("B", 1, 1),
]

def approval_rate(group):
    rows = [r for r in results if r[0] == group]
    return sum(r[2] for r in rows) / len(rows)

def true_positive_rate(group):
    qualified = [r for r in results if r[0] == group and r[1] == 1]
    return sum(r[2] for r in qualified) / len(qualified)

# Step 2: compute both metrics for each group
for group in ["A", "B"]:
    print(f"Group {group}: approval rate {approval_rate(group):.0%}, "
          f"true positive rate {true_positive_rate(group):.0%}")

# Step 3: compare groups (the "80% rule" is a common warning threshold)
ratio = approval_rate("B") / approval_rate("A")
print(f"\nApproval ratio B/A: {ratio:.2f}")
print("Warning: below 0.80, check for bias." if ratio < 0.8 else "Within the 80% rule.")
print(f"Equal opportunity gap: {abs(true_positive_rate('A') - true_positive_rate('B')):.0%}")
