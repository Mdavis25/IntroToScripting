import random


# Card class assigns suit and value to the cards
class Card:
    def __init__(self, val, suit):
        self.__value = val
        self.__suit = suit

    def getVal(self):
        return self.__value

    def getSuit(self):
        return self.__suit

    # Returns the names of the special cards
    def __str__(self):
        tempVal = str(self.getVal())
        if tempVal == "1":
            tempVal = "Ace"
        elif tempVal == "11":
            tempVal = "Jack"
        elif tempVal == "12":
            tempVal = "Queen"
        elif tempVal == "13":
            tempVal = "King"
        tempStr = tempVal + " of " + self.getSuit()
        return tempStr


# Array to hold deck
defaultDeck = []
for i in range(0, 4):
    tempSuit = ""
    if i == 0:
        tempSuit = "Clubs"
    elif i == 1:
        tempSuit = "Hearts"
    elif i == 2:
        tempSuit = "Spades"
    else:
        tempSuit = "Diamonds"
    for j in range(1, 14):
        tempCard = Card(j, tempSuit)
        defaultDeck.append(tempCard)


# The shoe shuffling 8 decks together
class Shoe:
    def __init__(self):
        self.__cards = []
        for num in range(0, 8):
            tempDeck = defaultDeck
            random.shuffle(tempDeck)
            self.__cards = self.__cards + tempDeck
        random.shuffle(self.__cards)

    # gets the top card of the deck
    def popShoe(self):
        return self.__cards.pop()


class Player:
    # play functions that will hold all the objects of the player
    def __init__(self):
        self.__currentBet = None
        self.__blackJackFlag = None
        self.__bustFlag = None
        self.__standFlag = None
        self.__score = None
        self.__playerCards = None
        self.__dropFlag = False
        self.__zeroCounter = 0
        self.reset()
        self.__balance = random.randint(500, 5000)

    # resets all the players cards and bets
    def reset(self):
        self.__playerCards = []
        self.__score = 0
        self.__standFlag = False
        self.__bustFlag = False
        self.__blackJackFlag = False
        self.__currentBet = 0

    def addCard(self, newCard, round):
        global choice
        self.__playerCards.append(newCard)
        # allows the player to choose the ace value
        if round > 1:
            if newCard.getVal() == 1:
                # input validation
                validInput = False
                while not validInput:
                    choice = input("Enter 1 or 11 for value of the ace card: ")
                    if choice.isnumeric():
                        choice = int(choice)
                        if choice == 1 or choice == 11:
                            validInput = True
                        else:
                            print("Invalid Input")
                            print("Please enter either 1 or 11")
                    else:
                        print("Invalid Input")
                        print("Please enter either 1 or 11")

                if choice == 1:
                    self.__score += 1
                elif choice == 11:
                    self.__score += 11
            else:
                # If the card is 10, jack, queen or king then 10 is added to score
                if newCard.getVal() > 9:
                    self.__score += 10
                # adds card if 2-9
                else:
                    self.__score += newCard.getVal()
        else:
            # corrects player score to 11 instead of 22 if player is delt 2 aces
            if newCard.getVal() == 1:
                self.__score += 11
                if self.__score == 22:  # Two aces
                    self.__score -= 10
            # adds 10 if jack queen and king or 10
            elif newCard.getVal() > 9:
                self.__score += 10
            # adds 2-9
            else:
                self.__score += newCard.getVal()

    # Prints player cards
    def displayCards(self):
        for card in self.__playerCards:
            print(card)

    # counter to drop player if they bet 0 three times
    def placeBet(self, bet):
        if bet == 0:
            self.__zeroCounter += 1
            if self.__zeroCounter == 3:
                self.drop()
        self.__currentBet = bet

    # multiplies bet by 2
    def doubleDown(self):
        self.__currentBet *= 2
        self.stand()

    # subtracts bet value from balance
    def lostBet(self):
        self.__balance -= self.getBet()

    # adds 2:1 pay back if user wins
    def regularWin(self):
        self.__balance += self.getBet()

    # adds 3:1 pay back if user wins by blackjack
    def blackJack(self):
        self.__blackJackFlag = True
        self.__balance += 2 * self.getBet()

    def getScore(self):
        return self.__score

    def hasStand(self):
        return self.__standFlag

    def stand(self):
        self.__standFlag = True

    def hasBust(self):
        return self.__bustFlag

    # calls lostBet function if the player loses
    def busts(self):
        self.__bustFlag = True
        self.lostBet()

    def hasBlackJack(self):
        return self.__blackJackFlag

    def getBalance(self):
        return self.__balance

    def getBet(self):
        return self.__currentBet

    def drop(self):
        self.__dropFlag = True

    def isDropped(self):
        return self.__dropFlag


