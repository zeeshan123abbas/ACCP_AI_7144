# Session 06: Logical Reasoning, Performance Metrics and Emerging AI Trends

> Module: AI Essentials · Term 6 (AI) · ⏱ ~2 hours

This session connects three ideas: how machines draw valid conclusions with logic, how we measure whether an AI system is any good, and where the field is heading with generative AI.

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Explain the role of logical reasoning in AI systems
- Classify deductive, inductive, abductive, common-sense and probabilistic reasoning
- Write statements in propositional and predicate (first-order) logic
- Compute and interpret accuracy, precision, recall, F1, MAE, RMSE and R²
- Analyse computational performance (time and memory) of an algorithm
- Summarise current trends such as generative AI, multimodal models and AI agents

## 📖 Concepts Explained

### 1. Why logical reasoning?

Logic lets an AI system derive **new, guaranteed-correct facts** from known ones. It is used in rule engines, verification of software and hardware, planning, and as a check on statistical models that can make inconsistent claims.

### 2. Types of reasoning

| Type | Direction | Example | Certainty |
|---|---|---|---|
| Deductive | General rule → specific conclusion | All students with 50+ pass; Ayesha has 82 → Ayesha passes | Certain if premises are true |
| Inductive | Specific observations → general rule | The last 100 orders on Friday were late → Friday orders are late | Probable |
| Abductive | Observation → best explanation | The road is wet → it probably rained | Plausible |
| Common-sense | Everyday background knowledge | A glass dropped on tiles may break | Informal |
| Probabilistic | Reasoning with likelihoods | 80% chance a message is spam | Quantified uncertainty |

### 3. Propositional logic

Statements are **propositions** that are True or False, joined by connectives:

| Symbol | Name | Read as |
|---|---|---|
| ¬P | Negation | not P |
| P ∧ Q | Conjunction | P and Q |
| P ∨ Q | Disjunction | P or Q |
| P → Q | Implication | if P then Q (false only when P true and Q false) |
| P ↔ Q | Biconditional | P if and only if Q |

A knowledge base **entails** a sentence (KB ⊨ α) if α is true in every situation (model) where the KB is true. Inference rules such as **Modus Ponens** (P, P→Q ⊢ Q) and **Modus Tollens** (¬Q, P→Q ⊢ ¬P) derive conclusions without checking every model.

### 4. Predicate (first-order) logic

Propositional logic cannot say "all students". First-order logic adds **objects, predicates, variables and quantifiers**:

- ∀x Student(x) ∧ Passes(x) → Certificate(x) ("for all x ...")
- ∃x Student(x) ∧ ¬Passes(x) ("there exists an x ...")

### 5. Measuring AI performance

**Classification** uses the confusion matrix:

| | Predicted positive | Predicted negative |
|---|---|---|
| Actually positive | TP | FN |
| Actually negative | FP | TN |

- **Accuracy** = (TP+TN) / all, misleading when classes are imbalanced.
- **Precision** = TP / (TP+FP): of everything flagged, how much was right? Important when false alarms are costly.
- **Recall** = TP / (TP+FN): of all real positives, how many did we catch? Important in disease or fraud detection.
- **F1** = harmonic mean of precision and recall.

**Regression**: MAE (average absolute error), RMSE (penalises big errors more), R² (share of variance explained, 1.0 is perfect).

**Computational performance**: time complexity (how runtime grows, e.g. O(n) vs O(1)), memory use, latency per prediction and throughput. A 99%-accurate model that takes 10 seconds per request may be useless in a chat app.

### 6. Emerging trends in AI

| Trend | What it means |
|---|---|
| Generative AI | Models that create text, images, code, audio and video (LLMs, diffusion models) |
| Multimodal models | One model understands text, images and speech together |
| AI agents | LLMs that plan, call tools and APIs, and complete multi-step tasks |
| Retrieval-Augmented Generation | Grounding model answers in your own documents |
| Small and on-device models | Efficient models that run on phones and laptops |
| Responsible AI & regulation | Fairness, transparency, privacy and safety requirements |

You will explore many of these hands-on in the NLP module.

## 💻 Code Examples

Install: `pip install numpy scikit-learn`.

### Example 1: Truth tables, entailment and a taste of predicate logic

📄 File: [`propositional_logic.py`](propositional_logic.py)

