def worst(sign):
    worst_enemy_animals = {
        'Rat': 'Goat',
        'Ox': 'Horse',
        'Tiger': 'Snake',
        'Rabbit': 'Dragon',
        'Dragon': 'Rabbit',
        'Snake': 'Tiger',
        'Horse': 'Ox',
        'Goat': 'Rat',
        'Monkey': 'Pig',
        'Rooster': 'Dog',
        'Dog': 'Rooster',
        'Pig': 'Monkey'
    }
    return worst_enemy_animals.get(sign)
