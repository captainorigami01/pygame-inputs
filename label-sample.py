from pygameinputs.Label import Label
import pygame

pygame.init()  # Initialises pygame
clock = pygame.time.Clock()  # Pygame builtin clock to set the fps limit

win = pygame.display.set_mode((500, 500))  # Creates a window which is 500 by 500 pixels in size

myLabel = Label(x=20, y=50, maxwidth=460, text="My Label", fontSize=20, color=(255, 255, 255))  # Creates a label with the identifier myLabel

myLabel.changeText("The new text")  # Sets the new text for the label
isLabelVisible = myLabel.getVisibility()  # gets wheter the label is visible or not as a boolean and stores it in the isLabelVisible variable
myLabel.toggleVisibility()  # If the label is hidden it becomes visible. If it is visible it becomes hidden


def update():
  win.fill((60, 60, 60))  # sets the background of the window
  myLabel.draw(window)  # Displays the label to the window
  pygame.display.update()  # Updates the display
 
run = True
while run:
  clock.tick(60)  # sets the maximum frame rate to 60 fps
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run=False  # Stops the main loop
pygame.quit()  # Stops pygame
  
