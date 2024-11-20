import os
import csv

class File:
    def __init__(self):
        self.player_rock = 0
        self.player_paper = 0
        self.player_scissors = 0

        self.games_won = 0
        self.games_lost = 0
        self.games_tie = 0

        self.game_count = 0

    def file_create(self):
        with open("data.csv", "w") as file:
            file.write("game conclution, AI choice, player choice, game_count\n")

    def file_read(self):
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for line in reader:
                print(line)

    def file_read_conclution(self):
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header if there's one
            for line in reader:
                if line[0] == "Tie!":
                    self.games_tie += 1
                if line[0] == "AI Wins!":
                    self.games_lost += 1
                if line[0] == "You Win!":
                    self.games_won += 1
        print(f"games won: {self.games_won}")
        print(f"games tied: {self.games_tie}")
        print(f"games lost: {self.games_lost}")

    def file_something(self):
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header if there's one
            for line in reader:
                pass

    def file_lastchoice(self):
        with open("data.csv", "r") as file:
            lines = file.readlines()
            last_line = lines[-1].strip() if lines else None
            return last_line

    def file_player_choice(self):
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header if there's one
            for line in reader:
                player_choice = line[2]  # Modify this if the AI choice is in a different column
                if player_choice == " ROCK":
                    self.player_rock += 1
                elif player_choice == " PAPER":
                    self.player_paper += 1
                elif player_choice == " SCISSORS":
                    self.player_scissors += 1

    def file_write(self,gameresult,choice,gesture):
        with open("data.csv", "a") as file:
            reader = csv.reader(file)
            for line in reader:
                game_count = line[3]
            file.write(f"{gameresult}, {choice}, {gesture}, {game_count}\n")

    def file_delete(self):
        print("are you shure????")



