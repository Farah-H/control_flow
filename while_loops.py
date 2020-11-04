# let's create a while loop 

# syntax: while variable_name condition value:

# number = 0
# while number < 10:
#     print(f'{number}. It\'s working!')
#     if number == 5:
#         break
#     number += 1

user_prompt = True

while user_prompt:
    age = input('Please enter your age.')
    if age.isdigit() and int(age) < 117:
        print('Thank you for providing your age.')
        user_prompt = False
    else:
        print('Please provide age in digits.')