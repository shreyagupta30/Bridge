import speech_recognition

recognizer = speech_recognition.Recognizer()
print("\n\nThreshold Value Before calibration:" + str(recognizer.energy_threshold))

with speech_recognition.Microphone() as src:
    while True: 
        try:
            audio = recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak:")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio).lower()
            print(speech_to_txt)
        except Exception as ex:
            print("Sorry. Could not understand.\n\n")
        continue
