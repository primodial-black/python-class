def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)
st="hello sayadh"
if __name__=='__main__':
    # speak("how are you sayadh")
    speak(st)
