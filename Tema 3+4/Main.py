import copy

import pygame


class Game:
    white_pawn_list = []
    black_pawn_list = []
    white_pawn_position = (0, 0)
    black_pawn_position = (0, 0)
    list_of_available_boxes = []
    turn = 1

    def __init__(self, white_list, black_list):
        self.white_pawn_list = white_list
        self.black_pawn_list = black_list

    def __str__(self):
        return "White list: " + self.white_pawn_list.__str__() + "\n Black list: " + self.black_pawn_list.__str__()

    def __deepcopy__(self, memo):
        return Game(copy.deepcopy(self.white_pawn_list), copy.deepcopy(self.black_pawn_list))

    def get_white_list(self):
        return self.white_pawn_list

    def get_black_list(self):
        return self.black_pawn_list


def draw_single_box(x, y, screen, rect):
    if x % 2 == 0 and y % 2 == 0:
        pygame.draw.rect(screen, (255, 255, 255), rect)
    elif x % 2 == 0 and not y % 2 == 0:
        pygame.draw.rect(screen, (128, 64, 0), rect)
    elif not x % 2 == 0 and y % 2 == 0:
        pygame.draw.rect(screen, (128, 64, 0), rect)
    else:
        pygame.draw.rect(screen, (255, 255, 255), rect)


def draw_board(screen):
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(x * 50, y * 50, 50, 50)
            draw_single_box(x, y, screen, rect)


def draw_pieces(screen):
    black_pawn = pygame.image.load("black_pawn.png").convert_alpha()
    white_pawn = pygame.image.load("white_pawn.png").convert_alpha()
    for i in range(8):
        screen.blit(black_pawn, (8 + 50*i, 58))
        screen.blit(white_pawn, (8 + 50*i, 308))
    # screen.blit(black_pawn, (58, 258))
    # screen.blit(black_pawn, (158, 258))


def initialize():
    pygame.init()
    pygame.display.set_caption('Cross the Board')
    icon = pygame.image.load("chess.png")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((400, 400))
    game = Game([(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)], [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)])
    draw_board(screen)
    draw_pieces(screen)
    pygame.display.update()
    play(game, screen)


def delete_element(pos, screen):
    rect = pygame.Rect(pos[0] * 50, pos[1] * 50, 50, 50)
    draw_single_box(pos[0], pos[1], screen, rect)
    pygame.display.update()


def draw_available_box(screen, pos, has_piece):
    black_pawn = pygame.image.load("black_pawn.png").convert_alpha()
    if not has_piece:
        rect = pygame.Rect(pos[0] * 50, pos[1] * 50, 50, 50)
        pygame.draw.rect(screen, (45, 185, 45), rect)
    if has_piece:
        rect = pygame.Rect(pos[0] * 50, pos[1] * 50, 50, 50)
        pygame.draw.rect(screen, (45, 185, 45), rect)
        screen.blit(black_pawn, (8 + 50 * pos[0], 8 + 50 * pos[1]))


def show_available_boxes(pos, screen, game):
    if not ((pos[0], pos[1] - 1) in game.white_pawn_list or (pos[0], pos[1] - 1) in game.black_pawn_list):
        draw_available_box(screen, (pos[0], pos[1] - 1), False)
        game.list_of_available_boxes.append((pos[0], pos[1] - 1))
    if (pos[0] + 1, pos[1] - 1) in game.black_pawn_list:
        draw_available_box(screen, (pos[0] + 1, pos[1] - 1), True)
        game.list_of_available_boxes.append((pos[0] + 1, pos[1] - 1))
    if (pos[0] - 1, pos[1] - 1) in game.black_pawn_list:
        draw_available_box(screen, (pos[0] - 1, pos[1] - 1), True)
        game.list_of_available_boxes.append((pos[0] - 1, pos[1] - 1))
    pygame.display.update()


