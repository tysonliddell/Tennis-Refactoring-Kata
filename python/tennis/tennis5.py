# -*- coding: utf-8 -*-


class TennisGame5:
    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]
    WIN_MESSAGE = "Win for {player}"
    ADVANTAGE_MESSAGE = "Advantage {player}"
    DEUCE_MESSAGE = "Deuce"
    TIE_MESSAGE = "{score}-All"
    SCORE_LOOKUP = {
        (0, 0): TIE_MESSAGE.format(score=SCORES[0]),
        (0, 1): f"{SCORES[0]}-{SCORES[1]}",
        (0, 2): f"{SCORES[0]}-{SCORES[2]}",
        (0, 3): f"{SCORES[0]}-{SCORES[3]}",
        (0, 4): WIN_MESSAGE.format(player="player2"),
        (1, 0): f"{SCORES[1]}-{SCORES[0]}",
        (1, 1): TIE_MESSAGE.format(score=SCORES[1]),
        (1, 2): f"{SCORES[1]}-{SCORES[2]}",
        (1, 3): f"{SCORES[1]}-{SCORES[3]}",
        (1, 4): WIN_MESSAGE.format(player="player2"),
        (2, 0): f"{SCORES[2]}-{SCORES[0]}",
        (2, 1): f"{SCORES[2]}-{SCORES[1]}",
        (2, 2): TIE_MESSAGE.format(score=SCORES[2]),
        (2, 3): f"{SCORES[2]}-{SCORES[3]}",
        (2, 4): WIN_MESSAGE.format(player="player2"),
        (3, 0): f"{SCORES[3]}-{SCORES[0]}",
        (3, 1): f"{SCORES[3]}-{SCORES[1]}",
        (3, 2): f"{SCORES[3]}-{SCORES[2]}",
        (3, 3): DEUCE_MESSAGE,
        (3, 4): ADVANTAGE_MESSAGE.format(player="player2"),
        (4, 0): WIN_MESSAGE.format(player="player1"),
        (4, 1): WIN_MESSAGE.format(player="player1"),
        (4, 2): WIN_MESSAGE.format(player="player1"),
        (4, 3): ADVANTAGE_MESSAGE.format(player="player1"),
        (4, 4): DEUCE_MESSAGE,
    }

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0

    def won_point(self, playerName):
        if playerName == "player1":
            self.player1Score += 1
        elif playerName == "player2":
            self.player2Score += 1
        else:
            raise ValueError("Invalid player name.")

    def score(self):
        p1 = self.player1Score
        p2 = self.player2Score

        # normalise scores
        while p1 > 4 or p2 > 4:
            p1 -= 1
            p2 -= 1

        table_entry = (p1, p2)
        if table_entry in TennisGame5.SCORE_LOOKUP:
            return TennisGame5.SCORE_LOOKUP[table_entry]
        else:
            raise ValueError("Invalid score.")
