#!/usr/bin/env pypy

import fileinput, hashlib, re

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class CheckingMaching:
    __debug = False

    def resolve(self):
        """
        This method parses the input using two stacks and returns the hex md5 of the result
        """
        strings = []
        multipliers = []
        readingString = False
        lastString = ''

        # Divide the string on numbers, strings and brackets
        dividedStr = []
        for part in re.split('(\[|\]|\d+)', self.__line):
            if part != '':
                dividedStr.append(part)
        
        if self.__debug:
            print dividedStr

        # Use a two stacks system in order to keep one with the operators (numbers) and
        # another one with the strings, each time than a new open bracket is found, create
        # a new string, in case of found a closer, apply the operation to the last string on
        # the strings stack
        operators = []
        strings = ['']
        prevStr = False
        for part in dividedStr:
            if part.isdigit():
                operators.append(int(part))
                prevStr = False
            else:
                if part != '' and part != ']':
                    if part == '[':
                        strings.append('')
                    else:
                        strings[len(strings) - 1] += part

                if part == ']':
                    operator = operators.pop()
                    string = strings.pop()
                    auxStr = string * operator

                    if len(strings) == 0:
                        strings = [auxStr]
                    else:
                        strings[len(strings) - 1] += auxStr

                prevStr = True

            if self.__debug:
                print "-- After Check --"
                print "Stirngs: %s" % (strings)
                print "Operators: %s" % (operators)
                print len(''.join(strings))

        if self.__debug:
            print ''.join(strings)
            print len(''.join(strings))

        finalStr = ''.join(strings)

        # Return the MD5
        return hashlib.md5(finalStr).hexdigest()

    def __init__(self, inLine):
        self.__line = inLine
        if self.__debug:
            print "Line: %s" % (self.__line) 

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for line in lines:
        print "%s" % (CheckingMaching(line).resolve())
