#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/01 $"

from PIL import Image

def a2bits(chars):
    """
    Convert a string to its bits representation as a string of 0's and 1's.
    """
    return bin(reduce(lambda x, y : (x<<8)+y, (ord(c) for c in chars), 1))[3:]

def bs(s):
    """
    Convert a int to its bits representation as a string of 0's and 1's.
    """
    return str(s) if s<=1 else bs(s>>1) + str(s&1)

def encode_image(img, message):
    """
    Hide a message (string) in an image with the
    LSB (Less Significant Bit) technic.
    """
    encoded = img.copy()
    width, height = img.size
    index = 0
    
    message = message + '~~~'
    message_bits = a2bits(message)
    
    for row in range(height):
        for col in range(width):

            if index + 3 <= len(message_bits) :

                (r, g, b) = img.getpixel((col, row))
                    
                # Convert in to bits
                r_bits = bs(r)
                g_bits = bs(g)
                b_bits = bs(b)

                # Replace (in a list) the least significant bit
                # by the bit of the message to hide
                list_r_bits = list(r_bits)
                list_g_bits = list(g_bits)
                list_b_bits = list(b_bits)
                list_r_bits[-1] = message_bits[index]
                list_g_bits[-1] = message_bits[index + 1]
                list_b_bits[-1] = message_bits[index + 2]

                # Convert lists to a strings
                r_bits = "".join(list_r_bits)
                g_bits = "".join(list_g_bits)
                b_bits = "".join(list_b_bits)
                
                # Convert strings of bits to int
                r = int(r_bits, 2)
                g = int(g_bits, 2)
                b = int(b_bits, 2)

                # Save the new pixel
                encoded.putpixel((col, row), (r, g , b))

            index += 3

    return encoded

def decode_image(img):
    """
    Find a message in an encoded image (with the
    LSB technic).
    """
    width, height = img.size
    bits = ""
    index = 0
    for row in xrange(height - 1, -1, -1):
        for col in xrange(width - 1, -1, -1):
            #print img.getpixel((col, row))
            r, g, b, aux = img.getpixel((col, row))
            #r, b, g, aux = img.getpixel((col, row))
            #b, g, r, aux = img.getpixel((col, row))
            #b, r, g, aux = img.getpixel((col, row))
            #g, b, r, aux = img.getpixel((col, row))
            #g, r, b, aux = img.getpixel((col, row))

            bits += bs(r)[-1] + bs(g)[-1] + bs(b)[-1]

            if len(bits) >= 8:
                if chr(int(bits[-8:], 2)) == '~':
                    list_of_string_bits = ["".join(list(bits[i*8:(i*8)+8])) for i in range(0, len(bits)/8)]

                    list_of_character = [chr(int(elem, 2)) for elem in list_of_string_bits]
                    return "".join(list_of_character)[:-1]
    return ""


if __name__ == '__main__':
     # Test it
     img2 = Image.open('map.png')
     print(decode_image(img2))
