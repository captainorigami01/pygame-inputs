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

## Important! The latest version to be released soon has a bug fix with cursors
To fix the cursors you need to check the hover states of all the inputs against each other and then change the cursor back to the default cursor of your choice. The code should look something like:
```python
def update():  # Uses the update loop from above with added inputs as an example
 win.fill((60, 60, 60))
 button1.draw(win)
 textBox1.draw(win)
 slider1.draw(win)
 if button1.hover == TextBox1.hover == Slider1.hover == False:  # Checks that all of the inputs are in their default state
  pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Changes the cursor to the default arrow
 pygame.display.update()
```
*Please note this update is not available yet. Doing this will not make any difference in the way your program reacts until the library has been updated. We highly reccomend you update the code to look like this so you don't have any bugs when the update is released*

### Button Creation

> [The buttons can be found here](https://captainorigami01.github.io/pygame-inputs/buttons)

### Text Box Creation

> [The text boxes can be found here](https://captainorigami01.github.io/pygame-inputs/text-box)

### Labels Creation

> [The labels can be found here](https://captainorigami01.github.io/pygame-inputs/labels)

### Sliders Creation

> [The sliders can be found here](https://captainorigami01.github.io/pygame-inputs/sliders)

