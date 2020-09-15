import random

HIGHER = "H"
LOWER = "L"
SAME = "S"
YES = "Y"
NO = "N"

def createDeck():
    deck = []
    for suit in ["♠","♥","♦","♣"]:
        for cardNumber in range(2,15):
            deck.append(str(cardNumber) + suit)
    random.shuffle(deck)
    return deck

def higherOrLower(thisCard, previousCard):
    thisCardNumber = int(thisCard[:-1])
    previousCardNumber = int(previousCard[:-1])
    if thisCardNumber > previousCardNumber:
        return HIGHER
    elif previousCardNumber > thisCardNumber:
        return LOWER
    return SAME

def printCardNumber(card):
    faceCards = ["J","Q","K","A"]
    thisCardNumber = int(card[:-1])
    if thisCardNumber > 10:
        return str(faceCards[thisCardNumber-11]) + card[-1] 
    return card

def getNextCardPrediction():
    nextCard = ""
    while nextCard.upper() not in [HIGHER,LOWER]:
        nextCard = input("Higher or Lower? (H or L?)")
    return nextCard

def wasUserCorrect(thisCard, previousCard, userPrediction):
    actualHigherLower = higherOrLower(thisCard, previousCard)
    if userPrediction.upper() == actualHigherLower:
        return True
    return False

def playGame():
    deck = createDeck()
    previousCard = None
    winningStreak = 0
    pickedCards = ""
    for thisCard in deck:
        if previousCard == None:
            pickedCards = printCardNumber(thisCard)
            print("First card is: " + pickedCards)
        else:
            pickedCards += " " + printCardNumber(thisCard)
            if wasUserCorrect(thisCard, previousCard, nextCardPrediction):
                print(pickedCards + " = correct!")
                winningStreak += 1
            else:
                print(pickedCards + " = WRONG!")
                break

        previousCard = thisCard
        nextCardPrediction = getNextCardPrediction()

    print("Game over - you got " + str(winningStreak) + " in a row!")

gameActive = YES
while gameActive.upper() == YES:
    playGame()
    gameActive = input("Play again? Y/N")
