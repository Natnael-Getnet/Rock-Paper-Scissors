import random
import art


def rock_paper_scissors():
    pass


def play_game():
    feed_back = input('Hello, Do you want to play Rock Paper Scissors?(Y) or (N)\n')
    while feed_back.lower() == 'y':
        choose = input('Choose Rock (R), Paper (P) or Scissors (S)\n')
        computer_choose = random.choice(art.RPS)
        if choose == 'r':
            if computer_choose == 'r':
                print(f'You choose {art.rock}')
                print(f'Computer choose {art.rock}')
                print("It's a draw.")
            elif computer_choose == 's':
                print(f'You choose {art.rock}')
                print(f'Computer choose {art.scissors}')
                print("You won.")
            elif computer_choose == 'p':
                print(f'You choose {art.rock}')
                print(f'Computer choose {art.paper}')
                print("You lose.")
        elif choose == 's':
            if computer_choose == 's':
                print(f'You choose {art.scissors}')
                print(f'Computer choose {art.scissors}')
                print("It's a draw.")
            elif computer_choose == 'r':
                print(f'You choose {art.scissors}')
                print(f'Computer choose {art.rock}')
                print("You lose.")
            elif computer_choose == 'p':
                print(f'You choose {art.scissors}')
                print(f'Computer choose {art.paper}')
                print("You won.")
        elif choose == 'p':
            if computer_choose == 'p':
                print(f'You choose {art.paper}')
                print(f'Computer choose {art.paper}')
                print("It's a draw.")
            elif computer_choose == 's':
                print(f'You choose {art.paper}')
                print(f'Computer choose {art.scissors}')
                print("You lose.")
            elif computer_choose == 'r':
                print(f'You choose {art.paper}')
                print(f'Computer choose {art.rock}')
                print("You won.")
        feed_back = input('Do you want to play again?(Y) or (N)\n')


play_game()

