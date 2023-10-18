# -*- coding: utf-8 -*-

from dataclasses import dataclass

PLAYER1_NAME = "player1"
BEFORE_DEUCE_SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]


@dataclass
class Player:
    name: str
    score: int


class TennisGame3:
    def __init__(self, player1Name: str, player2Name: str):
        self.player1 = Player(player1Name, 0)
        self.player2 = Player(player2Name, 0)

    def won_point(self, player_name: str):
        if player_name == PLAYER1_NAME:
            self.player1.score += 1
        else:
            self.player2.score += 1

    def has_deuce_been_scored(self) -> bool:
        return self.player1.score + self.player2.score >= 6

    def winning_player(self) -> Player:
        if self.player1.score > self.player2.score:
            return self.player1
        else:
            return self.player2

    def score(self) -> str:
        if self.has_deuce_been_scored():
            return self._after_deuce_score()
        else:
            return self._before_deuce_score()

    def _before_deuce_score(self) -> str:
        """Get the score, when deuce has been scored."""
        winning_player = self.winning_player()
        if winning_player.score == 4:
            return "Win for " + winning_player.name
        else:
            named_score = BEFORE_DEUCE_SCORE_NAMES[self.player1.score]
            if self.player1.score == self.player2.score:
                return named_score + "-All"
            else:
                return named_score + "-" + BEFORE_DEUCE_SCORE_NAMES[self.player2.score]

    def _after_deuce_score(self) -> str:
        """Get the score, when deuce has not been scored."""
        winning_player = self.winning_player()
        if self.player1.score == self.player2.score:
            return "Deuce"  # 40-All
        elif abs(self.player1.score - self.player2.score) == 1:
            return "Advantage " + winning_player.name
        else:
            return "Win for " + winning_player.name
