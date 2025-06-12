import colorgram


# Todo 1:  Extract 10 colours from the image into a list. Can get the list and comment out the code as well( For learing
## purposes- just leave it.  

rgb_colours=[]
colours = colorgram.extract('image.jpg', 8)

for i in colours:
    rgb_colours.append((i.rgb.r, i.rgb.g, i.rgb.b))




