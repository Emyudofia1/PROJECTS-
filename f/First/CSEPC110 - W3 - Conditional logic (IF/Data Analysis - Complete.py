# Loading the dataset
with open('life-expectancy.csv') as world_data:
    next(world_data)
    # Create variables to keep track of lowest and highest life expectancies
    lowest_expectancy = float('inf')
    highest_expectancy = float('-inf')
    # Create variables to keep track of country with lowest and highest life expectancies
    lowest_country = ''
    highest_country = ''
    # Create variables to keep track of overall lowest and highest life expectancies
    overall_lowest_expectancy = float('inf')
    overall_highest_expectancy = float('-inf')

    overall_lowest_country = ''
    overall_highest_country = ''
    # Create variables to store user input
    year_input = int(input("Enter your year of interest: "))
    sum_expectancy = 0
    count = 0
    # This part loops through the data line by line
    for line in world_data:
        line = line.strip()
        parts = line.split(",")
        # This part will extract data from the line
        name_of_country = parts[0]
        code = parts[1]
        year = int(parts[2])
        expectancy = float(parts[3])
        
        if expectancy < lowest_expectancy:
            lowest_expectancy = expectancy
            lowest_country = name_of_country
        if expectancy > highest_expectancy:
            highest_expectancy = expectancy
            highest_country = name_of_country
        # Here the overall lowest and highest life expectancies will be updated as necessary
        if expectancy < overall_lowest_expectancy:
            overall_lowest_expectancy = expectancy
            overall_lowest_country = name_of_country
        if expectancy > overall_highest_expectancy:
            overall_highest_expectancy = expectancy
            overall_highest_country = name_of_country
        # This part checks if the user input matches year
        if year == year_input:
            sum_expectancy += expectancy
            count += 1
            # Here the lowest and highest life expectancies for the given year is updated
            if count == 1 or expectancy < min_expectancy_year:
                min_expectancy_year = expectancy
                min_country_year = name_of_country
            if count == 1 or expectancy > max_expectancy_year:
                max_expectancy_year = expectancy
                max_country_year = name_of_country
    # This line computes the average life expectancy for the given year
    avg_expectancy = sum_expectancy / count
    # Overall lowest and highest life expectancies is shown
    print("Overall Lowest Life Expectancy:")
    print("Year:", year, "| Country:", overall_lowest_country, "| Expectancy:", overall_lowest_expectancy)
    print("Overall Highest Life Expectancy:")
    print("Year:", year, "| Country:", overall_highest_country, "| Expectancy:", overall_highest_expectancy)
    # Life expectancies for the given year is shown
    print("\nFor the year", year_input, ":")
    print("The average life expectancy across all countries was", round(avg_expectancy, 3))
    print("The max life expectancy was in", max_country_year, "with", round(max_expectancy_year, 3))
    print("The min life expectancy was in", min_country_year, "with", round(min_expectancy_year, 3))
