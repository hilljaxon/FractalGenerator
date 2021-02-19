# Takes a configuration file given to it from the main program
# from user and output a concrete fractal object
import Fractals


def makeFractal(file_string=None):
    dictionary = {}
    if file_string is None:
        dictionary = {
            'type': 'mandelbrot',
            'pixels': 640,
            'axislength': 4.0,
            'pixelsize': 0.00625,
            'iterations': 96,
            'min': {'x': -2.0, 'y': -2.0},
            'max': {'x': 2.0, 'y': 2.0},
            'creal': -1.125129803,
            'cimag': -0.668674699,
            'imagename': 'fullmandelbrot.png'
            }
    else:
        file = open(file_string)
        ls = file.read().split("\n")
        file.close()
        for i in ls:
            subList = i.split(": ")
            if len(subList) > 1:
                dictionary[subList[0].lower()] = subList[1].lower().strip()
        if "type" in dictionary and "pixels" in dictionary and "centerx" in dictionary and \
                "centery" in dictionary and "axislength" in dictionary and "iterations" in dictionary:
            typeCorrect(dictionary)
            fillDic(dictionary,file_string)
        else:
            raise NotImplementedError("Incorrect format in fractal configuration file")



        
    if dictionary.get('type') == "mandelbrot":
        return Fractals.Mandelbrot(dictionary)
    if dictionary.get("type") == "julia":
        return Fractals.Julia(dictionary)
    if dictionary.get("type") == "mandelbrot3":
        return Fractals.Mandelbrot3(dictionary)
    if dictionary.get("type") == "mandelbrot4":
        return Fractals.Mandelbrot4(dictionary)
    if dictionary.get("type") == "phoenix":
        return Fractals.Phoenix(dictionary)
    if dictionary.get("type") == "burningship":
        return Fractals.BurningShip(dictionary)
    if dictionary.get("type") == "burningshipjulia":
        return Fractals.BurningShipJulia(dictionary)
    else:
        raise NotImplementedError("Type of fractal not recognized")

def typeCorrect(dic):
    dic['pixels'] = eval(dic.get('pixels'))
    dic['iterations'] = eval(dic.get('iterations'))
    dic['centerx'] = eval(dic.get('centerx'))
    dic['centery'] = eval(dic.get('centery'))
    dic['axislength'] = eval(dic.get('axislength'))
    if("creal" in dic):
        dic['creal'] = eval(dic.get('creal'))
    if ("creal" in dic):
        dic['cimag'] = eval(dic.get('cimag'))

def fillDic(dic,s):
    minimum = {
        'x':(dic['centerx'] - (dic['axislength'] / 2.0)), 'y':(dic['centery'] - (dic['axislength'] / 2.0))
    }
    maximum = {
        'x':(dic['centerx'] + (dic['axislength'] / 2.0)), 'y':(dic['centery'] + (dic['axislength'] / 2.0))
    }
    pixelSize = abs(maximum['x'] - minimum['x']) / dic.get('pixels')
    dic['min']=minimum
    dic['max']=maximum
    dic['pixelsize']=pixelSize
    dic['imagename']=s.split('/')[len(s.split('/'))-1].split('.')[0]+".png"
