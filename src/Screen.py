import cv2
from File import File

file = File()

class Screen:
    def __init__(self, handrec):
        self.hr = handrec
        self.cap = cv2.VideoCapture(0)
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.game_status = False
        self.counting = False
        self.total_time = 0
        self.result = False

    def screen_pauze(self, image):
        if self.game_status:
            self.game_status = False
            self.counting = False
            self.total_time = 0
        else:
            cv2.rectangle(image, (int(self.frame_width / 2 - 50), 0), (int(self.frame_width / 2 + 50), 40), (0, 0, 0), -1)
            cv2.putText(image, "READY TO PLAY?", (int(self.frame_width / 2 - 50), 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    def screen_play(self, image):
        cv2.rectangle(image, (int(self.frame_width / 2 - 50), 0), (int(self.frame_width / 2 + 50), 40), (0, 0, 0), -1)
        cv2.putText(image, "Playing", (int(self.frame_width / 2 - 50), 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        

        

    def screen_result(self, image, gameresult, choice, gesture):
        
        cv2.putText(image,f"AI choice: {choice}", (0, 50 ),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(image,f"You choise: {gesture}", (0,100),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(image,F"Game result is: {gameresult}", (0,150),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        