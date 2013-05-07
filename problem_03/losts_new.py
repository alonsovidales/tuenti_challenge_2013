#!/usr/bin/env pypy

import fileinput, re

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class Losts:
    __debug = False

    def resolve(self):
        scenes = {}
        filteresScenes = []
        filteredOperators = []
        # Remove the duplicated scenes, and check if is all valid (the scenes are in order, etc)
        for scenePos in xrange(0, len(self.__initScenes)):
            if self.__initScenes[scenePos] not in scenes:
                filteresScenes.append(self.__initScenes[scenePos])
                filteredOperators.append(self.__operators[scenePos])
                scenes[self.__initScenes[scenePos]] = self.__operators[scenePos]
            else:
                # Check if the previous scene indicates is confronted with this
                if scenes[self.__initScenes[scenePos]] == '<' or (scenes[self.__initScenes[scenePos]] == '.' and self.__operators[scenePos] != '<'):
                    return 'invalid'

        # Check for ambiguous definitions on the original list os seassons
        opened = False
        prevChar = ''
        for operator in self.__operators:
            if self.__debug:
                print "Opened: %s Operator: %s Prev: %s" % (opened, operator, prevChar)
            if operator == '>':
                opened = True
            elif operator == '<':
                opened = False
            elif prevChar == '.' and opened:
                return 'valid'

            prevChar = operator

        # The scene is correct, reverse all the scenes with a < as delimiter
        for scenePos in xrange(0, len(filteredOperators)):
            if filteredOperators[scenePos] == '<':
                aux = filteresScenes[scenePos - 1]
                filteresScenes[scenePos - 1] = filteresScenes[scenePos]
                filteresScenes[scenePos] = aux

        if self.__debug:
            print "-- Filtered --"
            print "Operators: %s" % (filteredOperators)
            print "Scenes: %s" % (filteresScenes)

        return ','.join(filteresScenes)

    def __init__(self, inScript):
        self.__script = inScript
        self.__initScenes = re.split('[<|>|.]', inScript)[1:]
        self.__operators = re.findall('[<|>|.]', inScript)

        if self.__debug:
            print "--"
            print "Operators: %s" % (self.__operators)
            print "Scenes: %s" % (self.__initScenes) 

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for scriptPos in xrange(0, int(lines[0])):
        print "%s" % (Losts(lines[scriptPos + 1]).resolve())
