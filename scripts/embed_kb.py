import pathlib, textwrap
from langchain.docstore.document import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

KB_DIR    = pathlib.Path(__file__).resolve().parents[1] / "kb"
STORE_DIR = "chroma_store"

def build_vector_store():
    docs = [
        Document(
            page_content=textwrap.dedent(p.read_text()),
            metadata={"source": p.name}
        )
        for p in KB_DIR.glob("*.md")
    ]
    if not docs:
        raise RuntimeError("kb/ is empty – add Markdown files first!")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"  # ≈90 MB
    )

    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=STORE_DIR,
    )
    db.persist()
    print(f"✓ Embedded {len(docs)} docs → {STORE_DIR}/")

if __name__ == "__main__":
    build_vector_store()


