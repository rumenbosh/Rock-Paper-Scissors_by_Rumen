import random
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
computer_entry = ''
plyer_input = input('Choose entry: r for rock, p for paper or s for scissors: ')
if plyer_input == 'r':
    plyer_input = rock
elif plyer_input == 'p':
    plyer_input = paper
elif plyer_input == 's':
    plyer_input = scissors
else:
    raise SystemExit('Invalid Input. Try again...')
computer_entry_num = random.randint(1,3)
if computer_entry_num == 1:
    computer_entry = rock
elif computer_entry_num == 2:
    computer_entry = paper
elif computer_entry_num == 3:
    computer_entry = scissors
print(f'The computer chose {computer_entry}.')
if (plyer_input == rock and computer_entry == scissors) or \
        (plyer_input == paper and computer_entry == rock) or \
        (plyer_input == scissors and computer_entry == paper):
    print('You win!')
elif plyer_input == computer_entry:
    print('Draw!')
else:
    print('You lose!')