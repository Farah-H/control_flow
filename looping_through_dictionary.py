# for and while loops 
# for loop is used to iterate through the data

shopping_list = ['eggs', 'milk', 'supermalt']
print(shopping_list)

for _ in shopping_list:
    if _ == 'milk':
        print(_)
        break
# INDENTATION IS VERY IMPORTANT

# Task , using the dictionaries we created earlier, iterate through the keys and values

user_details = {
    'name': 'Farah Moshref Hassan',
    'DOB': '31/08/1998',
    'age': 22,
    'address' : '9 Something Lane, London, NS3 568',
    'national_insurance' : 'DH6735H',
    'highest_qualification' : 'MSc Nuclear Science and Engineering',
    'hobbies' : ['Painting', 'Gaming', 'Volunteering'], #create a list of hobbies of at least 3 items
    'course' : 'DevOps',
    'grades' : {
        'English' : 'A*',
        'Science' : 'A*',
        'Art' : 'B',
        'Chemistry' : 'A'
    }
}

for key, value in user_details.items():
    print(f'{key} = {value}')