# author: itzhik aviv
import random
import sys

NumberOfGames = 10
NumberOfDigits = 4
Number = 0
SecretNumber = 0
Zero = True
gameRounds_t = []
winner = 0
winner_avg = 0
avg_p1 = 0
avg_p2 = 0
p1_winner = 0
p2_winner = 0
draw_number = 0

class BH:

    def __createTable(self):
        """create the first table of options"""
        self.__L = []
        for x in range(10 ** (self.__numberOfDigits - 1),
                       10 ** self.__numberOfDigits):
            s1 = str(x)
            s2 = set(s1)
            if not Zero and "0" in s1:
                continue
            else:
                if len(s1) == len(s2):
                    self.__L.append(s1)
        # random.shuffle(self.__L)

    def __createTheNumber(self):
        """choose randomly number from the table (for start guessing"""
        self.__Number = random.choice(self.__L)
        self.__number = self.__Number


    def __createGuess(self):
        """create guess from the table """
        self.__guess = random.choice(self.__L)


    def __findBH(self):
        """check the NH AND NB status """
        self.__NH = 0
        self.__NB = 0
        for i in range(self.__numberOfDigits):
            c1 = self.__guess[i]
            j = self.__number.find(c1)
            if i == j:
                self.__NB += 1
            else:
                if j >= 0:
                    self.__NH += 1


    def __reduceTable(self):
        """reduce the table based on the BH status"""
        self.__L1 = []
        for self.__guess in self.__L:
            self.__findBH()
            if (self.__NB == self.__nb and \
                    self.__NH == self.__nh):
                self.__L1.append(self.__guess)
        self.__L.clear()
        self.__L = self.__L1.copy()
        # random.shuffle(self.__L)


    def __init__(self, number=0, numberOfDigits=4):
        """ the main func of the game"""
        this_game_tup = []
        self.__counter = 0
        try:
            if not isinstance(number, int) \
                    or number < 0:
                raise ValueError("number = " \
                                 + str(number) \
                                 + ": must be int (not string or float) and >= 0.")
            if not isinstance(numberOfDigits, int) \
                    or numberOfDigits <= 0 or numberOfDigits >= 9:
                raise ValueError("mumberOfDigits = " \
                                 + str(numberOfDigits)
                                 + ": must be int (not string or float) and > 0" \
                                 + " and <= 9.")
            if number == 0:
                self.__numberOfDigits = numberOfDigits
                self.__createTable()
                self.__createTheNumber()
            else:
                self.__Number = str(number)
                self.__number = self.__Number
                self.__numberOfDigits = len(self.__number)
                if not Zero and "0" in self.__Number:
                    raise ValueError(self.__number + \
                                     ": number must not include 0.")
                for c in self.__number:
                    if self.__number.count(c) > 1:
                        raise ValueError(self.__number + \
                                         ": every digit must appears only one time.")
                self.__createTable()
        except ValueError as e:
            print(e)
            return
        print("number: ", self.__number,
              " table size: ", len(self.__L))
        while True:
            self.__number = self.__Number
            self.__counter += 1
            self.__createGuess()
            self.__findBH()
            print("guess number ", self.__counter, \
                  " is: ", self.__guess, \
                  " table size: ", len(self.__L), \
                  " nb: ", self.__NB, " nh: ", self.__NH)
            global gameRounds_t
            t = (self.__counter, self.__guess, self.__NB, self.__NH, len(self.__L))
            # main.sendResult(t)
            this_game_tup.append(t)
            if self.__NB == self.__numberOfDigits:
                gameRounds_t.append(this_game_tup)
                # gameRounds_t.append(("0"))
                break
            else:
                # self.__L.remove(self.__guess)
                self.__number = self.__guess
                self.__nb = self.__NB
                self.__nh = self.__NH
                self.__reduceTable()
        print("number of tries: ", self.__counter)
        print(75 * "=", "\n")

    def getCounter(self):
        return self.__counter


def main():
    sys.stdout = open("bhOutput.txt", 'w')
    l = []
    for i in range(NumberOfGames):
        print("\ngame number ", str(i + 1))
        bh = BH(number=Number, numberOfDigits=NumberOfDigits)
        l.append(bh.getCounter())
    #   print("average number of guesses for ", \
    #         str(NumberOfGames), " games is: ", \
    #         sum(l)/len(l))
    total_p1 = 0
    total_p2 = 0
    games_per_player = NumberOfGames / 2
    global winner_avg
    global winner
    guess_p1_per_game =[]
    guess_p2_per_game =[]

    for gameindex in range(0, int(games_per_player)):
        guess_p1_per_game.insert(gameindex,l[gameindex])
        total_p1 = total_p1 + l[gameindex]

    for gameindex in range(int((games_per_player)), len(l)):
        guess_p2_per_game.insert(gameindex,l[gameindex])
        total_p2 = total_p2 + l[gameindex]

    winner_counter(guess_p1_per_game, guess_p2_per_game)
    global avg_p1
    avg_p1 = total_p1 / games_per_player
    avarageStr_p1 = "average number of guesses for ", \
                    str(games_per_player), \
                    "sum of guesses for p1 is: " + str(total_p1), \
                    "The avg is: " + str(avg_p1)

    global avg_p2
    avg_p2 = total_p2 / games_per_player
    avarageStr_p2 = "average number of guesses for ", \
                    str(NumberOfGames / 2), \
                    "sum of guesses for p2 is: " + str(total_p2), \
                    "The avg is: " + str(avg_p2)

    if avg_p2 == avg_p1:
        winner_avg = avg_p1
        winner = "draw"

    if avg_p2 < avg_p1:
        winner_avg = avg_p2
        winner = 2
    else:
        winner_avg = avg_p1
        winner = 1

    print("winner is " + str(winner) + " and the avg is: " + str(winner_avg))

    print(avarageStr_p1)
    print(avarageStr_p2)

    # print(avarageStr)
    sys.stdout.close()

def winner_counter(guess_p1_per_game,guess_p2_per_game):
    """
    A function that counts the number of wins and draws in a game.

    :params: List guess_p1_per_game a list of integers representing the guesses made by player 1 in each game.
        List guess_p2_per_game a list of integers representing the guesses made by player 2 in each game.
    """
    global p1_winner
    global p2_winner
    global draw_number
    p1_winner = 0
    p2_winner = 0
    draw_number = 0
    for index in range(len(guess_p1_per_game)):
        if guess_p1_per_game[index] > guess_p2_per_game[index]:
            p2_winner = p2_winner+1
        elif guess_p1_per_game[index] < guess_p2_per_game[index]:
            p1_winner = p1_winner+1
        elif guess_p1_per_game[index] == guess_p2_per_game[index]:
            draw_number = draw_number + 1



def startgamebh(user_digs, user_games):
    """
    Initializes the game with the given number of digits and games.

    :param: int user_digs The number of digits for the game.
        int user_games: The number of games to be played.
    """
    global NumberOfGames
    global NumberOfDigits
    NumberOfGames = int(user_games) * 2
    NumberOfDigits = user_digs
    global gameRounds_t
    gameRounds_t.clear()
    main()

# main()
