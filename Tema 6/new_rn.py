import numpy
import random
import math

# Aici stocam valorile modificate.
w_matrix_input = []
w_matrix_output = []
bias_list_input = []
bias_list_output = []
error_matrix = []

input_tested = []
output_expected = []

MSE = 0.0
input_number = 0
hidden_layer_number = 0


def populate_input_tested(case: str):
    input_tested.append([int(i) for i in case.split(" ")])


def populate_output_expected(out: str):
    output_expected.append([int(i) for i in out.split(" ")])


def populate_input_and_expected_output():
    f = open("rn.txt", "r")
    input_tested.clear()
    output_expected.clear()
    text = f.readline().split(" ")
    while text:
        text = f.readline()
        if len(text) > 0:
            information = text.replace('\n', '').split("  ")
            populate_input_tested(information[0].replace(',', ''))
            populate_output_expected(information[1].replace(',', ''))


def first_initialization():
    global w_matrix_input
    global w_matrix_output
    w_matrix_input.clear()
    w_matrix_output.clear()
    w_matrix_input = [[round(random.uniform(-0.1, 0.1), 4) for i in range(0, input_number)] for j in
                    range(0, hidden_layer_number)]
    w_matrix_output = [[round(random.uniform(-0.1, 0.1), 4) for i in range(0, hidden_layer_number)] for j in
                    range(0, len(output_expected))]

    global bias_list_input
    global bias_list_output
    bias_list_output.clear()
    bias_list_input.clear()
    bias_list_input = [round(random.uniform(-0.1, 0.1), 4) for i in range(0, hidden_layer_number)]
    bias_list_output = [round(random.uniform(-0.1, 0.1), 4) for i in range(0, len(output_expected))]

    global error_matrix
    error_matrix.clear()
    error_matrix = [[] for i in range(0, len(output_expected[0]))]


def start(numar_neuroni_strat_ascuns: int, rata_de_invatare: float,eroare_maxima: float, numar_epoci: int):
    global hidden_layer_number, input_number
    hidden_layer_number = numar_neuroni_strat_ascuns
    populate_input_and_expected_output()
    input_number = len(input_tested[0])
    first_initialization()

    for i in range(0, numar_epoci):
        print(i)
        antrenare_epoca(rata_de_invatare)
        if MSE < eroare_maxima:
            break
    


def suma_gradient_input(gradient_list, j):
    suma = 0
    for i in range(0, len(gradient_list)):
        suma += gradient_list[i] * w_matrix_output[j][i]
    return suma

def antrenare_epoca(rata_de_invatare: float):
    global MSE
    for i in range(0, input_number):

        # Calculare y de pe stratul ascuns, adica iesirile reale de pe stratul ascuns
        print("Crapa aici 1")
        input_y_list = numpy.dot(input_tested[i], w_matrix_input)
        print("Crapa aici 1.5")
        for j in range(0, len(input_y_list)):
            input_y_list[j] = 1 / numpy.exp(-(input_y_list[j] - bias_list_input[j]))

        print("Crapa aici 2")
        # Calculare y de pe stratul final, adica iesirile reale de pe stratul final/output
        output_y_list = numpy.dot(input_y_list, w_matrix_output)
        for j in range(0, len(output_y_list)):
            output_y_list[j] = 1 / numpy.exp(-(output_y_list[j] - bias_list_output[j]))

        # Calculare eroare pt inputul curent, calcularea gradientului erorii, update w_output si bias_output
        gradient_list = []
        for j in range(0, len(output_y_list)):
            error_matrix[i][j] = output_expected[i][j] - output_y_list[j]
            MSE += math.pow(error_matrix[i][j], 2)
            gradient_list[j] = output_y_list[j] * (1 - output_y_list) * error_matrix[i][j]
            for k in range(0, hidden_layer_number):
                w_matrix_output[k][j] = rata_de_invatare * input_y_list[k] * gradient_list[j]
            bias_list_output[j] = - (rata_de_invatare * gradient_list[j])

        #Calculare gradienti,w_input,bias_input
        input_gradient_list = []
        for j in range(0, len(input_y_list)):
            input_gradient_list[j] = input_y_list[j] * (1 - input_y_list) * suma_gradient_input(gradient_list, j)
            for k in range(0, input_number):
                w_matrix_input[k][j] += rata_de_invatare * input_tested[i][k] * input_gradient_list[j]
            bias_list_input[j] += -(rata_de_invatare * input_gradient_list[j])


        
