#generator password
import random

latinic = 'abcdefghijklmnopqrstuvwxyz'
#kirillik = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
number = '0123456789'
symbols = '!@#$%&*/\\'

uplat = latinic.upper()
#upkiril = kirillik.upper()

use_for = latinic + number + symbols + uplat # + kirillik + upkiril
length_for_pass = 8

password = "".join(random.sample(use_for, length_for_pass))
print(f'Your generated password is "{password}"')
