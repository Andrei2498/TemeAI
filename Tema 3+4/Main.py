import pygame


class Game:
    # white_pawn_dictionary = {}
    # black_pawn_dictionary = {}
    white_pawn_list = []
    black_pawn_list = []
    white_pawn_position = (0, 0)
    list_of_available_boxes = []

    def __init__(self):
        self.white_pawn_list = [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
        self.black_pawn_list = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (1, 5), (3, 5)]
        # self.white_pawn_dictionary = {0: (8, 308), 1: (58, 308), 2: (108, 308), 3: (158, 308),
        #                               4: (208, 308), 5: (258, 308), 6: (308, 308), 7: (358, 308)}
        # self.black_pawn_dictionary = {0: (8, 58), 1: (58, 58), 2: (108, 58), 3: (158, 58),
        #                               4: (208, 58), 5: (258, 58), 6: (308, 58), 7: (358, 58)}


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
    screen.blit(black_pawn, (58, 258))
    screen.blit(black_pawn, (158, 258))


def initialize():
    pygame.init()
    pygame.display.set_caption('Cross the Board')
    icon = pygame.image.load("chess.png")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((400, 400))
    game = Game()
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


def play(game, screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                event_handler(event.pos, screen, game)
            elif event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    initialize()

