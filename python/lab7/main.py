#the selected image file is outputted as 3 seperate, filtered images (embossed, blurred, and turned into a thumbnail)
from PIL import Image
from PIL import ImageFilter


im = Image.open("ButtersStotch.jpg")

im1 = im.filter(ImageFilter.CONTOUR)
im1.show()
im1.save("Contour.jpg")


OrgImage = Image.open("ButtersStotch.jpg")

blurredButters = OrgImage.filter(ImageFilter.BLUR)
blurredButters.show()
blurredButters.save("blurredButters.jpg")


def buttersthumbnail():
    try:
        image = Image.open("ButtersStotch.jpg")
        image.thumbnail((50,50))
        image.save("buttersthumbnail.jpg")
        image1 = Image.open("buttersthumbnail.jpg")
        image1.show()
    except IOError:
        pass


buttersthumbnail()

