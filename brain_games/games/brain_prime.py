from random import randint

from brain_games.engine import NUMBER_OF_ROUNDS, start_game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

NUM_FROM = 1
NUM_TO = 1000


def play_brain_prime():
    questions = [randint(NUM_FROM, NUM_TO) for _ in range(NUMBER_OF_ROUNDS)]
    answers = [None] * NUMBER_OF_ROUNDS

    def is_prime(n):
        if n == 1:
            return False
        for div in range(2, n // 2 + 1):
            if n % div == 0:
                return False
        return True
    
    for i in range(NUMBER_OF_ROUNDS):
        answers[i] = 'yes' if is_prime(questions[i]) else 'no'
        questions[i] = str(questions[i])
    start_game(RULES, questions, answers)