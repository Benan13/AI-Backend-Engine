import socket
import json
from dotenv import load_dotenv
import os
import ssl
from pathlib import Path
load_dotenv(Path(__file__).parent / ".env", override=True)
server_api = os.getenv("SERVER_API_KEY")
HOST = "127.0.0.1"
PORT = 39582
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
raw = context.wrap_socket(client, server_hostname=HOST)
raw.connect((HOST, PORT))
while True:
    try:
        message = input("You: ")
        if not message:
            continue
        data = {
            "my_api": server_api,
            "message": message
        }
        raw.send(json.dumps(data).encode('utf-8'))
        answer = raw.recv(4096).decode('utf-8')
        print("Answer from Server:", answer)
        while True:
            chunk = raw.recv(1024)
            if not chunk or b'\x00' in chunk:
                rest = chunk.replace(b'\x00', b'').decode('utf-8')
                print(rest)
                break
            print(chunk.decode('utf-8'), end="", flush=True)
        if not answer:
            raw.close()
            break
    except:
        continue
