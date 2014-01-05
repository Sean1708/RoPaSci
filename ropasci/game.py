import sys

from ropasci.player import Player, Computer


class Game:

    def __init__(self, mode="pvc"):
        self.mode = mode
        
        self.players = []

        self.plays = {
                "rock": "scissors",
                "paper": "rock",
                "scissors": "paper"
        }

    def setup_players(self):
        if self.players: return None

        name = input("Enter Player1's name: ")
        player1 = Player(self, name)
        self.players.append(player1)

        if self.mode == "pvc":
            player2 = Computer(self, "Clive the Computer")
        else:
            name = input("Enter Player2's name: ")
            player2 = Player(self, name)

        self.players.append(player2)

    def play(self):
        player1 = self.players[0]
        player2 = self.players[1]
        player1.wins = 0
        player2.wins = 0
        rounds = 0

        while True:
            rounds += 1

            print("\n\tRound {0}!".format(rounds))

            player1.choose()
            player2.choose()

            print()
            print("{0} chose {1}.".format(player1.name, player1.choices[-1]))
            print("{0} chose {1}.".format(player2.name, player2.choices[-1]))

            if self.plays[player1.choices[-1]] == player2.choices[-1]:
                print("{0} won round {1}!".format(player1.name, rounds))
                player1.wins += 1
            elif self.plays[player2.choices[-1]] == player1.choices[-1]:
                print("{0} won round {1}!".format(player2.name, rounds))
                player2.wins += 1
            else:
                print("Round {0} was a draw.".format(rounds))

            if player1.wins >= 2:
                print("\n{0} won the game!".format(player1.name))
                break
            elif player2.wins >=2:
                print("\n{0} won the game!".format(player2.name))
                break


class Engine:

    def __init__(self):
        self.commands = {
                "play": "start a new game",
                "help": "view an explanation of each command",
                "exit": "take a wild guess",
                "quit": "see exit"
        }
        
    def start(self, message=None):
        print("\n\tRoPaSci", end="\n\n")

        if message is None: message = """Welcome to RoPaSci, the interactive Rock, Paper, Scissors
game with customisable game modes and tournament play.

To play a game type "play" into the interactive prompt and
select the game mode.
"""
        
        print(message)

        self.run_input_loop()

    def run_input_loop(self):
        while True:
            command = input("> ").lower()

            if command == "play":
                self.play_game()
            elif command == "help":
                self.print_help()
            elif command in ("exit", "quit"):
                self.exit()
            else:
                print("ERROR: That is not a valid command.")
                self.print_help()

    def play_game(self, game=None):
        if game is None: game = Game()

        print("Choose game mode:")
        print("\t[0] Exit to main menu")
        print("\t[1] Player vs Player")
        print("\t[2] Player vs Computer")
        print("\t[3] Tournament")

        while True:
            mode = input(">> ")

            if mode == "0":
                return None
            elif mode == "1":
                game.mode = "pvp"
                break
            elif mode == "2":
                game.mode = "pvc"
                break
            elif mode == "3":
                game.mode = "tourney"
                break
            else:
                print("Not a valid mode. Choose again.")

        game.setup_players()
        game.play()

        while True:
            again = input("Would you like to play again? ")[0].lower()

            if again == 'y':
                game.play()
            elif again == 'n':
                break
            else:
                print("Please enter [y]es or [n]o: ", end='')

    def print_help(self):
        print("Available commands:")
        for k,v in self.commands.items():
            string = "\t{0:<6}  -  {1}".format(k, v)
            print(string)

    def exit(self):
        sys.exit("Goodbye!")


if __name__ == "__main__":
    GAME = Engine()
    GAME.start()