class Dealer:
    # Get cards for the shoe
    def __init__(self):
        self.__bustFlag = None
        self.__score = None
        self.__dealerCards = None
        self.reset()
        self.__gameDeck = Shoe()

    # resets dealers cards score and flag
    def reset(self):
        self.__dealerCards = []
        self.__score = 0
        self.__bustFlag = False

    # returns a card object from the shoe
    def dealCard(self):
        return self.__gameDeck.popShoe()

    # dealer deals himself a card from shoe
    def dealSelf(self):
        newCard = self.dealCard()
        self.__dealerCards.append(newCard)
        # adds ace value and corrects if score is > 11
        if newCard.getVal() == 1:
            if self.getScore() < 11:
                self.__score += 11
            else:
                self.__score += 1
        # If card is 10, jack, queen or king add 10 to score, otherwise add 2-9 value cards to score
        else:
            if newCard.getVal() > 9:
                self.__score += 10
            else:
                self.__score += newCard.getVal()

    def getScore(self):
        return self.__score

    # Displays the dealer cards
    def displayCards(self):
        for card in self.__dealerCards:
            print(card)

    def busts(self):
        self.__bustFlag = True

    def hasBust(self):
        return self.__bustFlag


if __name__ == '__main__':
    gameDealer = Dealer()
    playerArr = []

    # adds a random number of players to table 1-6
    randomPlayers = random.randint(1, 6)
    print("There are currently", randomPlayers, "Players")
    for index in range(0, randomPlayers):
        playerArr.append(Player())
        print("Player", index + 1, "starting balance is: $", playerArr[index].getBalance())
    print()

    # adds number of games between 10-16
    totalGames = random.randint(10, 16)
    print("There will be", totalGames, "rounds of Black Jack")
    for currentGame in range(0, totalGames):
        print("---------------------------------------------------------")
        print("Game", currentGame + 1, "\n")
        # Game starts

        if currentGame > 0:
            for index in range(0, randomPlayers):
                print("Player", index + 1, "balance is: $", playerArr[index].getBalance())
            print()

        round = 1
        # Starting bets, only players who haven't been dropped from all games can place bets
        for playerIn in range(0, len(playerArr)):
            if not playerArr[playerIn].isDropped():
                # input validation, players can only bet 0 to sit out, or 25 to their balance minus one (no
                # all in bets)
                validInput = False
                while not validInput:
                    print("Player", playerIn + 1, "please place your bet: ")
                    tempBet = input()
                    if tempBet.isnumeric():
                        tempBet = int(tempBet)
                        playerArr[playerIn].placeBet(tempBet)
                        if tempBet == 0 or 25 <= tempBet < playerArr[playerIn].getBalance():
                            validInput = True
                        else:
                            print("Invalid Input")
                            print("Please enter either 0 to sit out for the game or a number between 25 and",
                                  playerArr[playerIn].getBalance())
                    else:
                        print("Invalid Input")
                        print("Please enter either 0 to sit out for the game or a number between 25 and",
                              playerArr[playerIn].getBalance())
                # playerArr[playerIn].placeBet(tempBet)
                print("Player", playerIn + 1, "starting bet is: $", tempBet)
                print()

        # Displaying players who are dropped
        for playerIn in range(0, len(playerArr)):
            if playerArr[playerIn].isDropped() == True and playerArr[playerIn].getBalance() < 50:
                print("Player", playerIn + 1, "dropped from all future games since balance is less than 50")
            elif playerArr[playerIn].isDropped() == True and playerArr[playerIn].getBet() == 0:
                print("Player", playerIn + 1, "dropped from all future games due to three bets of zero")
            elif playerArr[playerIn].getBet() == 0:
                print("Player", playerIn + 1, "not in game since bet is zero")
        print()

        # First round, players are dealt one card, then the dealer
        for playerIn in range(0, len(playerArr)):
            if playerArr[playerIn].getBet() != 0 and playerArr[playerIn].isDropped() == False:
                playerArr[playerIn].addCard(gameDealer.dealCard(), round)

        gameDealer.dealSelf()

        # Players are dealt second cards
        for playerIn in range(0, len(playerArr)):
            if playerArr[playerIn].getBet() != 0 and playerArr[playerIn].isDropped() == False:
                print("Player", playerIn + 1, "Cards:")
                playerArr[playerIn].addCard(gameDealer.dealCard(), round)
                playerArr[playerIn].displayCards()
                print("Score:", playerArr[playerIn].getScore())
                print()
                if playerArr[playerIn].getScore() == 21:
                    playerArr[playerIn].blackJack()

        # Dealer deals himself his second card and his cards are displayed
        gameDealer.dealSelf()
        print("Dealer Cards:")
        # dealers score is also displayed
        gameDealer.displayCards()
        print("Dealer Score:", gameDealer.getScore(), "\n")

        # Player Rounds
        for playerIn in range(0, len(playerArr)):
            round = 2
            # If players bet is zero, or they've been dropped for balance less than 50 or they have blackjack,
            # skip their turn in this game
            if \
                    playerArr[playerIn].getBet() == 0 or playerArr[playerIn].isDropped() == True or playerArr[
                        playerIn].hasBlackJack() == True:
                if playerArr[playerIn].hasBlackJack():
                    print("Player", playerIn + 1, "has BlackJack, turn skipped")
                continue
            else:
                print("Player", playerIn + 1, "turn")
                print("----------------")

                if playerArr[playerIn].getBet() != 0 and playerArr[playerIn].isDropped() == False:
                    print("Player", playerIn + 1, "Cards:")
                    playerArr[playerIn].displayCards()
                    print("Score:", playerArr[playerIn].getScore())
                    print()

            # While player has not stood, bust, or gotten blackjack, continue to play
            while playerArr[playerIn].hasStand() == False and playerArr[playerIn].hasBust() == False and playerArr[
                playerIn].hasBlackJack() == False:
                # Only in round two can player double down, split not implemented
                if round == 2:
                    # input validation, user can only enter 1, 2 or 3
                    validInput = False
                    while not validInput:
                        print("Options Available: 1 Hit, 2 Double Down, 3 Stand")
                        userChoice = input("Enter option: ")
                        if userChoice.isnumeric():
                            userChoice = int(userChoice)
                            if userChoice == 1 or userChoice == 2 or userChoice == 3:
                                validInput = True
                            else:
                                print("Invalid Input")
                                print("Please enter either 1, 2, or 3")
                        else:
                            print("Invalid Input")
                            print("Please enter either 1, 2, or 3")

                    # If player chooses 1, deal a card, add to player, display it as well as players new score
                    if (userChoice == 1):
                        tempCard = gameDealer.dealCard()
                        playerArr[playerIn].addCard(tempCard, round)
                        print("Added Card:", tempCard, "\nUpdated Score:", playerArr[playerIn].getScore())
                    # checks player balance if player tries to double down
                    elif userChoice == 2:
                        if playerArr[playerIn].getBet() * 2 > playerArr[playerIn].getBalance():
                            print("Player does not have enough in balance to double down")
                        # adds card and bet if they have enough balance
                        else:
                            playerArr[playerIn].doubleDown()
                            tempCard = gameDealer.dealCard()
                            playerArr[playerIn].addCard(tempCard, round)
                            print("Added Card:", tempCard, "\nUpdated Score:", playerArr[playerIn].getScore(),
                                  "\nUpdated Bet:$", playerArr[playerIn].getBet())
                    # player stands and sets the flag to true
                    elif userChoice == 3:
                        playerArr[playerIn].stand()
                else:
                    # input validation, user can only enter 1 or 2 to hit or stand
                    validInput = False
                    while not validInput:
                        print("Options Available: 1 Hit or 2 Stand")
                        userChoice = input("Enter option: ")
                        if userChoice.isnumeric():
                            userChoice = int(userChoice)
                            if userChoice == 1 or userChoice == 2:
                                validInput = True
                            else:
                                print("Invalid Input")
                                print("Please enter either 1 or 2")
                        else:
                            print("Invalid Input")
                            print("Please enter either 1 or 2")

                    # If player chooses 1, deal a card, add to player, display it as well as players new score
                    if userChoice == 1:
                        tempCard = gameDealer.dealCard()
                        playerArr[playerIn].addCard(tempCard, round)
                        print("Added Card:", tempCard, "\nUpdated Score:", playerArr[playerIn].getScore())
                    # player stands and sets the flag to true
                    elif userChoice == 2:
                        playerArr[playerIn].stand()

                # If player gets blackjack the blackjack flag is set to true, win info displayed later
                if playerArr[playerIn].getScore() == 21:
                    playerArr[playerIn].blackJack()
                # If player busts during game, prompt displayed, busts decreases balance and sets flag to True,
                # new balance displayed
                elif playerArr[playerIn].getScore() > 21:
                    playerArr[playerIn].busts()
                    print("Player busts! Updated Balance: $", playerArr[playerIn].getBalance())
                # If player stands, prompt displayed
                elif playerArr[playerIn].hasStand():
                    print("Player stands, wait for dealer to play")
                print()
                round += 1
        print()

        # Dealer deals himself a card until he hits 17 or higher
        while gameDealer.getScore() < 17:
            gameDealer.dealSelf()
        # Updated cards displayer
        print("Updated Dealer Cards:")
        gameDealer.displayCards()
        print("Updated Dealer Score:", gameDealer.getScore())
        # If dealer busts then prompt is displayed and flag is set to true
        if gameDealer.getScore() > 21:
            print("Dealer busts!")
            gameDealer.busts()
        print()

        # If dealer busts then every player that hasn't busted during the game wins
        if gameDealer.hasBust():
            for playerIn in range(0, len(playerArr)):
                if \
                        playerArr[playerIn].hasBust() == False and playerArr[playerIn].getBet() != 0 and playerArr[
                            playerIn].isDropped() == False:
                    if playerArr[playerIn].hasBlackJack():
                        print("Player", playerIn + 1, "wins by Black Jack! Updated Balance: $",
                              playerArr[playerIn].getBalance())
                    else:
                        playerArr[playerIn].regularWin()
                        print("Player", playerIn + 1, "has won! Updated Balance: $", playerArr[playerIn].getBalance())
        # If dealer is between 17 and 21, blackjack winners are displayed, players above score of dealer get regular
        # win 2:1 payout. Players with score below dealers lose their bet
        else:
            for playerIn in range(0, len(playerArr)):
                if \
                        playerArr[playerIn].hasBust() == False and playerArr[playerIn].getBet() != 0 and playerArr[
                            playerIn].isDropped() == False:
                    if playerArr[playerIn].hasBlackJack():
                        print("Player", playerIn + 1, "wins by Black Jack! Updated Balance: $",
                              playerArr[playerIn].getBalance())
                    elif playerArr[playerIn].getScore() > gameDealer.getScore():
                        playerArr[playerIn].regularWin()
                        print("Player", playerIn + 1, "wins! Updated Balance: $", playerArr[playerIn].getBalance())
                    else:
                        playerArr[playerIn].lostBet()
                        print("Player", playerIn + 1, "loses to dealer. Updated Balance: $",
                              playerArr[playerIn].getBalance())
        print()

        # Check to see if players balance is below 50, if they are then set drop flag to true and prompt
        for playerIn in range(0, len(playerArr)):
            if playerArr[playerIn].isDropped() == False and playerArr[playerIn].getBalance() < 50:
                print("Player", playerIn + 1, "has been dropped since balance is less than 50")
                playerArr[playerIn].drop()
        print()

        # Resetting players and dealer
        for player in playerArr:
            player.reset()
        gameDealer.reset()
