def worse(sign):
    worse_enemy_animals = {
        'Rat': 'Horse',
        'Ox': 'Goat',
        'Tiger': 'Monkey',
        'Rabbit': 'Rooster',
        'Dragon': 'Dog',
        'Snake': 'Pig',
        'Horse': 'Rat',
        'Goat': 'Ox',
        'Monkey': 'Tiger',
        'Rooster': 'Rabbit',
        'Dog': 'Dragon',
        'Pig': 'Snake'
    }
    return worse_enemy_animals.get(sign)
