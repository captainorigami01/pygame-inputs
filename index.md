# Welcome to the documentation for pygame inputs

## Installation

You can install pygame inputs through the command line using the 'pip' command or downloading one of the releases from github

### PIP installation:

`pip install pygameinputs`

### github installation

 - Download the version of pygame inputs from the releases that you want
 - Open your python directory on your computer (If you don't know where this is you will have to look this up based on your operating system)
 - Go to your python version folder -> lib -> site-packages
 - paste the pygame inputs folder here

## Getting Started
### Creating the event loop
```python
import pygame  # import pygame

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((500, 500))  # Creates a window of 500 x 500 pixels in size


def update():
  win.fill((60, 60, 60))  # sets the background of the window to a RGB colour of 60, 60, 60
  pygame.display.update()  # Updates the display every frame
  
 
 run = True
 while run:
  clock.tick(60)  # sets the maximum frame rate to 60 fps
  for event in pygame.event.get():
    if event.type == pygame.QUIT:  # checks if the close button is pressed
      run = False  # if the close button was pressed then it will stop the main loop
  update()  # Calls the update function
 pygame.quit()  # stops pygame and closes the window
```
### Button Creation

> [The buttons can be found here](https://captainorigami01.github.io/pygame-inputs/buttons)

### Text Box Creation

> [The text boxes can be found here](https://captainorigami01.github.io/pygame-inputs/text-box)

### Labels Creation

> [The labels can be found here](https://captainorigami01.github.io/pygame-inputs/labels)

### Sliders Creation (version 0.0.6 - not released yet)

> [The sliders can be found here](https://captainorigami01.github.io/pygame-inputs/sliders)
