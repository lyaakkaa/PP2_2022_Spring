import pygame as pg


def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pg.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
BG_COLOR = pg.Color('gray12')
# The original image will never be modified.
IMAGE = pg.Surface((140, 60), pg.SRCALPHA)
pg.draw.polygon(IMAGE, pg.Color('dodgerblue3'), ((0, 0), (140, 30), (0, 60)))
# Store the original center position of the surface.
pivot = [200, 250]
# This offset vector will be added to the pivot point, so the
# resulting rect will be blitted at rect.topleft + offset.
offset = pg.math.Vector2(50, 0)
angle = 0

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        angle += 1
    elif keys[pg.K_a] or keys[pg.K_LEFT]:
        angle -= 1
    if keys[pg.K_f]:
        pivot[0] += 2

    # Rotated version of the image and the shifted rect.
    rotated_image, rect = rotate(IMAGE, angle, pivot, offset)

    # Drawing.
    screen.fill(BG_COLOR)
    screen.blit(rotated_image, rect)  # Blit the rotated image.
    pg.draw.circle(screen, (30, 250, 70), pivot, 3)  # Pivot point.
    pg.draw.rect(screen, (30, 250, 70), rect, 1)  # The rect.
    pg.display.set_caption('Angle: {}'.format(angle))
    pg.display.flip()
    clock.tick(30)

pg.quit()