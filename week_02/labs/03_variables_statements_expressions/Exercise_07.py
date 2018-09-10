'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''

seconds_per_year = 365*24*60*60
born = seconds_per_year / 6
dead = seconds_per_year / 12
immigrated = seconds_per_year / 40
pop_increase_per_year = born - (dead + immigrated)
pop_0 = 380123456

for year in range(4):
    print("Year", year, ":", pop_0 + year*pop_increase_per_year)
