from datetime import datetime

def log(text):
    tense = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logging.txt", "a", encoding="utf-8") as file:
        file.write(f"[INFO] [{tense}] [{text}]\n")
def error(text):
    tense = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logging.txt", "a", encoding="utf-8") as file:
        file.write(f"[ERROR] [{tense}] [{text}]\n")
def warn(text):
    tense = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logging.txt", "a", encoding="utf-8") as file:
        file.write(f"[WARNING] [{tense}] [{text}]\n")
