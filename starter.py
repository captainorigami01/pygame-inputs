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
