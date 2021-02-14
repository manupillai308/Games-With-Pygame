import pygame 
import sys

def get_rectangle(pos):
    x, y = pos

    if x <= 200 and y <= 200:
        if grid[0][0] is not None:
            return None, 0, 0
        return pygame.Rect(0, 0, 200, 200), 0, 0
    
    if x <= 400 and y <= 200:
        if grid[0][1] is not None:
            return None, 0, 0
        #left top width height
        return pygame.Rect(200, 0, 200, 200), 0, 1
    
    if x <= 600 and y <= 200:
        if grid[0][2] is not None:
            return None, 0, 0
        return pygame.Rect(400, 0, 200, 200), 0, 2
    
    if x <= 200 and y <= 400:
        if grid[1][0] is not None:
            return None, 0, 0
        return pygame.Rect(0, 200, 200, 200), 1, 0
    
    if x <= 400 and y <= 400:
        if grid[1][1] is not None:
            return None, 0, 0
        return pygame.Rect(200, 200, 200, 200), 1, 1
    
    if x <= 600 and y <= 400:
        if grid[1][2] is not None:
            return None, 0, 0
        return pygame.Rect(400, 200, 200, 200), 1, 2
    
    if x <= 200 and y <= 600:
        if grid[2][0] is not None:
            return None, 0, 0
        return pygame.Rect(0, 400, 200, 200), 2, 0
    
    if x <= 400 and y <= 600:
        if grid[2][1] is not None:
            return None, 0, 0
        return pygame.Rect(200, 400, 200, 200), 2, 1
    
    if x <= 600 and y <= 600:
        if grid[2][2] is not None:
            return None, 0, 0
        return pygame.Rect(400, 400, 200, 200), 2, 2

def draw_cell(screen):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200, 0, 10, 600))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(400, 0, 10, 600))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(600, 0, 10, 600))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 200, 600, 10))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 400, 600, 10))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 600, 600, 10))

def check_win(symbol, grid):
    for i in range(3):
        if grid[i][0] == symbol and grid[i][1] == symbol and grid[i][2] == symbol:
            return True
        if grid[0][i] == symbol and grid[1][i] == symbol and grid[2][i] == symbol:
            return True
        
    if grid[0][0] == symbol and grid[1][1] == symbol and grid[2][2] == symbol:
        return True
    
    if grid[0][2] == symbol and grid[1][1] == symbol and grid[2][0] == symbol:
        return True

    return False
        




pygame.init()

screen = pygame.display.set_mode((600, 600))
grid = [[None, None, None], [None, None, None], [None, None, None]]

pygame.display.set_caption("Tic Tac Toe")

cross = pygame.image.load("./cross.bmp")
cross = pygame.transform.scale(cross, (200, 200))
dot = pygame.image.load("./dot.bmp")
dot = pygame.transform.scale(dot, (200, 200))

images = [cross, dot]


filled_cells = []
current_running = 1
pause = False
text = None
font = pygame.font.SysFont(None, 60)
move_no = 0

while True:
    screen.fill((255, 255, 255))
    # rect = pygame.Rect(0, 0, 200, 200)
    # screen.blit(cross, rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not pause:
            rect, i, j = get_rectangle(event.pos)
            if rect is not None:
                move_no += 1
                grid[i][j] = current_running
                filled_cells.append((images[current_running], rect))
                current_running = 1 - int(current_running == 1)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_running = 1
                filled_cells.clear()
                text = None
                pause = False
                grid = [[None, None, None], [None, None, None], [None, None, None]]
                move_no = 0

    for img, rect in filled_cells:
        screen.blit(img, rect)
    draw_cell(screen)

    if check_win(0, grid):
        text = "CROSS WON"
    
    elif check_win(1, grid):
        text = "DOT WON"
    
    elif move_no >= 9:
        text = "GAME DRAW"

    if text is not None:
        img = font.render(text, True, (255, 0, 0))
        rect = img.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(img, rect)
        pygame.draw.rect(screen, (255, 0, 0), rect, 3)
        pause = True

    pygame.display.flip()