#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

import fileinput, copy

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class Cave:
    __debug = False

    def __checkByDeep(self, inCurrentPos, inTime, inVisitedPoints, inLastAction, inPath):
        if self.__debug:
            print inPath

        if inCurrentPos[0] == 6 and inCurrentPos[0] == 2:
            print "LAST LINE"
        # Check the current column, each column can be checked only two times, we will add to the set
        # the colun plus t or b in order to indicate tie way

        # Move to the Top of the column
        # In order to avoid stupid movements, on't move to the top if we previously moved to the bottom
        if inLastAction != 'b':
            newPos = inCurrentPos[:]
            while self.__map[newPos[0]][newPos[1]] != '#' and self.__map[newPos[0]][newPos[1]] != 'O':
                newPos[0] -= 1
            newPos[0] += 1

            if inCurrentPos[0] - newPos[0] != 0 or self.__map[newPos[0] - 1][newPos[1]] == 'O':
                empleasedTime = inTime + self.__delay + ((inCurrentPos[0] - newPos[0]) / self.__speed)
  
                # Ok, we found a solution, check we wate more time on this path than in a previus used path
                # where we found a solution
                if self.__minTime > empleasedTime:
                    if self.__map[newPos[0] - 1][newPos[1]] == 'O':
                        self.__minTime = empleasedTime
                        if self.__debug:
                            print "FOUND: %s - %s" % (self.__minTime, inPath + " TOP")

                    # Chec if the target point was previously visited in order to avoid useless movements
                    pointStr = ':'.join(map(str, newPos))
                    if pointStr not in inVisitedPoints:
                        visitedPoints = copy.copy(inVisitedPoints)
                        visitedPoints.add(':'.join(map(str, newPos)))
                        self.__checkByDeep(newPos, empleasedTime, visitedPoints, 't', inPath + " TOP")

        # Move to the bottom of the column
        # In order to avoid stupid movements, don't move to bottom  if we previously moved to the top
        if inLastAction != 't':
            newPos = inCurrentPos[:]
            while self.__map[newPos[0]][newPos[1]] != '#' and self.__map[newPos[0]][newPos[1]] != 'O':
                newPos[0] += 1
            newPos[0] -= 1

            if newPos[0] - inCurrentPos[0] != 0 or self.__map[newPos[0] + 1][newPos[1]] == 'O':
                empleasedTime = inTime + self.__delay + ((newPos[0] - inCurrentPos[0]) / self.__speed)

                # Ok, we found a solution, check we wate more time on this path than in a previus used path
                # where we found a solution
                if self.__minTime > empleasedTime:
                    if self.__map[newPos[0] + 1][newPos[1]] == 'O':
                        self.__minTime = empleasedTime
                        if self.__debug:
                            print "FOUND: %s - %s" % (self.__minTime, inPath + " BOTTOM")

                    # Chec if the target point was previously visited in order to avoid useless movements
                    pointStr = ':'.join(map(str, newPos))
                    if pointStr not in inVisitedPoints:
                        visitedPoints = copy.copy(inVisitedPoints)
                        visitedPoints.add(':'.join(map(str, newPos)))
                        self.__checkByDeep(newPos, empleasedTime, visitedPoints, 'b', inPath + " BOTTOM")

        # Move to the right of the row
        # In order to avoid stupid movements, don't move to the left if we previously moved to the right
        if inLastAction != 'l':
            newPos = inCurrentPos[:]
            while self.__map[newPos[0]][newPos[1]] != '#' and self.__map[newPos[0]][newPos[1]] != 'O':
                newPos[1] += 1

            newPos[1] -= 1

            if newPos[1] - inCurrentPos[1] != 0 or self.__map[newPos[0]][newPos[1] + 1] == 'O':
                empleasedTime = inTime + self.__delay + ((newPos[1] - inCurrentPos[1]) / self.__speed)

                # Ok, we found a solution, check we wate more time on this path than in a previus used path
                # where we found a solution
                if self.__minTime > empleasedTime:
                    if self.__map[newPos[0]][newPos[1] + 1] == 'O':
                        self.__minTime = empleasedTime
                        if self.__debug:
                            print "FOUND: %s - %s" % (self.__minTime, inPath + " RIGHT")

                    # Chec if the target point was previously visited in order to avoid useless movements
                    pointStr = ':'.join(map(str, newPos))
                    if pointStr not in inVisitedPoints:
                        visitedPoints = copy.copy(inVisitedPoints)
                        visitedPoints.add(':'.join(map(str, newPos)))
                        self.__checkByDeep(newPos, empleasedTime, visitedPoints, 'r', inPath + " RIGHT")

        # Move to the left of the row
        # In order to avoid stupid movements, don't move to the right if we previously moved to the left
        if inLastAction != 'r':
            newPos = inCurrentPos[:]
            while self.__map[newPos[0]][newPos[1]] != '#' and self.__map[newPos[0]][newPos[1]] != 'O':
                newPos[1] -= 1

            newPos[1] += 1

            if newPos[1] - inCurrentPos[1] != 0 or self.__map[newPos[0]][newPos[1] - 1] == 'O':
                empleasedTime = inTime + self.__delay + ((inCurrentPos[1] - newPos[1]) / self.__speed)

                # Ok, we found a solution, check we wate more time on this path than in a previus used path
                # where we found a solution
                if self.__minTime > empleasedTime:
                    if self.__map[newPos[0]][newPos[1] - 1] == 'O':
                        self.__minTime = empleasedTime
                        if self.__debug:
                            print "FOUND: %s - %s" % (self.__minTime, inPath + " LEFT")

                    # Chec if the target point was previously visited in order to avoid useless movements
                    pointStr = ':'.join(map(str, newPos))
                    if pointStr not in inVisitedPoints:
                        visitedPoints = copy.copy(inVisitedPoints)
                        visitedPoints.add(':'.join(map(str, newPos)))
                        self.__checkByDeep(newPos, empleasedTime, visitedPoints, 'l', inPath + " LEFT")

    def resolve(self):
        self.__checkByDeep(self.__currentPos, 0, set(), '', '')

        return int(round(self.__minTime + 0.5))

    def __init__(self, inWidthHeight, inSpeed, inDelay, inMap):
        self.__map = inMap
        self.__speed = float(inSpeed)
        self.__delay = inDelay
        self.__minTime = 2 ** 32

        for rowPos in xrange(0, len(self.__map)):
            for col in xrange(0, len(self.__map[rowPos])):
                if self.__map[rowPos][col] == 'X':
                    self.__currentPos = [rowPos, col]

                    break

        if self.__debug:
            print "-- -- --"
            print "WH: %s" % (self.__map) 
            print "Speed: %s" % (self.__speed) 
            print "Delay: %s" % (self.__delay) 
            print "CurrentPos: %s" % (self.__currentPos) 

if __name__ == "__main__":
    for problem in xrange(0, int(raw_input())):
        info = map(int, raw_input().split())

        caveMap = []
        for height in xrange(0, info[1]):
            # Replace the middle dot char by . in order to avoid problems with special chars
            caveMap.append(list(raw_input().replace('·', '.')))

        print "%s" % (Cave(
            [info[0], info[1]],
            info[2],
            info[3],
            caveMap).resolve())
