from PIL import Image

file = Image.open("image.png").convert("RGB")

pxls = file.load()

def make_bin(word):
    bin_word = ""
    for i in word:
        num = ord(i)
        bits = format(num, "08b")
        bin_word += bits
    return bin_word
    
def code_word(bin_word):
    height = file.height
    width = file.width

    bit_index = 0

    bit_word_len = (len(bin_word))

    bit_len = (format(bit_word_len, "032b"))

    full_bits = bit_len + bin_word

    bits_count = len(full_bits)

    for x in range(width):
        for y in range(height):
            if bit_index >= bits_count:
                file.save("new_img.png", "PNG")
                return
            else:
                channels = list(pxls[x, y])
                for i in range(3):
                    if bit_index < bits_count:
                        channels[i] = (channels[i] & 254) | int((full_bits[bit_index]))
                        bit_index += 1
                pxls[x, y] = tuple(channels)
    
word_for_code = str(input("Enter a word which you would like to insert in image (ONLY ENGLISH):"))
bits_of_word = make_bin(word_for_code)
code_word(bits_of_word)