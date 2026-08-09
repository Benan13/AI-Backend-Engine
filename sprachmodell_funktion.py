import ollama
import time
def sprachmodell(question, type);
    try:
        if type == "chat":
            system_prompt = "You are polite and answer the questions."
        elif type == "summary":
            system_prompt="Summarize the text in bullet points."
        elif type=="translate":
            system_prompt = "Translate the desired text into the desired language."
        stream = ollama.chat(model='qwen2.5:0.5b', messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user','content': question},
            ],
            stream=True
            )
        
        for chunk in stream:
            yield chunk['message']['content']
            time.sleep(0.1)
    except Exception as e:
        yield f"Error: {e}"

                                
