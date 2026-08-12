from sentence_transformers import SentenceTransformer
import chromadb
import os
from dotenv import load_dotenv
class VectorStorage:
    def __init__(self, db_name: str="vektor_db"):
        load_dotenv()
        HU_KEY = os.getenv("HUGGING_FACE_KEY")
        self.db_name = db_name
        self.folder_path = os.path.dirname(os.path.abspath(__file__))
        self.db_full_path = os.path.join(self.folder_path, self.db_name)
        self.chroma_client = chromadb.PersistentClient(path=self.db_full_path)
        self.collection = self.chroma_client.get_or_create_collection(name="pdf_dokumente")
        self.model = SentenceTransformer(
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            token="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"
        )
    def add_chunks(self, chunks: list[str]):
        BATCH_SIZE = 5461
        embeddings = self.model.encode(chunks)
        ids = [f"id_{i}" for i in range(len(chunks))]
        embedding_list = embeddings.tolist()
        for i in range(0, len(chunks), BATCH_SIZE):
            self.collection.add(
                embeddings=embedding_list[i : i + BATCH_SIZE],
                documents=chunks[i : i + BATCH_SIZE],
                ids=ids[i : i + BATCH_SIZE]
        )
        print("Daten erfolgreich eingetragen.")
    def search(self, query_text: str, n_results)-> list[str]:
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        documents = results.get("documents", [[]])
        if documents:
            return documents[0]
if __name__ == "main":
    vector = VectorStorage()
