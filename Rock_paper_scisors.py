import random, os.path
players = {}
file_name = 'rating.txt'

def file_exist(file_):
    existing = os.path.isfile(file_)
    if not existing:
        file_cr = open(file_, 'w')
        file_cr.close()

def check(name):
    p = 0
    _file = open(file_name , 'r+')
    if name in _file.read():
       return f'Hello, {name}'
    else:
        print('\n'+name, p, file=_file)
        _file.close()
        return f'Hello, {name}'

def points():
    file_po = open(file_name, 'r')
    for line in file_po.readlines():
        name, score = line.split()
        players[name] = int(score)
    return players

def win(name):
    for ind, value in players.items():
        if name == ind:
            players[ind] = value + 100
    return players

def draw(name):
    for ind, value in players.items():
        if name == ind:
            players[ind] = value + 50
    return players

def update():
    with open(file_name, 'w') as in_file:
        for name, score in players.items():
            in_file.write('{} {}\n'.format(name, score))
    in_file.close()

first_half = []
second_half = []

while True:
    file_exist(file_name)
    name = input('Enter your name: ')
    print(check(name))
    points()
    mod_game = input()
    
    if not mod_game:
        variables = ['rock','paper','scissors']
    else:
        variables = mod_game.split(',')

    print("Okay, let's start")
    
    while True:

        player_turn = input()
        option = random.choice(variables)
    
        for i in range(0, len(variables)):
            if player_turn in variables[i]:
                first_half = variables[0:i]
                second_half = variables[i+1:]

        for i in range(0, len(variables)):
            if len(first_half) > len(second_half):
                second_half.append(first_half[0])
                del first_half[0]

            elif len(first_half) < len(second_half):
                first_half.append(second_half[-1])
                del second_half[-1]
        if player_turn in variables:    
            if option in first_half:
                win(name)
                update()
                print (f'Well done. Computer chose {option} and failed')
                #print(first_half)
                #print(second_half)
            elif option == player_turn:
                draw(name)
                update()
                print (f'There is a draw ({option})')
                #print(first_half)
                #print(second_half)
            elif option in second_half:
                print(f'Sorry, but computer chose {option}')
                update()
                #print(first_half)
                #print(second_half)
        else:
            for key in variables:         
                if player_turn == '!rating':
                    for names, value in players.items():
                        if name == names:
                            print(f'Your rating: {value}')
                    break
                elif player_turn == '!exit':
                    print('Bye!')
                    quit()
                else:
                    print('Invalid input')
                    break