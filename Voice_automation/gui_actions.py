import pyautogui

# Faster: Moves mouse pointer by 200 pixels
# SLOWER: Moves mouse pointer by 20 pixels
FASTER=200
SLOWER=20


class gui_control:
    def __init__(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        pyautogui.size()

    def mouse_up(self,recognizer, source):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, -1*SLOWER, duration=0.25)
            try:
                audio = recognizer.listen(source)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, -1*FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, -1*SLOWER, duration=0.25)
                    
    def mouse_down(self,recognizer, source):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, 1*SLOWER, duration=0.25)
            try:
                audio = recognizer.listen(source)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, 1*FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, 1*SLOWER, duration=0.25)


    def mouse_left(self,recognizer, source):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(-1*SLOWER, 0, duration=0.25)
            try:
                audio = recognizer.listen(source)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(-1*FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(-1*SLOWER, 0, duration=0.25)
 
    def mouse_right(self,recognizer, source):
        pyautogui.moveRel(100, 0, duration=0.25)
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(1*SLOWER, 0, duration=0.25)
            try:
                audio = recognizer.listen(source)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(1*FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(1*SLOWER, 0, duration=0.25)
       
    def left_click(self):
        pyautogui.click()
 
    def right_click(self):
        pyautogui.click(button='right', clicks=2, interval=0.25)
 
    def double_click(self):
        pyautogui.click(button='left', clicks=2, interval=0.25)

    
    def open_firefox(self):
        icon_location = pyautogui.locateOnScreen(r'screenshots\firefox.png')
        if icon_location is not None:
            if len(icon_location) == 4:
                pyautogui.click(x=icon_location.left, y=icon_location.top, duration=0.25)
        else:
            print("Could not locate Firefox Icon on screen")
         
    def open_files(self):
        icon_location = pyautogui.locateOnScreen(r'screenshots\Files.png')
        if icon_location is not None:
            if len(icon_location) == 4:
                pyautogui.click(x=icon_location.left, y=icon_location.top, duration=0.25)
        else:
            print("Could not locate Files Icon on screen")
 
    # Simulates the MUTE/UNMUTE key press
    
    def mute_unmute(self):
        pyautogui.typewrite(['volumemute'])
 
    # Simulates the SPACE key press 
    def play_pause(self):
        pyautogui.typewrite(['space'])

    # Simulates the VOLUME UP key press       
    def volume_up(self):
        pyautogui.typewrite(['volumeup'])
 
    # Simulates the VOLUME DOWN key press
    def volume_down(self):
        pyautogui.typewrite(['volumedown'])