import copy
import time
from anytree import AnyNode, RenderTree, AsciiStyle
from anytree.cachedsearch import findall

import heuristic_white
import util
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
        return "White list: " + self.white_pawn_list.__str__() + " Black list: " + self.black_pawn_list.__str__()

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
        if util.is_final(game) == -1:
            if game.turn == 1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        event_handler(event.pos, screen, game)
                    elif event.type == pygame.QUIT:
                        running = False
            else:
                min_max_algorithm(game, 2)
                game.turn = 1
        else:
            running = False


def build_white_level(game, id, level, root):
    node_list = []
    white_possible_moves = util.get_all_available_white(game)
    for index in white_possible_moves:
        node_list.append(AnyNode(parent=root, id=(id + "/white_move_" + str(level)), game=util.return_new_state_after_move_white(index[0], index[1], game), new_move=index[1], last_move=index[0], cost=0))
    return node_list


def build_black_level(game, id, level, root):
    node_list = []
    white_possible_moves = util.get_all_available_black(game)
    for index in white_possible_moves:
        node_list.append(AnyNode(parent=root, id=(id + "/black_move_" + str(level)), game=util.return_new_state_after_move_black(index[0], index[1], game), new_move=index[1], last_move=index[0], cost=0))
    return node_list


def min_max_algorithm(game, level):
    root = AnyNode(id="/root", game=game)
    next_root = [root]
    new_root_list = []
    current_level = 1
    aux_level = level
    while aux_level > 0:
        for roots in next_root:
            if aux_level > 0:
                for i in build_black_level(roots.game, roots.id, current_level, roots):
                    for j in build_white_level(i.game, i.id, current_level, i):
                        new_root_list.append(j)
            else:
                break
        next_root.clear()
        next_root = copy.copy(new_root_list)
        aux_level -= 1
        current_level += 1
    leaves = util.get_all_leave(root, level)
    for leave in leaves:
        heuristic_white.heuristic_function(leave)
        print(leave)
    # print(leaves)


if __name__ == "__main__":
    # start_time = time.time()
    # game = Game([(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)], [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)])
    # min_max_algorithm(game, 2)
    # print(time.time() - start_time)
    initialize()
