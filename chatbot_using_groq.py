from groq import Groq
import os
import pyttsx3
import speech_recognition as sr
import sys

recognizer = sr.Recognizer()

api_key = os.environ.get("GROQ_API_KEY")

def chatbot():
    with sr.Microphone() as source:
        print("Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)  
        print("Listening...")

        while True:
            audio = recognizer.listen(source) 
            print("Converting...")

            try:
                question = recognizer.recognize_google(audio)
                print(f"User: {question}")

                if "goodbye" == question.lower():
                    print("Ok No Problem")
                    speak_answer("Ok No problem")
                    sys.exit()

                client = Groq(api_key=api_key)

                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "you are a helpful assistant."
                        },
                        {
                            "role": "user",
                            "content": question,
                        }
                    ],
                    model="llama3-8b-8192",
                )
                answer = chat_completion.choices[0].message.content
                print(f"AI: {answer}")
                speak_answer(answer)

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                speak_answer("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

def speak_answer(answer):
    try:
        obj = pyttsx3.init()
        obj.say(answer)
        obj.runAndWait()
    except Exception as e:
        print(f"Error with pyttsx3: {e}")

chatbot()
