https://docs.google.com/document/d/1f3pvsLGB0TziWXYZGr9yC5gSquKNUJ5udpV7xTtyacU/edit?usp=sharing


מקרי קצה : השחקן / הדגל מוקף בפצצות 



import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

board = [
    ["-", "-", "-", "-"],
    ["-", "M", "-", "-"],
    ["-", "-", "P", "-"],
    ["-", "-", "-", "-"]
]

cell_size = 50

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for row in range(len(board)):
        for col in range(len(board[row])):

            x = col * cell_size
            y = row * cell_size

            if board[row][col] == "M":
                # כאן מציירים מוקש
                pygame.draw.circle(
                    screen,
                    "black",
                    (x + cell_size // 2, y + cell_size // 2),
                    15
                )

            elif board[row][col] == "P":
                # כאן מציירים שחקן
                pygame.draw.rect(
                    screen,
                    "blue",
                    (x, y, cell_size, cell_size)
                )

    pygame.display.update()

pygame.quit()
