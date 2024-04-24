# With this, the dataset will be loaded
with open('life-expectancy.csv') as world_data:
    next(world_data)
    # Create variables to keep track of lowest and highest life expectancies
    lowest_expectancy = float('inf')
    highest_expectancy = float('-inf')
    for line in world_data:
        line = line.strip()
        parts = line.split(",")
        name_country = parts[0]
        code = parts[1]
        year = int(parts[2])
        expectancy = float(parts[3])
        # Here the lowest and highest life expectancies will be updated as necessary
        if expectancy < lowest_expectancy:
            lowest_expectancy = expectancy
        if expectancy > highest_expectancy:
            highest_expectancy = expectancy
# To print the highest and lowest life expectancies found
print("Lowest life expectancy:", lowest_expectancy)
print("Highest life expectancy:", highest_expectancy)
