import Gradients


def makeGradient(file_string, n):
    if file_string == "GrayScale":
        return Gradients.GrayScale(n)
    elif file_string == "Rainbow":
        return Gradients.Rainbow(n)
    elif file_string == "Deep":
        return Gradients.Deep(n)
    elif file_string == "ColorCube":
        return Gradients.ColorCube(n)
    elif file_string == "Cold":
        return Gradients.Cold(n)
    elif file_string == "Hot":
        return Gradients.Hot(n)
    elif file_string == "Test":
        return Gradients.Test(n)
    else:
        raise NotImplementedError("Concrete subclass of Gradient must implement __init__")

