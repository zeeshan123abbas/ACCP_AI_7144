"""Session 07 - Example 3: a complete mini RAG system.

Retrieve -> build a grounded prompt -> generate an answer with sources.
Works without an API key: the mock answer simply quotes the best chunk.
Run: python rag_answer.py
"""
from llm_client import ask_llm
from tfidf_retriever import retrieve

def answer(question):
    # Step 1: RETRIEVE the most relevant chunks
    results = retrieve(question, top_k=2)

    # Step 2: if nothing matches at all, say so instead of guessing
    if results[0][0] == 0:
        return "I could not find this in the documents.", []

    # Step 3: AUGMENT - put the chunks into the prompt as numbered context
    context = ""
    for number, (score, chunk) in enumerate(results, start=1):
        context += f"[{number}] ({chunk['source']}) {chunk['text']}\n"

    prompt = f"""Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know".
Mention the source number like [1].

Context:
{context}
Question: {question}
Answer:"""

    # Step 4: GENERATE - the mock answer quotes the top chunk so it works offline
    best_chunk = results[0][1]
    mock = f"{best_chunk['text']} [1]"
    reply = ask_llm(prompt, mock_answer=mock, temperature=0)
    sources = [chunk["source"] for _, chunk in results]
    return reply, sources


if __name__ == "__main__":
    for question in ["How much is the re-exam fee?",
                     "What time do evening classes start?",
                     "Who won the cricket match yesterday?"]:
        reply, sources = answer(question)
        print("Q:", question)
        print("A:", reply)
        print("Sources:", sources, "\n")
