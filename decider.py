import ollama
from vector_storage import VectorStorage
from document_processor import DocumentProcessor
class Decider:
    def __init__(self):
        self.processor = DocumentProcessor()
        self.vector = VectorStorage()
    def decide(self, text: str):
        stream = ollama.chat(model='qwen2.5:0.5b', messages=[
                {'role': 'system', 'content': "Du entscheidest mit ja oder nein, ob die Nachricht wichtige Informationen über den User enthält und wenn ja, fasst du den Text formell zusammen."},
                {'role': 'user','content': text
                 }
                ]
                )
        response = stream["message"]["content"]
        return response
    def check(self, input: str):
        if "Ja" in input or "ja" in input:
            text=self.processor.make_chunks(input)
            self.vector.add_chunks(text)
if __name__ == "__main__":
    decider = Decider()

