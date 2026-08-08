import ollama
import time
def sprachmodell(frage):
    try:
        stream = ollama.chat(model='qwen2.5:0.5b', messages=[
            {'role': 'system', 'content': 'Du bist nett und höflich.'},
            {'role': 'user','content': frage},
            ],
            stream=True
            )
        
        for chunk in stream:
            yield chunk['message']['content']
            time.sleep(0.1)
    except Exception as e:
        yield f"Es ist ein Fehler aufgetreten: {e}"

                                