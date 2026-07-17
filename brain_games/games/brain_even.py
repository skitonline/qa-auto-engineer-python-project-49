from random import randint
from brain_games.engine import NUMBER_OF_ROUNDS, start_game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

NUM_FROM = 0
NUM_TO = 100

def play_brain_even():
    questions = [randint(NUM_FROM, NUM_TO) for _ in range(NUMBER_OF_ROUNDS)]
    answers = ['yes' if x % 2 == 0 else 'no' for x in questions]
    start_game(RULES, questions, answers)