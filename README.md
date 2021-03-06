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

## Changelog ##

### Version 0.0.1 ###

Initial release for the alpha of the library

### Version 0.0.2 ###

Updated some documentation and added extra information to PyPi.

### Version 0.0.3 ###

Fixed a bug with the border width property overwriting the background when set to 0

## Future updates: ##
 - [ ] The textbox will be updated to have an indicator to show you are typing in the box.
 - [ ] Built-in features to handle button press and typing events making your code shorter and simpler
 - [x] Addition of cursors to add effect as you type or press buttons - partially done (cursors flickering so haven't been published to github)

> If you have any reccomendations or would like to contribute please visit the [GitHub](https://github.com/captainorigami01/pygame-inputs) and make a pull request to upload code or create an issue with the enhancement label


[Documentation](https://captainorigami01.github.io/pygame-inputs/)
