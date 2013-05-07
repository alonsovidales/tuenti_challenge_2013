#!/usr/bin/env pypy

import json, copy, operator

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class Boozzle:
    __debug = False
    __dictFile = 'boozzle-dict.txt'

    def __calcWordsWeight(self, inWordChars, inChars):
        """
        Returns the word lenght accorgding to the given algorithm
        """
        score = 0
        wordMultMax = 1
        for char in inWordChars:
            if int(char[1]) == 1:
                score += inChars[char[0]] * int(char[2])
            else:
                score += inChars[char[0]]
                if wordMultMax < int(char[2]):
                    wordMultMax = int(char[2])

        return score * wordMultMax + len(inWordChars)

    def __getAllThePossibleWordsByDeep(self, inCurrentPos, inCharValues, inDuration, inBoard, inPossibleWords, inVisitedChars, inVisitedPos):
        """
        Get all the possible words from the given position, checks against the dictionary, and returns the words plus the value on a dict
        """
        # Chec is we has yet visited this position
        currentPosStr =  "%d_%d" % (inCurrentPos[0], inCurrentPos[1])
        if currentPosStr in inVisitedPos or len(inVisitedPos) + 1 > inDuration or len(inVisitedChars) + 1 > self.__maxWordSize:
            if len(inVisitedChars) + 1 > self.__maxWordSize:
                print "Return by size: %s - %s" % ((len(inVisitedChars) + 1), self.__maxWordSize)
            return

        newVisited = copy.copy(inVisitedPos)
        newVisited.add(currentPosStr)

        newVisitedChars = copy.copy(inVisitedChars)
        newVisitedChars.append(inBoard[inCurrentPos[0]][inCurrentPos[1]])

        currentWord = ''.join([char[0] for char in newVisitedChars])

        # If the word is not in the plausible words dictionary (doesn't start with a string that is the
        # begging on one of the words at the dictionary)
        if currentWord not in self.__plausibleDict:
            return

        # Check if the curent word is one of the words on the dictionary, in this case, could be used
        if currentWord in self.__dict:
            weight = self.__calcWordsWeight(newVisitedChars, inCharValues)

            if currentWord not in inPossibleWords or inPossibleWords[currentWord] < weight:
                inPossibleWords[currentWord] = weight

        if self.__debug:
            print "PossibleStr: %s" % (currentWord)

        # Move to another letter in the board
        possiblePos = []
        # Check Top
        if inCurrentPos[0] - 1 >= 0:
            newPos = inCurrentPos[:]
            newPos[0] -= 1
            possiblePos.append(newPos)

        # Check Bottom
        if inCurrentPos[0] + 1 < len(inBoard):
            newPos = inCurrentPos[:]
            newPos[0] += 1
            possiblePos.append(newPos)

        # Check Left
        if inCurrentPos[1] - 1 >= 0:
            newPos = inCurrentPos[:]
            newPos[1] -= 1
            possiblePos.append(newPos)

        # Check Rght
        if inCurrentPos[1] + 1 < len(inBoard[0]):
            newPos = inCurrentPos[:]
            newPos[1] += 1
            possiblePos.append(newPos)

        # Check TopLeft diag
        if inCurrentPos[0] - 1 >= 0 and inCurrentPos[1] - 1 >= 0:
            newPos = inCurrentPos[:]
            newPos[0] -= 1
            newPos[1] -= 1
            possiblePos.append(newPos)

        # Check TopRight diag
        if inCurrentPos[0] - 1 >= 0 and inCurrentPos[1] + 1 < len(inBoard[0]):
            newPos = inCurrentPos[:]
            newPos[0] -= 1
            newPos[1] += 1
            possiblePos.append(newPos)

        # Check BottLeft diag
        if inCurrentPos[0] + 1 < len(inBoard[0]) and inCurrentPos[1] - 1 >= 0:
            newPos = inCurrentPos[:]
            newPos[0] += 1
            newPos[1] -= 1
            possiblePos.append(newPos)

        # Check BottRight diag
        if inCurrentPos[0] + 1 < len(inBoard[0]) and inCurrentPos[1] + 1 < len(inBoard[0]):
            newPos = inCurrentPos[:]
            newPos[0] += 1
            newPos[1] += 1
            possiblePos.append(newPos)

        for pos in possiblePos:
            self.__getAllThePossibleWordsByDeep(pos, inCharValues, inDuration, inBoard, inPossibleWords, newVisitedChars, newVisited)


    def __searchBestFitByDep(self, inSortedByWeight, inPossibleWords, inTime, inBestFit, inCurrentScore, inStop):
        """
        Returns using the mutable inCurrentScore the max possible value for the best fit
        The inSortedByWeight is sorted by score, the score is the relation between the necessary time to write
        the word, and the value
        """
        # If the remaining time is 0, this is the best fit, because of we are checking the list of words in sorted by score
        if inTime == 0:
            inStop[0] = True
            if inCurrentScore > inBestFit[0]:
                inBestFit[0] = inCurrentScore

        # We don't have anought time, this is a possible solution, but the we didn't use all the time :'(
        if inTime <= 0:
            return

        # Well, this path is the best by the moment
        if inCurrentScore > inBestFit[0]:
            inBestFit[0] = inCurrentScore

        # We don't have more chars to check
        if len(inSortedByWeight) == 0:
            return

        # Check if any other path found a perfect solution before than this one
        if not inStop[0]:
            # Check the path using the current char
            self.__searchBestFitByDep(inSortedByWeight[1:], inPossibleWords, inTime - (len(inSortedByWeight[0][0]) + 1), inBestFit, inCurrentScore + inPossibleWords[inSortedByWeight[0][0]], inStop)

        if not inStop[0]:
            # Check the path withous use the current char
            self.__searchBestFitByDep(inSortedByWeight[1:], inPossibleWords, inTime, inBestFit, inCurrentScore, inStop)

    def resolve(self, inChars, inSize, inDuration, inBoard):
        if self.__debug:
            print "Chars: %s" % (inChars)
            print "Size: %s" % (inSize)
            print "Duration: %s" % (inDuration)
            print "Board: %s" % (inBoard)

        # Get the list of all the possible words on the board
        possibleWords = {}
        for row in xrange(0, len(inBoard)):
            for col in xrange(0, len(inBoard[0])):
                words = self.__getAllThePossibleWordsByDeep([row, col], inChars, inDuration, inBoard, possibleWords, [], set())

        if self.__debug:
            print "Possible List: %s" % (possibleWords)

        # Create the list with scroes and sort it, the scores are the relation between the time points for this word,
        # and the time necessary to type it
        wordsScore = {}
        for word, weight in possibleWords.items():
            wordsScore[word] = float(weight) / (len(word) + 1)
        sortedByWeight = sorted(wordsScore.iteritems(), key = operator.itemgetter(1), reverse = True)

        if self.__debug:
            print "Sorted List: %s" % (sortedByWeight)


        # Use a mutable value to return the max fit, an array
        bestFit = [0]
        # Search in all the possible combinations
        self.__searchBestFitByDep(sortedByWeight, possibleWords, inDuration, bestFit, 0, [False])

        return bestFit[0]

    def __init__(self):
        self.__dict = set()
        self.__maxWordSize = 0
        self.__plausibleDict = set()

        for line in open(self.__dictFile).read().split('\n'):
            if self.__maxWordSize < len(line):
                self.__maxWordSize = len(line)
            self.__dict.add(line)

            # This set will store all init strings for the words at the dicitonary in orde to know if a path is
            # possible or not if it is included or not in this set
            for wordLen in xrange(1, len(line) + 1):
                self.__plausibleDict.add(line[:wordLen])

if __name__ == "__main__":
    boozzle = Boozzle()

    for problem in xrange(0, int(raw_input())):
        characters = json.loads(raw_input().replace("'", "\""))
        duration = int(raw_input())
        rows = int(raw_input())
        cols = int(raw_input())

        board = []
        for height in xrange(0, rows):
            # Replace the middle dot char by . in order to avoid problems with special chars
            board.append(map(tuple, raw_input().split()))

        print "%s" % (boozzle.resolve(
            characters,
            [cols, rows],
            duration,
            board))
