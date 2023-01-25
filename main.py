import whisper
import gradio as gr 
import time
from pyChatGPT import ChatGPT
import warnings
import os
from gtts import gTTS


warnings.filterwarnings('ignore')
try:
    secret_token = os.environ['CHATGPT_SESSION_TOKEN']
except:
    input('Please enter your ChatGPT session token: ')

model = whisper.load_model('base')

def transcribe(audio):

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    result_text = result.text

    # Pass the generated text to Audio
    chatgpt_api = ChatGPT(secret_token)
    resp = chatgpt_api.send_message(result_text)
    out_result = resp['message']
    gTTS(out_result, lang='en', tld='ie').save('out.mp3')


    return [result_text, 'out.mp3']

output_1 = gr.Textbox(label="Speech to Text")
output_2 = gr.outputs.Audio(label="Text to Speech", type='filepath')

gr.Interface(
    title = 'Speech to ChatGPT to Speech', 
    fn=transcribe, 
    inputs=[
        gr.inputs.Audio(source="microphone", type="filepath")
    ],

    outputs=[
        output_1,  output_2
    ],
    live=True).launch(share=False)

