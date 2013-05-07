#!/usr/bin/env pypy

import fileinput, binascii

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class Problem:
    """
    Ok, this problem is a bit special :)
    First of all from the specifications I have: "you can't reuse certain things, can you?"
    Well, encryption + reuse, we have the two used pad problem I reviewed a course about cryptography that I did time ago:
        https://www.coursera.org/course/crypto
    The problem is when the pad is used more more than two times we have (+ is the xor):
        c1 = m1 + K
        c2 = m2 + K
    Then:
        c1 + c2 = m1 + K + m2 + K
    Well, we can remove the K and obtain:
        c1 + c2 = m1 + m2
    Then if I do a xor of an known string to the m1 + m2 in all the possible positions for example " the " that is
    very common, if one of the strings contains this string, I'll obtain the sub string of the other string.
    For example I apply " the " an I detected " have", I deducted that after the have, I should to have a space, and I
    appyed " have ", obtaining a char more after the " the ", and doing this process, I detected a sub string that searched
    using Google, a sentence of "Woody Allen", and that's all :) I ontained a master string, the biggest of all them.
    Using the master string, I can decode string with a smaller size of this.
    I commented the code of the process to detect the strings, etc.
    """

    __debug = False
    __biggerDecodedLine = "Some humans would do anything to see if it was possible to do it. If you put a large switch in some cave somewhere, with a sign on it saying 'End-of-the-World Switch. PLEASE DO NOT TOUCH', the paint wouldn't even have time to dry."
    __biggestDecodedLineEncoded = "46fb200144df180dba5c8f52481c0ef515d9e963d0008b859c121b51ee8d0ca8e98b01d89a841257a1559174765d8ea95b9e69aaf014624eb5be51c415cfc5854aaa6c18b929b496e71a721303846856ae31c6d24529f4a9c19ef46a75819ea156598893e644f2c7f7ae39381b0184b5c937f8473a3800842e822014c4e8a94cc36373e81a6ee94632678625f2a5ff2eeb4eeae42d4190791cfd8fcc5f8dec2c2c5547fd63ebcb8a3c56303b4976dff9502d30e85955ed128114eb094b1667bb7da282be7ed7f1873d8e8c31d18ef24a48e990db46f5a591ecbc33704380a1b9b8babcdb4fe3"

    def __xorTwoStrings(self, xs, ys):
        """
        Do a xor of all the characters of a string char by char...
        """
        return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

    def resolve(self):
        results = []
        for line in self.__lines:
            # Do the xor with the encoded master line
            xortWithKnownString = self.__xorTwoStrings(self.__biggestDecodedLineEncoded.decode("hex"), line.decode("hex"))
            # Do the xor with the decoded master line, obtaining the decoded line
            results.append(self.__xorTwoStrings(xortWithKnownString, self.__biggerDecodedLine))

        return '\n'.join(results)

    def __init__(self, inLines):
        self.__lines = inLines

        # This code id commented, because I used it to test the decoder system and create a stragegy
        """pad = "Rather than XORing the Unicode representations, just convert each character into the number it represents in hex, XOR those, then convert it back to hex. You can still do that one character at a time"

        strCip = []
        strCip.append("The fact that it gives correct result is an artifact of the particular character encoding for digits and letters.")
        strCip.append("The should convert the numbers to BigInteger, XOR them, and convert back to String:")
        strCip.append("Why are you storing hex values as strings? it'd be a much better idea to represent hex numbers as hex integers or longs.")
        strCip.append("The solves the problem. But while xoring 4 XOR 4, the result is 0 which is lost when we store it in integer n3. Any idea how to solve it?")
        strCip.append("I edited my answer, now the printed results will always have 6 charac")
        strCip.append("but as it is stored in integer")

        for strToEncode in strCip:
            print self.__xorTwoStrings(strToEncode, pad).encode("hex")

        exit()"""

        """self.__xorMapTable = {}
        for left in xrange(31, 128):
            for right in xrange(31, 128):
                if chr(left ^ right) in self.__xorMapTable:
                    self.__xorMapTable[chr(left ^ right)].add(chr(left))
                    self.__xorMapTable[chr(left ^ right)].add(chr(right))
                else:
                    self.__xorMapTable[chr(left ^ right)] = set([chr(left), chr(right)])

        print self.__xorMapTable
        print len((self.__xorMapTable[chr(ord('T') ^ ord('W'))] & self.__xorMapTable[chr(ord('M') ^ ord('P'))]))
        exit()"""

        #Not necessary any more, I just decoded the first part of the lines using the part that I discovered + Google :)
        #I used the next lines in order to scan char by char all the possible sub strings doing the xor
        #with some common strings, after found a known part, I deduced the rest of the line

        """
        lineToDecode = inLines.pop(0).decode("hex")

        for linePos in range(len(inLines)):
            decoded = self.__xorTwoStrings(lineToDecode, inLines[linePos].decode("hex"))

            mixed = []
            subDecoder = "Some humans would do anything to see if it was possible to do it. If you put a large switch in some cave somewhere, with a sign on it saying 'End-of-the-World Switch. PLEASE DO NOT TOUCH', the paint wouldn't even have time to dry"
            print self.__xorTwoStrings(decoded, subDecoder)

            mixed.append((self.__xorTwoStrings(decoded[part: part + len(subDecoder)], subDecoder), linePos, part))

            for part in range(len(decoded) - len(subDecoder)):
                mixed.append((self.__xorTwoStrings(decoded[part: part + len(subDecoder)], subDecoder), linePos, part))

            for finalLine in mixed:
                print finalLine
            """

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    print "%s" % (Problem(lines).resolve())
