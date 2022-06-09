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
|  |  |  |

***INCOMPLETE DOCUMENTATION MORE COMING SOON***
