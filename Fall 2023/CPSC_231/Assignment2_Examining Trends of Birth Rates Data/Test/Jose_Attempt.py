counter_yr = 1
info_failed = False
info_approve = True
years = []
birth_rates = []
previous_year = 0

data_points = int(input("How many data points do you have?: "))

if data_points == 0:
    print("Must enter at least one data point.")
    info_failed = True

while data_points != 0 and info_approve:

    data_points -= 1
    if not info_failed:
        
        year_input = int(input("What is the year of data point %d?: " % counter_yr))
        years.append(year_input)

        if year_input <= 0:
            print("Invalid year.")
            info_failed = True

        elif counter_yr >= 2:
            
            if (year_input < previous_year):
                print("Years must be entered in order.")
                info_failed = True

            elif (previous_year == year_input):
                print("Same year entered twice.")
                info_failed = True
                
        if info_failed == False:
            birth_rate = float(input("What is the birth rate %d?: " % counter_yr))
            birth_rates.append(birth_rate)
            if birth_rate <= 0.0:
                print("Invalid birth rate.")
                info_failed = True

    counter_yr += 1
    previous_year = year_input

if info_failed == False and info_approve:
    start_year = int(input("Which year do you want to start with?: "))

    if start_year not in years:
        print("The start year does not exist.")
    else:
        end_year = int(input("Which year do you want to end with?: "))
        if end_year not in years:
            print("The end year does not exist.")
        elif end_year < start_year:
            print("End year must be after start year.")
        else:
            index_start_year = years.index(start_year)
            index_end_year = years.index(end_year)
            average_rate = (birth_rates[index_start_year] + birth_rates[index_end_year]) / 2
            average_rate = round(average_rate, 2)
            
            print("The average birth rate of these two years is {}.".format(average_rate))
            if birth_rates[index_start_year] < birth_rates[index_end_year]:
                print("There is an upward trend.")
            elif birth_rates[index_start_year] > birth_rates[index_end_year]:
                print("There is a downward trend.")
            elif birth_rates[index_start_year] == birth_rates[index_end_year]:
                print("There is a sideways trend.")