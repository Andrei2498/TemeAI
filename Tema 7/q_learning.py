import random
from copy import deepcopy

import numpy

table = []
gama = 1
epsilon = 1
alpha = 0.5
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


def calculare_u(stari, actiunile_pentru_s, probabilitatea_sp_s_a, recompensa, discount, epsilon):
    return []


def get_available_position(position: tuple):
    result = []
    if position[0] + 1 <= len(table) - 1:
        if isinstance(table[position[0] + 1][position[1]], int):
            result.append((position[0] + 1, position[1]))
    if position[1] + 1 <= len(table[0]) - 1:
        if isinstance(table[position[0]][position[1] + 1], int):
            result.append((position[0], position[1] + 1))
    if position[0] - 1 >= 0:
        if isinstance(table[position[0] - 1][position[1]], int):
            result.append((position[0] - 1, position[1]))
    if position[1] - 1 >= 0:
        if isinstance(table[position[0]][position[1] - 1], int):
            result.append((position[0], position[1] - 1))
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


def calculare_probalilitate(old_state, new_state, action):
    return 0


def q_learning_algorithm(qu_table):
    result = []
    for i in range(0, 100):
        current_position = (0, 0)
        for j in range(0, 100):
            positions = get_available_position(current_position)
            random_num = random.uniform(0, 1)
            if random_num <= epsilon:
                current_position1 = positions[random.randint(0, len(positions) - 1)]
                actiune = actiunea_facuta(current_position, current_position1)
                matr_pos = current_position1[0] * 10 + current_position1[1]
                qu_table[matr_pos][actiune] = qu_table[matr_pos][actiune] + 1
                current_position = current_position1
            else:
                print("`")
    return result


if __name__ == '__main__':
    prepare_table("level10x10.txt")
    end_s = table[6][9]
    # q_table = [[0] * 4] * (len(table) ** 2)
    q_table = [[0 for i in range(0, 4)] for j in range(0, len(table) ** 2)]
    new_q = numpy.zeros((len(table) ** 2, 4))
    utilitatea = numpy.zeros((len(table) ** 2, 4))
    q_learning_algorithm(q_table)

