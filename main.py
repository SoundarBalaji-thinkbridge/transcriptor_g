import speech_recognition as sr
import sys

from fastapi import FastAPI, Depends


app = FastAPI(title="transcriptor")

# filename = r'example.wav'
# def transcripting(filename = r'examplefinal.wav'):


# def transcripting(filename = "https://nikeshthinkbridge.sharepoint.com/:u:/s/Tiram.AI/ET0mmCFuTU9GnNxDD_o3hY4BhmuHbOznwnNwxykSdfg1pQ?e=5x3Wce"):
def transcripting(filename = r'examplefinal.wav'):
    # initialize the recognizer
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    # print(text)
    return text

@app.get('/')
async def transcripted_api(transcript=Depends(transcripting)):
    return transcript