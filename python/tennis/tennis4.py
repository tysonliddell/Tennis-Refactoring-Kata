# -*- coding: utf-8 -*-


class TennisGame4:
    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1Name, player2Name):
        self.server = player1Name
        self.receiver = player2Name
        self.serverScore = 0
        self.receiverScore = 0

    def won_point(self, playerName):
        if playerName == self.server:
            self.serverScore += 1
        else:
            self.receiverScore += 1

    def score(self):
        if self.isTie():
            if self.isDeuce():
                result = "Deuce"
            else:
                result = TennisGame4.SCORES[self.serverScore] + "-All"
        elif self.serverHasWon():
            result = "Win for " + self.server
        elif self.receiverHasWon():
            result = "Win for " + self.receiver
        elif self.serverHasAdvantage():
            result = "Advantage " + self.server
        elif self.receiverHasAdvantage():
            result = "Advantage " + self.receiver
        else:
            result = "-".join(
                [
                    TennisGame4.SCORES[self.serverScore],
                    TennisGame4.SCORES[self.receiverScore],
                ]
            )

        return result

    def receiverHasAdvantage(self):
        return self.receiverScore >= 4 and (self.receiverScore - self.serverScore) == 1

    def serverHasAdvantage(self):
        return self.serverScore >= 4 and (self.serverScore - self.receiverScore) == 1

    def receiverHasWon(self):
        return self.receiverScore >= 4 and (self.receiverScore - self.serverScore) >= 2

    def serverHasWon(self):
        return self.serverScore >= 4 and (self.serverScore - self.receiverScore) >= 2

    def isTie(self):
        return self.serverScore == self.receiverScore

    def isDeuce(self):
        return self.serverScore >= 3 and self.receiverScore >= 3 and self.isTie()
