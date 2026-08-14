import ollama
from serverlog import error
class Ask_Llm:
    def ask(self, question: str, type: str, context: str):
        try:
            system_prompt = f'You are polite.'
            if type == "chat":
                system_prompt = f"You are polite and answer the questions. You answer with the context: {context}"
            elif type == "summary":
                system_prompt=f"Summarize the text in bullet points and if it is useful, use the context: {context}."
            elif type=="translate":
                system_prompt = f"Translate the desired text into the desired language and use the context: {context}."
            stream = ollama.chat(model='qwen2.5:0.5b', messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user','content': question},
                ],
                stream=True
                )
            
            for chunk in stream:
                yield chunk['message']['content']
        except Exception as e:
            error(e)
