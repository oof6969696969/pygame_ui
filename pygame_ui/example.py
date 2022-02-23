if __name__ == "__main__":
    import pygame
    import pygame_ui

    pygame_ui.load_theme("basic_theme.json")

    wn = pygame.display.set_mode((500, 500))
    ui_manager = pygame_ui.UIManager((500, 500))
    pygame.display.set_caption("pygame_ui v1.0 - Example Window")

    test_btn_1 = pygame_ui.Widgets.Button((220, 50), (40, 40), "This is a button", lambda: print("You pressed the button!"))
    ui_manager.add(test_btn_1)

    test_label_1 = pygame_ui.Widgets.TextLabel((40, 100), "This is a label")
    ui_manager.add(test_label_1)

    test_gradient_rect_1 = pygame_ui.Shapes.GradientRect((420, 50), (40, 160), (255, 0, 255), (255, 255, 0))
    ui_manager.add(test_gradient_rect_1)

    test_smooth_circle_1 = pygame_ui.Shapes.SmoothCircle(50, (90, 270), (0, 0, 0))
    ui_manager.add(test_smooth_circle_1)

    test_smooth_circle_2 = pygame_ui.Shapes.SmoothCircle(50, (310, 270), (255, 0, 0))
    ui_manager.add(test_smooth_circle_2)

    test_toggle_1 = pygame_ui.Widgets.Toggle((280, 40), False, 50)
    ui_manager.add(test_toggle_1)


    def windowed_surface_cmd():
        ui_manager.remove(test_windowed_surface_1)


    test_windowed_surface_1 = pygame_ui.Widgets.WindowedSurface((40, 348), (420, 150), "This is a windowed surface",
                                                                windowed_surface_cmd)
    ui_manager.add(test_windowed_surface_1)

    test_gradient_rect_for_windowed_surface_1 = pygame_ui.Shapes.GradientRect((420, 150), (0, 0), (0, 255, 0), (255, 0, 0))

    clock = pygame.time.Clock()
    while True:
        wn.fill((255, 255, 255))

        pygame.draw.circle(wn, (0, 0, 0), (200, 270), 50)
        pygame.draw.circle(wn, (255, 0, 0), (420, 270), 50)

        test_gradient_rect_for_windowed_surface_1.render(test_windowed_surface_1.get_surface())

        ui_manager.render(wn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(60)
