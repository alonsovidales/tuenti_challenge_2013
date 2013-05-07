#!/usr/bin/env pypy

import fileinput, re

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class Losts:
    __debug = False

    def resolve(self):
        prevBuffer = []
        groupsMin = []
        # Get the possible positions for flashbacks
        for operatorPos in xrange(0, len(self.__operators)):
            if self.__operators[operatorPos] == '<':
                groupsMin.append(('<', prevBuffer[:]))
                prevBuffer = []
            elif self.__operators[operatorPos] == '.':
                prevBuffer.append('.')
            elif self.__operators[operatorPos] == '>':
                prevBuffer = []

        prevBuffer = []
        groupsBig = []
        # Get the possible positions for flashforwards
        for operatorPos in xrange(len(self.__operators) - 1, -1, -1):
            if self.__operators[operatorPos] == '>':
                groupsBig.append(('>', prevBuffer[:]))
                prevBuffer = []
            elif self.__operators[operatorPos] == '.':
                prevBuffer.append('.')
            elif self.__operators[operatorPos] == '<':
                prevBuffer = []

        finalOrder = []
        # Put in order all the operators with all the possible positions
        for operator in self.__operators:
            if operator == '<':
                finalOrder.append(groupsMin.pop(0))
            elif operator == '>':
                finalOrder.append(groupsBig.pop(0))

        if self.__debug:
            print "Final: %s" % (finalOrder)

        unique = True
        # Check if this is a unique solution
        for positions in finalOrder:
            if len(positions[1]) > 1:
                unique = False

        # This is a unique season, build and return it
        if unique:
            prevBuffer = []
            nextBuffer = []
            result = []
            for operatorPos in xrange(len(self.__operators) - 1, -1, -1):
                if self.__operators[operatorPos] == '>':
                    nextBuffer.append(self.__initScenes[operatorPos])
                elif self.__operators[operatorPos] == '<':
                    prevBuffer.append(self.__initScenes[operatorPos])
                else:
                    if len(nextBuffer) > 0:
                        result += nextBuffer
                        nextBuffer = []

                    result.append(self.__initScenes[operatorPos])

                    if len(prevBuffer) > 0:
                        result += prevBuffer
                        prevBuffer = []

            result.reverse()
            return ','.join(result)

            """
            result = []
            operators = []
            for operatorPos in xrange(0, len(self.__operators)):
                if self.__operators[operatorPos] == '>':
                    result.pop()
                    result.append(self.__initScenes[operatorPos - 1] + ',' + self.__initScenes[operatorPos])
                else:
                    result.append(self.__initScenes[operatorPos])
                    operators.append(self.__operators[operatorPos])

            if self.__debug:
                print "-- Removed flashforwards --"
                print operators
                print result

            for operatorPos in xrange(0, len(operators)):
                if operators[operatorPos] == '<':
                    aux = result[operatorPos]
                    result[operatorPos] = result[operatorPos - 1]
                    result[operatorPos - 1] = aux

            return ','.join(result)"""


        # Check if the solution is valid, checking if it doesn't contains anbiguous extremes
        if (
                (finalOrder[0][0] == '<' and len(finalOrder[0][1]) == 0) or
                finalOrder[0][0] == '>'
            ) and (
                (finalOrder[len(finalOrder) - 1][0] == '>' and len(finalOrder[len(finalOrder) - 1][1]) == 0) or
                finalOrder[len(finalOrder) - 1][0] == '<'
            ):
                return 'valid'

        return 'invalid'

    def __init__(self, inScript):
        self.__script = inScript
        self.__initScenes = re.split('[<|>|.]', inScript)[1:]
        self.__operators = re.findall('[<|>|.]', inScript)

        if self.__debug:
            print "Operators: %s" % (self.__operators)
            print "Scenes: %s" % (self.__initScenes) 

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for scriptPos in xrange(0, int(lines[0])):
        print "%s" % (Losts(lines[scriptPos + 1]).resolve())
