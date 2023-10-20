# -*- coding: utf-8 -*-


class TennisGame2:
    POINTS_TO_SCORE = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if self.p1points == self.p2points:
            # tied game
            if self.p1points < 3:
                result = TennisGame2.POINTS_TO_SCORE[self.p1points] + "-All"
            else:
                result = "Deuce"
        elif self.p1points < 4 and self.p2points < 4:
            # early game
            P1res = TennisGame2.POINTS_TO_SCORE[self.p1points]
            P2res = TennisGame2.POINTS_TO_SCORE[self.p2points]
            result = P1res + "-" + P2res
        else:
            # end game
            leading_player = "player1" if self.p1points > self.p2points else "player2"
            if abs(self.p1points - self.p2points) == 1:
                result = f"Advantage {leading_player}"
            else:
                result = f"Win for {leading_player}"
        return result

    def SetP1Points(self, number):
        self.p1points = number

    def SetP2Points(self, number):
        self.p2points = number

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1
