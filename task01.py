from random import randint
random_num = randint(1, 20)
num = 0
while True:
    num = int(input('son kiriting:'))
    if random_num > num:
        print('kattaroq')
    elif random_num < num:
        print('kichikroq')
    elif random_num == num:
        print('topdingiz')
        break  