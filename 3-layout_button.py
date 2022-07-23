import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

#layout position button (x, y, width, height)
button_layout_rect = pygame.Rect(30, 20, 100, 50)

hello_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                            text='Say Hello',
                                            manager=manager)


button_layout_rect = pygame.Rect(0, 0, 150, 50)
button_layout_rect.bottomright = (-30, -20)

ok_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                     text='Okay Thank you', manager=manager, anchors={'left': 'right', 'right': 'right',
                  'top': 'bottom',
                  'bottom': 'bottom'})

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()