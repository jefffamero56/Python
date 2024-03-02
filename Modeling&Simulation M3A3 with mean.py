import random
import statistics

losses = 20
betAgain = "Y"
totalOfDays = 0
triesCounter = 0
standardDeviationValues = []

for simCounter in range(50):
    print("\n\nSimulation #: ", simCounter + 1)
    money = 1000
    betCounter = 1
    days = 1
    while money >= 20:
        bet1 = random.randint(1, 40)
        bet2 = random.randint(1, 40)
        winningNumber1 = random.randint(1, 40)
        winningNumber2 = random.randint(1, 40)

        if (bet1 == winningNumber1 and bet2 == winningNumber2) or (bet1 == winningNumber2 and bet2 == winningNumber1):
            result = "Won"
            winnings = 2000
        else:
            result = "Loss"
            winnings = 0

        print("Bet #: ", "{:02d}".format(betCounter), "\tBet 1: ", "{:02d}".format(bet1), "\tBet2: ",
              "{:02d}".format(bet2), "\tWinning #1: ", "{:02d}".format(winningNumber1), "\tWinning #2: ",
              "{:02d}".format(winningNumber2), "\tResult: ", result, "\tLosses: ", losses, "\tWinnings: ", winnings,
              "\tMoney: ", money)
        betCounter += 1
        money += winnings - losses
    days = (betCounter - 1) / 3
    totalOfDays += days
    triesCounter += 1
    standardDeviationValues.append(days)

print("Mean: ", totalOfDays/50)
print("Standard Deviation: ", statistics.stdev(standardDeviationValues))