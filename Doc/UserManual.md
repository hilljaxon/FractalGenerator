## User Manual

Congratulations on your purchase of your every own Fractal Generator!

Here are some things that you need to know.
Firstly, this program is command line driven. Therefore, you will need to 
navigate using a terminal to the location of the scr directory included
in your package. Once there, you will need to enter the following command.

`$ python src/Main.py`

This command with generate the default case for both an execution pattern
and color pattern, as indicated by the output 

```
$ python src/Main.py
FractalFactory: Creating default fractal
GradientFactory: Creating default color gradient
```
To override the default configurations, use the optional arguments 
specification to provide to location to a alternate config file.
Currently, the data folder contains several sample configurations.
Please note that if you would like to utilize other config options,
you will need to provide a new config file, using one of the provided
samples as a template.

Below is an example of an over ridden fractal pattern:
```
$ python src/Main.py data/fullmandelbrot.frac
GradientFactory: Creating default color gradient
```
Provided configuration files are enumerated below:
```
branches.frac     fullmandelbrot.frac  mandelfull.frac   unconnected.frac
branches256.frac  funnel-down.frac     mandelthree.frac  wholly-squid.frac
burningship.frac  hourglass.frac       minibrot.frac     zoomed.frac
connected.frac    lakes.frac           seahorse.frac     
elephant.frac     leaf.frac            spiral0.frac
elephants.frac    lubber.frac          spiral1.frac
fulljulia.frac    mandelfour.frac      spiral-jetty.frac
```
Likewise, to override the default color configurations, use the optional arguments 
to specify a color gradient. Currently, the possible enumerated color gradients are:
```
GrayScale
Rainbow
Deep
ColorCube
Cold
Hot
Test
```
An example of overriding this is found below:
```
$ python src/Main.py data/fullmandelbrot.frac Rainbow
```
The "Test" Gradient is provided as an easy way for the user to modify
the output color gradient, found in the file "Gradients".

Should the syntax for the command line be satisfied, you will begin to watch
your fractal being rendered. Once the fractal is complete, close the pop up
window to save the image, and you will be greeted with the message
 `Wrote image fullmandelbrot.png`,
verifying that the image was saved. Check your current working 
directory for your new image!