def reset_available_boxes(screen, game):
    black_pawn = pygame.image.load("black_pawn.png").convert_alpha()
    for i in game.list_of_available_boxes:
        if i in game.black_pawn_list:
            rect = pygame.Rect(i[0] * 50, i[1] * 50, 50, 50)
            draw_single_box(i[0], i[1], screen, rect)
            screen.blit(black_pawn, (8 + 50 * i[0], 8 + 50 * i[1]))
        else:
            rect = pygame.Rect(i[0] * 50, i[1] * 50, 50, 50)
            draw_single_box(i[0], i[1], screen, rect)
    game.list_of_available_boxes.clear()
    pygame.display.update()


def move_piece(pos, screen, game):
    white_pawn = pygame.image.load("white_pawn.png").convert_alpha()
    rect = pygame.Rect(pos[0] * 50, pos[1] * 50, 50, 50)
    draw_single_box(pos[0], pos[1], screen, rect)
    screen.blit(white_pawn, (8 + 50 * pos[0], 8 + 50 * pos[1]))
    if pos in game.black_pawn_list:
        game.black_pawn_list.remove(pos)
    for i in range(0, len(game.white_pawn_list)):
        if game.white_pawn_list[i] == game.white_pawn_position:
            print(game.white_pawn_list[i])
            game.white_pawn_list[i] = pos
            print(game.white_pawn_list[i])
    game.list_of_available_boxes.remove(pos)
    delete_element(game.white_pawn_position, screen)


def event_handler(pos, screen, game):
    x = int(pos[0] / 50)
    y = int(pos[1] / 50)
    if (x, y) in game.white_pawn_list:
        reset_available_boxes(screen, game)
        show_available_boxes((x, y), screen, game)
        game.white_pawn_position = (x, y)
    elif (x, y) in game.list_of_available_boxes:
        move_piece((x, y), screen, game)
        reset_available_boxes(screen, game)
        game.turn = 2


def black_turn(pos, screen):
    black_pawn = pygame.image.load("black_pawn.png").convert_alpha()
    rect = pygame.Rect(pos[0] * 50, pos[1] * 50, 50, 50)
    draw_single_box(pos[0], pos[1], screen, rect)
    screen.blit(black_pawn, (8 + 50 * pos[0], 8 + 50 * pos[1]))


def play(game, screen):
    running = True
    while running:
        if not is_final(game):
            if game.turn == 1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        event_handler(event.pos, screen, game)
                    elif event.type == pygame.QUIT:
                        running = False
            else:
                print(heuristic_function(game))
                game_list = calculate_states(game)
                if len(game_list) == 0 and len(game.black_pawn_list) == len(game.white_pawn_list):
                    running = False
                    print("Draw")
                elif len(game_list) == 0 and len(game.black_pawn_list) < len(game.white_pawn_list):
                    running = False
                    print("Player won the game!")
                elif len(game_list) > 0:
                    sorted(game_list, key=lambda state: state[1])
                    set_minus = set(game.black_pawn_list).difference(set(game_list[0][0].black_pawn_list))
                    game.black_pawn_position = list(set_minus)[0]
                    set_minus_reverse = set(game_list[0][0].black_pawn_list).difference(set(game.black_pawn_list))
                    black_pawn_position_after = list(set_minus_reverse)[0]
                    game.white_pawn_list = game_list[0][0].white_pawn_list
                    game.black_pawn_list = game_list[0][0].black_pawn_list
                    black_turn(black_pawn_position_after, screen)
                    delete_element(game.black_pawn_position, screen)
                    print(game.black_pawn_list)
                    game.turn = 1
        else:
            running = False


def is_final(game):
    for state in game.white_pawn_list:
        if state[1] == 0:
            print("Player won the game!")
            return True
    for state in game.black_pawn_list:
        if state[1] == 7:
            print("Computer won the game!")
            return True
    if len(game.black_pawn_list) == 1 and len(game.white_pawn_list) == 1 and game.white_pawn_list[0][1] == game.black_pawn_list[0][1] + 1:
        print("Draw")
        return True
    if len(game.black_pawn_list) == 0:
        print("Player won the game!")
        return True
    if len(game.white_pawn_list) == 0:
        print("Computer won the game!")
        return True
    return False


