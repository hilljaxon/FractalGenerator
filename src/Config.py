# These are the different views of the Mandelbrot set you can make with this
# program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.

imageTypes = {
        'fullmandelbrot': {
            'type': "mandelbrot",
            'centerX': -0.6,
            'centerY': 0.0,
            'axisLength': 2.5,
            'z': complex(0, 0),
            },
        'spiral0': {
            'type': "mandelbrot",
            'centerX': -0.761335372924805,
            'centerY': 0.0835704803466797,
            'axisLength': 0.004978179931102462,
            'z': complex(0, 0),
            },
        'spiral1': {
            'type': "mandelbrot",
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLength': 0.002,
            'z': complex(0, 0),
            },
        'seahorse': {
            'type': "mandelbrot",
            'centerX': -0.745,
            'centerY': 0.105,
            'axisLength': 0.01,
            'z': complex(0, 0),
            },
        'elephants': {
            'type': "mandelbrot",
            'centerX':  0.30820836067024604,
            'centerY':  0.030620936230004017,
            'axisLength':  0.03,
            'z': complex(0, 0),
            },
        'leaf': {
            'type': "mandelbrot",
            'centerX': -1.543577002,
            'centerY': -0.000058690069,
            'axisLength':  0.000051248888,
            'z': complex(0, 0),
            },
        'fulljulia': {
            'type': "julia",
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  4.0,
            'z': complex(-1, 0),
            },
        'hourglass': {
            'type': "julia",
            'centerX':     0.618,
            'centerY':     0.00,
            'axisLength':  0.017148277367054,
            'z': complex(-1, 0),
        },
        'lakes': {
            'type': "julia",
            'centerX': -0.339230468501458,
            'centerY': 0.417970758224314,
            'axisLength': 0.164938488846612,
            'z': complex(-1, 0),
            },
        }
