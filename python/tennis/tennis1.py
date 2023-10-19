# -*- coding: utf-8 -*-

SCORE_FROM_POINTS_VALUE = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}
TIE_SCORE_FROM_POINTS_VALUE = {
    0: f"{SCORE_FROM_POINTS_VALUE[0]}-All",
    1: f"{SCORE_FROM_POINTS_VALUE[1]}-All",
    2: f"{SCORE_FROM_POINTS_VALUE[2]}-All",
}
DEUCE_SCORE = "Deuce"
PLAYER1_ADVANTAGE_SCORE = "Advantage player1"
PLAYER2_ADVANTAGE_SCORE = "Advantage player2"
PLAYER1_WIN_SCORE = "Win for player1"
PLAYER2_WIN_SCORE = "Win for player2"


class TennisGame1:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Points = 0
        self.player2Points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.player1Points += 1
        else:
            self.player2Points += 1

    def _is_early_game(self) -> bool:
        return self.player1Points < 4 and self.player2Points < 4

    def score(self):
        if self.player1Points == self.player2Points:
            result = TIE_SCORE_FROM_POINTS_VALUE.get(self.player1Points, DEUCE_SCORE)
        elif self._is_early_game():
            result = "-".join(
                [
                    SCORE_FROM_POINTS_VALUE[self.player1Points],
                    SCORE_FROM_POINTS_VALUE[self.player2Points],
                ]
            )
        else:
            minusResult = self.player1Points - self.player2Points
            if minusResult == 1:
                result = PLAYER1_ADVANTAGE_SCORE
            elif minusResult == -1:
                result = PLAYER2_ADVANTAGE_SCORE
            elif minusResult >= 2:
                result = PLAYER1_WIN_SCORE
            else:
                result = PLAYER2_WIN_SCORE
        return result
