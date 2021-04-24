"""
You should use terminal for that code
"""
import os
def func():
    account = 0
    purchase_history = []
    choice = '4'
    while choice!='4':
        print('1. Account')
        print('2. Purchase')
        print('3. Purchase history')
        print('4. Break')

        if choice == '1':
            os.system('cls')
            account += int(input('How much money do you want to deposit into your account?: '))
            continue
        elif choice == '2':
            os.system('cls')
            price = int(input('How much does it cost?: '))
            if price > account:
                os.system('cls')
                print('You do not have enough money to buy that merchandise: ')
                input()
                continue
            merchandise = input('Name that merchandise ')
            account -= price
            purchase_history.append([merchandise, price])
            continue
        elif choice == '3':
            os.system('cls')
            print(*purchase_history)
            input()
            continue
        elif choice == '4':
            break
        else:
            print('Wrong choice')