from Button import Button, LinkButton, AppButton, ImageButton
import pygame

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))  # creates a window of 500 x 500 pixels

myButton = Button(x=155, y=225, text="My Button", fontsize=18, font="calibri")  # sets a button to the myButton variable
myAppButton = AppButton(app="C:\\Windows\\System32\\cmd.exe", text="CMD")
myLinkButton = LinkButton(y=80, link="https://google.com/search?q=cute%20dogs", text="cute dogs")
myImageButton = ImageButton(y=160, image="button.png")  # Requires an image named button.png.

def update():
  win.fill((60, 60, 60))  # sets the background of the window in RGB
  myButton.draw(win)  # draws the button to the window
  myAppButton.draw(win)
  myLinkButton.draw(win)
  myImageButton.draw(win)
  if myAppButton.hover == myLinkButton.hover == myImageButton.hover == False:
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
  pygame.display.update()  # updates the display


run = True
while run:
  clock.tick(60)  # sets the fps to a maximum 60
  for event in pygame.event.get():
    if event.type == pygame.QUIT:  # checks if the close button is pressed
      run = False  # Stops the while loop
    if myButton.getPressed(event):  # Checks if the button is pressed
        print("Button pressed")  # Ouputs "Button pressed" if the button is pressed
    if myAppButton.getPressed(event):
      print("Opening cmd")
    if myLinkButton.getPressed(event):
      print("Opening google to find cute dogs")
    if myImageButton.getPressed(event):
      print("Image button pressed")
  update()  # Runs the update function
pygame.quit()  # Stops pygame and closes the window
