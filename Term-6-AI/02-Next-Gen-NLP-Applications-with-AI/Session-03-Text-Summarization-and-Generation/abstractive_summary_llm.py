"""Session 03 - Example 2: abstractive summarization with an LLM prompt.

Abstractive = write NEW sentences that keep the meaning.
The prompt controls length, audience and format.
Works live with OPENAI_API_KEY, or shows mock answers without it.
Run: python abstractive_summary_llm.py
"""
from llm_client import ask_llm

ARTICLE = ("Karachi's new electric bus service started on two routes last year and now carries "
           "thousands of passengers daily. Riders say it is cleaner and cheaper than rickshaws. "
           "The city plans four more routes by next summer, but experts say dedicated bus lanes "
           "and better footpaths are also needed to reduce traffic jams.")

# Step 1: three prompts for three different kinds of summary
prompts = {
    "one sentence": f"Summarize this article in one sentence:\n{ARTICLE}",
    "3 bullet points": f"Summarize this article in exactly 3 short bullet points:\n{ARTICLE}",
    "for a child": f"Explain this news to a 10-year-old in two simple sentences:\n{ARTICLE}",
}

# Step 2: sample answers, used only when there is no API key
mock_answers = {
    "one sentence": "Karachi's popular electric buses will expand to four new routes, though experts want bus lanes too.",
    "3 bullet points": "- Electric buses run on two routes\n- Riders find them clean and cheap\n- Four more routes planned; bus lanes needed",
    "for a child": "Karachi has new clean buses that many people like. The city wants more of them, but they need their own lanes.",
}

# Step 3: ask for each summary and print it
for name, prompt in prompts.items():
    summary = ask_llm(prompt, mock_answer=mock_answers[name], temperature=0.3)
    print(f"[{name}]\n{summary}\n")
