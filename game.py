from enum import Enum
from itertools import zip_longest


class Guess:
    def __init__(self, number, result):
        self.number = number
        self.result = result


class Player:
    def __init__(self, number: str):
        self.number = number
        self.guesses = []

    def guess(self, guess: Guess):
        self.guesses.append(guess)


class Turns(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2


class Result:
    def __init__(self):
        self.x = 0
        self.p = 0
        self.t = 0

    def __str__(self):
        statements = []
        if self.x:
            statements.append(f"{self.x}X")
        if self.p:
            statements.append(f"{self.p}P")
        if self.t:
            statements.append(f"{self.t}T")

        return ", ".join(statements)


class Game:
    def __init__(self, number_1: str, number_2: str):
        self.validate_input(number_1)
        self.validate_input(number_2)

        self.player_1 = Player(number_1)
        self.player_2 = Player(number_2)
        self.turn = Turns.PLAYER_1

    def evaluate_guess(self, number: str, target: str):
        """
        we need to use this O(n^2) (for + in) because
        we have to compare not only the intersection
        but their indexes.
        """
        result = Result()
        for i, n in enumerate(number):
            if n in target:
                if i == target.index(n):
                    result.x += 1
                else:
                    result.p += 1
            else:
                result.t += 1

        return result

    def pass_turn(self):
        self.turn = Turns.PLAYER_2 if self.turn == Turns.PLAYER_1 else Turns.PLAYER_1

    def is_ended(self, result: Result):
        return result.x == 4

    def validate_input(self, _input: str):
        assert len(set(_input)) == 4

    def guess(self, number: str):
        self.validate_input(number)

        player = self.player_1 if self.turn == Turns.PLAYER_1 else self.player_2
        opponent = self.player_2 if self.turn == Turns.PLAYER_1 else self.player_1

        result = self.evaluate_guess(number, opponent.number)

        player.guess(Guess(number, result))

        self.pass_turn()

        return self.is_ended(result), result

    def __str__(self):
        statement = "Player 1 | Player 2"

        for g1, g2 in zip_longest(self.player_1.guesses, self.player_2.guesses):
            statement += f"\nGuess: {g1.number} | "
            statement += g2.number if g2 else "-"
            statement += f"\nResult: {g1.result} | "
            statement += g2.result if g2 else "-"

        return statement
