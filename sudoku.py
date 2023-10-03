import pygame
from board import Board
from sudoku_generator import generate_sudoku


def draw_welcome(screen, width, height):
    welcome_message = pygame.font.SysFont('Corbel', 60)
    welcome_text = welcome_message.render('Welcome to Sudoku!', True, (0, 0, 0))
    screen.blit(welcome_text, (150, 200))

    difficulty_mess = pygame.font.SysFont('Corbel', 45)
    difficulty_text = difficulty_mess.render('Select Game Mode:', True, (0, 0, 0))
    screen.blit(difficulty_text, (220, 350))

    easy_mess = pygame.font.SysFont('Corbel', 35, bold=True)
    easy_text = easy_mess.render('Easy', True, (0, 0, 0))

    medium_mess = pygame.font.SysFont('Corbel', 35, bold=True)
    medium_text = medium_mess.render('Medium', True, (0, 0, 0))

    hard_mess = pygame.font.SysFont('Corbel', 35, bold=True)
    hard_text = hard_mess.render('Hard', True, (0, 0, 0))

    # Green button
    pygame.draw.rect(screen, (0, 0, 0), [width / 6 - 5, height - 305, 160, 80])
    pygame.draw.rect(screen, (0, 255, 0), [width / 6, height - 300, 150, 70])
    screen.blit(easy_text, (172, 618))

    # Yellow button
    pygame.draw.rect(screen, (0, 0, 0), [width - 476.5, height - 305, 160, 80])
    pygame.draw.rect(screen, (255, 255, 0), [width - 471.5, height - 300, 150, 70])
    screen.blit(medium_text, (340, 618))

    # Red button
    pygame.draw.rect(screen, (0, 0, 0), [width - 280, height - 305, 160, 80])
    pygame.draw.rect(screen, (255, 0, 0), [width - 275, height - 300, 150, 70])
    screen.blit(hard_text, (562.5, 618))


def general_level(screen, board, running, width, height):
    click_count = 0
    reset_mess = pygame.font.SysFont('Corbel', 35, bold=True)
    reset_text = reset_mess.render('Reset', True, (0, 0, 0))
    restart_mess = pygame.font.SysFont('Corbel', 35, bold=True)
    restart_text = restart_mess.render('Restart', True, (0, 0, 0))
    exit_mess = pygame.font.SysFont('Corbel', 35, bold=True)
    exit_text = exit_mess.render('Exit', True, (0, 0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    board.sketch(1)
                if event.key == pygame.K_2:
                    board.sketch(2)
                if event.key == pygame.K_3:
                    board.sketch(3)
                if event.key == pygame.K_4:
                    board.sketch(4)
                if event.key == pygame.K_5:
                    board.sketch(5)
                if event.key == pygame.K_6:
                    board.sketch(6)
                if event.key == pygame.K_7:
                    board.sketch(7)
                if event.key == pygame.K_8:
                    board.sketch(8)
                if event.key == pygame.K_9:
                    board.sketch(9)
                if event.key == pygame.K_DOWN:
                    row_clicked += 1
                    if row_clicked > 8:
                        row_clicked = 0
                    board.select(row_clicked, col_clicked)
                if event.key == pygame.K_UP:
                    row_clicked -= 1
                    if row_clicked < 0:
                        row_clicked = 8
                    board.select(row_clicked, col_clicked)
                if event.key == pygame.K_RIGHT:
                    col_clicked += 1
                    if col_clicked > 8:
                        col_clicked = 0
                    board.select(row_clicked, col_clicked)
                if event.key == pygame.K_LEFT:
                    col_clicked -= 1
                    if col_clicked < 0:
                        col_clicked = 8
                    board.select(row_clicked, col_clicked)
                if event.key == pygame.K_RETURN:
                    board.place_number(board.cells[row_clicked][col_clicked].sketched_value)
                    if board.cells[row_clicked][col_clicked].sketched_value is None:
                        board.cells[row_clicked][col_clicked].value = 0
                    board.update_board()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width - 800 <= mouse[0] <= width and height - 100 <= mouse[1] <= height:
                    click_count = 0
                    if width - 678 <= mouse[0] <= width - 518 and height - 88 <= mouse[1] <= height - 8:
                        board.reset_to_original()
                        board.update_board()
                    if width - 478 <= mouse[0] <= width - 318 and height - 88 <= mouse[1] <= height - 8:
                        return False, 1
                    if width - 278 <= mouse[0] <= width - 118 and height - 88 <= mouse[1] <= height - 8:
                        pygame.quit()

                click_count += 1
                if click_count > 1:
                    row_clicked = board.click(mouse[0], mouse[1])[0]
                    col_clicked = board.click(mouse[0], mouse[1])[1]
                    board.select(row_clicked, col_clicked)


        board.draw()
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (0, 0, 0), [width - 678, height - 88, 160, 80])
        pygame.draw.rect(screen, (135, 206, 250), [width - 673, height - 83, 150, 70])
        screen.blit(reset_text, (158, 833))

        pygame.draw.rect(screen, (0, 0, 0), [width - 478, height - 88, 160, 80])
        pygame.draw.rect(screen, (135, 206, 250), [width - 473, height - 83, 150, 70])
        screen.blit(restart_text, (347, 833))

        pygame.draw.rect(screen, (0, 0, 0), [width - 278, height - 88, 160, 80])
        pygame.draw.rect(screen, (135, 206, 250), [width - 273, height - 83, 150, 70])
        screen.blit(exit_text, (570, 833))

        if board.is_full():
            if board.check_board():
                return True, 1
            else:
                return False, -1

        pygame.display.flip()


def win_screen(screen, width, height, running):
    while running:
        # See if user clicked on window close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((width - 476.5) <= mouse[0] <= (width - 316.5)) and ((height - 305) <= mouse[1] <= (height - 225)):
                    pygame.quit()

        mouse = pygame.mouse.get_pos()
        # Fill the background with white
        screen.fill((255, 255, 255))
        won_message = pygame.font.SysFont('Corbel', 75, bold=True)
        won_text = won_message.render('Game Won!', True, (0, 0, 0))
        screen.blit(won_text, (210, 200))

        exit_mess = pygame.font.SysFont('Corbel', 35, bold=True)
        exit_text = exit_mess.render('Exit', True, (0, 0, 0))

        pygame.draw.rect(screen, (0, 0, 0), [width - 476.5, height - 305, 160, 80])
        pygame.draw.rect(screen, (135, 206, 250), [width - 471.5, height - 300, 150, 70])
        screen.blit(exit_text, (370, 618))

        pygame.display.flip()


def lose_screen(screen, width, height, running):
    while running:
        # See if user clicked on window close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((width - 476.5) <= mouse[0] <= (width - 316.5)) and ((height - 305) <= mouse[1] <= (height - 225)):
                    return 1

        # Fill the background with white
        screen.fill((255, 255, 255))
        lose_message = pygame.font.SysFont('Corbel', 75, bold=True)
        lose_text = lose_message.render('Game Over', True, (0, 0, 0))
        screen.blit(lose_text, (210, 200))

        restart_mess = pygame.font.SysFont('Corbel', 35, bold=True)
        restart_text = restart_mess.render('Restart', True, (0, 0, 0))

        pygame.draw.rect(screen, (0, 0, 0), [width - 476.5, height - 305, 160, 80])
        pygame.draw.rect(screen, (135, 206, 250), [width - 471.5, height - 300, 150, 70])
        screen.blit(restart_text, (347.5, 618))

        mouse = pygame.mouse.get_pos()

        pygame.display.flip()


def main_menu(width, height, screen, running):
    while running:

        # See if user clicked on window close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((width / 6 - 5) <= mouse[0] <= (width / 6 + 155)) and (
                        (height - 305) <= mouse[1] <= (height - 225)):
                    return 1

                if ((width - 476.5) <= mouse[0] <= (width - 316.5)) and ((height - 305) <= mouse[1] <= (height - 225)):
                    return 2

                if ((width - 280) <= mouse[0] <= (width - 120)) and ((height - 305) <= mouse[1] <= (height - 225)):
                    return 3

        # Fill the background with white
        screen.fill((255, 255, 255))
        draw_welcome(screen, width, height)

        mouse = pygame.mouse.get_pos()
        # Flip the display
        pygame.display.flip()


