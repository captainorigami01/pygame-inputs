## Buttons

> [HOME](https://captainorigami01.github.io/pygame-inputs/)

Place the code below with the imports at the top of your [script](https://github.com/captainorigami01/pygame-inputs/blob/c1b627e65933d34479a9376751eaf7d4776e48b1/starter.py)
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
|borderWeight (int)|myButton = Button(borderWeight=2)|Sets the thickness of the border in pixels|
|bold (Boolean)|myButton = Button(bold=True)|True sets the text to bold, it is false by default|
|italic (Boolean)|myButton = Button(italic=True)|Sets the text to italic when True, is False by default|
|link (string)|myButton = LinkButton(link="https://google.com")|Takes a link to open as a URL in a webbrowser. ***Link buttons only***|
|app( string)|myButton = AppButton(app="C:\\Windows\\System32\\notepad.exe")|Takes a link to the app that you want to open. In this case notepad. ***App buttons only***|

#### Button methods

Methods are pre defined functions within the buttons that help them behave correctly

**draw(window)**
Draws the button to the screen

`window` is the display you want to put the button on

The code below uses the update function from the [starter.py script](https://github.com/captainorigami01/pygame-inputs/blob/c1b627e65933d34479a9376751eaf7d4776e48b1/starter.py)

```python
def update():
  win.fill((60, 60, 60))
  myButton.draw(win)  # win is defined earlier on in the script
  pygame.display.update()
```

**getPressed(event)**
Finds out whether the button is pressed or not

`event` is passed from the event loop within your project

In link buttons, if it detects that the button is pressed it will open the link as well
In app buttons, if it detects that the button is pressed it will open the app as well

The code below uses the event handler from the [starter.py script](https://github.com/captainorigami01/pygame-inputs/blob/c1b627e65933d34479a9376751eaf7d4776e48b1/starter.py)

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if myButton.getPressed(event):
      print("Button pressed")  # outputs "Button pressed" when the button is pressed
```
> [Sample script](https://github.com/captainorigami01/pygame-inputs/blob/b18fc5c870276ac123a5987894f9d5c2120b06b8/button-sample.py)

Documentation is up to date for version 0.0.4
