from random import randint, choice
from brain_games.engine import NUMBER_OF_ROUNDS, start_game

RULES = 'What is the result of the expression?'
NUM_FROM = 0
NUM_TO = 10
SIGNS = ['+', '-', '*']

def play_brain_calc():
    #генерируем кортеж для составления задания: первое число, операцию между числами и второе число
    questions = [(randint(NUM_FROM, NUM_TO), 
                  choice(SIGNS) , 
                  randint(NUM_FROM, NUM_TO)) for _ in range(NUMBER_OF_ROUNDS)]

    answers = [None] * NUMBER_OF_ROUNDS
    for i in range(NUMBER_OF_ROUNDS):
        a, sign, b = questions[i]
        
        if sign == '+':
            answers[i] = str(a + b)
            questions[i] = f'{a} + {b}'
        elif sign == '-':
                answers[i] = str(a - b)
                questions[i] = f'{a} - {b}'
        else: #sign == '*'
            answers[i] = str(a * b)
            questions[i] = f'{a} * {b}'

    start_game(RULES, questions, answers)