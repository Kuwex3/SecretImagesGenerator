from PIL import Image

file = Image.open("new_image.png").convert("RGB")

pxls = file.load()

pxl1 = pxls[530, 502]
pxl2 = pxls[531, 502]
pxl3 = pxls[532, 502]

def decode():
    bit1 = str(pxl1[0] & 1)
    bit2 = str(pxl1[1] & 1)
    bit3 = str(pxl1[2] & 1)
    bit4 = str(pxl2[0] & 1)
    bit5 = str(pxl2[1] & 1)
    bit6 = str(pxl2[2] & 1)
    bit7 = str(pxl3[0] & 1)
    bit8 = str(pxl3[1] & 1)
    print(bit1+bit2+bit3+bit4+bit5+bit6+bit7+bit8)

decode()