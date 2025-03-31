'''
This is the simplest implementation of a game of tennis
'''

import unittest

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def winning_point(self):
        self.score += 1

    def score_display(self):
        if self.score == 0:
            return 0
        elif self.score == 1:
            return 15
        elif self.score == 2:
            return 30
        elif self.score == 3:
            return 40

    def __str__(self):
        return f'{self.name} score: {self.score}'

class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)

    def assign_point_to_player(self, player_name):
        if player_name == self.player1.name:
            self.player1.winning_point()
        elif player_name == self.player2.name:
            self.player2.winning_point()
        else:
            raise NameError(f"Player '{player_name}' is not a valid name")

    def get_score(self):
        if self.player1.score >= 3 and self.player2.score >= 3:
            if abs(self.player1.score - self.player2.score) >= 2:
                # Winning
                if self.player1.score > self.player2.score:
                    return "Player 1 wins"
                else:
                    return "Player 2 wins"
            elif abs(self.player1.score - self.player2.score) == 1:
                # First point after deuce 40-40
                if self.player1.score > self.player2.score:
                    return "Advantage Player 1"
                else:
                    return "Advantage Player 2"
            else: # 40-40
                return "Deuce"
        else:
            return f"{self.player1.score_display()}-{self.player2.score_display()}"

    def __str__(self):
        return self.get_score()


class TestTennisGame(unittest.TestCase):
    def test_tennis_game_score1(self):
        game = TennisGame("Roger","Rafael")
        game.assign_point_to_player("Roger")
        expected = "15-0"
        actual = game.__str__()
        self.assertEqual(expected, actual)

    def test_tennis_game_score2(self):
        game = TennisGame("Roger","Rafael")
        game.assign_point_to_player("Rafael")
        expected = "0-15"
        actual = game.__str__()
        self.assertEqual(expected, actual)

    def test_tennis_game_deuce(self):
        game = TennisGame("Roger","Rafael")
        game.assign_point_to_player("Roger")
        game.assign_point_to_player("Roger")
        game.assign_point_to_player("Rafael")
        game.assign_point_to_player("Rafael")
        game.assign_point_to_player("Roger")
        game.assign_point_to_player("Rafael")
        expected = "Deuce"
        actual = game.__str__()
        self.assertEqual(expected, actual)

    def test_tennis_game_advantage1(self):
        game = TennisGame("Roger","Rafael")
        game.assign_point_to_player("Roger")
        game.assign_point_to_player("Roger")
        game.assign_point_to_player("Rafael")
        game.assign_point_to_player("Rafael")
        game.assign_point_to_player("Roger")
        game.assign_point_to_player("Rafael")
        game.assign_point_to_player("Roger")
        expected = "Advantage Player 1"
        actual = game.__str__()
        self.assertEqual(expected, actual)

    def test_tennis_game_won2(self):
        game = TennisGame("Roger","Rafael")
        game.assign_point_to_player("Roger")
        game.assign_point_to_player("Roger")
        game.assign_point_to_player("Rafael")
        game.assign_point_to_player("Rafael")
        game.assign_point_to_player("Roger")
        game.assign_point_to_player("Rafael")
        game.assign_point_to_player("Rafael")
        game.assign_point_to_player("Rafael")
        expected = "Player 2 wins"
        actual = game.__str__()
        self.assertEqual(expected, actual)

    def test_tennis_game_wrong_player(self):
        game = TennisGame("Roger","Rafael")
        with self.assertRaises(NameError) as context:
            game.assign_point_to_player("Serena")
        self.assertEqual(str(context.exception), "Player 'Serena' is not a valid name")
