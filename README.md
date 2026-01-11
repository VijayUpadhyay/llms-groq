# llms-test
This will have test code which will create a LLM Model client using the apikey and try to communicate with the model and get the answer for the questions

Create Virtual Environment
--------------------------
    1. rm -rf /Users/vijay/_github_tuts/genai-workspace/llms-groq/.venv
    2. python3 -m venv /Users/vijay/_github_tuts/genai-workspace/llms-groq/.venv
    3. /Users/vijay/_github_tuts/genai-workspace/llms-groq/.venv/bin/python -m pip install -r requirements.txt

Groq
-----
Get API key from groq.com and use it to create Groq Client. Use the client to initiate the communication with the Groq LLM

Ollama
------------
    1. download ollama as per system: windows/mac/linux
    2. run command: ollama serve
    3. run command: ollama run gemma3:1b. It will download and 4. run this model. Ref: [text](https://ollama.com/library/gemma3)

Langchain and LamaIndex
------------------------
![Packages To Download](./resources/image.png)