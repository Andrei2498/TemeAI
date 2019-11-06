import copy
from anytree.cachedsearch import findall


defense_patterns = {(1, 0, -1, 0, 0, 0, 1, 0, 1): 10, (-1, 0, 1, 0, 0, 0, 1, 0, 1): 10,
                    (-1, 1, -1, 0, 0, 0, 0, 0, 1): -5, (1, 0, -1, 0, 0, 0, 0, 0, 1): 10,
                    (-1, 0, 1, 0, 0, 0, 0, 0, 1): 0, (1, 0, -1, 0, 0, 0, 0, 0, 0): 3,
                    (-1, 0, 1, 0, 0, 0, 0, 0, 0): 3, (1, -1, -1, 0, 0, 0, 1, 0, 1): 5,
                    (-1, -1, 1, 0, 0, 0, 1, 0, 1): 5, (-1, 1, -1, 0, 0, 0, 1, 0, 1): 5}

initial_patterns_white = {(0, 1, 0, 1, 0, 1, 0, 0, 0): 5, (1, 0, 0, 0, 1, 1, 0, 0, 0): 5, (0, 0, 1, 1, 1, 0, 0, 0, 0): 5,
                    (0, 0, 0, 0, 1, 0, 0, 0, 0): 4, (0, 0, 0, 1, 0, 0, 0, 0, 0): 4, (0, 0, 0, 0, 0, 1, 0, 0, 0): 4,
                    (0, 0, 0, 0, 1, 0, 0, 0, 1): 5, (0, 0, 0, 0, 1, 0, 1, 0, 0): 5, (0, 0, 0, 1, 0, 0, 0, 1, 0): 5,
                    (0, 0, 0, 0, 0, 1, 0, 1, 0): 5, (0, 0, 0, 1, 0, 0, 0, 0, 1): 5, (0, 0, 0, 0, 0, 1, 1, 0, 0): 5,
                    (0, 0, 0, 0, 1, 0, 1, 0, 1): 6, (0, 0, 0, 1, 0, 0, 0, 1, 1): 6, (0, 0, 0, 0, 0, 1, 1, 1, 0): 6,
                    (0, 0, 0, 0, 1, 1, 1, 0, 0): 7, (0, 0, 0, 1, 1, 0, 0, 0, 1): 7, (0, 0, 0, 1, 1, 0, 0, 0, 1): 7,
                    (0, 0, 0, 1, 0, 1, 0, 0, 1): 7, (0, 0, 0, 1, 0, 1, 0, 1, 0): 7, (0, 0, 0, 0, 1, 1, 1, 0, 0): 7}

initial_black_patterns = {(0, -1, 0, -1, 0, -1, 0, 0, 0): -3, (-1, 0, 0, 0, -1, -1, 0, 0, 0): -3, (0, 0, -1, -1, -1, 0, 0, 0, 0): -3,
                          (0, 0, 0, 0, -1, 0, 0, 0, 0): -2, (0, 0, 0, -1, 0, 0, 0, 0, 0): -2, (0, 0, 0, 0, 0, -1, 0, 0, 0): -2,
                          (0, 0, 0, 0, -1, 0, 0, 0, -1): -3, (0, 0, 0, 0, -1, 0, -1, 0, 0): -3, (0, 0, 0, -1, 0, 0, 0, -1, 0): -3,
                          (0, 0, 0, 0, 0, -1, 0, -1, 0): -3, (0, 0, 0, -1, 0, 0, 0, 0, -1): -3, (0, 0, 0, 0, 0, -1, -1, 0, 0): -3,
                          (0, 0, 0, 0, -1, 0, -1, 0, -1): -4, (0, 0, 0, -1, 0, 0, 0, -1, -1): -4, (0, 0, 0, 0, 0, -1, -1, -1, 0): -4,
                          (0, 0, 0, 0, -1, -1, -1, 0, 0): -5, (0, 0, 0, -1, -1, 0, 0, 0, -1): -5, (0, 0, 0, -1, -1, 0, 0, 0, -1): -5,
                          (0, 0, 0, -1, 0, -1, 0, 0, -1): -5, (0, 0, 0, -1, 0, -1, 0, -1, 0): -5, (0, 0, 0, 0, -1, -1, -1, 0, 0): -5}

attack_patterns = {(0, 1, 0, 1, 0, 1, 0, 0, 0): 5, (1, 0, 0, 0, 1, 1, 0, 0, 0): 5, (0, 0, 1, 1, 1, 0, 0, 0, 0): 5,
                   (0, 0, 0, 0, 1, 0, 0, 0, 0): 10, (-1, 0, 0, 0, 1, 0, 0, 0, 0): -5, (0, 0, -1, 0, 1, 0, 0, 0, 0): -5,
                   (-1, 0, -1, 0, 1, 0, 0, 0, 0): -10, (-1, 0, 0, 0, 1, 0, 0, 0, 1): 1, (-1, 0, 0, 0, 1, 0, 1, 0, 1): 5,
                   (-1, 0, -1, 0, 1, 0, 1, 0, 0): 0, (0, -1, 0, -1, 1, 0, 0, 0, 0): -5, (0, 0, 0, -1, 1, 0, 0, 0, 0): 6,
                   (0, 0, 0, -1, 1, -1, 0, 0, 0): 7, (0, -1, 0, -1, 1, -1, 0, 0, 0): -6, (-1, -1, -1, 0, 1, 0, 0, 0, 0): -7}


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
            available_white.append((state, (state[0] - 1, state[1] + 1)))
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


def get_id_by_level_and_player(level, player):
    result = "/root"
    current_level = 1
    while level > 0:
        if player is "white":
            result += "/black_move_" + str(current_level) + "/white_move_" + str(current_level)
        elif player is "black":
            if level == 1:
                result += "/black_move_" + str(current_level)
            else:
                result += "/black_move_" + str(current_level) + "/white_move_" + str(current_level)
        level -= 1
        current_level += 1
    return result


def get_all_leave(root, level):
    text_id = get_id_by_level(level)
    return list(findall(root, filter_=lambda node: node.id == text_id))


def get_node_by_player_and_move(root, parent, player_color, move):
    id = get_id_by_level_and_player(move, player_color)
    return list(findall(root, filter_=lambda node: node.id == id and node.parent == parent))


def get_black_nodes_level(root, level):
    id = get_id_by_level_and_player(level, "black")
    return list(findall(root, filter_=lambda node: node.id == id))


def get_white_nodes_level(root, level):
    id = get_id_by_level_and_player(level, "white")
    return list(findall(root, filter_=lambda node: node.id == id))


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


def board_patterns(updated_game, i, j):
    current_board = []
    current_board.append(convert_position_type_in_number((i + 2, j), updated_game))
    current_board.append(convert_position_type_in_number((i + 2, j + 1), updated_game))
    current_board.append(convert_position_type_in_number((i + 2, j + 2), updated_game))

    current_board.append(convert_position_type_in_number((i + 1, j), updated_game))
    current_board.append(convert_position_type_in_number((i + 1, j + 1), updated_game))
    current_board.append(convert_position_type_in_number((i + 1, j + 2), updated_game))

    current_board.append(convert_position_type_in_number((i, j), updated_game))
    current_board.append(convert_position_type_in_number((i, j + 1), updated_game))
    current_board.append(convert_position_type_in_number((i, j + 2), updated_game))
    return current_board


if __name__ == "__main__":
    print(get_id_by_level_and_player(2, "black"))
