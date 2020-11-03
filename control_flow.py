import random

# age taken as input
age = int(input('What is your age?'))
# movie_rating randomly selected and printed
movie_rating = random.choice(['U', 'PG', 12, 15, 18])
print(movie_rating)


# control flow based on age
if age >= 18: 
    print('Enjoy the movie!')
elif age >= 15 and movie_rating != 18:  # a 15 year old can watch any movie except 18 rated
    print('Enjoy the movie!')
elif age >= 12 and movie_rating not in (15, 18): # a 12 year old can watch any movie except 15 and 18 rated
    print('Enjoy the movie!')
elif age < 12 and movie_rating == 'U': # anyone can watch a U rated movie 
    print('Enjoy the movie!')
elif age < 12 and movie_rating == 'PG': # parental guidance for young kids, although it is technically legal 
    print('Enjoy the movie, but please be aware some content may distress younger viewers. Parental guidance is advised.')
else: # only condition left is if age is too young for the movie rating
    print('You are too young for this movie, please try another one or come back when you are older!')
