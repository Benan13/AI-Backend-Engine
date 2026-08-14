from vector_storage import VectorStorage
from serverlog import error
from document_processor import DocumentProcessor
from decider import Decider
from llm import Ask_Llm
class Pipeline:
    def __init__(self):
        self.decider = Decider()
        self.vektor = VectorStorage()
        self.processor = DocumentProcessor()
        self.llm = Ask_Llm()
    def ingestion(self):
        try:
            print("Starting Pipeline")
            text = self.processor.extract()
            print("Make Chunks...")
            chunks = self.processor.make_chunks(text)
            if len(chunks) > 0:
                print(f"Chunks: {len(chunks)}")
                print("Generate Chunks...")
                self.vektor.add_chunks(chunks)
                print("I am Finish.")
            else:
                print("ERROR: There are no chunks.")
        except Exception as e:
            error(e)
    def ask_database(self, question: str):
        self.decider.check(self.decider.decide(question))
        relevant_chunks = self.vektor.search(question, n_results=3)
        context = "\n---\n".join(relevant_chunks)
        result = self.llm.ask(question=question, type="chat", context=context)
        return result


if __name__  == "__main__":
    pipeline = Pipeline()
    pipeline.ingestion()
