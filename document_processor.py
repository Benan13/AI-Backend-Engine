from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
class DocumentProcessor:
    def __init__(self, chunk_size: int=1200, chunk_overlap: int=270):
        self.folder_path = os.path.dirname(os.path.abspath(__file__))
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitters = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )
    def extract(self) -> str:
        folder = os.path.join(self.folder_path, "documents")
        documents_list = ""
        if os.path.exists(folder):
            for file in os.listdir(folder):
                if file.endswith(".pdf"):
                    print(f"loading file: {file}")
                    loader = PyPDFLoader(os.path.join(folder, file))
                    for doc in loader.load():
                        documents_list += doc.page_content + "\n"
        else:
            print(f"Konnte Ordner nicht finden, lade ihn in {folder}")
        return documents_list
    def make_chunks(self, text: str) -> list[str]:
        return self.text_splitters.split_text(text)


if __name__ == "__main__":
    processor = DocumentProcessor()
    text = processor.extract()
    chunks = processor.make_chunks(text)
    print(f"Erfolgreich {len(chunks)} Chunks extrahiert!")