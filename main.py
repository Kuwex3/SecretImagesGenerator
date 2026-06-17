from PIL import Image

file = Image.open("image.png").convert("RGB")

pxls = file.load()

pxl1 = pxls[530, 502]
pxl2 = pxls[531, 502]
pxl3 = pxls[532, 502]

secret_letter = ord("X")
print(secret_letter)
bits_of_secret = format(secret_letter, "08b")
print(bits_of_secret)

r1 = pxl1[0]
b1 = pxl1[1]
g1 = pxl1[2]

new_pxl_r1 = (r1 & 254) | 0
new_pxl_b1 = (b1 & 254) | 1
new_pxl_g1 = (g1 & 254) | 0

r2 = pxl2[0]
b2 = pxl2[1]
g2 = pxl2[2]

new_pxl_r2 = (r2 & 254) | 1
new_pxl_b2 = (b2 & 254) | 1
new_pxl_g2 = (g2 & 254) | 0
# print(r,bin(r))
# print(new_pxl,bin(new_pxl))