# AI Backend Engine

## 😁About the project
My main aim was to learn more about servers and build my own API, rather than paying for one. I decided to undertake this project because it helps me develop my skills, gain new programming experience, and because I’m very interested in AI. This AI server is intended to serve as the core of a future app built using flet, a framework based on Flutter.

## 🚀Features
  -The server receives questions and answers them using the Qwen2.5:0.5b language model.
  -The server automatically verifies the client using a generated API key.
  -The data is sent in a JSON payload.
  -The server can handle multiple requests via threads.
  -The server maintains a log on the computer containing data such as the question, answer, time, errors and warnings.
  -The client gets the answer in a stream.

## 🏠Architecture
Internally, the server largely consists of a single large function that accepts and processes the JSON payload, passes the processed payload to the language model, and sends the encrypted response back to the client. The function is then passed as the target of a thread and started. I use threads so that I can handle multiple requests reliably.

## 🔮Technology Stack
Python 3.12🐍, socket, threading, ssl, os, datetime, pathlib, json, ollama and time⏲️

## 📖Installation & Setup
Install Python 3.12 from the official Python website. Install a development environment such as Visual Studio Code. Install all the modules and tools listed above using `pip install [module name]`. Now install the language model using the command `ollama pull qwen2.5:0.5b`. Create a certificate using OpenSSL in your project folder with the command `openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key`. In your [project folder], start by entering your country. Press ENTER to proceed until you reach a question labelled ‘Common name’; enter ‘localhost’ there. Now open a terminal and navigate to the project folder. First, run `python server.py` there, and then, in a new terminal, run `python client.py`.

## Roadmap🎯
In future, I want to integrate the server into an app. In this app, users should be able to change the prompt for the language model using buttons. I’ll also be putting the server online for my app and to provide a free API for beginners, as it doesn’t cost me anything either. This is because I was very unsure about APIs at first, as you need credit. 💸🫰
