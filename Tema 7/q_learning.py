import numpy
import gym
import random
import time
from copy import deepcopy

import numpy

table = []

alpha = 0.5
gamma = 0.6
epsilon = 1

utilitatea = []
tabelul_de_frecventa = []
final_states = dict()


def prepare_table(file_level):
    file_content = open(file_level, "r")
    matrix = file_content.read().split("\n")
    global table
    for i in range(0, len(matrix)):
        lst = []
        text = matrix[i].split(" ")
        for j in range(0, len(text)):
            if text[j] == 'x':
                lst.append('x')
            elif text[j] == '0':
                lst.append(0)
            elif text[j] == '1':
                final_states[(i, j)] = 1
                lst.append(1)
            elif text[j] == '-1':
                final_states[(i, j)] = -1
                lst.append(-1)
        table.append(lst)


def is_final_state(state):
    if state in final_states.keys():
        return True
    return False


def functiea_de_recompensa(state):
    if is_final_state(state):
        return final_states[state]
    return -0.4


def get_available_position(position: tuple):
    result = []
    if position[0] + 1 <= len(table) - 1:
        if isinstance(table[position[0] + 1][position[1]], int):
            result.append((position[0] + 1, position[1], 1))
    if position[1] + 1 <= len(table[0]) - 1:
        if isinstance(table[position[0]][position[1] + 1], int):
            result.append((position[0], position[1] + 1, 3))
    if position[0] - 1 >= 0:
        if isinstance(table[position[0] - 1][position[1]], int):
            result.append((position[0] - 1, position[1], 0))
    if position[1] - 1 >= 0:
        if isinstance(table[position[0]][position[1] - 1], int):
            result.append((position[0], position[1] - 1, 2))
    return result


def actiunea_facuta(old_state, new_state):
    action = (new_state[0] - old_state[0], new_state[1] - old_state[1])
    if action[0] == 1:
        return 1
    elif action[0] == -1:
        return 0
    elif action[1] == 1:
        return 3
    else:
        return 2


def efectueaza_mutare(state, action):
    if action == 0:
        return state[0] - 1, state[1]
    elif action == 1:
        return state[0] + 1, state[1]
    elif action == 2:
        return state[0], state[1] - 1
    elif action == 3:
        return state[0], state[1] + 1


def is_valid_state(position: tuple):
    if position[0] + 1 <= len(table) - 1:
        if isinstance(table[position[0] + 1][position[1]], int):
            return True
    if position[1] + 1 <= len(table[0]) - 1:
        if isinstance(table[position[0]][position[1] + 1], int):
            return True
    if position[0] - 1 >= 0:
        if isinstance(table[position[0] - 1][position[1]], int):
            return True
    if position[1] - 1 >= 0:
        if isinstance(table[position[0]][position[1] - 1], int):
            return True
    return False


def q_learning_algorithm(qu_table, start_pos):
    result = []
    global epsilon
    episoade = 0
    for i in range(0, 1000):
        next_action = -1
        last_action = -1
        current_position = deepcopy(start_pos)
        while not is_final_state(current_position):
            positions = get_available_position(current_position)
            random_num = random.uniform(0, 1)
            valid_actions = [actiunea_facuta(current_position, i) for i in positions]
            if random_num <= epsilon:
                # Explore action space
                new_pos = random.choice(positions)
                next_action = actiunea_facuta(current_position, (new_pos[0], new_pos[1]))
            else:
                # Exploit learned values
                actiuni = [i[2] for i in positions]
                new = []
                for k in actiuni:
                    new.append(qu_table[current_position[0] * 10 + current_position[1], k])
                mx = numpy.argmax(new)
                next_action = actiuni[mx]

            next_state = efectueaza_mutare(current_position, next_action)

            new1 = []
            for k in valid_actions:
                new1.append(qu_table[current_position[0] * 10 + current_position[1], k])
            maxx = numpy.argmax(new1)
            aux = gamma * qu_table[next_state[0] * 10 + next_state[1], maxx]

            curent_q = qu_table[current_position[0] * 10 + current_position[1], last_action]

            qu_table[current_position[0] * 10 + current_position[1], last_action] = curent_q + alpha * (functiea_de_recompensa(current_position) + aux - curent_q)

            current_position = deepcopy(efectueaza_mutare(current_position, next_action))
            episoade += 1
            last_action = next_action
            # if episoade > 150:
            #     episoade = 0
            #     break
        if epsilon > 0.4:
            epsilon -= 0.005
    return result


if __name__ == '__main__':
    prepare_table("level10x10.txt")
    end_s = table[6][9]
    q_table = [[0 for i in range(0, 4)] for j in range(0, len(table) ** 2)]
    new_q = numpy.zeros((len(table) ** 2, 4))
    utilitatea = numpy.zeros((len(table) ** 2, 4))
    q_learning_algorithm(new_q, (0, 0))
    print(new_q)
