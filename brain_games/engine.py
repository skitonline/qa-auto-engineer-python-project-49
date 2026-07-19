from brain_games.cli import welcome_user

NUMBER_OF_ROUNDS = 3


def start_game(rules, questions, answers):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(rules)

    for i in range(NUMBER_OF_ROUNDS):
        print(f'Question: {questions[i]}')

        cureent_answer = input('Your answer: ')
        if cureent_answer != answers[i]:
            print(f"'{cureent_answer}' is wrong answer ;(. \
                    Correct answer was '{answers[i]}'.")
            print(f"Let's try again, {name}!")
            return 
        print('Correct!')
        
    print(f'Congratulations, {name}!') 