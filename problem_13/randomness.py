#!/usr/bin/env pypy

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class Randomness:
    __debug = False

    def resolve(self):
        result = []
        for subSeq in self.__subSequences:
            if self.__debug:
                print "-- SubSeq (%s) --" % (subSeq)

            # Get the number to study from the sequence array
            firstNum = self.__sequence[subSeq[0] - 1]
            secNum = self.__sequence[subSeq[1] - 1]

            # If both numbers are the same, the frecuency will be the mrange to study
            if firstNum == secNum:
                maxFreq = subSeq[1] - subSeq[0] + 1
            else:
                # Get the number frequencies for all the numbers between the given positions without the numbers at the borders
                rangeFrom = self.__rangesMap[firstNum]
                rangeTo = self.__rangesMap[secNum]
                rangeToStudy = self.__ranges[rangeFrom + 1 : rangeTo]

                # Append the borders, use the start and end positions to know the number of times that the number can be repeated
                rangeToStudy.append(self.__startEndNumber[firstNum][1] - (subSeq[0] - 1) + 1)
                rangeToStudy.append((subSeq[1] - 1) - self.__startEndNumber[secNum][0] + 1)

                if self.__debug:
                    print "RangeToStudy: %s" % (rangeToStudy)

                # The max frecuency are the max frecuency between the numbers at the etrems, and the frecuency of the numbers
                # at the extremes
                maxFreq = max(rangeToStudy)

            result.append(str(maxFreq))
            if self.__debug:
                print "FirstNum: %d SecNum: %d" % (firstNum, secNum)

        return '\n'.join(result)

    def __init__(self, inSequence, insubsequences):
        self.__sequence = inSequence

        # This dict will contain the start and end positions of each number in order to be
        # able to study the borders
        self.__startEndNumber = {}
        # This list will contain the number of repetitions by each number on the same
        # order as the numbers appears on the sequence
        self.__ranges = []
        # This dict maps each number to the position of the repetitions on the ranges list
        self.__rangesMap = {}
        prevRange = -1
        for numberPos in range(len(inSequence)):
            if inSequence[numberPos] in self.__startEndNumber:
                self.__startEndNumber[inSequence[numberPos]][1] = numberPos
                prevRange += 1
            else:
                if prevRange != -1:
                    self.__ranges.append(prevRange)
                    self.__rangesMap[inSequence[numberPos - 1]] = len(self.__ranges) - 1
                prevRange = 1
                self.__startEndNumber[inSequence[numberPos]] = [numberPos, numberPos]

        self.__ranges.append(prevRange)
        self.__rangesMap[inSequence[numberPos]] = len(self.__ranges) - 1

        self.__subSequences = insubsequences

        if self.__debug:
            print "Seed: %s" % (self.__seed) 
            print "Sequence: %s" % (self.__sequence) 
            print "Number Repetitions: %s" % (self.__startEndNumber) 
            print "Ranges: %s" % (self.__ranges) 
            print "RangesMap: %s" % (self.__rangesMap) 
            print "Subsequences: %s" % (self.__subSequences) 

if __name__ == "__main__":
    problems = int(raw_input())
    for case in range(problems):
        problemInfo = map(int, raw_input().split())
        numbers = map(int, raw_input().split())

        subsequences = []
        for seq in range(problemInfo[1]):
            subsequences.append(map(int, raw_input().split()))

        print "Test case #%d" % (case + 1)
        print "%s" % (Randomness(
            numbers,
            subsequences
        ).resolve())
