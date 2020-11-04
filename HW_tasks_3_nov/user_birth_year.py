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

if int(birth_month) > time.month():
    print(f'Your birthday hasn\'nt happened yet! You will be {age + 1} in {birth_month}.')
elif birth_month = time.month() and birth_day > time.day():
    print(f'Your birthday hasn\'nt happened yet! You will be {age + 1} in {birth_day - time.day()} days!')
else:
    print('Happy belated Birthday!!')

# print out amt of hours the person has lived (optional)
hours_lived = datetime.today() - dat
