"""Session 14 - Example 5: a safer LLM prompt for a domain task.

We ask an LLM to turn a doctor's note into a patient-friendly summary.
Domain prompts need extra rules: no new facts, no diagnosis, plain words,
and a reminder to follow the doctor. A redaction step removes personal data.
Run: python clinical_summary_llm.py   (mock answer without OPENAI_API_KEY)
"""
import re
from llm_client import ask_llm

note = ("Mr. Imran Ali, MRN 445821, 52y. Type 2 diabetes. HbA1c 8.9%. "
        "Increase metformin to 1000 mg twice daily. Review in 3 months. Advise daily walk 30 min.")

# Step 1: remove direct identifiers before the text leaves our system
redacted = re.sub(r"\bMRN \d+\b", "MRN [ID]", note)
redacted = re.sub(r"\bMr\. [A-Z][a-z]+ [A-Z][a-z]+", "[PATIENT]", redacted)

# Step 2: a domain-safe prompt with clear rules
system = ("You explain medical notes to patients in simple English. Use ONLY facts in the note. "
          "Do not add diagnoses, doses or advice that are not in the note. "
          "End with: 'Please follow your doctor's advice and ask them if anything is unclear.'")
prompt = f"Rewrite this note for the patient in 4 short bullet points:\n{redacted}"

mock = ("- You have type 2 diabetes and your sugar test (HbA1c) is 8.9%, which is higher than the goal.\n"
        "- Your metformin dose is increased to 1000 mg, taken twice a day.\n"
        "- Walk for 30 minutes every day.\n"
        "- Come back for a check-up in 3 months.\n"
        "Please follow your doctor's advice and ask them if anything is unclear.")

print("Sent to the model:", redacted, "\n")
print(ask_llm(prompt, mock_answer=mock, system=system, temperature=0))
