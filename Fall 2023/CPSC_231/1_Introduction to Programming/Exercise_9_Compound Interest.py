INTPERYEAR = 1.04
    
moneyDeposited = int(input("Amount Money Deposited: "))

firstYear = float(format(moneyDeposited * INTPERYEAR, ".2f"))
secYear = float(format(firstYear * INTPERYEAR, ".2f"))
thirdYear = float(format(secYear * INTPERYEAR, ".2f"))

print(f'First Year Interest {firstYear}, \nSecond Year Interest {secYear}, \nand Third Year Interest {thirdYear}')