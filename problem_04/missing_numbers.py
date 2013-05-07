#!/usr/bin/env pypy

# Use the bit string libs: http://pythonhosted.org/bitstring/
from bitstring import BitArray
import fileinput, struct, os.path

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class MissingNumbers:
    __debug = False
    # The path to the input file with the numbers
    __file = '/Users/socialpoint/Downloads/integers'
    # Location for the index file with all the missing numbers sorted in ascending order
    # IMPORTANT: You need write access to the directory where this file will be located
    __indexFile = 'integers.index'

    def resolve(self, inPos):
        if self.__debug:
            print "Position: -%s-" % (inPos) 

        try:
            return self.__missingNumbers[inPos - 1]
        except:
            return -1

    def __init__(self):
        # Check if the index file with the missing number was previously generated,
        # in that case, only read it
        if os.path.isfile(self.__indexFile):
            self.__missingNumbers = open(self.__indexFile).read().split(',')
        else:
            # Create the index file from the file with all the numbers
            # A Bit map is used with 2^32 position in order to allocate all the
            # possible numbers with the smallest memory ussage
            maxNumber = 0
            self.__numbers = BitArray(2 ** 32)

            # Initialize all the values of the bit map to False
            for pos in xrange(0, 2 ** 32):
                self.__numbers[pos] = False

            self.__missingNumbers = []

            f = open(self.__file, "rb")
            numbersProcessed = 0
            # Read the complete file in order to obtain the max number and a binary map with all
            # the numbers on the file
            try:
                while True:
                    number = struct.unpack('i', f.read(4))
                    self.__numbers[number[0]] = True

                    if maxNumber < number[0]:
                        maxNumber = number[0]

                    if self.__debug:
                        numbersProcessed += 1

                        if numbersProcessed % 1000000 == 0:
                            print numbersProcessed

            except:
                f.close()
            finally:
                f.close()

            if self.__debug:
                print "Max Number %s" % (maxNumber)

            # Go number by number until reach the maximun number generating the missing numbers array
            # The missing number at the position th, will be the same position on the bit array
            for num in xrange(0, maxNumber):
                if not self.__numbers[num]:
                    self.__missingNumbers.append(str(num))
       
            # Create the index file with all the missing files
            if self.__debug:
                print "Writting into index file:"
                print self.__missingNumbers

            f = open(self.__indexFile, 'wb')
            f.write(','.join(self.__missingNumbers))
            f.close()

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    missingNumbers = MissingNumbers()
    for problem in xrange(0, int(lines[0])):
        print "%s" % (missingNumbers.resolve(int(lines[problem + 1])))
