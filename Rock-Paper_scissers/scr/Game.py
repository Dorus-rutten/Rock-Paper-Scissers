import random
import time



class Game:
    def __init__(self, handrec,screc,fl):
        self.hr = handrec
        self.scr = screc
        self.file = fl
        self.result = False
        self.game_status = False
        self.counting = False
        self.total_time = 0
        self.choice = ""
        self.gameresult = ""
        self.elapsed_time = 0

    def game_running(self):
        
        current_time = time.time()
        self.game_status = True
        if not self.counting:
            print("Initializing...")
            self.start_time = current_time
            self.counting = True
            self.total_time = 0
            self.elapsed_time = 0  # Initialize elapsed time here

        else:
            print("Counting...")
            self.elapsed_time = current_time - self.start_time

            if self.elapsed_time >= 1:
                self.total_time += self.elapsed_time
                self.start_time = current_time

            if self.total_time > 3:
                print("Total time")
                rpc = ["ROCK", "PAPER", "SCISSORS"]
                self.choice = random.choice(rpc)
                self.result = True
                self.game_status = False
                # print(f"AI choise: {self.choice}")
                

        # print(f"Current Time: {current_time}")
        # print(f"Start Time: {self.start_time}")
        # print(f"Elapsed Time: {self.elapsed_time}")
        # print(f"Total Time: {self.total_time}")


    def game_result(self):
            print("Game result")
            if self.choice == self.hr.gesture:
                self.gameresult = "Tie!"
            elif (self.choice == "ROCK" and self.hr.gesture == "PAPER") or \
                (self.choice == "PAPER" and self.hr.gesture == "SCISSORS") or \
                (self.choice == "SCISSORS" and self.hr.gesture == "ROCK"):
                self.gameresult = "You Win!"
            elif self.hr.gesture == "None":
                self.gameresult = "No contest"
            else:
                self.gameresult = "AI Wins!"
            self.counting = False
            self.result = False
            print("false")
            self.file.file_write(self.gameresult,self.choice,self.hr.gesture)
            
            self.file.file_read()
            # self.file.file_player_choic()
            self.file.file_read_conclution()

            
            print(f"Result is: {self.gameresult}")
            print(f"AI choise: {self.choice}")
            print(f"your is: {self.hr.gesture}")


