#!/bin/bash

## Download the Chatbot Ollama tool ##
git clone https://github.com/ivanfioravanti/chatbot-ollama.git
cd chatbot-ollama/

## Download the Ollama Chatbot Daemon ##
curl https://raw.githubusercontent.com/soltros/ollama-chatbot-daemon/main/daemon.py -o daemon.py

## Setup Ollama Chatbot Daemon ##
chmod +x daemon.py

echo "Installation completed."
