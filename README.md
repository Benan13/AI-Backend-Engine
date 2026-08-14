# AI Backend Engine

## 😁About the project
My main aim was to learn more about servers and build my own API, rather than paying for one. I decided to undertake this project because it helps me develop my skills, gain new programming experience, and because I’m very interested in AI. This AI server is intended to serve as the core of a future app built using flet, a framework based on Flutter and it sows very good the structure of RAG Architecture.

## 🚀Features
  -The server receives questions and answers them using the Qwen2.5:0.5b language model.
  -The server automatically verifies the client using a generated API key.
  -The data is sent in a JSON payload.
  -The server can handle multiple requests via threads.
  -The server maintains a log on the computer containing data such as the question, answer, time, errors and warnings.
  -The client gets the answer in a stream.
  -The LLM learns with PDFs

## 🏠Architecture
Internally, the server largely consists of a single large function that accepts and processes the JSON payload, passes the processed payload to the language model, and sends the encrypted response back to the client. The function is then passed as the target of a thread and started. I use threads so that I can handle multiple requests reliably. The recently added RAG system works as follows: first, the text is extracted from the PDFs in the ‘documents’ folder using the PyMuPDFLoader module. The text is then divided into chunks. These chunks are subsequently converted into embeddings using Chromadb. The embeddings are then stored in a vector database. The language model then acquires this knowledge by converting the question into embeddings as well, and subsequently performing a similarity search amongst the embeddings in the database. The most similar embeddings are then passed back to the language model, enabling it to utilise the knowledge contained in the PDFs much more effectively.

## 🔮Technology Stack
I used: Python 3.12🐍, socket, threading, ssl, os, datetime, pathlib, json, ollama, langchain, chromadb, sentence_transformer

## 📖Installation & Setup
Install Python 3.12 from the official Python website. Install a development environment such as Visual Studio Code. Install all the modules and tools listed above using `pip install [module name]`. Now install the language model using the command `ollama pull qwen2.5:0.5b`. Create a certificate using OpenSSL in your project folder with the command `openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key`. In your [project folder], start by entering your country. Press ENTER to proceed until you reach a question labelled ‘Common name’; enter ‘localhost’ there. Now open a terminal and navigate to the project folder. First, load the desired PDFs to let the LLM learn. After that, you have to run `python pipeline.py` to load the PDFs into the vector database. Now you can run `python server.py` and then run `python client.py` to start conversation.

## Roadmap🎯
In future, I want to integrate the server into an app. In this app, users should be able to change the prompt for the language model using buttons like translate or chat. I’ll also be putting the server online for my app and to provide a free API for beginners, as it doesn’t cost me anything either. This is because I was very unsure about APIs at first, as you need credit. 💸🫰 I will start a new project with a RAG pipeline and give the LLM datas about me to make my own business card on a website.
