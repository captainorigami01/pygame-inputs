# pygame inputs #
a python library used to create input boxes and buttons in pygame for a GUI

This is a free open source python library.
Please read the license before editing or sharing online

## Installation: ##

 - To use the package use the `pip install pygameinputs` command

## How to use: ##

To get started ensure you have pygame. If you don't use: `pip install pygame` to get started.

I recommend an IDE when designing an app but is not required.

### button creation ###
Import the button scripts:
`from PygameInputs.Button import Button`
this line will import the button module from the Pygame Inputs library

To create a button firstly give it an identifier, in this case I am going to give mine an identifier of startGame.

The button has a blueprint and will work straight away without editing any of its attributes however it can be fully customised.

`startGame =  Button()`

### Input box creation ###
Import the input box scripts:
`from PygameInputs.TextBox import TextBox`
this line will import the textbox module form the Pygame Inputs library

To create a textbox firstly give it an identifier, in this case I am going to give mine an identifier of searchBar.

The textbox has a blueprint and will work straight away without editing any of its attributes however it can be fully customised.

`searchBar = TextBox()`

### Label creation ###
Import the label scripts:
`from pygameinputs.Label import Label`
this line will import the label module from the Pygame Inputs library

To create a label firstly give it an identifier, in this case I am going to give mine an identifier of myLabel.

The label has a blueprint and will work straight away without editing any of its attributes however it can be fully customised.

`myLabel = Label()`

### Slider creation ###
Import the slider scripts: `from pygameinputs.Sliders import HorizontalSlider, VerticalSlider` this line will import the slider module from the pygame inputs library

To create a slider firstly give it an identifier. In this case I am goting to give mine and idetifier of myHorizontalSlider.

The slider has a blueprint and will work straight away without editing any of its attributes however it can be fully customised

`myHorizontalSlider = HorizontalSlider()`

for a vertical slider replace `HorizontalSlider()` with `VerticalSlider()`

## Changelog ##

### Version 0.0.1 ###

Initial release for the alpha of the library

### Version 0.0.2 ###

Updated some documentation and added extra information to PyPi.

### Version 0.0.3 ###

Fixed a bug with the border width property overwriting the background when set to 0

### Version 0.0.4 ###

 - Added typing indicator
 - Added built in event handling within the button and textbox

### Version 0.0.5 ###

 - Added text labels

### Version 0.0.6 ###

 - Added vertical and horizontal sliders
 - Added hyperlink functionality within buttons to open apps and urls

### Version 0.1 ###

 - Minor bug fix - centre handles on sliders
 - Fixed buttons not loading ttf files
 - Major bug fix - fixed flickering cursors (read documentation to ensure your cursors are fixed)
 - Added image buttons

### Version 0.1.1 ###
 - Added a hover state to the image buttons
 - Fixed a bug with buttons still checking the hover state when not visible
 
 ### Version 0.1.2 ###
 - Fixed a bug with buttons not changing their hover state to False when hidden

## Future updates: ##
 - Bug fixes
 - Your reccomendations (read the paragraph below how to submit a feature request)

> If you have any reccomendations or would like to contribute please visit the [GitHub](https://github.com/captainorigami01/pygame-inputs) and make an issue with the enhancement label


[Documentation](https://captainorigami01.github.io/pygame-inputs/)

This library is not associated with pygame, it just uses their library to add input functionality
