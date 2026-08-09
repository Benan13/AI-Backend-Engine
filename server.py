import socket
import threading
import ssl
from sprachmodell_funktion import sprachmodell
import json
from dotenv import load_dotenv
import os
from serverlog import log, error, warn
load_dotenv()
MY_KEY=os.getenv("SERVER_API_KEY")
HOST="127.0.0.1"
PORT=39582
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
log("Server started succesfully")
def client_handle(client, address):
    while True:
        try:
            roh = client.recv(4096).decode('utf-8')
            if not roh:
                break
            try:
                data=json.loads(roh)
                log(f"Message from {address}: {data.get("message")}")
            except json.JSONDecodeError:
                client.send("Error: Invalid data format.".encode('utf-8'))
                continue
            if data.get("my_api") != MY_KEY:
                warn(f"Unauthorized acces attempt: Invalid API key from {address}")
                client.send("ERROR: Invalid API key.".encode('utf-8'))
                client.close()
                return
            if not data.get("message"):
                break
            for stuck in sprachmodell(data.get("message")):
                client.send(stuck.encode('utf-8'))
            client.send(b'\x00')
            log(f"Streamed response succesfully transmitted to {address}.")
        except Exception as e:
            error(f"Error handling connection with {address}: {e}")
            break
    log(f"Server turned off Connection succesfully: {address}")
    client.close()

while True:
    client, address = server.accept()
    log(f"New incoming connection from: {address}")
    try:
        secure_client = context.wrap_socket(client, server_side=True)
        threading.Thread(target=client_handle, args=(secure_client, address), daemon=True).start()
    except Exception as e:
        error(f"SSL handshake failed with {address}: {e}")

