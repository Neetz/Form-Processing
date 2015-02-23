from PIL import Image

test_image = "pre-result.jpg"
original = Image.open(test_image)
#original.show()

width, height = original.size   # Get dimensions
left = 31*width/50
top = 5*height/26
right = 18*width/25
bottom = 11*height/51
cropped_example = original.crop((left, top, right, bottom))
cropped_example.show()
print type(cropped_example)