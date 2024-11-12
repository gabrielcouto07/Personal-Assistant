import speech_recognition as sr

def take_voice_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice).lower()
        if 'assistant' in command:
            return command.replace('assistant', '').strip()
    return ""
