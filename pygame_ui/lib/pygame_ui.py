# ## IMPORTS ## #
import pygame
from pygame import gfxdraw
import json

print('\npygame_ui v1.0')
pygame.init()

# ## THEME_VARS ## #

# buttons
btn_colour_normal = 180, 180, 180
btn_colour_hover = 160, 160, 160
btn_colour_click = 210, 210, 210
btn_colour_border = 140, 140, 140
btn_radius_border = 10
btn_size_border = 4
btn_font = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 30)
btn_font_colour = 0, 0, 0

# text labels
txt_colour = 0, 0, 0
txt_font = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 50)

# toggles
tgl_fill_false_colour = 255, 255, 255
tgl_fill_true_colour = 0, 255, 0
tgl_main_colour = 0, 0, 0
tgl_border_width = 4

# windowed surfaces
wds_border_width = 2
wds_border_colour = 160, 160, 160
wds_title_font_height = 12
wds_border_radius = 10
wds_title_font_colour = 0, 0, 0
wds_title_font = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 12)
wds_close_btn_colour = 255, 0, 0

print('\033[94mBasic theme loaded. To use more themes, use the \033[0mpygame_ui.load_theme(theme) \033['
      '94mfunction.\033[0m')

# ## other ## #
disable_click_features = False


class UIManager:
    def __init__(self, size):
        self.w, self.h = size
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        self.objects = []

        if pygame.display.get_window_size() != size:
            print("\n\033[93mWarning: UIManager display size does not match the Pygame window size. This may cause "
                  "problems if you are using it for the main window surface and it is recommended that you keep them "
                  "as the same values.\033[0m")

    def render(self, target):
        self.surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        for i in self.objects:
            i.render(self.surface)
        target.blit(self.surface, (0, 0))

    def add(self, target):
        self.objects.append(target)

    def remove(self, target):
        self.objects.remove(target)


class Widgets:
    class Button:
        def __init__(self, size, position, text, on_click_command):
            self.w, self.h = size
            self.x, self.y = position
            self.cmd = on_click_command
            self.fill_colour = btn_colour_normal
            self.btn_txt = text
            self.is_pressed = False

        def render(self, render_target):
            self.update_fill_colour()
            pygame.draw.rect(render_target, self.fill_colour, (self.x, self.y, self.w, self.h),
                             border_radius=btn_radius_border)
            pygame.draw.rect(render_target, btn_colour_border, (self.x, self.y, self.w, self.h), btn_size_border,
                             border_radius=btn_radius_border)
            render_txt = btn_font.render(self.btn_txt, True, btn_font_colour)
            txt_x = self.x + round(self.w / 2) - round(render_txt.get_width() / 2)
            txt_y = self.y + round(self.h / 2) - round(render_txt.get_height() / 2)
            render_target.blit(render_txt, (txt_x, txt_y))

        def update_fill_colour(self):
            if not disable_click_features:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h:
                    self.fill_colour = btn_colour_hover
                    if pygame.mouse.get_pressed()[0]:
                        self.fill_colour = btn_colour_click
                        if not self.is_pressed:
                            self.cmd()
                            self.is_pressed = True
                    else:
                        self.is_pressed = False
                else:
                    self.fill_colour = btn_colour_normal

    class TextLabel:
        def __init__(self, position, text):
            self.x, self.y = position
            self.label_txt = text

        def render(self, render_target):
            render_text = txt_font.render(self.label_txt, True, txt_colour)
            render_target.blit(render_text, (self.x, self.y))

    class Toggle:
        def __init__(self, position, state, size, slider_speed=5):
            self.x, self.y = position
            self.render_x = self.x
            self.state = state
            self.size = size
            self.slider_speed = slider_speed
            self.presses = 0

        def render(self, render_target):
            if not self.state:
                if self.render_x != self.x:
                    self.render_x -= self.slider_speed
                if self.render_x < self.x:
                    self.render_x = self.x
                pygame.draw.rect(render_target, tgl_fill_false_colour,
                                 (self.x, self.y, self.size * 2, self.size + round(tgl_border_width)),
                                 border_radius=self.size + round(tgl_border_width))
            else:
                if self.render_x != self.x + self.size - round(self.size / 10) - round(tgl_border_width / 2):
                    self.render_x += self.slider_speed
                if self.render_x > self.x + self.size - round(self.size / 10) - round(tgl_border_width / 2):
                    self.render_x = self.x + self.size - round(self.size / 10) - round(tgl_border_width / 2)
                pygame.draw.rect(render_target, tgl_fill_true_colour,
                                 (self.x, self.y, self.size * 2, self.size + round(tgl_border_width)),
                                 border_radius=self.size + round(tgl_border_width))

            pygame.draw.rect(render_target, tgl_main_colour,
                             (self.x, self.y, self.size * 2, self.size + round(tgl_border_width)), tgl_border_width,
                             border_radius=self.size + round(tgl_border_width))

            Shapes.SmoothCircle(round(self.size / 2) - round(self.size / 10), (
                self.render_x + round(self.size / 2) + round(tgl_border_width / 2),
                self.y + round(self.size / 2) + round(tgl_border_width / 2)), tgl_main_colour).render(render_target)

            self.update_state()

        def get_state(self):
            return self.state

        def update_state(self):
            if not disable_click_features:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if self.x <= mouse_x <= self.x + self.size * 2 and self.y <= mouse_y <= self.y + self.size:
                    if pygame.mouse.get_pressed()[0]:
                        self.presses += 1
                    else:
                        self.presses = 0
                else:
                    self.presses = 0

                if self.presses == 1:
                    if self.state:
                        self.state = False
                    else:
                        self.state = True

    class WindowedSurface:
        def __init__(self, position, size, title, on_close_command):
            self.x, self.y = position
            self.w, self.h = size
            self.wds_txt = title
            self.cmd = on_close_command
            self.surface = pygame.Surface(size)

            self.prev_m_x, self.prev_m_y = pygame.mouse.get_pos()

        def render(self, render_target):
            render_target.blit(self.surface, (self.x, self.y))
            pygame.draw.rect(render_target, wds_border_colour, (self.x, self.y, self.w, self.h), wds_border_width)
            pygame.draw.rect(render_target, wds_border_colour,
                             (self.x, self.y - wds_title_font_height - 10, self.w, wds_title_font_height + 10),
                             border_top_left_radius=wds_border_radius, border_top_right_radius=wds_border_radius)

            self.close_button(render_target)

            render_txt = wds_title_font.render(self.wds_txt, True, wds_title_font_colour)
            render_target.blit(render_txt, (self.x + wds_title_font_height + 10, self.y - wds_title_font_height - 4))

            self.update_pos()

        def update_pos(self):
            global disable_click_features

            curr_m_x, curr_m_y = pygame.mouse.get_pos()
            diff_x = curr_m_x - self.prev_m_x
            diff_y = curr_m_y - self.prev_m_y

            disable_click_features = False
            if pygame.mouse.get_pressed()[0]:
                if self.x <= self.prev_m_x <= self.x + self.w and self.y - wds_title_font_height - 10 <= self.prev_m_y <= self.y:
                    disable_click_features = True
                    self.x += diff_x
                    self.y += diff_y

            self.prev_m_x, self.prev_m_y = pygame.mouse.get_pos()

        def close_button(self, render_target):
            pygame.draw.circle(render_target, wds_close_btn_colour,
                               (self.x + wds_title_font_height, self.y - wds_title_font_height + 3),
                               wds_title_font_height - 5)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.x + 5 <= mouse_x <= self.x + wds_title_font_height + 5 and self.y - wds_title_font_height - 2 <= \
                    mouse_y <= self.y - 2:
                if pygame.mouse.get_pressed()[0]:
                    self.cmd()

        def get_surface(self):
            return self.surface


