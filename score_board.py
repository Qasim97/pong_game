import turtle
from ball import Ball


class ScoreBoard(Ball):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.totalPoints = turtle.textinput("Total Points", "Enter Total Points: ")

    def show_score(self):
        self.goto(-100, 200)
        self.write(self.player2_score, False, "center", ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player1_score, False, "center", ("Courier", 80, "normal"))

    def add_score_player1(self):
        self.player1_score += 1

    def add_score_player2(self):
        self.player2_score += 1

    def check_score(self):
        if self.player1_score > int(self.totalPoints):
            self.goto(0, 0)
            self.write("Player 1 Won", False, "center", ("Courier", 60, "bold"))
            return True
        elif self.player2_score > int(self.totalPoints):
            self.goto(0, 0)
            self.write("Player 2 Won", False, "center", ("Courier", 60, "bold"))
            return True
        elif self.player1_score == int(self.totalPoints) and self.player2_score == int(self.totalPoints):
            self.goto(0, 0)
            self.write("Game Draw and Both Scores Decrease by 2", False, "center", ("Courier", 60, "bold"))
            self.player1_score -= 2
            self.player2_score -= 2
            self.refresh()

        return False
