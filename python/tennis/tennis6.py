# -*- coding: utf-8 -*-


class TennisGame6:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0

    def won_point(self, playerName):
        if playerName == "player1":
            self.player1Score += 1
        else:
            self.player2Score += 1

    def _is_end_game(self):
        return self.player1Score >= 4 or self.player2Score >= 4

    def score(self):
        def regular_score_name(score: int) -> str:
            match (score):
                case 0:
                    return "Love"
                case 1:
                    return "Fifteen"
                case 2:
                    return "Thirty"
                case _:
                    return "Forty"

        def tie_score() -> str:
            if self.player1Score < 3:
                return f"{regular_score_name(self.player1Score)}-All"
            else:
                return "Deuce"

        def end_game_score():
            if self.player1Score > self.player2Score:
                leading_player = self.player1Name
            else:
                leading_player = self.player2Name

            if abs(self.player1Score - self.player2Score) == 1:
                return "Advantage " + leading_player
            else:
                return "Win for " + leading_player

        def regular_score():
            score1 = regular_score_name(self.player1Score)
            score2 = regular_score_name(self.player2Score)
            return score1 + "-" + score2

        if self.player1Score == self.player2Score:
            scoreString = tie_score()
        elif self._is_end_game():
            scoreString = end_game_score()
        else:
            scoreString = regular_score()

        return scoreString
