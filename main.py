from game import Game

if __name__ == "__main__":
    done = False
    n1 = input("Digite o número do player 1: ")
    n2 = input("Digite o número do player 2: ")
    game = Game(n1, n2)
    while not done:
        n = input(f"Digite a tentativa do player {game.turn.value}: ")
        done, result = game.guess(n)
        print(f"Resultado: {result}")

    print(game)
