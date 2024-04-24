"""
with open("hr_system.txt") as f:
    # The file has now been opened and stored in a variable "f"

    # Read each line, one by one, into a variable: current_line
    for line in f:
        # Split the current line into its parts based on a space " " as the separator
        parts = line.split(" ")

        # Save the parts we need into variables
        name = parts[0]
        title = parts[2]

        # Output the name and title as desired
        print(f"Name: {name}, Title: {title}")
"""

with open("life-expectancy.csv") as world_data:
    next(world_data)
    for line in world_data:
        line = line.strip()
        parts = line.split(',')
        name_country = parts[0]
        code = parts[1]
        year = int(parts[2])
        expectancy = float(parts[3])
