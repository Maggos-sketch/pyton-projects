MONEY_HAS = 550
WATER_HAS = 400
MILK_HAS = 540
COFFEE_BEANS_HAS = 120
CUPS_HAS = 9

# for espresso
ESPRESSO_WATER = 250
ESPRESSO_COF_BEANS = 16
ESPRESSO_COST = 4

# for latte
LATTE_WATER = 350
LATTE_MILK = 75
LATTE_COF_BEANS = 20
LATTE_COST = 7

# for cappuccino
CAPPUCCINO_WATER = 200
CAPPUCCINO_MILK = 100
CAPPUCCINO_COF_BEANS = 12
CAPPUCCINO_COST = 6

def output_resurces():
    print('')
    print('The coffee machine has:')
    print(WATER_HAS,'of water')
    print(MILK_HAS,'of milk')
    print(COFFEE_BEANS_HAS, 'of coffee beans')
    print(CUPS_HAS, 'of disposable cups')
    print(MONEY_HAS, 'of money')
    print('')
def buy_espresso():
    global WATER_HAS
    global COFFEE_BEANS_HAS
    global CUPS_HAS
    global MONEY_HAS
    global ESPRESSO_WATER
    global ESPRESSO_COF_BEANS
    global ESPRESSO_COST

    if WATER_HAS >= ESPRESSO_WATER and COFFEE_BEANS_HAS >= ESPRESSO_COF_BEANS and CUPS_HAS >= 1:
        
        print('I have enough resources, making you a coffee!')
        WATER_HAS -= ESPRESSO_WATER
        COFFEE_BEANS_HAS -= ESPRESSO_COF_BEANS
        CUPS_HAS -= 1
        MONEY_HAS += ESPRESSO_COST
    elif WATER_HAS < ESPRESSO_WATER:
        print('Sorry, not enough water!')
    elif COFFEE_BEANS_HAS < ESPRESSO_COF_BEANS:
        print('Sorry, not enough coffee beans!')
    else:
        print('Sorry, not enough cups')
    print('')
    
    #output_resurces()

def buy_latte():
    global WATER_HAS
    global MILK_HAS
    global COFFEE_BEANS_HAS
    global CUPS_HAS
    global MONEY_HAS
    global LATTE_WATER
    global LATTE_MILK
    global LATTE_COF_BEANS
    global LATTE_COST

    if WATER_HAS >= LATTE_WATER and MILK_HAS >= LATTE_MILK and COFFEE_BEANS_HAS >= LATTE_COF_BEANS and CUPS_HAS >= 1:
        print('I have enough resources, making you a coffee!')
        WATER_HAS -= LATTE_WATER
        MILK_HAS -= LATTE_MILK
        COFFEE_BEANS_HAS -= LATTE_COF_BEANS
        CUPS_HAS -= 1
        MONEY_HAS += LATTE_COST
        #output_resurces()
    elif WATER_HAS < LATTE_WATER:
        print('Sorry, not enough water!')
    elif MILK_HAS < LATTE_MILK:
        print('Sorry, not enough milk!')
    elif COFFEE_BEANS_HAS < LATTE_COF_BEANS:
        print('Sorry, not enough coffee beans!')
    else:
        print('Sorry, not enough cups')
    print('')

    
def buy_cappuccino():
    global WATER_HAS
    global MILK_HAS
    global COFFEE_BEANS_HAS
    global CUPS_HAS
    global MONEY_HAS
    global CAPPUCCINO_WATER
    global CAPPUCCINO_MILK
    global CAPPUCCINO_COF_BEANS
    global CAPPUCCINO_COST

    if WATER_HAS >= CAPPUCCINO_WATER and MILK_HAS >= CAPPUCCINO_MILK and COFFEE_BEANS_HAS >= CAPPUCCINO_COF_BEANS and CUPS_HAS >= 1:
        print('I have enough resources, making you a coffee!')
        WATER_HAS -= CAPPUCCINO_WATER
        MILK_HAS -= CAPPUCCINO_MILK
        COFFEE_BEANS_HAS -= CAPPUCCINO_COF_BEANS
        CUPS_HAS -= 1
        MONEY_HAS += CAPPUCCINO_COST
    elif WATER_HAS < CAPPUCCINO_WATER:
        print('Sorry, not enough water!')
    elif MILK_HAS < CAPPUCCINO_MILK:
        print('Sorry, not enough milk!')
    elif COFFEE_BEANS_HAS < CAPPUCCINO_COF_BEANS:
        print('Sorry, not enough coffee beans!')
    else:
        print('Sorry, not enough cups')
    print('')


    #output_resurces()
def fill_resourses():
    global WATER_HAS
    global MILK_HAS
    global COFFEE_BEANS_HAS
    global CUPS_HAS

    print('Write how many ml of water do you want to add:')
    fill_water = int(input())
    print('Write how many ml of milk do you want to add:')
    fill_milk = int(input())
    print('Write how many grams of coffee beans do you want to add:')
    fill_coffee = int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    fill_cups = int(input())

    WATER_HAS += fill_water
    MILK_HAS += fill_milk
    COFFEE_BEANS_HAS += fill_coffee
    CUPS_HAS += fill_cups
    print('')
    #output_resurces() 

def take_money():
    global MONEY_HAS
    print('I gave you $', MONEY_HAS)
    MONEY_HAS -= MONEY_HAS
    print('')
    #output_resurces() 

i = 0

while i < 3:
    print('Write action (buy, fill, take, remaining, exit):')
    action = str(input())
    if action == 'buy':
        while i < 1:
            print('')
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            action = input()
            if action == '1':
                buy_espresso()
                break
            elif action == '2':
                buy_latte()
                break
            elif action == '3':
                buy_cappuccino()
                break
            elif action == 'back':
                break
    elif action == 'fill':
        print('')
        fill_resourses()
    elif action == 'take':
        take_money()
    elif action == 'remaining':
        output_resurces()
    elif action == 'exit':
        break    

