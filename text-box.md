## Text Boxes

> [HOME](https://captainorigami01.github.io/pygame-inputs/)

Place the code below with the imports at the top of your [script](https://github.com/captainorigami01/pygame-inputs/blob/c1b627e65933d34479a9376751eaf7d4776e48b1/starter.py)

```python
from pygameinputs.TextBox import TextBox  # import the text box objects
```

Place the code below beneath your pygame.init and before the while loop (while run)

```python
myTextBox = TextBox()
```

The code below should be placed below the win.fill((60, 60, 60)) and above the pygame.display.update()

```python
myTextBox.draw(win)
```

If you run the code you should see a text box appear in the top left of your screen

### TextBox Customistations

The text box object allows different customisations, the table below describes these customisations

|**Attribute**|**Example**|**Description**|
|--|--|--|
| x (int) | myTextBox = TextBox(x=5) | Sets the X coordinate on the window in pixels |
| y (int) | myTextBox = TextBox(y=10) | Sets the Y coordinate on the window in pixels |
| width (int) | myTextBox = TextBox(width=200) | Sets the width of the TextBox in pixels |
| height (int) | myTextBox = TextBox(height=50) | Sets the height of the TextBox in pixels |
| placeholder (string) | myTextBox = TextBox(placeholder="Placeholder text") | Sets the placeholder text on the text box. It is shown whilst no text has been entered into the box |
| font (string) | myTextBox = TextBox(font="font.ttf") | Takes a font name in the form of a string. This can be the path to a font such as the way the example shows or a font name such as 'calibri' |
| fontSize (int) | myTextBox = TextBox(fontSize=11) | Sets the size of the font in pixels |
| color (tuple) | myTextBox = TextBox(color=()) | Sets the color of the text on the text box in RGB |
| background (tuple) | myTextBox = TextBox(background=(230, 230, 230)) | Sets the background colour of the text box in RGB |
| backgroundHover (tuple) | myTextBox = TextBox(backgroundHover(200, 200, 200)) | Sets the background when hovering over the text box in RGB |
| borderColour (tuple) | myTextBox = TextBox(borderColour(230, 230, 230)) | Sets the colour for the border around the text box in RGB |
| borderHoverColour (tuple) | myTextBox = TextBox(borderHoverColour=(200, 200, 200)) | Sets the hover colour for the border in RGB |
| borderWeight (int) | myTextBox = TextBox(borderWeight=1) | Sets the width of the border in pixels |
| bold (Boolean) | myTextBox = TextBox(bold=True) | Sets the text to bold when True |
| italic (Boolean) | myTextBox = TextBox(italic=True) | Makes the text italic when True |
| minlen (int) | myTextBox = TextBox(minlength=5) | The minimum input length before the input is accepted **Not functional yet** |
| maxlen (int) | myTextBox = TextBox(maxlen=10) | Te maximum accepted length for the input in the text box |
|borderRadius (int)| myTextBox = TextBox(borderRadius=5)|Sets the border radius in pixels. This creates rounded corners on your text box|

### TextBox methods

Methods are pre defined functions within the text boxes that help them behave correctly

**draw(window)** Draws the button to the screen
`window` is the display you want to put the button on

The code below uses the update function form the [starter.py script](https://github.com/captainorigami01/pygame-inputs/blob/c1b627e65933d34479a9376751eaf7d4776e48b1/starter.py)

```python
def update():
  win.fill((60, 60, 60))
  myTextBox.draw(win)  # win is defined earlier on in the script
  pygame.display.update()
```

**events(event)** finds out wheter or not the text box is being typed in or clicked on
`event` is passed form the event loop within your script

The code below uses the event handler from the [starter.py script](https://github.com/captainorigami01/pygame-inputs/blob/c1b627e65933d34479a9376751eaf7d4776e48b1/starter.py)

```python
for event in pygame.event.get():
  if event.type == pygame.QUIT:
    run = False
  myTextBox.events(event)
```
> [Sample script](https://github.com/captainorigami01/pygame-inputs/blob/b18fc5c870276ac123a5987894f9d5c2120b06b8/button-sample.py)

Documentation is up to date for version 0.1.4
