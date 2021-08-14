import speech_recognition as sr
import pyttsx3

question = ""

def speak():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    # Reading Microphone as source
     # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        engine = pyttsx3.init()
        """ RATE"""
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        #print(rate)  # printing current voice rate
        engine.setProperty('rate', 115)  # setting up new voice rate

        """VOLUME"""
        volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        #print(volume)  # printing current volume level
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

        """VOICE"""
        voices = engine.getProperty('voices')  # getting details of current voice
        # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine.setProperty('voice', voices[1].id)

        """ASK THE QUESTION"""
        engine.say("Hello, this is Leo. Ask me a question about New Mexico Volcanoes")
        engine.runAndWait()
        print("Ask A Question")
        r.adjust_for_ambient_noise(source)  # adjust for ambient noise
        audio_text = r.listen(source)
        #print("ask question")
        # recoginize_() method will throw a request error if the API is unreachable, h
        try:
            # using google speech recognition
            question = r.recognize_google(audio_text)
            print("Question: "+question)
        except:
            print("Sorry, I did not get that")

        engine.say('You asked:'+question)
        engine.runAndWait()

        return question

if __name__ == '__main__':
    speak()