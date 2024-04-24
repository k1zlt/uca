import pygame
import random

available_locations = [i for i in range(36)]


class LinkListNode:
    def __init__(self, data, next, index):
        self.data = data
        self.next = next
        self.index = index
        self.loc = available_locations.pop(random.randint(0, len(available_locations) - 1))

    def __str__(self):
        return str(self.data)


def render_list(array, screen):
    for i, node in enumerate(array):
        text = font.render(str(node.data), True, black)
        loc = small_font.render(str(node.loc), True, black)
        text_rect = text.get_rect(center=(i * 80 + 40, screen.get_height() // 2 + 20))
        loc_rect = loc.get_rect(center=(i * 80 + 40, screen.get_height() // 2 - text_rect.height // 2 + 10))
        next_text = small_font.render(f'{node.next.loc if node.next else "Null"}', True, black)
        next_rect = next_text.get_rect(center=(i * 80 + 40, screen.get_height() // 2 + 40))
        loc_rect.width = 51
        text_rect.width = 51
        screen.blit(next_text, next_rect)
        screen.blit(text, text_rect)
        screen.blit(loc, loc_rect)


def create_button(text, pos, screen, color, text_color, action=None):
    button = pygame.draw.rect(screen, color, (pos[0], pos[1], 100, 40))
    text = small_font.render(text, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = button.center
    screen.blit(text, text_rect)
    return button, text, text_rect, action


def render_memory(array, screen):
    for i in range(36):
        if i in available_locations:
            t = font.render(str(i), True, black)
        else:
            k = list(filter(lambda x: x.loc == i, array))[0]
            if k.next is None:
                t = font.render(f'{i}-{k.data}-None', True, black)
            else:
                t = font.render(f'{i}-{k.data}-{k.next.loc}', True, black)
        t_rect = t.get_rect(topleft=(i // 9 * 200+10, i % 9 * 32 + 60))
        screen.blit(t, t_rect)


linkedList = [LinkListNode('Head', None, 0)]
for i in range(1, 10):
    a = LinkListNode(random.randint(0, 100), None, i)
    linkedList[-1].next = a
    linkedList.append(a)


def _(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))


pygame.init()
width = 800
height = 750
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Linked List Dashboard")


red = _("fe6b40")
orange = _("ff8829")
light_orange = _("ffb366")
light_green = _("a5c90f")
green = _("6f9c3d")
black = _("000000")
disabled = _("d3d3d3")

# font = pygame.font.Font('font/Pixeltype.ttf', 36)
# small_font = pygame.font.Font('font/Pixeltype.ttf', 20)

font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 20)

# First Section with List
array_screen = pygame.Surface((width, height // 4))
# Second Section with List representation in memory
memory_screen = pygame.Surface((width, height // 2))
# Third Section with List with actions
actions_screen = pygame.Surface((width, height // 4))

buttons = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            y -= height // 4 * 3
            if buttons[0][0].collidepoint(x, y) and len(available_locations) != 0 and len(linkedList) < 10:
                if len(linkedList) == 0:
                    linkedList = [LinkListNode('Head', None, 0)]
                    break
                linkedList.append(LinkListNode(random.randint(0, 100), None, i))
                linkedList[-2].next = linkedList[-1]
            if buttons[1][0].collidepoint(x, y) and len(linkedList) > 1:
                available_locations.append(linkedList[-1].loc)
                linkedList.pop()
                if linkedList:
                    linkedList[-1].next = None
                break
            if buttons[2][0].collidepoint(x, y):
                linkedList = [LinkListNode('Head', None, 0)]
                available_locations = [i for i in range(36)]
                break
    screen.fill(black)
    array_screen_title = font.render("Array Representation", True, black)
    array_screen_title_rect = array_screen_title.get_rect(center=(width // 2, 30))
    array_screen.fill(light_orange)
    array_screen.blit(array_screen_title, array_screen_title_rect)
    render_list(linkedList, array_screen)

    memory_screen.fill(light_green)
    memory_screen_title = font.render("Memory Representation", True, black)
    memory_screen_title_rect = memory_screen_title.get_rect(center=(width // 2, 30))
    render_memory(linkedList, memory_screen)
    memory_screen.blit(memory_screen_title, memory_screen_title_rect)
    
    actions_screen.fill(light_orange)
    actions_screen_title = font.render("Actions", True, black)
    actions_screen_title_rect = actions_screen_title.get_rect(center=(width // 2, 30))
    actions_screen.blit(actions_screen_title, actions_screen_title_rect)

    buttons = [
        create_button('Insert', (actions_screen.get_width() // 2 - 252, actions_screen.get_height() // 2), actions_screen, orange, black),
        create_button('Delete', (actions_screen.get_width() // 2 - 52, actions_screen.get_height() // 2), actions_screen, orange, black),
        create_button('Clear', (actions_screen.get_width() // 2 + 148, actions_screen.get_height() // 2), actions_screen, orange, black),
    ]

    screen.blit(array_screen, (0, 0))
    screen.blit(memory_screen, (0, height // 4))
    screen.blit(actions_screen, (0, height // 4 * 3))
    pygame.display.update()
