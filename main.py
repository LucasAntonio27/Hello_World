from multiprocessing.connection import wait
from time import sleep
import speech_recognition as sr
from scipy.io.wavfile import write
from playsound import playsound
import pyttsx3
import wavio as wv
import robot
import numpy as np
import scipy.io.wavfile as wavfile
from waveshaper import Waveshaper
from playsound import playsound
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
"""
Constants
"""
duracao = 5
freq = 44100
# Diode constants (must be below 1; paper uses 0.2 and 0.4)
VB = 0.2
VL = 0.4

# Controls distortion
H = 4

# Controls N samples in lookup table; probably leave this alone
LOOKUP_SAMPLES = 1024

# Frequency (in Hz) of modulating frequency
MOD_F = 50

# Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
   engine.say(text)
   engine.runAndWait()
r = sr.Recognizer()

speak("Olá, no que posso lhe ajudar?")
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)
        fala = r.recognize_google(audio, language='pt')
        print(fala)
        if fala == ("robotizar" or "robotizar robotizar"):
            speak("Você solicitou a função robotizar")
            speak("Iniciando gravação do trecho de áudio em 3...2...1...")
            
            gravacao = sd.rec(int(duracao * freq), samplerate=freq, channels=2)
            sd.wait()
            wv.write("stereo_audio.wav", gravacao, freq, sampwidth=2)
            robot.main()
            playsound("robot.wav")
            break
        elif fala == ("inverter"):
            speak("Você solicitou a função inverter")
            speak("Iniciando gravação do trecho de áudio em 3...2...1...")
            gravacao = sd.rec(int(duracao * freq), samplerate=freq, channels=2)
            sd.wait()
            wv.write("stereo_audio.wav", gravacao, freq, sampwidth=2)
            robot.main()
            playsound("invert.wav")
        elif fala == ("filtro baixo"):
            speak("Você solicitou a função filtro baixo")
            speak("Iniciando gravação do trecho de áudio em 3...2...1...")
            gravacao = sd.rec(int(duracao * freq), samplerate=freq, channels=2)
            sd.wait()
            wv.write("stereo_audio.wav", gravacao, freq, sampwidth=2)
            robot.main()
            playsound("baixo.wav")
        else:
            print("\"\"")

