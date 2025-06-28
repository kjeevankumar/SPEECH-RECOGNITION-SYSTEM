# Task 2: Speech-to-Text using SpeechRecognition

import speech_recognition as sr

# Load recognizer
recognizer = sr.Recognizer()

# Load audio file
with sr.AudioFile("sample.wav") as source:
    print("Listening from file...")
    audio = recognizer.record(source)

# Convert speech to text
try:
    text = recognizer.recognize_google(audio)
    print("\n🎤 Transcribed Text:\n")
    print(text)

except sr.UnknownValueError:
    print("Could not understand audio.")

except sr.RequestError as e:
    print(f"Could not request results; {e}")
