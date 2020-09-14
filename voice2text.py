import speech_recognition
import gui_actions

gui = gui_actions.gui_control()
recognizer = speech_recognition.Recognizer()
print("\n\nThreshold Value Before calibration:" + str(recognizer.energy_threshold))

with speech_recognition.Microphone(chunk_size=8192) as source:
    while True: 
        try:
            audio = recognizer.adjust_for_ambient_noise(source)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak:")
            audio = recognizer.listen(source)
            speech_to_txt = recognizer.recognize_google(audio).lower()
            print(speech_to_txt)
        except Exception as ex:
            print("Sorry. Could not understand.\n\n")
        continue
            
    print("I heard : " + speech_to_txt)
        
    #---------------------------------------------------------------------
    # The following if-else block is for the commands I have chosen and 
    # call their respective GUI action
    #--------------------------------------------------------------------
    if speech_to_txt == "quit program" or speech_to_txt == "exit program":
        sys.exit()
    elif speech_to_txt == "mouse up" or speech_to_txt == "move up":
        gui.mouse_up(recognizer, source)
    elif speech_to_txt == "mouse down" or speech_to_txt == "move down":
        gui.mouse_down()
    elif speech_to_txt == "mouse left" or speech_to_txt == "move left":
        gui.mouse_left()
    elif speech_to_txt == "mouse right" or speech_to_txt == "move right":
        gui.mouse_right()
    elif speech_to_txt == "left click" or speech_to_txt == "click" or speech_to_txt == "left-click":
        gui.left_click()
    elif speech_to_txt == "right click" or speech_to_txt == "right-click":
        gui.right_click()
    elif speech_to_txt == "double click" or speech_to_txt == "double-click":
        gui.double_click()
    elif speech_to_txt == "open firefox":
        gui.open_firefox()
    elif speech_to_txt == "open files":
        gui.open_files()
    elif speech_to_txt == "mute" or speech_to_txt=="unmute":
        gui.mute_unmute()
    elif speech_to_txt == "play" or speech_to_txt=="pause":
        gui.play_pause()
    elif speech_to_txt == "volume up" or speech_to_txt=="sound up":
        gui.volume_up()
    elif speech_to_txt == "volume down" or speech_to_txt=="sound down":
        gui.volume_down()