from random import *

# подбор пароля, большие и маленькие буквы на латинице, цифры и символы

guess = ''
password = input('Введите пароль: ')
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','\'','!','@','#','$','%','&','*','/','\\','`','~','?','-','+','=','_',',','.','(',')','^','<','>','|','[',']','{','}',':',';','"',' ']

while(guess != password):
    guess = ''
    for letter in password:
        guessletter = letters[randint(0, 94)]
        guess = str(guessletter) + str(guess)
    print(guess)
print('Пароль найден!')
print(f'Your password: <{guess}>')