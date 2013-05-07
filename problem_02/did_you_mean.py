#!/usr/bin/env pypy

import os, fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class DidYouMean:
    # This is the directory where the dictionaries files should to be allocated
    __dictionariesDir = 'dictionaries/'

    def __getSortedLetters(self, inWord):
        return ''.join(sorted(list(inWord)))

    def getWords(self, inWord):
        """
        If the key exists in the dictionary on memory, return the list of words without the given word
        sorted
        """
        key = self.__getSortedLetters(inWord)
        if key in self.__indexDict:
            return sorted(list(self.__indexDict[self.__getSortedLetters(inWord)] - set([inWord])))

        return []

    def __init__(self, inFileName):
        """
        Creates the index from the given dictionary file in a dictionary on memory in order to locate
        the possible words in O(1)
        """
        if os.path.isfile(os.path.join(self.__dictionariesDir, inFileName)):
            fileDir = os.path.join(self.__dictionariesDir, inFileName)

            # Create a dictionary with the letters of the work sorted alfabetically
            # and as values all the possible words, doing this we will be able to fin
            # all the possible words with the same characters
            self.__indexDict = {}
            for line in open(fileDir).read().split('\n'):
                dictKey = self.__getSortedLetters(line)
                if dictKey in self.__indexDict:
                    self.__indexDict[dictKey].add(line)
                else:
                    self.__indexDict[dictKey] = set([line])
              
if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    didYouMean = DidYouMean(lines[1])

    for wordPos in xrange(0, int(lines[3])):
        print "%s -> %s" % (lines[wordPos + 5], ' '.join(didYouMean.getWords(lines[wordPos + 5])))
