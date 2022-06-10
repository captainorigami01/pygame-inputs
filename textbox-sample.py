from pygameinputs.TextBox import TextBox
import pygame

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))  # Creates a window 500 x 500 pixels

myTextBox = TextBox(x=150, y=225, placeholder="A placeholder", fontSize=18)  # Creates a text box


def update():
  win.fill((60, 60, 60)) # Sets the background of the window in RGB
  myTextBox.draw(win)  # Displays the text box to the screen
  pygame.display.update()
  

run = True
while run:
  clock.tick(60)  # sets the maximum fps to 60
  for event in pygame.event.get():
    if event.type == pygame.QUIT:  # Checks if the close button is pressed
      run = False  # Stops the while loop
    myTextBox.events(event)  # Checks for different events within the text box
  update()  # runs the update function
pygame.quit()  # Stop pygame and close the window
  
