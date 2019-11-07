import copy
from anytree import AnyNode
import heuristic_white
import util
import pygame

algorithm = ""
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
            game.white_pawn_list[i] = pos
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
                # choose_node = min_max_algorithm(game, 2)
                choose_node = alpha_beta_pruning(game, 2)
                black_turn(choose_node.new_move, screen)
                delete_element(choose_node.last_move, screen)
                game = copy.deepcopy(choose_node.game)
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
    root = AnyNode(id="/root", game=game, cost=0)
    next_root = [root]
    new_root_list = []
    current_level = 1
    aux_level = level
    while aux_level > 0:
        for roots in next_root:
            if aux_level > 0:
                for i in build_black_level(copy.deepcopy(roots.game), roots.id, current_level, roots):
                    for j in build_white_level(copy.deepcopy(i.game), i.id, current_level, i):
                        new_root_list.append(j)
            else:
                break
        next_root.clear()
        next_root = copy.copy(new_root_list)
        aux_level -= 1
        current_level += 1
    leaves = util.get_all_leave(root, level)
    aux_level = level
    for leave in leaves:
        heuristic_white.heuristic_function(leave)
    turn = 0
    while aux_level > 0:
        if turn == 0:
            level_nodes = util.get_black_nodes_level(root, aux_level)
            for nod in level_nodes:
                node_child = list(nod.children)
                if len(node_child) > 0:
                    node_child.sort(key=lambda nod_b: nod_b.cost, reverse=True)
                    nod.cost = node_child[0].cost
            turn = 1
            aux_level -= 1
        else:
            level_nodes = util.get_white_nodes_level(root, aux_level)
            for nod in level_nodes:
                node_child1 = list(nod.children)
                if len(node_child1) > 0:
                    node_child1.sort(key=lambda nod_c: nod_c.cost, reverse=False)
                    nod.cost = node_child1[0].cost
            turn = 0
    root_child = list(root.children)
    root_child.sort(key=lambda nod_b: nod_b.cost, reverse=False)
    return root_child[0]


def alpha_beta_pruning(game, level):
    root = AnyNode(id="/root", game=game, cost=0)
    next_root = [root]
    new_root_list = []
    current_level = 1
    aux_level = level
    while aux_level > 0:
        for roots in next_root:
            if aux_level > 0:
                for i in build_black_level(copy.deepcopy(roots.game), roots.id, current_level, roots):
                    for j in build_white_level(copy.deepcopy(i.game), i.id, current_level, i):
                        new_root_list.append(j)
            else:
                break
        next_root.clear()
        next_root = copy.copy(new_root_list)
        aux_level -= 1
        current_level += 1
    black_level = util.get_black_nodes_level(root, level)
    end = 0
    tmp = 0
    maxim = 0
    for i in black_level:
        if len(i.children) > 0 and end == 0:
            auxiliar = list(i.children)
            for j in auxiliar:
                heuristic_white.heuristic_function(j)
            auxiliar.sort(key=lambda nod: nod.cost, reverse=True)
            i.cost = auxiliar[0].cost
            maxim = auxiliar[0].cost
            end = 1
        elif end == 1 and tmp == 1:
            auxiliar = list(i.children)
            if len(auxiliar) > 0:
                for j in auxiliar:
                    heuristic_white.heuristic_function(j)
                    if j.cost >= maxim:
                        i.cost = j.cost
                        break
                if i.cost == 0:
                    auxiliar.sort(key=lambda nod: nod.cost, reverse=True)
                    i.cost = auxiliar[0].cost
        tmp = 1
    level -= 1
    util.update_line_values(root, level, 1)
    root_child = list(root.children)
    root_child.sort(key=lambda nod_b: nod_b.cost, reverse=False)
    return root_child[0]


if __name__ == "__main__":
    initialize()
