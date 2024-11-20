import mediapipe as mp

class Handrecognition:
    def __init__(self):
        # Initialize MediaPipe Hands and Drawing Utilities
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.gesture = "None"
        #self.index_tip = 0.0

    def landmark_update(self, hand_landmarks):
        # Finger tips
        self.thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
        self.index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        self.middle_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        self.ring_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP]
        self.pinky_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP]
        # Finger pips
        self.index_pip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP]
        self.middle_pip = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
        self.ring_pip = hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP]
        self.pinky_pip = hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP]

    def hand_gesture(self):
        if (self.index_tip.y < self.index_pip.y and
            self.middle_tip.y < self.middle_pip.y and
            self.ring_tip.y < self.ring_pip.y and
            self.pinky_tip.y < self.pinky_pip.y):
            self.gesture = "PAPER"
        elif (self.index_tip.y < self.index_pip.y and
              self.middle_tip.y < self.middle_pip.y and
              self.ring_tip.y > self.ring_pip.y and
              self.pinky_tip.y > self.pinky_pip.y):
            self.gesture = "SCISSORS"
        elif (self.index_tip.y > self.index_pip.y and
              self.middle_tip.y > self.middle_pip.y and
              self.ring_tip.y > self.ring_pip.y and
              self.pinky_tip.y > self.pinky_pip.y):
            self.gesture = "ROCK"
        else:
            self.gesture = "None"
    
    def hand_tipcords(self):
        # Store the landmarks in a list for easier access can be made better in loop but for now it is fine
        hand_tips = [
        self.thumb_tip,
        self.index_tip,
        self.middle_tip,
        self.ring_tip,
        self.pinky_tip,
        ]
        hand_tips_cords = [(tip.x, tip.y) for tip in hand_tips]
        return hand_tips_cords