import random
import time

### TODO - Refactor GetDrawNumbers (add timers)
### TODO - Refactor CheckNumbers

def GetDrawNumbers():
    drawNumbers = []
    for i in range(6):
        x = None
        while (x == None or x in drawNumbers):
            x = random.randint(1,49)
        drawNumbers.append(x)
    return drawNumbers

def CheckNumbers(myTicket, actualNumbers):
    numbersMatched = 0
    for number in myTicket:
        if number in actualNumbers:
            numbersMatched += 1
    return numbersMatched

### Script starts here

startTime = time.perf_counter()

myNumbers = [4, 8, 15, 16, 23, 42]

for draw in range(100000000):
    drawNumber = draw + 1
    thisWeeksDraw = GetDrawNumbers()
    numbersMatched = CheckNumbers(myNumbers, thisWeeksDraw)
    ## print("Week " + str(drawNumber) + " numbers : " + str(thisWeeksDraw) + " (" + str(numbersMatched) + " matched)") 
    if numbersMatched == 6 :
        print("Week " + str(drawNumber) + " numbers : " + str(thisWeeksDraw) + " (" + str(numbersMatched) + " matched)") 
        
endTime = time.perf_counter()
elapsedTime = endTime - startTime

print("Completed in " + str(elapsedTime) + " seconds!")
