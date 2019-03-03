import random


# name maker

with open('firstnames', 'r') as fir:
    first = fir.read().splitlines()
    first = random.choice(first)

with open('lastnames', 'r') as las:
    last = las.read().splitlines()
    last = random.choice(last)

    # password generators

symbols = ["!", "@", "$"]
ransym = random.choice(symbols)

with open('nouns', 'r') as nou:
    noun = nou.read().splitlines()
    noun = random.choice(noun)

with open('adjectives', 'r') as adj:
    adjective = adj.read().splitlines()
    adjective = random.choice(adjective)

    numbers = random.randint(3420, 9229)
    password = adjective.capitalize()+noun+str(numbers)+ransym

    # age generator
age = random.randint(18, 50)

username = adjective.capitalize()+noun+str(random.randint(100, 500))

firstname = first
lastname = last
agenumber = age
passwordgen = password
user = username




