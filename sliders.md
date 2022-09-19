## Sliders

> [HOME](https://captainorigami01.github.io/pygame-inputs/)

Place the code below with the imports at the top of your [script](https://github.com/captainorigami01/pygame-inputs/blob/c1b627e65933d34479a9376751eaf7d4776e48b1/starter.py)
```python
from pygameinputs.Sliders import VerticalSlider, HorizontalSlider
```

Place the code below beneath your pygame.init and before the while loop (while run)

```python
myHorizontalSlider = HorizontalSlider()  # For a horizontal slider
myVerticalSlider = VerticalSlider()  # For a vertical slider
```

If you run this code you should see a window appear with a horizontal and / or vertical slider in the top left corner of the screen.

#### Slider customisations
Both sliders have the exact same properties. The difference is the direction in which they work

|**Attribute**|**Example**|**Description**|
|--|--|--|
|x (int)|myslider(x=20)|Sets the x coordinate of the slider (the origin is the top left corner of the slider)|
|y (int)|myslider(y=20)|sets the y coordinate of the slider (the origin is the top left corner of the slider)|
|width (int)|mySlider(width=200)|Sets the width of the slider (this is not the width of the handle. on the horizontal slider this is the length of the slider and on the vertical slider it is the width of the rail)|
|height (int)|mySlider(height=10)|Sets the height of the slider (This is not the height of the handle. On the horizontal slider it is the height of the rail and on the verical slider it is the length of the rail)|
|handleWidth (int)|mySlider(handlewidth=10)|The size of the handle. Currently the handle can only be a square. Rectangles and circles are currently not possible|
|color (tuple)|mySlider(color=(20, 20, 20))|This is the colour of the rail in RGB|
|sliderColor (tuple)|myslider(sliderColor=(200, 0, 0))|The colour of the rail where the handle has passed. Like that on a progress bar. This is an RGB colour|
|handleColor (tuple)|myslider(handleColor=(50, 50, 50))|The colour of the handle in RGB|
|sliderPercent (int)|mySlider(sliderPercent=20)|The percentage of how far along the slider the handle should be. In the example it is 20%|
|visible (boolean)|mySlider(visible=True)|Whether the slider should be visble|
