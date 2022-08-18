import pygame

width = 750
height = 400


def main():
    string = input('Insert machine string: ')

    string = string[9:-3]
    id = string[:string.index(',')]
    string = string[string.index(',') + 4:]

    columns = get_columns(string)

    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption(id)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        draw_columns(columns, screen)

        # Draw lines
        for x in range(8):
            pygame.draw.line(screen, (0, 0, 0), ((width / 7) * x, 0), ((width / 7) * x, height))
        for y in range(6):
            pygame.draw.line(screen, (0, 0, 0), (0, (height / 5) * y), (width, (height / 5) * y), 3 if y == 2 else 1)

        pygame.display.flip()

    pygame.quit()


def draw_columns(columns, screen):
    for y in range(6):
        for x, col in enumerate(columns):
            if len(col) <= y:
                pygame.draw.rect(screen, (255, 255, 255),
                                 ((width / 7) * x, (height / 5) * y, int(width / 7), int(height / 5)))
                continue
            if type(col[y]) == pygame.Surface:
                screen.blit(col[y], ((width / 7) * x, (height / 5) * y))
                continue
            c = col[y]
            pygame.draw.rect(screen, c, ((width / 7) * x, (height / 5) * y, int(width / 7), int(height / 5)))


def get_columns(string):
    columns = []
    for i, s in enumerate(string.split('t')):

        col = [(255, 255, 0) if i % 2 == 0 else (146, 208, 80)]
        if i in [0, 1]:
            file = 'images/kangaroo.jpeg'
        elif i in [2, 3]:
            file = 'images/Emu.webp'
        elif i in [4, 5]:
            file = 'images/wombat.jpg'
        else:
            file = 'images/platypus.jpg'
        col.append(pygame.transform.scale(pygame.image.load(file), (int(width / 7), int(height / 5))))

        s = s[1:-2 if len(s) == 13 else -1]
        vals = s.split(',')

        col.append((255, 255, 0) if vals[2] == 'y' else (146, 208, 80))
        if vals[3] == 'k':
            file = 'images/kangaroo.jpeg'
        elif vals[3] == 'e':
            file = 'images/Emu.webp'
        elif vals[3] == 'w':
            file = 'images/wombat.jpg'
        else:
            file = 'images/platypus.jpg'
        col.append(pygame.transform.scale(pygame.image.load(file), (int(width / 7), int(height / 5))))

        if vals[4] == 'wa':
            file = 'images/wattletree.jpeg'
        else:
            file = 'images/ghostgum.jpg'
        col.append(pygame.transform.scale(pygame.image.load(file), (int(width / 7), int(height / 5))))

        columns.append(col)
    return columns


if __name__ == '__main__':
    main()