def main():
    # Initialize the pygame library
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([800, 900])
    width = screen.get_width()
    height = screen.get_height()
    # Run until the user asks to quit
    running = True
    easy_mode_click = 0
    medium_mode_click = 0
    hard_mode_click = 0
    main_menu_click = 1
    in_loop = True
    while in_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if main_menu_click == 1:
            click = main_menu(width, height, screen, running)
            if click == 1:
                easy_mode_click += 1
                main_menu_click = 0
            if click == 2:
                medium_mode_click += 1
                main_menu_click = 0
            if click == 3:
                hard_mode_click += 1
                main_menu_click = 0

        if easy_mode_click == 1:
            sudoku_board = generate_sudoku(9, 30)
            board = Board(width, height, screen, 'Easy', sudoku_board)
            if general_level(screen, board, running, width, height)[0] is False:
                if general_level(screen, board, running, width, height)[1] == 1:
                    easy_mode_click -= 1
                    main_menu_click += 1
                elif lose_screen(screen, width, height, running) == 1:
                    easy_mode_click -= 1
                    main_menu_click += 1
            elif general_level(screen, board, running, width, height)[0]:
                win_screen(screen, width, height, running)


        if medium_mode_click == 1:
            sudoku_board = generate_sudoku(9, 40)
            board = Board(width, height, screen, 'Medium', sudoku_board)
            if general_level(screen, board, running, width, height)[0] is False:
                if general_level(screen, board, running, width, height)[1] == 1:
                    medium_mode_click -= 1
                    main_menu_click += 1
                elif lose_screen(screen, width, height, running) == 1:
                    medium_mode_click -= 1
                    main_menu_click += 1
            elif general_level(screen, board, running, width, height)[0]:
                win_screen(screen, width, height, running)

        if hard_mode_click == 1:
            sudoku_board = generate_sudoku(9, 50)
            board = Board(width, height, screen, 'Hard', sudoku_board)
            if general_level(screen, board, running, width, height)[0] is False:
                if general_level(screen, board, running, width, height)[1] == 1:
                    hard_mode_click -= 1
                    main_menu_click += 1
                elif lose_screen(screen, width, height, running) == 1:
                    hard_mode_click -= 1
                    main_menu_click += 1
            elif general_level(screen, board, running, width, height)[0]:
                win_screen(screen, width, height, running)

    # Quit
    pygame.quit()


if __name__ == '__main__':
    main()