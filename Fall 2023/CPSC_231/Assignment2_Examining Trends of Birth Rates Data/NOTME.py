# Step 2: Data entry
data_points = []

# Ask the user how many data points they want to enter
num_data_points = int(input("How many data points do you want to enter? "))

if num_data_points <= 0:
    print("Must enter at least one data point.")
else:
    # Initialize variables to track the previous year and duplicate years
    prev_year = None
    seen_years = set()

    for i in range(num_data_points):
        # Ask the user to enter a year
        year = int(input("Enter year: "))

        if year <= 0:
            print("Invalid year.")
            break

        if prev_year is not None and year <= prev_year:
            print("Years must be entered in order.")
            break

        if year in seen_years:
            print("Same year entered twice.")
            break

        seen_years.add(year)
        prev_year = year

        # Ask the user to enter birth rate
        birth_rate = float(input(f"Enter Birth Rate for {year}: "))

        if birth_rate < 0:
            print("Invalid birth rate.")
            break

        data_points.append((year, birth_rate))

# Step 4: Data analysis
# Ask the user to enter the two years for analysis
start_year = int(input("Enter the start year for analysis: "))
end_year = int(input("Enter the end year for analysis: "))

# Error checking for step 4
if start_year not in [year for year, _ in data_points]:
    print("The start year does not exist.")
elif end_year not in [year for year, _ in data_points]:
    print("The end year does not exist.")
elif start_year >= end_year:
    print("End year must be after start year.")
else:
    # Calculate the average birth rate and trend
    data_in_range = [birth_rate for year, birth_rate in data_points if start_year <= year <= end_year]
    average_birth_rate = sum(data_in_range) / len(data_in_range)
    
    if average_birth_rate > data_points[-1][1]:
        trend = "There is an upward trend."
    elif average_birth_rate < data_points[0][1]:
        trend = "There is a downward trend."
    else:
        trend = "There is a sideways trend."

    # Output the result
    print(f"The average birth rate between {start_year} and {end_year} is: {average_birth_rate:.2f}")
    print(trend)