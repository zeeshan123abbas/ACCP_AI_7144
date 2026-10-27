# Module 02: Next-Gen NLP Applications with AI

> Term 6 (AI) · 15 sessions · ⏱ ~2 hours each

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white) ![NLTK](https://img.shields.io/badge/NLTK-154F5B?logo=python&logoColor=white) ![spaCy](https://img.shields.io/badge/spaCy-09A3D5?logo=spacy&logoColor=white) ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-FFD21E?logo=huggingface&logoColor=black) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI%20API-412991?logo=openai&logoColor=white)

Natural Language Processing (NLP) is the part of AI that reads, understands and writes human language. This module takes you from the classic NLP pipeline (tokens, stop words, tags) all the way to modern Large Language Model (LLM) applications: entity extraction, summarization, transformers, prompt engineering, fine-tuning with LoRA, Retrieval-Augmented Generation (RAG), chat agents, speech, vision, deployment and responsible AI. Every session has small, commented Python programs that run on a normal laptop. Scripts that call the OpenAI API also work **without a key** in a built-in mock mode, so you can practise anywhere.

## 🎯 What You Will Learn

- The NLP pipeline (tokenization, normalization, stop words, stemming, lemmatization, POS tags) and how NLU finds intent and meaning
- Named Entity Recognition with rules, spaCy, BERT and LLM prompts, and how to measure it with precision, recall and F1
- Extractive and abstractive summarization, and how decoding settings change generated text
- How attention, positional encoding and transformer blocks work, and encoder-only vs decoder-only models
- Advanced prompting: zero/few-shot, chain-of-thought, self-consistency, ReAct and prompt optimization
- Parameter-efficient fine-tuning with LoRA and QLoRA
- Building RAG systems with embeddings and a vector store to reduce hallucination
- Conversational agents with memory and tool calling
- Multimodal (vision + language) and speech AI (Whisper, text-to-speech)
- Deploying NLP apps as APIs, plus ethics, bias and safety
- Semantic search, recommendations and domain NLP for healthcare and finance

## 📋 Prerequisites

- Python basics: variables, loops, functions, lists, dictionaries, `pip`
- Module 01 (AI Essentials), especially machine learning basics and the OpenAI API session
- A little NumPy (arrays, dot product) helps in Sessions 04 and 06

## 🛠 Tools to Install

| Tool | Purpose | Official link |
|---|---|---|
| Python 3.12 | Run all examples | https://www.python.org/downloads/ |
| VS Code + Python extension | Code editor | https://code.visualstudio.com/ |
| Google Colab | Free GPU notebooks for heavier labs (fine-tuning, speech) | https://colab.research.google.com/ |
| NLTK | Classic NLP toolkit | https://www.nltk.org/install.html |
| spaCy | Fast industrial NLP pipeline | https://spacy.io/usage |
| Hugging Face Transformers | Pre-trained transformer models | https://huggingface.co/docs/transformers/installation |
| PyTorch (CPU is enough) | Deep learning backend | https://pytorch.org/get-started/locally/ |
| scikit-learn | TF-IDF, classifiers, similarity | https://scikit-learn.org/stable/install.html |
| sentence-transformers | Text embeddings for search and RAG | https://sbert.net/docs/installation.html |
| PEFT | LoRA fine-tuning library | https://huggingface.co/docs/peft/install |
| OpenAI Python SDK | LLM calls (optional key; mock mode without it) | https://platform.openai.com/docs/quickstart |

Quick setup (run once inside this module folder):

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate     macOS/Linux: source .venv/bin/activate
pip install nltk spacy scikit-learn numpy openai
python -m spacy download en_core_web_sm
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install transformers sentence-transformers peft
```

Small models (DistilBERT, DistilGPT-2, FLAN-T5-small, MiniLM) download automatically the first time a script uses them and are cached afterwards. To use a real LLM, set `OPENAI_API_KEY` (and optionally `OPENAI_MODEL`); otherwise you will see `(mock)` answers.

## 🗂 Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Introduction to NLP and NLU | [Open](./Session-01-Introduction-to-NLP-and-NLU/README.md) |
| 02 | Named Entity Recognition (NER) with Large Language Models | [Open](./Session-02-Named-Entity-Recognition-with-LLMs/README.md) |
| 03 | Text Summarization and Generation with LLMs | [Open](./Session-03-Text-Summarization-and-Generation/README.md) |
| 04 | Understanding Transformers and Attention Mechanisms | [Open](./Session-04-Transformers-and-Attention/README.md) |
| 05 | Advanced Prompt Engineering and Reasoning Techniques | [Open](./Session-05-Advanced-Prompt-Engineering-and-Reasoning/README.md) |
| 06 | Parameter-Efficient Fine-Tuning with LoRA and QLoRA | [Open](./Session-06-Fine-Tuning-with-LoRA-and-QLoRA/README.md) |
| 07 | Retrieval-Augmented Generation (RAG) Systems | [Open](./Session-07-Retrieval-Augmented-Generation-RAG/README.md) |
| 08 | Building Intelligent Conversational Agents | [Open](./Session-08-Building-Conversational-Agents/README.md) |
| 09 | Multimodal AI: Integrating Vision and Language Models | [Open](./Session-09-Multimodal-AI-Vision-and-Language/README.md) |
| 10 | Modern Speech AI with Whisper and Text-to-Speech | [Open](./Session-10-Speech-AI-with-Whisper-and-TTS/README.md) |
| 11 | Deploying NLP Applications to Production | [Open](./Session-11-Deploying-NLP-Applications/README.md) |
| 12 | Ethics, Bias and Safety in Large Language Models | [Open](./Session-12-Ethics-Bias-and-Safety-in-LLMs/README.md) |
| 13 | Intelligent Search and Recommendation Systems | [Open](./Session-13-Intelligent-Search-and-Recommendation/README.md) |
| 14 | Domain-Specific NLP: Healthcare and Finance | [Open](./Session-14-Domain-Specific-NLP-Healthcare-and-Finance/README.md) |
| 15 | Build and Deploy Your Next-Gen NLP Application | [Open](./Session-15-Build-and-Deploy-Your-NLP-Application/README.md) |

## 🚀 Module Mini-Project

**Campus Help Desk Assistant**

Build a question-answering assistant for an institute's help desk (fees, timings, courses, exam rules):

1. **Knowledge base**: write 15-20 short policy documents in a `docs/` folder.
2. **Preprocessing and NER**: clean the text and extract entities such as dates, amounts and course names (Sessions 01-02).
3. **RAG**: chunk the documents, embed them, retrieve the top 3 chunks for each question and answer only from them (Session 07).
4. **Agent features**: keep chat memory and add at least one tool, for example a fee calculator (Session 08).
5. **Summaries**: a command that summarizes any long document in 3 bullet points (Session 03).
6. **Deploy and review**: expose the assistant as a small API and add a safety check that refuses off-topic or harmful requests (Sessions 11-12).

Deliverables: source code with a `README.md`, a `requirements.txt`, 10 test questions with the bot's answers, and a one-page note on the limitations you found.

## 📚 Resources (official docs)

- [NLTK documentation](https://www.nltk.org/)
- [spaCy usage guide](https://spacy.io/usage)
- [Hugging Face Transformers docs](https://huggingface.co/docs/transformers/index)
- [Hugging Face LLM course](https://huggingface.co/learn/llm-course)
- [PEFT documentation](https://huggingface.co/docs/peft/index)
- [Sentence Transformers documentation](https://sbert.net/)
- [scikit-learn text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [OpenAI API documentation](https://platform.openai.com/docs)

---

[🏠 Term Home](../README.md) · [Term 6 Capstone ➡](../Capstone/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
