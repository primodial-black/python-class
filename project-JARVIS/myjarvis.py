import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia  #pip install wikipedia
import webbrowser
import os
import random
import smtplib
import requests


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak("Hello Sir, Good Morning!")
    elif 12<=hour<18:
        speak("Hello Sir, Good Afternoon!")
    else:
        speak("Hello Sir, Good Evening!")
    speak("I am Jarvis . PLEASE TELL ME HOW MAY I HELP YOU TODAY")

def takecommand():
    '''it takes microphone input from user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold =200
        audio=r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        speak("Say it again please....")
        return "None"
    return query





def sendEmail(to,emailcontent):
    #to send emails you need to enable less secure apps in gmail
    #to do it go to google browser search "less secure app in google"
    #go to ur account in that search result and enable the less secure apps in settings
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("your email id",'password') #for security store ur pwd in seperate txtfile and bring the variable here
    server.sendmail("your email id",to,emailcontent)
    

excluded_words = ['search', 'in', 'browser', 'google','hey','jarvis']
def search_google(query):
    words = query.split()
    search_word = ''
    for word in words:
        if word not in excluded_words:
            search_word += word + " +"
            search_word = search_word[:len(search_word)-1]
    print(search_word)
    webbrowser.open("https://www.google.co.in/search?q="+search_word)
    if __name__ == "__main__":
        speak("Here is what I found on your request")


if __name__=="__main__":
    wishme()
    end= True
    while end:
        query = takecommand().lower()

    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=1)
            speak('According to Wikipedia..')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'search' in query:
            search_google(query)

        
        elif 'play music' in query:
            music_dir="D:\\songs"   #your music directory path
            songs = os.listdir(music_dir)
            print(songs)
            # os.startfile(os.path.join(music_dir,songs[0]))
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        

        elif 'how are you' in query:
            speak('I am an AI, I do not have feelings, but I am functioning as expected.')
        elif 'what is your name' in query:
            speak('You can call me Jarvis.')
        elif 'tell me a joke' in query:
            speak('Why don\'t scientists trust atoms? Because they make up everything!')
        elif 'what is the weather' in query:
            speak('I\'m sorry, I cannot fetch real-time data. Please check a reliable weather website.')
        elif 'who are you' in query:
            speak('I am Jarvis, your personal AI assistant.')
        elif 'what can you do' in query:
            speak('I can help you search the web, answer questions, and have a casual conversation with you.')
        elif 'tell me a fact' in query:
            speak('Did you know that the speed of light is approximately 299,792 kilometers per second?')

        elif 'tell me a story' in query:
            speak('Once upon a time, in a world where AIs and humans coexisted...')
        elif 'what is your favorite color' in query:
            speak('As an AI, I don\'t have personal experiences or preferences, but I can tell you that the most common favorite color among humans is blue.')
        elif 'do you like music' in query:
            speak('As an AI, I don\'t have personal experiences or preferences, but I can help you find music you might enjoy.')
        
        

        elif 'list some applications of ai' in query:
            speak('AI has a wide range of applications, including but not limited to, healthcare, autonomous vehicles, voice assistants, recommendation systems, and gaming.')
        elif 'what is artificial intelligence' in query:
            speak('Artificial Intelligence is a branch of computer science that aims to create systems capable of performing tasks that would normally require human intelligence. These tasks include learning, reasoning, problem-solving, perception, and language understanding.')
        elif 'what are the pros of ai' in query:
            speak('AI has several advantages, such as automation of repetitive tasks, ability to work with large amounts of data, and potential to perform complex tasks faster and more accurately than humans.')
        elif 'what are ai neural networks' in query:
            speak('Artificial Neural Networks are computing systems inspired by the biological neural networks that constitute animal brains. They are a key tool used in machine learning and help to solve complex tasks.')
        elif 'what are intelligent agents' in query:
            speak('In artificial intelligence, an intelligent agent is a system that perceives its environment and takes actions to maximize its chances of achieving its goals.')
        elif 'what are the types of ai' in query:
            speak('AI can be classified into two main types: Narrow AI, which is designed to perform a narrow task, and General AI, which is an AI system with generalized human cognitive abilities.')
        elif 'what is deep learning' in query:
            speak('Deep learning is a subset of machine learning where artificial neural networks, algorithms inspired by the human brain, learn from large amounts of data.')
        elif 'how can we apply artificial intelligence' in query:
            speak('AI can be applied in many fields. For example, in healthcare, AI can be used for predicting diseases. In finance, AI can be used for fraud detection. In transportation, AI is used in the development of self-driving cars.')
        elif 'how powerful is ai' in query:
            speak('AI is very powerful and has the potential to revolutionize many aspects of our lives. It can process and analyze large amounts of data quickly and accurately, automate repetitive tasks, and even perform tasks that are difficult for humans.')
        elif 'what is turing test' in query:
            speak('The Turing Test, proposed by Alan Turing in 1950, is a test of a machine\'s ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human.')
        elif 'explain tensorflow' in query:
            speak('TensorFlow is an open-source software library for machine learning and artificial intelligence. It provides a flexible platform for defining and running machine learning algorithms.')
        elif 'what is game theory' in query:
            speak('Game theory is a theoretical framework for conceiving social situations among competing players. In some respects, game theory is the science of strategy, or at least the optimal decision-making of independent and competing actors in a strategic setting.')
        elif 'what is an expert system' in query:
            speak('An expert system is a computer system that emulates the decision-making ability of a human expert. They are designed to solve complex problems by reasoning through bodies of knowledge, represented mainly as if–then rules rather than through conventional procedural code.')
        elif 'what is computer vision in ai' in query:
            speak('Computer vision in AI is a field that involves automatically extracting, analyzing, and understanding useful information from digital images. It includes methods for acquiring, processing, analyzing, and understanding images from the real world in order to produce numerical or symbolic information.')
        elif 'what is natural language processing' in query:
            speak('Natural Language Processing, or NLP, is a branch of artificial intelligence that deals with the interaction between computers and humans through natural language. The ultimate objective of NLP is to read, decipher, understand, and make sense of human language in a valuable way.')
        elif 'what is supervised versus unsupervised learning' in query:
            speak('Supervised learning is a type of machine learning where the model is trained on a labeled dataset, i.e., a dataset where the target variable is known. Unsupervised learning, on the other hand, is a type of machine learning where the model is trained on an unlabeled dataset, i.e., a dataset where the target variable is not known.')
        elif 'explain the hidden markov model' in query:
            speak('A Hidden Markov Model (HMM) is a statistical Markov model in which the system being modeled is assumed to be a Markov process with unobserved (hidden) states. HMMs are known for their application in temporal pattern recognition such as speech, handwriting, gesture recognition, part-of-speech tagging, musical score following, partial discharges and bioinformatics.')
        elif 'state fuzzy approximation theorem' in query:
            speak('The Fuzzy Approximation Theorem states that given any real number, there exists a fuzzy set that approximates that number to within any desired degree of accuracy. This theorem is fundamental to the theory of fuzzy numbers and fuzzy arithmetic.')










        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {strTime}")

        elif 'vs code' in query:
            codePath = "C:\\Users\\syeda\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"     #Your VSCode Directory Path
            speak('opening vs code')
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should i say?")
                emailcontent= takecommand()
                to = "recipient@gmail.com"     #add your recipient gmail id here
                sendEmail(to,emailcontent)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry bhai, may Email nahee bhejsaka")
            #to send email to a particular person create a dict where names of contact 
            #should be used as keys and their mail as value


            

        elif 'exit' in query:
            end = False
            speak('Okay sir. Call me whenever you want. Have a nice day!')

