# pygame_ui
## _A library to easily add UI elements to pygame_
![Liscence](https://warehouse-camo.ingress.cmh1.psfhosted.org/8bf50b0c5f81019aff2c2c589b22779c6fb149b1/68747470733a2f2f696d672e736869656c64732e696f2f707970692f6c2f707967616d652d323034382e737667) ![Python Version](https://warehouse-camo.ingress.cmh1.psfhosted.org/04739c918077558cfc75e580cead419e67d36d5f/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f707967616d652d323034382e737667)
pygame_ui attempts to achieve decreasing the difficuilty of
creating UI elements of pygame by doing them for you.

## Features

- Easily understandable UI manager which manages all of the UI elements
- Widgets: Buttons, Toggles, Windowed Surfaces, Text Labels
- Shapes: Anti-Aliased Circles, Gradient Rectangles
- Themes: Editable theme types using json files
- Much, much more will be added in the future, this is still in early development

## Installation
Install the library with pip:

```sh
pip install pygame_ui
```

## Development

This project is still in development, if you find any issues, please e-mail me - rayner.freddie@btinternet.com.

## Usage

_An example file can be found in the package folder_

**Loading a theme:**
by default, the basic theme is used for pygame_ui. Feel free to create your own themes and if you do so please email them to me so I can add it to my defaults. An example theme named basic_theme.json can be found in the package folder. To first load a theme, use the load_theme() function. This takes one argument, the theme file. Usage:
```sh
import pygame_ui
import pygame

pygame_ui.load_theme('filename.json')
```

**Creating the UI Manager**
First, create a pygame window. Then, we need to create a UI manager for this window. The UI manager controlls the elements on the screen. This takes in one argument, the size of the manager's surface. It is recommended that you use the same width and height as the window. Usage:
```sh
window = pygame.display.set_mode((600, 800))
ui_manager = pygame_ui.UIManager((600, 800))
```

**Adding elements to the UI Manager**
to add an element to the manager, you must first initialize the element. For example, if we wanted a button to be added to the screen:
```sh
button1 = pygame_ui.Widgets.Button(size, position, text, command)
ui_manager.add(button1)
```
Similarly, to remove an element from the screen, we use:
```sh
ui_manager.remove(button1)
```
Arguments for all elements:
Under Widgets:
- **Button:** size, position, text, command
- **TextLabel:** position, text
- **Toggle:** position, state, slider_speed=5
- **WindowedSurface:** position, size, title, command

Under Shapes:
- **GradientRect:** size, position, colour1, colour2
- **SmoothCircle:** radius, position, colour

**Rendering the UI Manager**
To display the manager, in the main loop of your python file, add the following:
```sh
ui_manager.render(target_surface)
```
