      # Homework 8.1: The mood checker


mood = input('What is your mood? : ')

if mood == 'happy':
    print('It is great to see you happy!')
elif mood == 'nervous':
    print('Take a deep breath 3 times.')
elif mood == 'sad':
    print('Do not be sad.')
elif mood == 'corona':
    print('Dont worry! It will be over soon.')
elif mood == 'relaxed':
    print('What are you smoking?')
else:
    print('I do not recognize this mood.')





      # Homework 8.2: Guess the secret number


secret = 25

guess = int(input('Guess the secret number: '))
if secret == guess:
    print('You guessed the number,congratulations!')
elif 20 == guess:
    print('Almost there!')
elif 2 == guess:
    print('Bad luck,leave game.')
else:
    print('Sorry you didnt guess the number,more luck next time!')





      # Homework 8.3: Calculator


number1 = int(input('enter the first number : '))
number2 = int(input('enter the second number : '))
operation = input('enter the arithmetic operation : ')

if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '/':
    print(number1 / number2)
elif operation == '*':
    print(number1 * number2)