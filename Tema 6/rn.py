import random

intrari = []
test_case = []
out_c = []
initial_value = []

def activation(input_1):
    if input_1 > 0:
        return 1
    return 0


def create_test_case(case: str):
    test_case.append([int(i) for i in case.split(" ")])


def create_output(out: str):
    out_c.append([int(i) for i in out.split(" ")])


def creare_intrari(input_strat):
    for i in range(0, input_strat):
        intrari.append([0] * input_strat)
        intrari[i][i] = 1


def create_test_case_and_out():
    f = open("rn.txt", "r")
    intrari.clear()
    test_case.clear()
    out_c.clear()
    initial_value.clear()
    text = f.readline().split(" ")
    init_size = text[0]
    iesiri = text[1]
    test = text[2].replace("\n", '')
    creare_intrari(int(init_size))
    while text:
        text = f.readline()
        if len(text) > 0:
            information = text.replace('\n', '').split("  ")
            create_test_case(information[0].replace(',', ''))
            create_output(information[1].replace(',', ''))


def create_first_prob(intrari_1):
    initial_value.clear()
    for i in range(0, intrari_1):
        initial_value.append(random.uniform(-0.1, 0.1))
