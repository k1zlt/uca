import pygame as pg
import sys
import random

def _(hex): return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

pg.init()
red = _("fe6b40")
orange = _("ff8829")
light_orange = _("ffb366")
light_green = _("a5c90f")
green = _("6f9c3d")
black = _("000000")
disabled = _("d3d3d3")
font = pg.font.Font('Pixeltype.ttf', 30)


def render_list(l, start_pos, screen, color, text_color):
    for i, num in enumerate(l):
        rect = pg.draw.rect(screen, color, (start_pos[0] + i * 100, start_pos[1], 60, 50))
        text = font.render(str(num), True, text_color)
        text_rect = text.get_rect()
        text_rect.center = rect.center
        screen.blit(text, text_rect)

def render_length(l, height, screen, color, text_color):
    text = font.render("Length: " + str(len(l)), True, text_color)
    text_rect = text.get_rect()
    rect = pg.draw.rect(screen, color, (width-text_rect.width, height, 60, 50))
    text_rect.center = rect.center
    screen.blit(text, text_rect)


def create_button(text, pos, screen, color, text_color, action=None):
    button = pg.draw.rect(screen, color, (pos[0], pos[1], 200, 50))
    text = font.render(text, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = button.center
    screen.blit(text, text_rect)
    return button, text, text_rect

width, height = 1200, 900
clock = pg.time.Clock()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Queue vs Stack")

queue_screen = pg.Surface((width, height // 2))
stack_screen = pg.Surface((width, height // 2))


stack = [random.randint(1, 120) for _ in range(5)]
queue = [random.randint(1, 120) for _ in range(5)]


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            if enqueue_button.collidepoint(event.pos) and len(queue) < 10 and y < height // 2:
                queue.append(random.randint(1, 120))
            if dequeue_button.collidepoint(event.pos) and queue and y < height // 2:
                queue.pop(0)
            if push_button.collidepoint(x, y - height // 2) and len(stack) < 10 and not y < height // 2:
                stack.append(random.randint(1, 120))
            if pop_button.collidepoint(x, y - height // 2) and stack and not y < height // 2:
                stack.pop(-1)
            if reset_stack_button.collidepoint(x, y - height // 2) and not y < height // 2:
                stack = [random.randint(1, 120) for _ in range(5)]
            if reset_queue_button.collidepoint(event.pos) and y < height // 2:
                queue = [random.randint(1, 120) for _ in range(5)]
    
    queue_screen.fill(light_orange)
    stack_screen.fill(light_green)
    if len(queue) != 10:
        enqueue_button, enqueue_text, enqueue_rect = \
            create_button("Enqueue", (100, 3 * height // 8 + 25), queue_screen, light_green, black)
    else:
        enqueue_button, enqueue_text, enqueue_rect = \
            create_button("Enqueue", (100, 3 * height // 8 + 25), queue_screen, disabled, black)
    if len(queue) != 0:
        dequeue_button, dequeue_text, dequeue_rect = \
            create_button("Dequeue", (width // 2 - enqueue_button.w // 2, 3 * height // 8 + 25), queue_screen, light_green, black)
    else:
        dequeue_button, dequeue_text, dequeue_rect = \
            create_button("Dequeue", (width // 2 - enqueue_button.w // 2, 3 * height // 8 + 25), queue_screen, disabled, black)
    reset_queue_button, reset_text, reset_rect = \
        create_button("Reset Queue", (width - 300, 3 * height // 8 + 25), queue_screen, light_green, black)
    
    render_list(queue, (120, 150), queue_screen, light_green, black)
    render_length(queue, 0, queue_screen, light_orange, black)
    screen.blit(queue_screen, (0, 0))
    pg.draw.line(screen, black, (0, height // 4+100), (width, height // 4+100), 2)

    if len(stack) != 10:
        push_button, push_text, push_rect = \
            create_button("Push", (100, 3 * height // 8 + 25), stack_screen, light_orange, black)
    else:
        push_button, push_text, push_rect = \
            create_button("Push", (100, 3 * height // 8 + 25), stack_screen, disabled, black)
    if len(stack) != 0:
        pop_button, pop_text, pop_rect = \
            create_button("Pop", (width // 2 - enqueue_button.w // 2, 3 * height // 8 + 25), stack_screen, light_orange, black)
    else:
        pop_button, pop_text, pop_rect = \
            create_button("Pop", (width // 2 - enqueue_button.w // 2, 3 * height // 8 + 25), stack_screen, disabled, black)
    reset_stack_button, reset_text, reset_rect = \
        create_button("Reset Stack", (width - 300, 3 * height // 8 + 25), stack_screen, light_orange, black)

    render_list(stack, (120, 150), stack_screen, light_orange, black)
    render_length(stack, 0, stack_screen, light_green, black)
    screen.blit(stack_screen, (0, height // 2))
    pg.draw.line(screen, black, (0, 3 * height // 4+100), (width, 3 * height // 4+100), 2)

    pg.display.flip()
    clock.tick(60)