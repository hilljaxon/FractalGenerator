from tkinter import Tk, Canvas, PhotoImage
window = Tk()

def paint(fractal, g):
    screenSize = fractal.getPixels()
    img = PhotoImage(width=fractal.getPixels(), height=fractal.getPixels())
    # Display the image on the screen
    canvas = Canvas(window, width=fractal.getPixels(), height=fractal.getPixels(), bg=g.getColor(0))
    canvas.pack()
    canvas.create_image((fractal.getPixels() / 2, fractal.getPixels() / 2), image=img, state="normal")
    for row in range(screenSize, 0, -1):
        for col in range(screenSize):
            x = fractal.getMin()['x'] + col * fractal.getPixelSize()
            y = fractal.getMin()['y'] + row * fractal.getPixelSize()
            color = g.getColor(fractal.count(complex(x,y)))
            img.put(color, (col, screenSize - row))
        window.update()  # display a row of pixels
    return img
