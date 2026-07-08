from PIL import Image

file = Image.open("new_img.png").convert("RGB")

pxls = file.load()

def get_bits(quote_of_bits):
    height = file.height
    width = file.width
    
    collected_bits = ""
    
    for x in range(width):
        for y in range(height):
            channels = pxls[x, y]
            for i in range(3):
                collected_bits += str((channels[i] & 1))
                if len(collected_bits) == quote_of_bits:
                    return collected_bits
                
def decode():
    bits_len_of_word = get_bits(32)
    int_word_len = int(bits_len_of_word, 2)

    full_bits = get_bits(32 + int_word_len)

    bits_of_word = full_bits[32:]
    word = ""

    for i in range(0, len(bits_of_word), 8):
        byte = bits_of_word[i:i+8]
        word += chr(int(byte, 2))

    return word

word = decode()
print(word)