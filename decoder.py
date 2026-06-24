from PIL import Image

file = Image.open("new_img.png").convert("RGB")

pxls = file.load()

def decode():
    height = file.height
    width = file.width
    
    collected_bits = ""
    
    str_word = ""
    for x in range(width):
        for y in range(height):
            r, g, b = pxls[x, y]
            r = (r & 1)
            collected_bits += str(r)
            if len(collected_bits) == 8:
                letter = chr(int(collected_bits, 2))
                str_word += letter
                collected_bits = ""
                if str_word.endswith("###"):
                    return(str_word.removesuffix("###"))
            g = (g & 1)
            collected_bits += str(g)
            if len(collected_bits) == 8:
                letter = chr(int(collected_bits, 2))
                str_word += letter
                collected_bits = ""
                if str_word.endswith("###"):
                    return(str_word.removesuffix("###"))
            b = (b & 1)
            collected_bits += str(b)
            if len(collected_bits) == 8:
                letter = chr(int(collected_bits, 2))
                str_word += letter
                collected_bits = ""
                if str_word.endswith("###"):
                    return(str_word.removesuffix("###"))
    return str_word
word = decode()
print(word)