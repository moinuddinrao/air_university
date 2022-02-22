from PIL import Image
from PIL.ImageFilter import EDGE_ENHANCE_MORE

# Original image
img = Image.open('jaun-elia.jpg')
img.show()

# Function to apply padding
def addPadding(img, top, right, bottom, left, color):
    width, height = img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(img.mode, (new_width, new_height), color)
    result.paste(img, (left, top))
    return result

img_padded = addPadding(img, 50, 100, 50, 100, (0, 0, 0))
img_padded.save('padded.jpg', quality=95)
img_padded.show()

# Applying the filter
img1 = img_padded.filter(EDGE_ENHANCE_MORE)
img1.save('filter.jpg')
img1.show()