## Buttons
Place the code below with the imports at the top of your script
```python
from pygameinputs.Button import Button  # import the Button objects
```

Place the code below beneath your pygame.init and before the while loop (while run)
```python
myButton = Button()
```
The code below should be placed below the win.fill((60, 60, 60)) and above the pygame.display.update()
```python
myButton.draw(win)
```

If you run the code you should see a window appear with a button in the top left corner of your screen

#### Button Customisations

The button object allows different customisations, the table below describes these customisations

|**Attribute**  | **Example** | **Description**|
|--|--|--|
| x (int) | myButton = Button(x=5) | Sets the X coordinate on the window to 5 pixels where the (0, 0) is the top left|
|y (int) |myButton = Button(y=10) | Sets the Y coordiante on the window to 5 pixels where the (0, 0) is the top left|
|width (int)|myButton = Button(width=200)|Sets the width of the button to 200 pixels|
|height (int) |myButton = Button(height=50)|Sets the height of the button to 50 pixels|
|text (string) | myButton = Button(text="Some text")|Sets the text on the button to 'Some text'|
|font (string) | myButton = Button(font="font.ttf") | Takes a font name in the form of a string. This can be the path to a font such as the way the example shows or a font name such as 'calibri' |
| fontsize (int) | myButton = Button(fontsize=18) | Sets the font size of the text on the button |
| background (tuple) | myButton = Button(background=(100, 100, 100)) | Sets the background colour of the button using RGB colour values |
| backgroundHover (tuple) | myButton = Button(backgroundHover(80, 80, 80)) | Sets the background colour of the button in the hover state in RGB |
|borderColour (tuple)|myButton = button(borderColour((255, 0, 0)) | Sets the colour of the border using RGB colour values|
|borderHoverColour (tuple) |myButton = Button(borderHoverColour=(200, 0, 0))|Sets the hover colour of the border in RGB|
|borderWeight (int)|myButton = Button(borderWeight=2)|Sets the thickness of the border in pixels ***Please note a border of 0 pixels will overwrite the default background to the border colour - this is a bug and will be fixed in the next version***|
|bold (Boolean)|myButton = Button(bold=True)|True sets the text to bold, it is false by default|
|italic (Boolean)|myButton = Button(italic=True)|Sets the text to italic when True, is False by default|
