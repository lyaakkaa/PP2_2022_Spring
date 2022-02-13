import random
def guess():
    print('Hello! What is your name?')
    name = input()
    print()
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    num = random.randint(1, 20)
    print("Take a guess.")
    input_num = int(input())
    count = 0

    while input_num != num:
        if input_num > num:
            count += 1
            print()
            print('Your guess is too high')
            print("Take a guess.")
            input_num = int(input())
            continue
        elif input_num < num:
            count += 1
            print()
            print('Your guess is too low')
            print("Take a guess.")
            input_num = int(input())
            continue
    else:
        print(f'Good job, {name}! You guessed my number in {count+1} guesses!')


guess()