# ollama-chatbot-daemon
A simple Ollama Chatbot Python-based daemon. Is capable of running the Chatbot Ollama program without the need to keep a terminal open. 

To run, ensure you have:
- Ollama set up on your Linux system.
- Cloned [chatbot-ollama](https://github.com/ivanfioravanti/chatbot-ollama) to your system, and used ``npm ci`` to install the required dependencies.
- Cloned the [Ollama-Mini-Daemon](https://github.com/soltros/ollama-mini-daemon) tool to make running ``ollama serve`` in the background much easier.
- Python installed.



  ```
  git clone https://github.com/soltros/ollama-chatbot-daemon.git
  cd ollama-chatbot-daemon/
  chmod +x *.py
   ```
Edit ``daemon.py``, and change the username from my username to yours.
```
def run_command():
    # Change the directory to the desired path
    os.chdir('/home/derrik/chatbot-ollama/')
```
Finally, run with:
```
./daemon.py
```
  
  To shut down the daemon, simply invoke:
   ```
  ./shutdown.py
   ```
   
