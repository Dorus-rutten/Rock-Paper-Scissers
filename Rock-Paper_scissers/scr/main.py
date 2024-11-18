# Imports
# cmd = input("Dorus zijn cli > ")
import cv2
import mediapipe as mp
import numpy as np
import os

from Handrecognition import Handrecognition
from Game import Game
from Screen import Screen
from File import File
from AI import AI
print("import sucecse")
# Instantiate classes
print("class")
print("test")
ai = AI()
file = File()
hr = Handrecognition()
scr = Screen(hr) 
game = Game(hr,scr,file)
file_path = "data.csv"
def update():
    #update the landmarks and the tips
    hr.landmark_update(hand_landmarks)
    hr.hand_tipcords()
    hr.hand_gesture()
    # print(hr.gesture)    
    #game update
        
    if game.result == True:           
        file.file_lastchoice()
        game.game_result()
    scr.screen_result(image,game.gameresult, game.choice, hr.gesture,)

    if(hr.index_tip.x * scr.frame_width > int(scr.frame_width / 2 - 50) and
        hr.index_tip.x * scr.frame_width < int(scr.frame_width / 2 + 50) and
        hr.index_tip.y * scr.frame_height < 40 and
        hr.index_tip.y * scr.frame_height > 0 or game.game_status == True):
        game.game_running()
        scr.screen_play(image)
    else:
        scr.screen_pauze(image)






#create a file
if not os.path.exists(file_path):
    file.file_create()

# Start MediaPipe hands detection
with mp.solutions.hands.Hands(
        min_detection_confidence=0.8,
        max_num_hands=1,
        min_tracking_confidence=0.8) as hands:

    while game.scr.cap.isOpened():
        success, image = game.scr.cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the image and convert to RGB
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # Process the image for hand detection
        results = hands.process(image)

        # Convert the image back to BGR for OpenCV display
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Check if any hand landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                # Draw landmarks
                hr.mp_drawing.draw_landmarks(image, hand_landmarks, hr.mp_hands.HAND_CONNECTIONS)

                # Update hand landmarks and perform gesture recognition
                

                # Run the game logic
                update()
                # Update the display with the modified image
        else:
            print("Hand landmarks not detected")

        # Display the result
        cv2.imshow('ROCK PAPER SCISSORS', image)

        # Break loop if 'q' is pressed
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# Release resources
scr.cap.release()
cv2.destroyAllWindows()
