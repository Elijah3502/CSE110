from PIL import Image

cactus_image = Image.open("/Users/elijah/BYUI/Programming Building Blocks/Week 4/cse110_images/cactus.jpg")
background_image = Image.open("/Users/elijah/BYUI/Programming Building Blocks/Week 4/cse110_images/desert.jpg")
#Gets dimensions of green screen
c_width, c_height = cactus_image.size
#Gets dimesnsions of background image
b_height, b_width = background_image.size
#Loads the green screen pixels
pixels_cactus = cactus_image.load()
#Loads the background image pixels
pixels_background = background_image.load()


#Checks the columns
for h in range(c_height):
    #checks the width
    for w in range(c_width):
        #Green screen pixel
        check_pixel = pixels_cactus[w,h]
        #Background pixel
        change_pixel = pixels_background[w,h]
        #Gets sub pixels for the checked pixel
        c_r, c_g, c_b = check_pixel
        #if checked pixel is within range of color
        if (c_g >= 200 and c_g <=255) and (c_r <= 180) and (c_b <= 180):
            #change green screen image pixel to background image pixel
            pixels_cactus[w,h] = change_pixel  
#show image
cactus_image.show()