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

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/captainorigami01/pygame-inputs/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
***Uploaded***
