"""Session 07 - System prompts, refining prompts and few-shot prompting."""
from llm_client import chat

# 1) A vague prompt vs a refined prompt
vague = [{"role": "user", "content": "Tell me about Python."}]
refined = [
    {"role": "system", "content": "You are a patient programming tutor for beginners in Pakistan. "
                                  "Answer in at most 3 bullet points, simple English."},
    {"role": "user", "content": "Why is Python popular for AI? Give one real example per point."},
]
print("VAGUE   ->", chat(vague, temperature=0.7))
print("REFINED ->", chat(refined, temperature=0.3))

# 2) Few-shot prompting: show examples of the exact output format we want
few_shot = [
    {"role": "system", "content": "Classify customer messages. Reply with JSON only: "
                                  '{"intent": <billing|delivery|complaint|other>, "urgent": <true|false>}'},
    {"role": "user", "content": "My parcel was supposed to arrive yesterday."},
    {"role": "assistant", "content": '{"intent": "delivery", "urgent": false}'},
    {"role": "user", "content": "You charged my card twice, fix it today!"},
    {"role": "assistant", "content": '{"intent": "billing", "urgent": true}'},
    {"role": "user", "content": "The rider was very rude to my mother."},    # new input
]
print("FEW-SHOT ->", chat(few_shot, temperature=0))
