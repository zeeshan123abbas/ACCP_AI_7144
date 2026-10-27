"""Session 07 - Example 1: load documents and split them into chunks.

RAG never sends whole books to the LLM. We cut documents into small,
overlapping chunks (here: 2 sentences each, sharing 1 sentence with the
next chunk) so we can later retrieve only the useful pieces.
Run: python chunk_documents.py
"""
import os
import re

def load_documents(folder):
    """Read every .txt file in the folder into a dictionary {filename: text}."""
    documents = {}
    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename), encoding="utf-8") as f:
                documents[filename] = f.read()
    return documents


def split_sentences(text):
    """Very simple sentence splitter: break after '.', '?' or '!' followed by a space."""
    text = text.replace("\n", " ")
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+", text) if s.strip()]


def chunk_text(text, sentences_per_chunk=2, overlap=1):
    """Group sentences into chunks; neighbouring chunks share `overlap` sentences."""
    sentences = split_sentences(text)
    chunks = []
    step = sentences_per_chunk - overlap           # how far to move each time
    for start in range(0, len(sentences), step):
        chunk = " ".join(sentences[start:start + sentences_per_chunk])
        chunks.append(chunk)
        if start + sentences_per_chunk >= len(sentences):   # last chunk reached
            break
    return chunks


if __name__ == "__main__":
    # Step 1: load the four policy files from the docs folder
    docs = load_documents("docs")
    print("Loaded:", list(docs))

    # Step 2: chunk each document and remember where each chunk came from
    all_chunks = []
    for filename, text in docs.items():
        for chunk in chunk_text(text):
            all_chunks.append({"source": filename, "text": chunk})

    # Step 3: show the result
    print("Total chunks:", len(all_chunks))
    for chunk in all_chunks[:3]:
        print(f"- [{chunk['source']}] {chunk['text']}")
