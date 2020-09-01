import random
import time

contestants = [["Neil",[4,8,15,16,23,42]],["Jim",[1,2,3,4,5,6]],["Bob",[10,20,30,31,43,44]]]

def GetDrawNumbers():
    return random.sample(range(1,49),6)

def CheckNumbers(myTicket, actualNumbers):
    return len([a for a in actualNumbers if a in myTicket])

for draw in range(10000000):
    thisWeeksDraw = GetDrawNumbers()
    for contestant in contestants:
        print(contestant[0] + " won the jackpot in week " + str(draw + 1)) if CheckNumbers(contestant[1], thisWeeksDraw) == 6 else None       
