from PIL import Image

cactus_image = Image.open("/Users/elijah/BYUI/Programming Building Blocks/Week 4/cse110_images/cactus.jpg")
background_image = Image.open("/Users/elijah/BYUI/Programming Building Blocks/Week 4/cse110_images/desert.jpg")

c_width, c_height = cactus_image.size
b_height, b_width = background_image.size
pixels_cactus = cactus_image.load()
pixels_background = background_image.load()

for h in range(c_height):
    for w in range(c_width):
        check_pixel = pixels_cactus[w,h]
        change_pixel = pixels_background[w,h]
        c_r, c_g, c_b = check_pixel
        if (c_g >= 200 and c_g <=255) and (c_r <= 180) and (c_b <= 180):
            pixels_cactus[w,h] = change_pixel  

cactus_image.show()