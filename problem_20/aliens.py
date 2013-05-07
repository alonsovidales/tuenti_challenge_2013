#!/usr/bin/env pypy

import fileinput, base64, binascii

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-05-06"

class Problem:
    __debug = False

    def resolve(self):
        result = []
        for line in self.__lines:
            result.append(base64.b64decode(line))

        result = '\n'.join(result)
        return result

    def __init__(self, inLines):
        self.__lines = inLines

        if self.__debug:
            print "Line: %s" % (self.__line) 

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    print "%s" % (Problem(lines).resolve())
