import pygame
from Sliders import HorizontalSlider, VerticalSlider

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))  # Creates a display 500 x 500 pixels

# slider creation:

myVerticalSlider = VerticalSlider(x=20, y=20, sliderColor=(0, 200, 0), handleColor=(200, 200, 200))
myHorizontalSlider = HorizontalSlider(x=40, y=20, sliderPercent=80, sliderColor=(10, 90, 255), handleColor=(200, 200, 20), color=(100, 100, 100))

myVerticalSlider.setPercent(20)  # Changes the position of the slider to 20 percent
print(myHorizontalSlider.getPercent())  # outputs the percentage of the horizontal slider


def update():
    win.fill((60, 60, 60))
    myVerticalSlider.draw(win)  # Displays the slider to the screen
    myHorizontalSlider.draw(win)  # same again
    if myVerticalSlider.hover == myHorizontalSlider.hover == False:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.display.update()


run = True
while run:
    clock.tick(60)  # sets the maximum frame rate to 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        myVerticalSlider.getPressed(event)  # Detects whether the slider is active and returns true or false
        myHorizontalSlider.getPressed(event)

    update()
pygame.quit()
