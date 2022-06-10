from pygameinputs.Button import Button
import pygame

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))

myButton = Button(x=155, y=225, text="My Button", fontsize=18, font="calibri")


def update():
  win.fill((60, 60, 60))
  myButton.draw(win)
  pygame.display.update()

run = True
while run:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if myButton.getPressed(event):
      print("Button pressed")
pygame.quit()
