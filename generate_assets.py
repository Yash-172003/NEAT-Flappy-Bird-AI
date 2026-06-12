"""
Generate simple Flappy Bird game assets using pygame drawing.
Creates bird1.png, bird2.png, bird3.png, pipe.png, base.png, bg.png
"""
import pygame
import os

pygame.init()

imgs_dir = os.path.join(os.path.dirname(__file__), "imgs")
os.makedirs(imgs_dir, exist_ok=True)

# ---- Bird images (3 frames: wings up, mid, down) ----
# Each bird is 34x24 pixels (will be scaled 2x by the game)
def draw_bird(surface, wing_pos):
    """Draw a simple flappy bird. wing_pos: 'up', 'mid', 'down'"""
    surface.fill((0, 0, 0, 0))  # transparent
    # Body (yellow)
    pygame.draw.ellipse(surface, (255, 200, 0), (4, 6, 24, 16))
    # Eye (white + black pupil)
    pygame.draw.circle(surface, (255, 255, 255), (24, 10), 4)
    pygame.draw.circle(surface, (0, 0, 0), (25, 10), 2)
    # Beak (orange)
    pygame.draw.polygon(surface, (255, 120, 0), [(28, 13), (34, 15), (28, 17)])
    # Wing
    if wing_pos == 'up':
        pygame.draw.ellipse(surface, (220, 170, 0), (8, 2, 12, 8))
    elif wing_pos == 'mid':
        pygame.draw.ellipse(surface, (220, 170, 0), (8, 8, 12, 6))
    else:  # down
        pygame.draw.ellipse(surface, (220, 170, 0), (8, 14, 12, 8))

for i, wing in enumerate(['up', 'mid', 'down'], 1):
    bird_surf = pygame.Surface((34, 24), pygame.SRCALPHA)
    draw_bird(bird_surf, wing)
    pygame.image.save(bird_surf, os.path.join(imgs_dir, f"bird{i}.png"))
    print(f"Created bird{i}.png")

# ---- Pipe image ----
# Green pipe, 52x320 pixels (will be scaled 2x by the game)
pipe_surf = pygame.Surface((52, 320), pygame.SRCALPHA)
# Main pipe body
pygame.draw.rect(pipe_surf, (40, 180, 40), (4, 0, 44, 320))
# Pipe rim at top
pygame.draw.rect(pipe_surf, (30, 140, 30), (0, 0, 52, 26))
# Highlights
pygame.draw.rect(pipe_surf, (60, 210, 60), (8, 26, 8, 294))
# Dark edge
pygame.draw.rect(pipe_surf, (20, 100, 20), (40, 26, 4, 294))
pygame.image.save(pipe_surf, os.path.join(imgs_dir, "pipe.png"))
print("Created pipe.png")

# ---- Base (ground) image ----
# 336x112 pixels
base_surf = pygame.Surface((336, 112), pygame.SRCALPHA)
# Sandy ground
base_surf.fill((222, 184, 135))
# Top edge (green grass)
pygame.draw.rect(base_surf, (80, 180, 50), (0, 0, 336, 12))
# Texture lines
for x in range(0, 336, 24):
    pygame.draw.line(base_surf, (200, 160, 110), (x, 20), (x + 12, 50), 2)
    pygame.draw.line(base_surf, (200, 160, 110), (x + 12, 60), (x + 24, 90), 2)
pygame.image.save(base_surf, os.path.join(imgs_dir, "base.png"))
print("Created base.png")

# ---- Background image ----
# 288x512 pixels
bg_surf = pygame.Surface((288, 512))
# Sky gradient (light blue to blue)
for y in range(512):
    r = int(78 + (135 - 78) * (y / 512))
    g = int(192 + (206 - 192) * (y / 512))
    b = int(202 + (235 - 202) * (y / 512))
    pygame.draw.line(bg_surf, (r, g, b), (0, y), (288, y))
# Clouds
for cx, cy in [(60, 80), (180, 50), (240, 100), (100, 140)]:
    pygame.draw.ellipse(bg_surf, (255, 255, 255, 200), (cx - 30, cy - 10, 60, 20))
    pygame.draw.ellipse(bg_surf, (255, 255, 255, 200), (cx - 15, cy - 20, 40, 22))
# Ground hint at bottom
pygame.draw.rect(bg_surf, (222, 184, 135), (0, 400, 288, 112))
pygame.draw.rect(bg_surf, (80, 180, 50), (0, 400, 288, 10))
# City silhouette
buildings = [(10, 340, 30, 60), (50, 320, 25, 80), (85, 350, 35, 50),
             (130, 310, 20, 90), (160, 330, 40, 70), (210, 340, 30, 60), (250, 320, 30, 80)]
for bx, by, bw, bh in buildings:
    pygame.draw.rect(bg_surf, (80, 120, 80), (bx, by, bw, bh))
    # Windows
    for wy in range(by + 5, by + bh - 5, 10):
        for wx in range(bx + 4, bx + bw - 4, 8):
            pygame.draw.rect(bg_surf, (200, 200, 100), (wx, wy, 4, 4))

pygame.image.save(bg_surf, os.path.join(imgs_dir, "bg.png"))
print("Created bg.png")

print("\nAll assets generated successfully!")
pygame.quit()
