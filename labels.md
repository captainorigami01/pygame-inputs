## Labels

> [HOME](https://captainorigami01.github.io/pygame-inputs/)

Place the code below with the imports at the top of your [script](https://github.com/captainorigami01/pygame-inputs/blob/c1b627e65933d34479a9376751eaf7d4776e48b1/starter.py)
```python
from pygameinputs.Label import Label
```

Place the code below beneath your pygame.init and before the while loop (while run)
```python
myLabel = Label()
```

The code below should be placed below the win.fill((60, 60, 60)) and above the pygame.display.update()
```python
myLabel.draw(win)
```

If you run this code you should see a window appear with a label in the top left corner of your screen

#### Label customisations

The label object allows different customisations, the tabel below describes these customisations

|**Attribute**  | **Example** | **Description** |
|--|--|--|
|x (int) | myLabel(x=10) | Sets the x coordinate on the window |
|y (int) | myLabel(y=20) | Sets the y coordinate on the window |
|maxwidth (int) | myLabel(maxwidth=10)|Sets the maximum width of the text in pixels. If it is 0 then this attribute is ignored|
|text (string)| myLabel(text="My Text")|Sets the text displayed on the label|
|font (string)| myLabel(font="myFont.ttf")|Sets the font on the label. It can use a ttf font or a font such as calibri|
|fontSize (int)|myLabel(fontSize=20)|Sets the size of the font|
|bold (boolean)|myLabel(bold=False|Sets the text to bold when True or regular when False|
|italic (boolean)|myLabel(italic=True)|Sets the font to italic when True or regular when False|
|color (tuple)|myLabel(color=(0, 0, 0))|Takes an RGB colour in a tuple format. In this case I set my font colour to black|
|background (tuple)|myLabel(background=(255, 255, 255))|Takes an RGB colour in a tuple format. In this case I set the background colour to white|
|transparentBackground (boolean)|myLabel(transparentBackground=True)|Whether or not the background should be transparent or not|
|visible (boolean)|myLabel(visible=True)|Whether the label should be displayed or hidden (useful if you want to hide it at some point)|

#### Label methods

Methods are pre defined functions within the labels

**draw(window)**
Draws the label to the screen

`window` is the display that you want to put the label on

The code below uses the update function from the [starter.py script](https://github.com/captainorigami01/pygame-inputs/blob/c1b627e65933d34479a9376751eaf7d4776e48b1/starter.py)

```python
def update():
  win.fill((60, 60, 60))
  myLabel.draw(win)  # win is defined earlier on in the script
  pygame.display.update()
```
**getVisibility**
Returns the visibility of the label as a boolean

If the label is hidden it returns False otherwise it returns True

```python
label_visible = myLabel.getVisibility()
```

**toggleVisibility()**
Toggles the visibility of the label

If the label is hidden it becomes visible and if it is visible it becomes hidden.

```python
myLabel.toggleVisibility()
```

**changeText(text)**
Changes the text on the label to `text` where text is a string

```python
myLabel.changeText("New Text")
```

> [Sample script](https://github.com/captainorigami01/pygame-inputs/blob/gh-pages/label-sample.py)

Documentation up to date for version 0.0.6
