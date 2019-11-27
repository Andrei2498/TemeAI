import random
import numpy

input_neuroni = 0
strat_ascuns_number = 0

test_case = []
out_c = []

w_matrix_int = []
teta_strat_ascuns = []
teta_strat_final = []
w_matrix_out = []
teta_list = []

error_matrix = []


def create_test_case(case: str):
    test_case.append([int(i) for i in case.split(" ")])


def create_output(out: str):
    out_c.append([int(i) for i in out.split(" ")])


def create_test_case_and_out():
    f = open("rn.txt", "r")
    test_case.clear()
    out_c.clear()
    text = f.readline().split(" ")
    while text:
        text = f.readline()
        if len(text) > 0:
            information = text.replace('\n', '').split("  ")
            create_test_case(information[0].replace(',', ''))
            create_output(information[1].replace(',', ''))


def create_first_prob(intrari_1, neuroni_ascunsi):
    global w_matrix_int
    global w_matrix_out
    w_matrix_int.clear()
    w_matrix_out.clear()
    w_matrix_int = [[round(random.uniform(-0.1, 0.1), 4) for i in range(0, input_neuroni)] for j in
                    range(0, strat_ascuns_number)]
    w_matrix_out = [[round(random.uniform(-0.1, 0.1), 4) for i in range(0, neuroni_ascunsi)] for j in
                    range(0, len(out_c))]

    global teta_strat_ascuns
    global teta_strat_final
    teta_strat_final.clear()
    teta_strat_ascuns.clear()
    teta_strat_ascuns = [round(random.uniform(0.0, 1.0), 4) for i in range(0, strat_ascuns_number)]
    teta_strat_final = [round(random.uniform(0.0, 1.0), 4) for i in range(0, len(out_c))]

    global error_matrix
    error_matrix.clear()
    error_matrix = [[] for i in range(0, len(out_c[0]))]


def antreneaza_reteaua(numar_neuroni, rata_de_invatare, eroare_maxima, nr_epoci):
    create_test_case_and_out()
    create_first_prob(7, numar_neuroni)
    MSE = 0.0
    for i in range(0, nr_epoci):
        for j in range(0, len(test_case)):
            instanta_testata = test_case[j]
            # expected_out = out_c[j]

            y_strat_ascuns = []
            ## Ceva dubios
            for n in range(0, numar_neuroni):
                curent_y = 0.0
                for k in range(0, len(instanta_testata)):
                    curent_y += instanta_testata[k] * w_matrix_int[n][k]
                curent_y = curent_y - teta_strat_ascuns[n]
                y_strat_ascuns.append(round(1 / (1 + numpy.exp(-curent_y)), 4))

            y_strat_iesire = []
            for n in range(0, len(out_c[0])):
                curent_y = 0.0
                for k in range(0, len(y_strat_ascuns)):
                    curent_y += y_strat_ascuns[k] * w_matrix_out[n][k]
                curent_y = curent_y - teta_strat_final[n]
                y_strat_iesire.append(round(1 / (1 + numpy.exp(-curent_y)), 4))

            error_list = []
            for l in range(0, len(out_c[j])):
                error_list.append(round(out_c[j][l] - y_strat_iesire[l], 4))
            error_matrix[j] = error_list

            gradientii_de_eroare = []
            for l in range(0, len(out_c[0])):
                gradientii_de_eroare.append(round(y_strat_iesire[l] * (1 - y_strat_iesire[l]) * error_matrix[j][l], 4))

            delta_w_o = []
            delta_teta = []
            gradientii_de_eroare_level_ascuns = []
            for k in range(0, len(w_matrix_out)):
                local_delta = []
                nd = 0
                for l in range(0, len(w_matrix_out[0])):
                    local_delta.append(round(rata_de_invatare * y_strat_ascuns[l] * gradientii_de_eroare[l]))
                    if nd == 0:
                        delta_teta.append(rata_de_invatare * (-1) * gradientii_de_eroare[l])
                        nd = 1
                delta_w_o.append(local_delta)
            for k in range(0, numar_neuroni):
                gradientii_de_eroare_level_ascuns.append(
                    round(sum(w_matrix_out[k]) * gradientii_de_eroare[k] * y_strat_ascuns[k] * (1 - y_strat_ascuns[k]),
                          4))

            delta_teta_ascuns = []
            for k in range(0, numar_neuroni):
                delta_ascuns = []
                for l in range(0, len(instanta_testata)):
                    delta_ascuns.append(rata_de_invatare * instanta_testata[l] * gradientii_de_eroare_level_ascuns[k])
                    w_matrix_int[k][l] = round(w_matrix_int[k][l] + delta_ascuns[-1], 4)
                delta_w_o.append(delta_ascuns)
                delta_teta_ascuns.append(gradientii_de_eroare_level_ascuns[k] * (-1) * rata_de_invatare)
                teta_strat_ascuns[k] = round(teta_strat_ascuns[k] + delta_teta_ascuns[-1], 4)
        MSE = 0.0
        for q in error_matrix:
            for j in q:
                MSE += j * j
        MSE = MSE / (len(test_case) * 10)
        if MSE <= eroare_maxima:
            return error_matrix, round(MSE, 2)
    return error_matrix, round(MSE, 2)


def recunoastere_numar(bits_number):
    print(out_c)


def return_number_from_segment(segments):
    if segments == [1, 1, 1, 1, 1, 1, 1]:
        return 8
    elif segments == [1, 1, 1, 1, 0, 1, 1]:
        return 9
    elif segments == [1, 1, 0, 1, 1, 1, 1]:
        return 6
    elif segments == [1, 1, 1, 0, 1, 1, 1]:
        return 0
    elif segments == [0, 0, 1, 0, 0, 1, 0]:
        return 1
    elif segments == [1, 0, 1, 1, 1, 0, 1]:
        return 2
    elif segments == [1, 0, 1, 1, 0, 1, 1]:
        return 3
    elif segments == [0, 1, 1, 1, 0, 1, 0]:
        return 4
    elif segments == [1, 1, 0, 1, 0, 1, 1]:
        return 5
    elif segments == [1, 0, 1, 0, 0, 1, 0]:
        return 7
