import random

table = []
gama = 1
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


def validate_position(position):
    if 0 <= position <= len(table):
        return True
    return False


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
            if validate_position(position[0] + 1):
                result.append((position[0] + 1, position[1]))
    if position[1] + 1 <= len(table[0]) - 1:
        if isinstance(table[position[0]][position[1] + 1], int):
            if validate_position(position[1] + 1):
                result.append((position[0], position[1] + 1))
    if position[0] - 1 >= 0:
        if isinstance(table[position[0] - 1][position[1]], int):
            if validate_position(position[0] - 1):
                result.append((position[0] - 1, position[1]))
    if position[1] - 1 >= 0:
        if isinstance(table[position[0]][position[1] - 1], int):
            if validate_position(position[1] - 1):
                result.append((position[0], position[1] - 1))
    return result


def q_learning_algorithm(qu_table):
    result = []
    for i in range(0, 100):
        current_position = (0, 0)
        for j in range(0, 100):
            positions = get_available_position(current_position)
            random_num = random.uniform(0, 1)
            if random_num <= epsilon:
                current_position = positions[random.randint(0, len(positions) - 1)]
            else:
                print("`")
    return result


if __name__ == '__main__':
    prepare_table("level10x10.txt")
    end_s = table[6][9]
    q_table = [[0] * 4] * (len(table) ** 2)
    q_learning_algorithm(q_table)
    print(q_table)
    print(final_states)
