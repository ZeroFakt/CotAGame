import pygame
import sys
import ctypes

clock = pygame.time.Clock()

pygame.init()

# Определение цветов (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Размеры экрана
window_width, window_height = 1600, 900
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('CotA')

# Загрузка изображения игрока
player = pygame.image.load('assets/images/heroes.png')
player_rect = player.get_rect(topleft=(50, 50))

player_speed = 1

# Начальная позиция игрока
initial_player_position = player_rect.topleft

# Загрузка изображения врага
enemy = pygame.image.load('assets/images/enemy.png')
enemy_rect = enemy.get_rect(topleft=(100, 100))

# Загрузка музыки и звуков
pygame.mixer.music.load('assets/music/background_sound.mp3')
pygame.mixer.music.play(-1)


# Установка значка
icon = pygame.image.load('assets/images/icon.png')
pygame.display.set_icon(icon)


# Функция для установки значка
def set_icon(icon_path):
    icon_path = icon_path.replace("/", "\\")

    ctypes.windll.kernel32.SetConsoleIcon(ctypes.windll.shell32.ExtractIconW(0, icon_path, 0))


set_icon("assets/images/icon.png")


# Функция для отображения текста на экране
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(topleft=(x, y))
    screen.blit(text_obj, text_rect)


# Функция для отображения меню
def show_menu():
    menu_font = pygame.font.Font(None, 36)

    running_menu = True
    selected_button = None

    while running_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running_menu = False
                elif event.key == pygame.K_RETURN:
                    if selected_button == "Играть":
                        print("Нажата кнопка 'Играть'")
                        running_menu = False
                    elif selected_button == "Выйти":
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, button in enumerate(buttons):
                        button_rect = pygame.Rect(
                            (window_width // 2) - 100,
                            (window_height // 2) + i * button_spacing,
                            200,
                            40,
                        )
                        if button_rect.collidepoint(event.pos):
                            if button == 'Играть':
                                print("Нажата кнопка 'Играть' ")
                                running_menu = False
                            elif button == 'Выйти':
                                pygame.quit()
                                sys.exit()

        screen.fill(BLACK)

        buttons = ["Играть", "Выйти"]
        button_spacing = 50

        for i, button in enumerate(buttons):
            button_rect = pygame.Rect(
                (window_width // 2) - 100,
                (window_height // 2) + i * button_spacing,
                200,
                40,
            )

            if button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, WHITE, button_rect)
                selected_button = button
            else:
                pygame.draw.rect(screen, WHITE, button_rect, 2)

            draw_text(button, menu_font, WHITE, screen, (window_width // 2) - 90,
                      (window_height // 2) + i * button_spacing + 10)

        pygame.display.flip()


# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_rect.topleft = initial_player_position
            elif event.key == pygame.K_m:
                show_menu()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # обработка клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.move_ip(-player_speed, 0)
    if keys[pygame.K_d]:
        player_rect.move_ip(player_speed, 0)
    if keys[pygame.K_w]:
        player_rect.move_ip(0, -player_speed)
    if keys[pygame.K_s]:
        player_rect.move_ip(0, player_speed)
    if keys[pygame.K_SPACE]:
        player_rect.move_ip(0, 0)

    # ограничение окна
    player_rect.x = max(0, min(player_rect.x, window_width - player_rect.width))
    player_rect.y = max(0, min(player_rect.y, window_height - player_rect.height))

    screen.fill(BLACK)
    screen.blit(player, player_rect)

    pygame.display.flip()
    clock.tick(60)
