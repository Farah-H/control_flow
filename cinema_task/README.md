# Control Flow Task , Sparta Global
## Task Requirements 

Create a control flow for movie ratings, which allows or stops the user from viewing a movie depending on whether they meet the age requirements. 

The film ratings are: 
1. U
2. PG
3. 12
4. 15 
5. 18


## Pre-Requisites 
It is easier to complete this task when using a code editor, such as Visual Studio Code or PyCharm. You can learn how to [install VSC](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019) or [install PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) using these hyperlinks. 

## Syntax 
`input` was used to take the user's age information, which must be an integer value.

```python 
age = int(input('How old are you?'))
```

using the `random` model one of the ratings was randomly sected for testing purposes. 

```python
movie_rating = random.choice(['U', 'PG', 12, 15, 18])
```

Finally control flow was used to display a message allowing or stopping the user from accessing the movie using the syntax:

```python
if condition:
    do_something 
elif another_condition:
    do_something_else
elif more_conditions:
    do_something
else:
    do_something
```
- `while` loops are not in regular use, however you do see it being used for monitoring.
- we have a keywords `break` and `continue` to help control the flow of our loop 

```python
# user prompt to increment while loop
user_prompt = True

while user_prompt:
    # takes age input from user 
    age = input('Please enter your age.')
    if age.isdigit() and int(age) < 117:
        print('Thank you for providing your age.')
        # ending the loop
        user_prompt = False
    else:
        print('Please provide age in digits.')
```


