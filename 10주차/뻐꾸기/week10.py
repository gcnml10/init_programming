from PIL import Image
from PIL import ImageFilter

img = Image.open('cat.jpg')


img3 = img.filter(ImageFilter.CONTOUR)

img3.show()