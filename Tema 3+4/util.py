import copy
from anytree.cachedsearch import findall

defense_patterns = {(1, 0, -1, 0, 0, 0, 1, 0, 1): 10, (-1, 0, 1, 0, 0, 0, 1, 0, 1): 10, (-1, 1, -1, 0, 0, 0, 1, 0, 1): 5, (-1, 1, -1, 0, 0, 0, 0, 0, 1): -5,
                    (1, 0, -1, 0, 0, 0, 0, 0, 1): 10, (-1, 0, 1, 0, 0, 0, 0, 0, 1): 0, (1, 0, -1, 0, 0, 0, 0, 0, 0): 3, (-1, 0, 1, 0, 0, 0, 0, 0, 0): 3,
                    (1, -1, -1, 0, 0, 0, 1, 0, 1): 5, (-1, -1, 1, 0, 0, 0, 1, 0, 1): 5}

attack_patterns = {(0, 1, 0, 1, 0, 1, 0, 0, 0): 5, (1, 0, 0, 0, 1, 1, 0, 0, 0): 5, (0, 0, 1, 1, 1, 0, 0, 0, 0): 5}


def get_all_available_white(game):
    available_white = []
    for state in game.white_pawn_list:
        if (state[0], state[1] - 1) not in game.white_pawn_list and (state[0], state[1] - 1) not in game.black_pawn_list:
            available_white.append((state, (state[0], state[1] - 1)))
        if (state[0] + 1, state[1] - 1) not in game.white_pawn_list and (state[0] + 1, state[1] - 1) in game.black_pawn_list and (state[0] == 0 or 1 <= state[0] <= 6):
            available_white.append((state, (state[0] + 1, state[1] - 1)))
        if (state[0] - 1, state[1] - 1) not in game.white_pawn_list and (state[0] - 1, state[1] - 1) in game.black_pawn_list and (state[0] == 7 or 1 <= state[0] <= 6):
            available_white.append((state, (state[0] - 1, state[1] - 1)))
    return available_white


def get_all_available_black(game):
    available_white = []
    for state in game.black_pawn_list:
        if (state[0], state[1] + 1) not in game.black_pawn_list and (state[0], state[1] + 1) not in game.white_pawn_list:
            available_white.append((state, (state[0], state[1] + 1)))
        if (state[0] + 1, state[1] + 1) not in game.black_pawn_list and (state[0] + 1, state[1] + 1) in game.white_pawn_list and (state[0] == 0 or 1 <= state[0] <= 6):
            available_white.append((state, (state[0] + 1, state[1] + 1)))
        if (state[0] - 1, state[1] + 1) not in game.black_pawn_list and (state[0] - 1, state[1] + 1) in game.white_pawn_list and (state[0] == 7 or 1 <= state[0] <= 6):
            available_white.append((state, (state[0] - 1, state[1] - 1)))
    return available_white


def return_new_state_after_move_white(old_position, position, current_game):
    new_game = copy.deepcopy(current_game)
    new_game.white_pawn_list.remove(old_position)
    new_game.white_pawn_list.append(position)
    if position in new_game.black_pawn_list:
        new_game.black_pawn_list.remove(position)
    return new_game


def return_new_state_after_move_black(old_position, position, current_game):
    new_game = copy.deepcopy(current_game)
    new_game.black_pawn_list.remove(old_position)
    new_game.black_pawn_list.append(position)
    if position in new_game.white_pawn_list:
        new_game.white_pawn_list.remove(position)
    return new_game


def get_id_by_level(level):
    result = "/root"
    current_level = 1
    while level > 0:
        result += "/black_move_" + str(current_level) + "/white_move_" + str(current_level)
        current_level += 1
        level -= 1
    return result


def get_all_leave(root, level):
    text_id = get_id_by_level(level)
    return list(findall(root, filter_=lambda node: node.id == text_id))


"""
    0 -> Draw
    1 -> Player win
    2 -> Computer win
    -1 -> Not final state
"""
def is_final(game):
    draw = 1
    black_locked_paw = 0
    white_locked_paw = 0
    for state in game.white_pawn_list:
        if state[1] == 0:
            print("Player won the game!")
            return 1
        if (state[0], state[1] + 1) not in game.black_pawn_list:
            draw = 0
        else:
            black_locked_paw += 1
            white_locked_paw += 1
    for state in game.black_pawn_list:
        if state[1] == 7:
            print("Computer won the game!")
            return 2
    if white_locked_paw == black_locked_paw and white_locked_paw == len(game.white_pawn_list) and black_locked_paw == len(game.black_pawn_list):
        print("Draw")
        return 0
    if len(game.black_pawn_list) == 1 and len(game.white_pawn_list) == 1 and game.white_pawn_list[0][1] == game.black_pawn_list[0][1] + 1 and draw == 1:
        print("Draw")
        return 0
    if len(game.black_pawn_list) == 0:
        print("Player won the game!")
        return 1
    if len(game.white_pawn_list) == 0:
        print("Computer won the game!")
        return 2
    return -1


def convert_position_type_in_number(position, game):
    if position in game.white_pawn_list:
        return 1
    elif position in game.black_pawn_list:
        return -1
    else:
        return 0