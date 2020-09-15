import random

def createDeck():
    deck = []
    suits = ["♠","♥","♦","♣"]
    for suit in suits:
        for cardNumber in range(2,15):
            deck.append(str(cardNumber) + suit)
    return deck

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

def higherOrLower(thisCard, previousCard):
    thisCardNumber = int(thisCard[:-1])
    previousCardNumber = int(previousCard[:-1])
    if thisCardNumber > previousCardNumber:
        return "H"
    elif previousCardNumber > thisCardNumber:
        return "L"
    return "S"

def printCardNumber(card):
    thisCardNumber = int(card[:-1])
    suit = card[-1]
    faceCards = ["J","Q","K","A"]
    if thisCardNumber > 10:
        return str(faceCards[thisCardNumber-11]) + suit 
    return card

### Script starts here

deck = createDeck()
shuffledDeck = shuffleDeck(deck)

previousCard = None
winningStreak = 0
for thisCard in shuffledDeck:
    if previousCard == None:
        print("First card is: " + printCardNumber(thisCard))
    else:
        actualHigherLower = higherOrLower(thisCard, previousCard)
        if nextCardPrediction == actualHigherLower:
            print(printCardNumber(thisCard) + " = correct!")
            winningStreak += 1
        else:
            print(printCardNumber(thisCard) + " = WRONG!")
            print("Game over - you got " + str(winningStreak) + " in a row!")
            exit()
        
    nextCardPrediction = input("Higher or Lower? (H or L?)")
    print(nextCardPrediction)
    previousCard = thisCard

print("You got every card right! You are a genius!")

#todo validate input is H or L
#todo convert magic numbers/letters to constants
#todo make script 'exit' more elegantly
#todo change how the initial shuffle works