def heuristic_function(game):
    cost = 0
    for state in game.black_pawn_list:
        cost += state[1]
    for state in game.white_pawn_list:
        cost -= (7 - state[1])
    for position in game.black_pawn_list:
        cost += calculate_attack_and_defense_position(position, game)
    # comentariu pentru Andrei
    # pentru orice pozitie
    last_state = (3, 1)
    state = (3, 2) # am modificat pionul de pe (3, 6)
    cost += calculate_attack_and_defense_position(state, game.black_pawn_list.remove(last_state))
    return cost


def calculate_attack_and_defense_position(state, game):
    cost = 0
    if 1 <= state[0] <= 6:
        if game.white_pawn_list.count((state[0] + 1, state[1] + 1)) == 1:
            cost -= 1
        if game.white_pawn_list.count((state[0] - 1, state[1] + 1)) == 1:
            cost -= 1
        if game.black_pawn_list.count((state[0] - 1, state[1] - 1)) == 1:
            cost += 1
        if game.black_pawn_list.count((state[0] + 1, state[1] - 1)) == 1:
            cost += 1
    if state[0] == 0:
        if game.white_pawn_list.count((state[0] + 1, state[1] + 1)) == 1:
            cost -= 1
        elif game.black_pawn_list.count((state[0] + 1, state[1] - 1)) == 1:
            cost += 1
    if state[0] == 7:
        if game.black_pawn_list.count((state[0] - 1, state[1] - 1)) == 1:
            cost += 1
        elif game.white_pawn_list.count((state[0] - 1, state[1] + 1)) == 1:
            cost -= 1
    return cost


def create_new_game(white_list, black_list):
    game = Game(white_list, black_list)
    return game


def calculate_states(game):
    lst = []
    for it in game.black_pawn_list:
        auxiliar_state = get_available_position(it, game)
        for i in auxiliar_state:
            new_game = copy.deepcopy(game)
            new_game.black_pawn_list[new_game.black_pawn_list.index(it)] = i
            if new_game.white_pawn_list.count(i) > 0:
                new_game.white_pawn_list.remove(i)
            lst.append((new_game, heuristic_function(new_game)))
    return lst


def get_available_position(state, game):
    state_list = []
    if state[0] == 0:
        if game.white_pawn_list.count((state[0], state[1] + 1)) == 0 and game.black_pawn_list.count((state[0], state[1] + 1)) == 0:
            state_list.append((state[0], state[1] + 1))
        if game.white_pawn_list.count((state[0] + 1, state[1] + 1)) == 1 and game.black_pawn_list.count((state[0] + 1, state[1] + 1)) == 0:
            state_list.append((state[0] + 1, state[1] + 1))
    if state[0] == 7:
        if game.white_pawn_list.count((state[0], state[1] + 1)) == 0 and game.black_pawn_list.count((state[0], state[1] + 1)) == 0:
            state_list.append((state[0], state[1] + 1))
        if game.white_pawn_list.count((state[0] - 1, state[1] + 1)) == 1 and game.black_pawn_list.count((state[0] - 1, state[1] + 1)) == 0:
            state_list.append((state[0] - 1, state[1] + 1))
    if 1 <= state[0] <= 6:
        if game.white_pawn_list.count((state[0], state[1] + 1)) == 0 and game.black_pawn_list.count((state[0], state[1] + 1)) == 0:
            state_list.append((state[0], state[1] + 1))
        if game.white_pawn_list.count((state[0] - 1, state[1] + 1)) == 1 and game.black_pawn_list.count((state[0] - 1, state[1] + 1)) == 0:
            state_list.append((state[0] - 1, state[1] + 1))
        if game.white_pawn_list.count((state[0] + 1, state[1] + 1)) == 1 and game.black_pawn_list.count((state[0] + 1, state[1] + 1)) == 0:
            state_list.append((state[0] + 1, state[1] + 1))
    return state_list


if __name__ == "__main__":
    initialize()
