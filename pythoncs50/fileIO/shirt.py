import sys
from PIL import Image ,ImageOps
# if len(sys.argv) !=3:
#     sys.exit("enter a valid number of  agument")
# lis=['.jpg','.jpeg','.png']
# if any(sys.argv[1].endswith(i) for i in lis):
#     sys.exit("not a valid input")
# if any(sys.argv[2].endswith(i) for i in lis):
#     sys.exit("not a valid input")
# try: 
#     image1=Image.open(sys.argv[1])
#     image2=Image.open(sys.argv[2])
#     s1=(300,300)
#     image1=ImageOps.fit(image1,size=s1)
#     image2=ImageOps.fit(image2,size=s1)
#     final=Image.new('RGB',s1)
#     final.paste(image1, (0, 0))
#     final.paste(image2, (0, 0))
#     final.save("output.jpg")
# except FileNotFoundError:
#     sys.exit("no file found ")

try:
    # Read the input image
    input_image = Image.open(sys.argv[1])

    # Resize and crop the input image to the same size
    size = input_image.size
    shirt_image = Image.open("shirt.png")
    shirt_image = ImageOps.fit(shirt_image, size)
    img2 = Image.open("before3.png")

    # Overlay the shirt on the input image
    input_image.paste(shirt_image, (0, 0), mask=img2)

    # Save the result as the output image
    input_image.save("output.png")
    print("Image overlay completed successfully.")

except FileNotFoundError:
    sys.exit("Input file not found.")

