import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")

    try:
        while True:
            audio = recognizer.listen(source) 
            print("Converting...")

            try:
                text = recognizer.recognize_google(audio)
                print(f"Converting: {text}")

                #If you want converted speech to listen, uncomment this: 
                if text:
                    obj = pyttsx3.init()
                    obj.say(text)
                    obj.runAndWait()
                else:
                    print('error: No text available for this post.')
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
    except KeyboardInterrupt:
        print("Stopped listening.")
