import pygame

# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình
WIDTH, HEIGHT = 512,512  # Kích thước cửa sổ hiển thị
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wizard Animation")  # Đặt tiêu đề cho cửa sổ
clock = pygame.time.Clock()

# Load sprite sheet
sprite_sheet = pygame.image.load("corrected_sprite_sheet.png").convert_alpha()

# Cấu hình animation
FRAME_WIDTH, FRAME_HEIGHT = 256,256 # Kích thước mỗi frame (512 / 4 = 128)
COLUMNS, ROWS = 4, 4  # Sprite sheet có 4 cột, 4 hàng
NUM_FRAMES = COLUMNS * ROWS  # Tổng số frame = 16
current_frame = 0

# Lưu danh sách các frame (tọa độ x, y, width, height)
frame_rects = [
    (col * FRAME_WIDTH, row * FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT)
    for row in range(ROWS)
    for col in range(COLUMNS)
]

# Biến để kiểm soát tốc độ animation
animation_speed = 15  # FPS (tăng tốc độ để mượt hơn)

running = True
while running:
    screen.fill((0, 0, 0))  # Xóa màn hình với màu đen

    # Lấy frame hiện tại
    frame_rect = pygame.Rect(frame_rects[current_frame])
    sprite = sprite_sheet.subsurface(frame_rect)

    # Scale sprite lên để hiển thị lớn hơn trên màn hình
    sprite = pygame.transform.scale(sprite, (FRAME_WIDTH * 2, FRAME_HEIGHT * 2))

    # Vẽ sprite lên màn hình (đặt ở giữa)
    screen.blit(sprite, (WIDTH // 2 - (FRAME_WIDTH * 2) // 2, HEIGHT // 2 - (FRAME_HEIGHT * 2) // 2))

    # Cập nhật frame
    current_frame = (current_frame + 1) % NUM_FRAMES

    pygame.display.flip()
    clock.tick(animation_speed)  # Điều chỉnh tốc độ animation

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()