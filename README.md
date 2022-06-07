# pygame inputs
a python library used to create input boxes and buttons in pygame for a GUI

This is a free open source python library.
Please read the license before editing or sharing online

## Installation:

 - To use it download one of the releases provided or download the source code.
 - Go to your python installation folder. On windows it can be found here:
 C:\Users\YOU USER HERE\AppData\Local\Programs\Python\YOUR PYTHON VERSION\Lib\site-packages
 - Put the library in this folder

## How to use:

To get started ensure you have pygame. If you don't use: `pip install pygame` to get started.

I recommend an IDE when designing an app but is not required.

### button creation
Import the button scripts:
`from PygameInputs.Button import Button`
this line will import the button module from the Pygame Inputs library

To create a button firstly give it an identifier, in this case I am going to give mine an identifier of startGame.

The button has a blueprint and will work straight away without editing any of its attributes however it can be fully customised.

`startGame =  Button()`

### Input box creation
Import the input box scripts:
`from PygameInputs.TextBox import TextBox`
this line will import the textbox module form the Pygame Inputs library

To create a textbox firstly give it an identifier, in this case I am going to give mine an identifier of searchBar.

The textbox has a blueprint and will work straight away without editing any of its attributes however it can be fully customised.

`searchBar = TextBox()`

## Future updates:

 - The textbox will be updated to have an indicator to show you are typing in the box.
 - Built in features to handle button press and typing events making your code shorter and simpler
[Documentation (link doesn't work yet)](https://captain-vc.com/pygame-inputs)

