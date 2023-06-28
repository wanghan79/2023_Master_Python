import os



while (True):
    index = input("Please enter the homework number you want to display （1-3）:")
    if index == '1':
        os.system('python Homework_1.py')
    elif index == '2':
        os.system('python Homework_2.py')
    elif index == '3':
        os.system('python Homework_3.py')
    else:
        print("Invalid input. Please enter a valid homework number.")

    print('-' * 200)
