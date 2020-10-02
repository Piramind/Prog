import random
import os


chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
number = int(input('Кол-во паролей'))
leight = int(input('Кол-во символов'))

for x in range(number):
    password = ""

    for i in range(leight):
        password += random.choice(chars)
    print(password)

    file = open( 'password.txt', 'a' )
    file.write('\n' + password)
    file.close()

os.system('pause')