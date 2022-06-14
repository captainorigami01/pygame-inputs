import pygame

pygame.init()

### Creates the TextBox Class ###

class TextBox(object):
    def __init__(self, x:int = 0, y:int = 0, width:int = 200, height:int = 50, placeholder:str = "", font:str = "calibri",
                 fontSize:int = 11, color:tuple = (0, 0, 0), background:tuple = (230, 230, 230), backgroundHover:tuple = (200, 200, 200),
                 borderColour:tuple = (230, 230, 230), borderHoverColour:tuple = (200, 200, 200), borderWeight:int = 1, bold:bool = False, italic:bool = False,
                 minlen:int = 0, maxlen:int = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.placeholder = placeholder
        self.text = ""
        self.font = font
        self.fs = fontSize
        self.bold = bold
        self.italic = italic
        self.color = color
        self.bg = background
        self.minlen = minlen
        self.maxlen = maxlen
        self.bgHover = backgroundHover
        self.border = borderColour
        self.hborder = borderHoverColour
        self.borderWidth = borderWeight
        self.hover = False
        self.active = False

    def draw(self, window):
        self.isHover()
        if self.hover or self.active:  # hover state when hovering or currently active
            pygame.draw.rect(window, self.bgHover, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(window, self.hborder, (self.x, self.y, self.width, self.height), self.borderWidth)
        else:  # Default state
            pygame.draw.rect(window, self.bg, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(window, self.border, (self.x, self.y, self.width, self.height), self.borderWidth)

        font = pygame.font.SysFont(self.font, self.fs, self.bold, self.italic)  # Creates the information for the font
        if self.text == "":
            text = font.render(self.placeholder, True, self.color)  # sets the tex to the placeholder if no text is inputted yet
        else:
            text = font.render(self.text, True, self.color)

        text_rect = text.get_rect()
        width = text_rect.width  # Gets the width of the text
        height = text_rect.height  # Gets the height of the text

        textX = (self.x + (self.width // 2)) - width // 2  # Centres the text in the horizontal (x) axis
        textY = (self.y + (self.height // 2)) - height // 2  # Centres the text in the vertical (y) axis

        window.blit(text, (textX, textY))  # Displays the text to the window

    def backspacePressed(self):  # Removes an item from the end of the string of the backspace key is pressed
        text = list(self.text)
        if text.__len__() >= 1:
            text.pop()
        self.text = ''.join(text)

    def textAppend(self, character:str):  # Adds text to the end of the string
        text = list(self.text)
        if text.__len__() < self.maxlen or self.maxlen <= 0:
            text.append(character)
        self.text = ''.join(text)

    def isHover(self):  # This function checks if the mouse is hovering over the button
        mouse = pygame.mouse.get_pos()  # Gets the position of the mouse

        if mouse[0] >= self.x and mouse[0] <= self.x + self.width:  # The horizontal (x) axis
            if mouse[1] >= self.y and mouse[1] <= self.y + self.height:  # The vertical (y) axis
                self.hover = True  # The mouse is hovering
            else:
                self.hover = False
        else:
            self.hover = False
        return self.hover  # Returns the hover state (is there if needed)

