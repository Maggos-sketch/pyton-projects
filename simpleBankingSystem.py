import random, sqlite3, os.path




count = 0

check_file = os.path.exists('card.s3db')

con = sqlite3.connect('card.s3db') # связь
cur = con.cursor()  # клешня управления

def table_creator():
    global check_file
    if check_file == False:
        con = sqlite3.connect('card.s3db') # связь
        cur = con.cursor()  # клешня управления
        cur.execute('''CREATE TABLE card(
                       id INTEGER,
                       number TEXT,
                       pin TEXT,
                       balance INTEGER DEFAULT 0 
                    );''')
        con.commit()
    else:
        con = sqlite3.connect('card.s3db') # связь
        cur = con.cursor()  # клешня управления


def card_in_sql():
    global card, pin
    con = sqlite3.connect('card.s3db') # связь
    cur = con.cursor()  # клешня управления

    cur.execute('''
        INSERT INTO card(number, pin) VALUES({}, {})
    '''.format(card, pin))
    con.commit()

    #for row in cur.execute('''SELECT * FROM card'''):
        #print(row)

def balance_card():
    global in_card
    con = sqlite3.connect('card.s3db') # связь
    cur = con.cursor()  # клешня управления

    cur.execute('''SELECT balance FROM card WHERE number = {}'''.format(in_card))
    bal = cur.fetchone()
    print('Balance:', bal[0])

def add_income_card():
    global inc
    global in_card
    con = sqlite3.connect('card.s3db') # связь
    cur = con.cursor()  # клешня управления
    new_bal = cur.execute('''UPDATE card SET balance = balance + {} 
                          WHERE number = {}'''.format(inc, in_card))
    con.commit()
    print('Income was added!')

def transfer_do():
    global in_card
    all_count = 0

    last_num_algorythm = 0
    con = sqlite3.connect('card.s3db') # связь
    cur = con.cursor()  # клешня управления

    trans_card = input()
    last_num = trans_card[-1] # последгяя цифра номера

    int_card = int(trans_card)
    for num in range(0, len(trans_card) - 1, 2):
        if int(trans_card[num]) * 2 >= 10:
            all_count += (int(trans_card[num]) * 2) - 9
        else:
            all_count += int(trans_card[num]) * 2

    for num in range(1, len(trans_card) - 1 , 2):
        all_count += int(trans_card[num])

    while all_count % 10 != 0:
        last_num_algorythm += 1
        all_count += 1 # Mick Gordon is best

    if trans_card == in_card:
        return "You can't transfer money to the same account!"
    elif int(last_num) != last_num_algorythm:
        #print(last_num, ':', last_num_algorythm)
        return "Probably you made mistake in the card number. Please try again!"
    for row in cur.execute('''SELECT EXISTS (SELECT number FROM card WHERE number = {})'''.format(trans_card)):
        if row[0] == True:
            print('Enter how much money you want to transfer:')
            dep_money = int(input())
            for row in cur.execute('''SELECT balance FROM card 
                                    WHERE number = {}'''.format(in_card)):
                if dep_money > row[0]:
                   return 'Not enough money!'
                else:
                   out_money = cur.execute('''UPDATE card SET balance = balance - {}
                          WHERE number = {}'''.format(dep_money, in_card))
                   in_money = cur.execute('''UPDATE card SET balance = balance + {}
                          WHERE number = {}'''.format(dep_money, trans_card))
                   con.commit()
                   return "Success!"
        else:
            return "Such a card does not exist."

def card_create():
    d = 0
    last_num = 0
    card = random.randint(100000000, 999999999)
    all_card = '400000' + str(card)
    card_list = list(all_card)

    i_num = [int(item) for item in card_list]

    for i in range(0, len(all_card), 2):
        if i_num[i] * 2 >= 10:
            d += (i_num[i] * 2) - 9
        else:
            d += i_num[i] *2
    for i in range(1, len(all_card), 2):
        d += i_num[i]

    while d % 10 != 0:
        last_num += 1
        d += 1

    all_card_total = str(all_card) + str(last_num)
    return str(all_card_total)

def close_account():
    con = sqlite3.connect('card.s3db') # связь
    cur = con.cursor()  # клешня управления

    global in_card

    cur.execute('''DELETE FROM card WHERE number = {}'''.format(in_card))
    con.commit()
    return "The account has been closed!"

i = 0
table_creator()
while True:
    print('')
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    act = input(' ')
    print(' ')

    if act == '1':
        card = card_create()

        pinc = random.randint(1000, 9999)
        pin = str(pinc)

        print('Your card has been created')
        print('Your card number: ')
        print(card)
        print('Your card PIN:')
        print(pin)

        card_in_sql()

    elif act == '2':
        print('Enter your card number:')
        in_card = input()
        print('Enter your PIN:')
        in_pin = input()
        for key in cur.execute('''SELECT EXISTS (SELECT number, pin FROM card WHERE number = {} AND pin = {})'''.format(in_card, in_pin)):

            if key[0] == True:
                print('')
                print('You have successfully logged in!')
                print('')
                while i < 3:
                    print('')
                    print('1. Balance')
                    print('2. Add income')
                    print('3. Do transfer')
                    print('4. Close account')
                    print('5. Log out')
                    print('0. Exit')
                    action = input()
                    if action == '1':
                        print('')
                        balance_card()
                        print('')
                    elif action == '2':
                        print('')
                        print('Enter income:')
                        inc = int(input())
                        add_income_card()
                        print('')
                    elif action == '3':
                        print('')
                        print('Transfer')
                        print('Enter card number:')
                        print(transfer_do())
                    elif action == '4':
                        print('')
                        print(close_account())
                        print('')
                        break
                    elif action == '5':
                        break
                    elif action == '0':
                        print('')
                        print('Bye!')
                        print('')
                        quit()
            else:
                print('')
                print('Wrong card number or PIN!')
                print('')
                break
    elif act == '0':
        print('')
        print('Bye!')
        print('')
        break
    else:
        break



