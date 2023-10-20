Years = [] 
birthRates = []

dataPoints = int(input("How many data points do you have? "))

inputYears = 0 
infoPassed = True
infoFailed = True

if dataPoints <= 0: 

    print("Must enter at least one data point.")

for i in range(dataPoints): 

    if infoFailed: 

        prevYear = inputYears
        i = str(i + 1)

        inputYears = int(input(f"What is the year of data point {i}?"))

        if inputYears in Years: 

            print("Same year entered twice.")
            infoFailed = False

        else: 

            if inputYears <= 0: 

                print("Invalid year.")
                infoFailed = False

            else: 

                if prevYear > inputYears:

                    print("Years must be entered in order. ")
                    infoFailed = False

                else: 

                    Years.append(inputYears)

                    inputRates = float(input(f"What is the birth rate of data point {i}?"))

                    if inputRates < 0.0:

                        print("Invalid birth rate.")
                        infoFailed = False

                    else: 

                        birthRates.append(inputRates)
                        infoPassed = False

if infoFailed and not infoPassed:

    startYear = int(input("Which year would you like to start with?"))

    if startYear not in Years: 

        print("The start year does not exist.")

    else: 

        endYear = int(input("Which year would you like to end with?"))

        if endYear not in Years: 

            print("The end year does not exist.")

        elif endYear < startYear: 

            print("End year must be after start year.")

        else: 

            startIndex = birthRates[Years.index(startYear)]
            endIndex = birthRates[Years.index(endYear)]

            averRate = (startIndex + endIndex) / 2

            averRate = format(averRate, ".2f")
            print(f"The average birth rate of these two years is {averRate}.")

            if startIndex < endIndex:

                print("There is an upward trend.")

            elif startIndex > endIndex:

                print("There is a downward trend.")

            elif startIndex == endIndex:

                print("There is a sideways trend.")