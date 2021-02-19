from abc import ABC,abstractmethod


class Fractal(ABC):
    def __init__(self, dic):
        self.__data = dic
        # TODO fix this
        # ABC should prevent this Class form being utilized.
        # raise NotImplementedError("Concrete subclass of Fractal must implement __init__")

    def count(self, c):  # takes a complex number and returns an int that is the max number of iterations
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

    def getType(self):
        return self.__data.get("type")

    def getPixels(self):
        return self.__data.get("pixels")

    def getAxis(self):
        return self.__data.get("axislength")

    def getPixelSize(self):
        return self.__data.get("pixelsize")

    def getIter(self):
        return self.__data.get("iterations")

    def getMin(self):
        return self.__data.get("min")

    def getCreal(self):
        return self.__data.get("creal")

    def getCimag(self):
        return self.__data.get("cimag")

    def getMax(self):
        return self.__data.get("max")

    def getName(self):
        return self.__data.get("imagename")


class Mandelbrot(Fractal, ABC):
    def __init__(self, dic):
        super().__init__(dic)

    def count(self,c):
        z = complex(0,0)
        for i in range(self.getIter()):
            z = z * z + c # Get z1, z2, ...
            if abs(z) > 2:
                return i  # The sequence is unbounded
        return self.getIter() - 1  # Indicate a bounded sequence


class Julia(Fractal, ABC):
    def __init__(self, dic):
        super().__init__(dic)

    def count(self, c):
        z = complex(self.getCreal(),self.getCimag())
        for i in range(self.getIter()):
            c = c * c + z  # Iteratively compute z1, z2, z3 ...
            if abs(c) > 2:
                return i  # The sequence is unbounded
        return self.getIter() - 1  # Else this is a bounded sequence


class Mandelbrot3(Fractal, ABC):
    def __init__(self, dic):
        super().__init__(dic)

    def count(self,c):
        z = complex(0,0)
        for i in range(self.getIter()):
            z = z * z + c # Get z1, z2, ...
            if abs(z) > 2:
                return i  # The sequence is unbounded
        return self.getIter() - 1  # Indicate a bounded sequence


class Mandelbrot4(Fractal, ABC):
    def __init__(self, dic):
        super().__init__(dic)

    def count(self, c):
        z = complex(0, 0)
        for i in range(self.getIter()):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                return i  # The sequence is unbounded
        return self.getIter() - 1  # Indicate a bounded sequence


class Phoenix(Fractal, ABC):
    def __init__(self, dic):
        super().__init__(dic)

    def count(self, c):
        z = complex(0, 0)
        for i in range(self.getIter()):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                return i  # The sequence is unbounded
        return self.getIter() - 1  # Indicate a bounded sequence


class BurningShip(Fractal, ABC):
    def __init__(self, dic):
        super().__init__(dic)

    def count(self, c):
        z = complex(0, 0)
        for i in range(self.getIter()):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                return i  # The sequence is unbounded
        return self.getIter() - 1  # Indicate a bounded sequence


class BurningShipJulia(Fractal, ABC):
    def __init__(self, dic):
        super().__init__(dic)

    def count(self, c):
        z = complex(-1, 0)
        for i in range(self.getIter()):
            c = c * c + z  # Iteratively compute z1, z2, z3 ...
            if abs(c) > 2:
                return i  # The sequence is unbounded
        return self.getIter() - 1  # Else this is a bounded sequence