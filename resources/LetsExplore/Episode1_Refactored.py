import random
import time

myNumbers = [4, 8, 15, 16, 23, 42]

def GetDrawNumbers():
    return random.sample(range(1,49),6)

def CheckNumbers(myTicket, actualNumbers):
    return len([a for a in actualNumbers if a in myTicket])

startTime = time.perf_counter()

for draw in range(20000000):
    thisWeeksDraw = GetDrawNumbers()
    numbersMatched = CheckNumbers(myNumbers, thisWeeksDraw)
    if numbersMatched > 5 :
        print("Week " + str(draw + 1) + " numbers : " + str(thisWeeksDraw) + " (" + str(numbersMatched) + " matched)") 
        
endTime = time.perf_counter()
print("Completed in " + str(endTime - startTime) + " seconds!")
