import util


def heuristic_function(leave):
    cost = 0
    state_situation = util.is_final(leave.game)
    if state_situation == 0:
        leave.cost = 0
    elif state_situation == 1:
        leave.cost = 200
    elif state_situation == 2:
        leave.cost = -200
    elif state_situation == -1:
        leave.cost = calculate_attack_and_defense_position(leave.new_move, leave.last_move, leave.game)


def calculate_attack_and_defense_position(new_position, last_position, updated_game):
    cost = 0
    # Defense 1 - 3
    if 4 <= last_position[1] <= 6:
        cost += defensive_game_style(new_position, last_position, updated_game)
    # Offensive
    else:
        cost += offensive_game_style(new_position, last_position, updated_game)
    return cost


def defensive_game_style(new_position, last_position, updated_game):
    cost = 0
    for i in [6, 5, 4, 3]:
        for j in [0, 1, 2, 3, 4, 5]:
            current_board = util.board_patterns(updated_game, i, j)
            if tuple(current_board) in util.defense_patterns:
                cost += util.defense_patterns.get(tuple(current_board))
            if tuple(current_board) in util.initial_patterns_white:
                cost += util.initial_patterns_white.get(tuple(current_board))
    for i in [1, 2, 3, 4]:
        for j in [0, 1, 2, 3, 4, 5]:
            current_board = util.board_patterns(updated_game, i, j)
            if tuple(current_board) in util.initial_black_patterns:
                cost += util.initial_black_patterns.get(tuple(current_board))
    return cost


def offensive_game_style(new_position, last_position, updated_game):
    cost = 0
    for i in [3, 2, 1]:
        for j in [0, 1, 2, 3, 4, 5]:
            current_board = util.board_patterns(updated_game, i, j)
            if tuple(current_board) in util.attack_patterns:
                cost += util.attack_patterns.get(tuple(current_board))
    return cost


def number_of_enemy_on_position(state, game):
    count = 0
    if 1 <= state[0] <= 6:
        if (state[0] - 1, state[1] - 1) in game.black_pawn_list:
            count += 1
        if (state[0] + 1, state[1] - 1) in game.black_pawn_list:
            count += 1
    elif state[0] == 0:
        if (state[0] + 1, state[1] - 1) in game.black_pawn_list:
            count += 1
    elif state[0] == 7:
        if (state[0] - 1, state[1] - 1) in game.black_pawn_list:
            count += 1
    return count


def paw_from_column(state, game):
    enemy = 0
    ally = 0
    for i in range(0, 8):
        if (state[0], i) in game.white_pawn_list:
            ally += 1
        if (state[0], i) in game.black_pawn_list:
            enemy += 1
    return ally, enemy


def pawns_in_defense(position, game):
    cnt = 0
    if 1 <= position[0] <= 6:
        if (position[0] + 1, position[1] + 1) in game.white_pawn_list:
            cnt += 1
        if (position[0] - 1, position[1] + 1) in game.white_pawn_list:
            cnt += 1
    elif position[0] == 0:
        if (position[0] + 1, position[1] + 1) in game.white_pawn_list:
            cnt += 1
    elif position[0] == 7:
        if (position[0] - 1, position[1] + 1) in game.white_pawn_list:
            cnt += 1
    return cnt
