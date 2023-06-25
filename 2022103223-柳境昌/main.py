import os
in_put = input("Please enter the number from 1 to 3）:")
print("the result is " +result + ":")


if in_put == '1':
    os.system('python ./L1/rand_create.py')
elif in_put == '2':
    os.system('python ./L2/datasamplying.py')
elif in_put == '3':
    os.system('python ./L3/factoryMethod.py')
