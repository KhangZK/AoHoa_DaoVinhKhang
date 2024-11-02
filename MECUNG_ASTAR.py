import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Giao diện Pygame đơn giản")

# Màu sắc
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Phông chữ
font = pygame.font.Font(None, 36)

# Hàm vẽ nút
def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, BLUE, (x, y, width, height))
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Làm mới màn hình
    screen.fill(WHITE)

    # Vẽ các nút
    draw_button("Nút 1", 100, 100, 200, 50)
    draw_button("Nút 2", 100, 200, 200, 50)

    # Cập nhật màn hình
    pygame.display.flip()