```python
"""Session 06 - Propositional logic: truth tables and entailment by model checking.

Knowledge base (KB):
  R  : "It is raining"
  W  : "The road is wet"
  S  : "The match is suspended"
  KB = (R -> W) AND (W -> S) AND R
Question: does KB entail S?   (KB |= S)
"""
from itertools import product

def implies(a, b):
    return (not a) or b

SYMBOLS = ["R", "W", "S"]

def kb(m):
    return implies(m["R"], m["W"]) and implies(m["W"], m["S"]) and m["R"]

def entails(kb_fn, query_fn):
    """KB |= query if query is true in EVERY model where KB is true."""
    for values in product([True, False], repeat=len(SYMBOLS)):
        m = dict(zip(SYMBOLS, values))
        if kb_fn(m) and not query_fn(m):
            return False
    return True

print(" R     W     S    | KB")
for values in product([True, False], repeat=3):
    m = dict(zip(SYMBOLS, values))
    print(" ".join(f"{str(v):<5}" for v in values), "|", kb(m))

print("\nKB |= S ?      ", entails(kb, lambda m: m["S"]))
print("KB |= not R ?  ", entails(kb, lambda m: not m["R"]))

# Inference rules shown as code
print("\nModus Ponens   : from R and (R -> W) conclude W")
print("Modus Tollens  : from not S and (W -> S) conclude not W")

# A taste of predicate (first-order) logic: "All students who pass get a certificate"
students = {"Ayesha": 82, "Bilal": 45, "Hamza": 67}
passes = lambda x: students[x] >= 50                 # Passes(x)
certificate = {x for x in students if passes(x)}     # forall x: Passes(x) -> Certificate(x)
print("\nforall x Passes(x) -> Certificate(x):", sorted(certificate))
print("exists x not Passes(x)?", any(not passes(x) for x in students))
```

Run it:

```bash
python propositional_logic.py
```

**How it works**

- `implies(a, b)` encodes the truth table of →: it is only False when a is True and b is False.
- `product([True, False], repeat=3)` enumerates all 8 models of R, W, S; the table shows the KB is true in exactly one model.
- `entails()` checks that the query holds in every model where the KB holds; KB ⊨ S is True, KB ⊨ ¬R is False.
- The last part models ∀x Passes(x) → Certificate(x) with a set comprehension and ∃x ¬Passes(x) with `any()`.

### Example 2: Quality metrics and runtime analysis

📄 File: [`performance_metrics.py`](performance_metrics.py)

```python
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
```

Run it:

```bash
python performance_metrics.py
```

**How it works**

- `confusion_matrix(...).ravel()` returns TN, FP, FN, TP for binary labels; precision, recall and F1 are computed by hand and checked against scikit-learn.
- Regression metrics compare predicted and actual prices; RMSE is higher than MAE because one large error (31.0 vs 28.9) is squared.
- The timing table shows list search growing linearly (O(n)) while set lookup stays almost constant (O(1) average).

## 🧪 Lab Practice

1. Add a fourth symbol `C` ("cricket match is cancelled") with rule S → C and test whether KB ⊨ C.
2. Write the sentence "If a student attends all labs and submits the eProject, they qualify for the exam" in propositional logic and check two cases in code.
3. Change `y_pred` so that recall becomes 1.0. What happens to precision?
4. Create an imbalanced dataset (95 negatives, 5 positives) where a model predicting all negatives gets 95% accuracy. Compute its recall.
5. Pick one trend from the table and find one real product that uses it; write 5 lines on how it works.

## 📝 Assignment

Train any two classifiers on `load_breast_cancer()` and produce a short evaluation report: confusion matrix, accuracy, precision, recall, F1, and average prediction time per sample. Recommend one model for a screening clinic, justifying whether precision or recall matters more there.

## ❓ Quick Quiz

**Q1.** When is P → Q false?

<details><summary>Show answer</summary>

Only when P is true and Q is false.

</details>

**Q2.** Which reasoning type is 'the grass is wet, so it probably rained'?

<details><summary>Show answer</summary>

Abductive reasoning (inference to the best explanation).

</details>

**Q3.** Formula for recall?

<details><summary>Show answer</summary>

TP / (TP + FN).

</details>

**Q4.** Why is accuracy misleading for fraud detection?

<details><summary>Show answer</summary>

Fraud is rare; a model that predicts 'not fraud' for everything gets very high accuracy but catches no fraud.

</details>

**Q5.** What does ∃ mean in first-order logic?

<details><summary>Show answer</summary>

'There exists' at least one object for which the statement holds.

</details>

## 💼 Interview Questions

**1. Precision vs recall: which matters more for a cancer screening model?**

<details><summary>Model answer</summary>

Usually recall, because missing a real case (false negative) is far more harmful than a false alarm that leads to a follow-up test. The threshold can be tuned to raise recall while monitoring precision.

</details>

**2. What is the difference between deductive and inductive reasoning in AI?**

<details><summary>Model answer</summary>

Deduction applies general rules to reach certain conclusions (rule engines, theorem provers). Induction generalises from examples to rules, which is what machine learning does; its conclusions are probable, not guaranteed.

</details>

**3. Name a current AI trend and a risk that comes with it.**

<details><summary>Model answer</summary>

Generative AI: it boosts productivity but can hallucinate false facts, reproduce bias, or be misused for deepfakes. Mitigations include grounding (RAG), evaluation, watermarking and human review.

</details>

## ✅ Summary

- Logic derives guaranteed conclusions; deduction, induction and abduction differ in certainty.
- Propositional logic uses true/false statements; first-order logic adds objects and quantifiers.
- Entailment means the query is true in every model of the knowledge base.
- Choose metrics by cost of errors: precision, recall, F1 for classification; MAE, RMSE, R² for regression.
- Generative, multimodal and agentic AI are the major current trends, with responsible-AI concerns attached.

---

[⬅ Previous](../Session-05-Knowledge-Representation/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-07-Working-with-the-OpenAI-API/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
