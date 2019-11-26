inputuri_ramase = len(test_case)
    procesat = 0
    error_list = []
    eroare = 0.0
    erorare_medie = 0.0
    while inputuri_ramase > 0:
        expexted_exit = out_c[procesat]
        for i in range(0, numar_neuroni):
            temp_result = 1.0
            aux = 0.0
            for j in range(0, len(w_matrix_int[i])):
                aux += w_matrix_int[i][j] * test_case[procesat][j]
            temp_result = 1 / (1 + numpy.exp(-(aux - teta_strat_ascuns[i])))
            neuroni_interni_output[i] = round(temp_result, 4)
        for i in range(0, numar_neuroni):
            temp_result = 1.0
            aux = 0.0
            for j in range(0, len(out_c)):
                aux += w_matrix_out[i][j] * neuroni_interni_output[i]
            temp_result = 1 / (1 + numpy.exp(-(aux - teta_strat_final[i])))
            neuroni_iesire_output[i] = round(temp_result, 4)
        for i in range(0, len(out_c[procesat])):
            eroare = out_c[procesat][i] - neuroni_iesire_output[i]
            error_list.append(eroare)
        error_matrix.append(error_list)
        MSE = sum(error_list)
        # print(MSE)
        # print(error_list)
        inputuri_ramase -= 1
        procesat += 1
        error_list.clear()
    # print(error_matrix)
    print(neuroni_interni_output)