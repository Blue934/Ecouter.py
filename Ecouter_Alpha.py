import speech_recognition as sr
def ecouter():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            # Écouter l'audio
            print("Je vous ecoute ... !")
            audio = recognizer.listen(source) # timeout=25, phrase_time_limit=5
            # Reconnaissance vocale avec Google Speech Recognition
            texte = recognizer.recognize_google(audio, language="fr-FR")
            print(f"Vous avez dit : {texte}")
            # Écouter l'audio
            print("Je vous ecoute ... !")
            audio2 = recognizer.listen(source) # timeout=25, phrase_time_limit=5
            # Reconnaissance vocale avec Google Speech Recognition
            reponseE = recognizer.recognize_google(audio2, language="fr-FR")
            reponseE = reponseE.lower()
            if reponseE.lower() == "oui":
                print("Merci de votre precision !")
                reponseE = "oui"
            else:
                print("Desole recommencencer !")
                reponseE = "non"
            return reponseE
        except sr.UnknownValueError:
            print("Désolé, je n'ai pas compris votre requete !.")
        except sr.RequestError as e:
            print(f"Erreur de requête ; {e}")
        except Exception as e:
            print(f"Une erreur est survenue ; {e}")
boucle = True
while boucle:
    reponse = ecouter()
    continue