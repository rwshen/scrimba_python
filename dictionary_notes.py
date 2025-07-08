movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

print(movie['title'])
print(movie['cast'])
# errors if you ask for a key that doesn't exist
print(movie.get('budget')) # <= will not throw an error None
print(movie.get('budget', 'Not Found')) # custom message for None
# update a value
# movie['title'] = 'The Holy Grail'
# print(movie['title'])

# add a new key value pair
movie['budget'] = 250000

print(movie)

# update the value in the dictionary
movie.update({'title' : 'The Holy Grail', 'year': 1975, 'cast': ['John','Eric','Michael','George','Terry'] })
print(movie)
# del movie['year]
year = movie.pop('year')
print(movie)
print(year)

print(movie.keys(), movie.values(), movie.items())

for key, value in movie.items():
    print(key, value)

print(movie)

python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

#membership test
print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print('He\'s not here')

# putting dictionaries together
people = {}
people1 = {}
people2 = {}
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)

print(people)

#method 2
for groups in (python, holy_grail, life_of_brian): people1.update(groups)
print(people1)

# method 3 unpacking 3.5 python and later
people2 = {**python, **holy_grail, **life_of_brian}
print(people2)

# find the sum of all the values
print(f'The sum of the ages {sum(people.values())}')