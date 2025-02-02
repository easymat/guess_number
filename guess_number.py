from random import randint

number = randint(1,100)

while True:
    print('Введите число:')
    guess = int(input())
    if guess < number:
        print('Ваше число меньше того, что загадано')
    elif guess > number:
        print('Ваше число больше того, что загадано')
    elif guess == number:
        break


print('Отличная интуиция! Вы угадали число :)')