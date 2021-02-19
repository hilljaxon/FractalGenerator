from abc import ABC, abstractmethod
from colour import Color
RAINBOW = [Color("blue"), Color("yellow"), Color("red"), Color("green"), Color("orange"), Color("purple")]
ZRAINBOW = [Color("blue"), Color("orange"), Color("green"), Color("red"), Color("yellow"), Color("purple")]
deep = [Color("blue"), Color("black"), Color("green"), Color("black"), Color("red"), Color("black"), Color("blue")]
COLD = [Color("black"), Color("blue"), Color("white"), Color("blue")]
HOT = [Color("red"), Color("orange"), Color("yellow"), Color("white"), Color("red")]
# TEST = [Color("black"), Color("blue"), Color("white"), Color("red"), Color("purple")]
TEST = [Color("white"), Color("black"), Color("blue"), Color("orange"), Color("white")]



class Gradient(ABC):
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Gradient must implement __init__")

    def getColor(self, n):  # takes an int as input and returns a string "#RRGGBB".
        raise NotImplementedError("Concrete subclass of Gradient must implement getColor() method")


class GrayScale(Gradient, ABC):
    def __init__(self, n):
        temp = []
        ls = list(Color("black").range_to(Color('white'), n))
        for i in range(n):
            temp.append(ls[i].hex)
        while len(ls) < n:
            ls+=ls
        self.__colorList = temp

    def getColor(self, n):
        return self.__colorList[n]


class Rainbow(Gradient, ABC):
    def __init__(self, n):
        ls = []
        for i in range(n//20):
            temp = (list(RAINBOW[(i)%len(RAINBOW)].range_to(RAINBOW[(i+1)%len(RAINBOW)], 20)))
            for e in temp:
                ls.append(e.hex)
        while len(ls) < n:
            ls+=ls
        self.__colorList = ls

    def getColor(self, n):
        return self.__colorList[n]


class Deep(Gradient, ABC):
    def __init__(self, n):
        ls = []
        for i in range(n // 10):
            temp = (list(deep[(i) % len(deep)].range_to(deep[(i + 1) % len(deep)], 10)))
            for e in temp:
                ls.append(e.hex)
        while len(ls) < n:
            ls += ls
        self.__colorList = ls

    def getColor(self, n):
        return self.__colorList[n]


class ColorCube(Gradient, ABC):
    def __init__(self, n):
        ls = []
        for i in range(n // 10):
            temp = (list(ZRAINBOW[(i) % len(ZRAINBOW)].range_to(ZRAINBOW[(i + 1) % len(ZRAINBOW)], 10)))
            for e in temp:
                ls.append(e.hex)
        while len(ls) < n:
            ls += ls
        self.__colorList = ls

    def getColor(self, n):
        return self.__colorList[n]

class Cold(Gradient, ABC):
    def __init__(self, n):
        ls = []
        for i in range(n//20):
            temp = (list(COLD[(i)%len(COLD)].range_to(COLD[(i+1)%len(COLD)], 20)))
            for e in temp:
                ls.append(e.hex)
        while len(ls) < n:
            ls+=ls
        self.__colorList = ls

    def getColor(self, n):
        return self.__colorList[n]


class Hot(Gradient, ABC):
    def __init__(self, n):
        ls = []
        for i in range(n//20):
            temp = (list(HOT[(i)%len(HOT)].range_to(HOT[(i+1)%len(HOT)], 20)))
            for e in temp:
                ls.append(e.hex)
        while len(ls) < n:
            ls+=ls
        self.__colorList = ls

    def getColor(self, n):
        return self.__colorList[n]

class Test(Gradient, ABC):
    def __init__(self, n):
        ls = []
        for i in range(n//10):
            temp = (list(TEST[(i)%len(TEST)].range_to(TEST[(i+1)%len(TEST)], 10)))
            for e in temp:
                ls.append(e.hex)
        while len(ls) < n:
            ls+=ls
        self.__colorList = ls

    def getColor(self, n):
        return self.__colorList[n]


    def getColor(self, n):
        return self.__colorList[n]