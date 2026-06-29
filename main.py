from PIL import Image

file = Image.open("image.png").convert("RGB")

pxls = file.load()

def make_bin(word):
    bin_word = ""
    for i in word:
        num = ord(i)
        bits = format(num, "08b")
        bin_word += bits
    sharp_code = ord("#")
    bits_of_sharp = format(sharp_code, "08b")
    for i in range(0, 3):
        bin_word += bits_of_sharp
    return bin_word
    
def code_word(bin_word):
    height = file.height
    width = file.width
    
    bit_index = 0
    is_done = False
    bit_len = len(bin_word)
    
    for x in range(width):
        if is_done:
            break
        else:
            for y in range(height):
                r, g ,b = pxls[x, y]
                if bit_index < bit_len:
                    r = (r & 254) | int(bin_word[bit_index])
                    bit_index += 1
                else:
                    is_done = True
                if bit_index < bit_len:
                    g = (g & 254) | int(bin_word[bit_index])
                    bit_index += 1
                else:
                    is_done = True
                if bit_index < bit_len:
                    b = (b & 254) | int(bin_word[bit_index])
                    bit_index += 1
                else:
                    is_done = True
                pxls[x, y] = (r, g, b)
                if is_done:
                    is_done = True
    file.save("new_img.png", "PNG")
    
    
word_for_code = str(input("Enter a word which you would like to insert in image (ONLY ENGLISH):"))
bits_of_word = make_bin(word_for_code)
code_word(bits_of_word)