# Virtual Assistant using ChatGPT with Speech-to-Text and Text-to-Speech

This project was inspired by [this Google Colab notebook.](https://colab.research.google.com/github/bhattbhavesh91/voice-assistant-whisper-chatgpt/blob/main/OpenAI-Whisper-ChatGPT-Notebook.ipynb)

## Installation

Use `pip install -r requirements.txt` to install the libraries needed. You may need to install chromium browser and xvfb (virtual framebuffer) to run it on a linux server.

See [here](https://github.com/terry3041/pyChatGPT#obtaining-session_token) for instructions on obtaining your ChatGPT session token. You can set the token as the environment variable `$CHATGPT_SESSION_TOKEN` or paste it in manually when prompted.

Set `share=True` within the `launch()` function within main.py to host the gradio app publically.
 
