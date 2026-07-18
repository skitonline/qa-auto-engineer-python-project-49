from random import randint
from brain_games.engine import NUMBER_OF_ROUNDS, start_game

RULES = 'What number is missing in the progression?'

def play_brain_progression():
    step = [randint(1, 10) for _ in range(NUMBER_OF_ROUNDS)]
    how_many_generate = [randint(5, 12) for _ in range(NUMBER_OF_ROUNDS)]
    start = [randint(0, 100)  for _ in range(NUMBER_OF_ROUNDS)]

    def count_number(start, step, index):
        return start + index * step
    
    questions = [[count_number(start[j], step[j], i) for i in range(how_many_generate[j])] 
                  for j in range(NUMBER_OF_ROUNDS)]
    
    hide_index = [randint(0, how_many_generate[j] - 1) for j in range(NUMBER_OF_ROUNDS)]

    answers = [None] * NUMBER_OF_ROUNDS
    for i in range(NUMBER_OF_ROUNDS):
        answers[i] = str(questions[i][hide_index[i]])
        questions[i][hide_index[i]] = '..'
        questions[i] = ' '.join(map(str, questions[i]))

    start_game(RULES, questions, answers)