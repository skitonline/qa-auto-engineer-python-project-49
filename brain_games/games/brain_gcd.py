from random import randint
from math import gcd
from brain_games.engine import NUMBER_OF_ROUNDS, start_game

RULES = 'Find the greatest common divisor of given numbers.'

NUM_FROM = 0
NUM_TO = 100

def play_brain_gcd():
    questions = [(randint(NUM_FROM, NUM_TO), randint(NUM_FROM, NUM_TO)) for _ in range(NUMBER_OF_ROUNDS)]
    answers = [None] * NUMBER_OF_ROUNDS

    for i in range(NUMBER_OF_ROUNDS):
        a, b = questions[i]
        answers[i] = str(gcd(a, b))
        questions[i] = f'{a} {b}'
    start_game(RULES, questions, answers)