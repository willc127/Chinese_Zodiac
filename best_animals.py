def best(sign):
    best_friend_animals = {
        'Rat': 'Ox',
        'Ox': 'Rat',
        'Tiger': 'Pig',
        'Rabbit': 'Dog',
        'Dragon': 'Rooster',
        'Snake': 'Monkey',
        'Horse': 'Goat',
        'Goat': 'Horse',
        'Monkey': 'Snake',
        'Rooster': 'Dragon',
        'Dog': 'Rabbit',
        'Pig': 'Tiger'
    }
    return best_friend_animals.get(sign)
