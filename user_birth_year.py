import datetime


# take the user's name
name = input('What is your name?').title()

# define varibles age and time 
age = int(input('What is your age?'))
time = datetime.datetime.today()
print(time)

# make a calculation for the year in which the person was born 
birth_year = time.year - age 

# print "OMG <person>, you are <age> years old so you were born in <year>"
print(f'OMG {name}, you are {age} years old so you were born in {birth_year}!')

# account for whether the person's birthday has happened or no
birth_month = input('What is your birth month? Please enter in the format MM')
birth_day = input('What day is your birthday? Please enter in the format DD')

if birth_month > 
# print out amt of hours the person has lived (optional)

