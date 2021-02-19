#!/bin/env python3

# Mandelbrot Set Visualizer
import sys
from tkinter import mainloop
from ImagePainter import paint
from Config import imageTypes
from FractalFactory import makeFractal
from GradientFactory import makeGradient

fractal = None
gradient = None

if len(sys.argv) < 2:
    print("FractalFactory: Creating default fractal\nGradientFactory: Creating default color gradient")
    fractal = makeFractal()
    gradient = makeGradient("GrayScale", fractal.getIter())
elif len(sys.argv) < 3:
    print("GradientFactory: Creating default color gradient")
    fractal = makeFractal(sys.argv[1])
    gradient = makeGradient(file_string="GrayScale", n=fractal.getIter())
else:
    fractal = makeFractal(sys.argv[1])
    gradient = makeGradient(sys.argv[2], fractal.getIter())

# Set up the GUI so that we can paint the fractal image on the screen
img = paint(fractal,gradient)
# Save the image as a PNG
img.write(fractal.getName())
print(f"Wrote image {fractal.getName()}")
# Call tkinter.mainloop so the GUI remains open
mainloop()
