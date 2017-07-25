from PIL import Image

# RGB values for recoloring.
darkBlue = (200, 33, 55)
red = (200, 25, 15)
lightBlue = (98, 135, 188)
yellow = (100, 270, 200)

# Import image.
my_image = Image.open("kelseaballerini.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.
#print(image_list)

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
for item in image_list:
    intensity = item[0]+item[1]+item[2]
    if intensity < 182:
        recolored.append (darkBlue)
    if intensity >= 182 and intensity<364:
        recolored.append (red)
    if intensity >= 364 and intensity<546:
        recolored.append (lightBlue)
    if intensity >= 546:
        recolored.append (yellow)


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
