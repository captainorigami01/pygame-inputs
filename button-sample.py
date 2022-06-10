from pygameinputs.Button import Button
import pygame

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))  # creates a window of 500 x 500 pixels

myButton = Button(x=155, y=225, text="My Button", fontsize=18, font="calibri")  # sets a button to the myButton variable


def update():
  win.fill((60, 60, 60))  # sets the background of the window in RGB
  myButton.draw(win)  # draws the button to the window
  pygame.display.update()  # updates the display

run = True
while run:
  clock.tick(60)  # sets the fps to a maximum 60
  for event in pygame.event.get():
    if event.type == pygame.QUIT:  # checks if the close button is pressed
      run = False  # Stops the while loop
    if myButton.getPressed(event):  # Checks if the button is pressed
      print("Button pressed")  # Ouputs "Button pressed" if the button is pressed
  update()  # Runs the update function
pygame.quit()  # Stops pygame and closes the window
