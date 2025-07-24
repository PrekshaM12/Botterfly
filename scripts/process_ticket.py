import pathlib, textwrap
from typing import Dict
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama

# ---------- config ----------
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
DB_DIR       = PROJECT_ROOT / "chroma_store"
EMBED_MODEL  = "sentence-transformers/all-MiniLM-L6-v2"
CACHE_DIR    = PROJECT_ROOT / ".hf_cache"
THRESHOLD    = 1.3
CHAT_MODEL   = "llama2:7b"   # model you pulled with Ollama
# ----------------------------

embeddings = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL,
    cache_folder=str(CACHE_DIR)
)
vectordb = Chroma(
    persist_directory=str(DB_DIR),
    embedding_function=embeddings
)

llm = ChatOllama(model=CHAT_MODEL, temperature=0.2)

PROMPT = PromptTemplate.from_template(textwrap.dedent("""
    You are Botterfly 🦋. Respond in **≤ 45 words**.
    User question: "{question}"

    Relevant passage:
    {passage}

    If the passage does not contain the answer, reply exactly:
    "I’m not sure from our docs."
"""))

def process_ticket(text: str) -> Dict:
    """Return {'answer': str, 'source': str, 'similarity': float}."""
    # 1. similarity search
    docs = vectordb.similarity_search_with_score(text, k=1)
    passage, score = docs[0][0].page_content, docs[0][1]
    source = docs[0][0].metadata["source"]

    # 2. confidence gate
    if score > THRESHOLD:
        return {
            "answer": "🤔 I’m not sure from our docs.",
            "source": source,
            "similarity": score,
        }

    # 3. generate concise reply
    prompt = PROMPT.format(question=text, passage=passage)
    answer = llm.invoke(prompt).content

    return {"answer": answer, "source": source, "similarity": score}

if __name__ == "__main__":
    while True:
        try:
            q = input("\nAsk Botterfly › ")
            if not q.strip():
                break
            out = process_ticket(q)
            print(
                f"\n🦋  {out['answer']}"
                f"\n(source: {out['source']} | score={out['similarity']:.3f})"
            )
        except KeyboardInterrupt:
            break
