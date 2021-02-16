#Load data set
max = -1
min = -1
max_country = ""
max_country_year = ""
max_year = -1
min_year = 999
min_country = ""
min_country_year = ""
max_expectancy = -1
max_expectancy_year = -1
min_expectancy = 999
min_expectancy_year = 999

dates_count = -1
average_age = -1
print("\n\n")
with open("/Users/elijah/BYUI/Programming Building Blocks/Week 6/life-expectancy.csv") as life_data:
    get_year = int(input("Enter the year of interest : "))
    for line in life_data:
        part = line.split(",")
        country  = part[0]
        code = part[1]
        year = int(part[2])
        expectancy = float(part[3])
        if(expectancy < min_expectancy):
            min_expectancy = expectancy
            min_country = country
            min_year = year
        if(expectancy > max_expectancy):
            max_expectancy = expectancy
            max_country = country
            max_year = year
        if(year == get_year):
            average_age += expectancy
            dates_count += 1
            if(expectancy < min_expectancy_year):
                min_expectancy_year = expectancy
                min_country_year = country
            if(expectancy > max_expectancy_year):
                max_expectancy_year = expectancy
                max_country_year = country
        
    print(f"\n\nThe overall max life expectancy is: {max_expectancy} in {max_country} in the year {max_year}")
    print(f"The overall min life expectancy is : {min_expectancy} from {min_country} in the year {min_year}")
    print()
    print(f"For the year : {get_year}:")
    average_age = average_age/dates_count
    print(f"\n\nThe average life expectancy across all countries was : {average_age:.3f}")
    print(f"The max life expectancy for the year {get_year} is  : {max_expectancy_year} from {max_country_year}")
    print(f"The min life expectancy for the year {get_year} is  : {min_expectancy_year} from {min_country_year}")
#Iterate through the data
#Split into parts
#Lowest value
#Highest value