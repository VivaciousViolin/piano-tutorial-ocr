
import os
import numpy
from PIL import Image


utilspath = os.getcwd() + r'\utils'
print(utilspath)


frame = Image.open(utilspath + r'\test.png')
imagearray = numpy.array(frame, dtype=numpy.uint8)
print(imagearray)

pixels = [list(i[:3]) for i in imagearray[1400]]