class Shapes:
    class GradientRect:
        def __init__(self, size, position, colour1, colour2):
            self.x, self.y = position
            self.w, self.h = size
            self.col1 = colour1
            self.col2 = colour2

            try:
                self.dif_r = (self.col1[0] - self.col2[0]) / self.w
            except ZeroDivisionError:
                self.dif_r = 0

            try:
                self.dif_g = (self.col1[1] - self.col2[1]) / self.w
            except ZeroDivisionError:
                self.dif_g = 0

            try:
                self.dif_b = (self.col1[2] - self.col2[2]) / self.w
            except ZeroDivisionError:
                self.dif_b = 0

        def render(self, render_target):
            render_x = self.x
            render_colour = self.col1

            for x in range(self.w):
                pygame.draw.rect(render_target,
                                 (round(render_colour[0]), round(render_colour[1]), round(render_colour[2])),
                                 (render_x, self.y, 1, self.h))
                render_x += 1

                render_colour = render_colour[0] - self.dif_r, render_colour[1] - self.dif_g, render_colour[
                    2] - self.dif_b

    class SmoothCircle:
        def __init__(self, radius, position, colour):
            self.rad = radius
            self.x, self.y = position
            self.col = colour

        def render(self, render_target):
            gfxdraw.aacircle(render_target, self.x, self.y, self.rad, self.col)
            gfxdraw.filled_circle(render_target, self.x, self.y, self.rad, self.col)


def load_theme(theme):
    global btn_colour_normal, btn_colour_hover, btn_colour_click, btn_colour_border, btn_radius_border, \
        btn_size_border, btn_font, btn_font_colour, txt_colour, txt_font, tgl_fill_false_colour, tgl_fill_true_colour, \
        tgl_main_colour, tgl_border_width, wds_border_radius, wds_border_colour, wds_border_width, \
        wds_close_btn_colour, wds_title_font_colour, wds_title_font, wds_title_font_height

    file = json.load(open(theme, "r"))

    btn_colour_normal = file["btn"]["btn_colour_normal"]
    btn_colour_hover = file["btn"]["btn_colour_hover"]
    btn_colour_click = file["btn"]["btn_colour_click"]
    btn_colour_border = file["btn"]["btn_colour_border"]
    btn_radius_border = file["btn"]["btn_radius_border"]
    btn_size_border = file["btn"]["btn_size_border"]
    btn_font = pygame.font.Font(file["btn"]["btn_font"], file["btn"]["btn_font_size"])
    btn_font_colour = file["btn"]["btn_font_colour"]

    txt_colour = file["txt"]["txt_colour"]
    txt_font = pygame.font.Font(file["txt"]["txt_font"], file["txt"]["txt_font_size"])

    tgl_fill_false_colour = file["tgl"]["tgl_fill_false_colour"]
    tgl_fill_true_colour = file["tgl"]["tgl_fill_true_colour"]
    tgl_main_colour = file["tgl"]["tgl_main_colour"]
    tgl_border_width = file["tgl"]["tgl_border_width"]

    wds_border_width = file["wds"]["wds_border_width"]
    wds_border_colour = file["wds"]["wds_border_colour"]
    wds_title_font_height = file["wds"]["wds_title_font_height"]
    wds_border_radius = file["wds"]["wds_border_radius"]
    wds_title_font_colour = file["wds"]["wds_title_font_colour"]
    wds_title_font = pygame.font.Font(file["wds"]["wds_title_font"], file["wds"]["wds_title_font_height"])
    wds_close_btn_colour = file["wds"]["wds_close_btn_colour"]

    print(f"\033[92mTheme: \033[0m{theme}\033[92m loaded.\033[0m")
