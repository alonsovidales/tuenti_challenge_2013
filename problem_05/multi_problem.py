#!/usr/bin/env pypy

import fileinput, itertools, multiprocessing, time, os, copy

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class Problem:
    __debug = False

    def __checkByDeep(self, inPos, inSeconds, inScore = 0, inVisitedPos = {}):
        # Check if this pos is yet visited
        if inPos[0] in inVisitedPos and inPos[1] in inVisitedPos[inPos[0]]:
            if self.__debug:
                print "Yet visited: %s" % (inPos)
            return

        visitedPos = copy.deepcopy(inVisitedPos)
        if inPos[0] in visitedPos:
            visitedPos[inPos[0]].add(inPos[1])
        else:
            visitedPos[inPos[0]] = set([inPos[1]])

        if self.__maxScore < inScore:
            if self.__debug:
                print "Pos: %s Seconds: %s Score: %s VisitedPos: %s" % (inPos, inSeconds, inScore, visitedPos)
            self.__maxScore = inScore

        if inSeconds == 0:
            if self.__debug:
                print "No seconds left :'(  %s" % (visitedPos)
            return

        # Move right if possible
        if (inPos[0] + 1) < self.__initGrid[0]:
            newPos = inPos[:]
            newPos[0] += 1

            if self.__debug:
                print "Right from: %s" % (inPos)
            self.__checkByDeep(newPos, inSeconds - 1, inScore + self.__initGems[newPos[0]][newPos[1]], visitedPos)

        # Move left if possible
        if (inPos[0] - 1) >= 0:
            newPos = inPos[:]
            newPos[0] -= 1

            if self.__debug:
                print "Left from: %s" % (inPos)
            self.__checkByDeep(newPos, inSeconds - 1, inScore + self.__initGems[newPos[0]][newPos[1]], visitedPos)

        # Move Bottom if possible
        if (inPos[1] + 1) < self.__initGrid[1]:
            newPos = inPos[:]
            newPos[1] += 1

            if self.__debug:
                print "Bottom from: %s" % (inPos)
            self.__checkByDeep(newPos, inSeconds - 1, inScore + self.__initGems[newPos[0]][newPos[1]], visitedPos)

        # Move top if possible
        if (inPos[1] - 1) >= 0:
            newPos = inPos[:]
            newPos[1] -= 1

            if self.__debug:
                print "Top from: %s" % (inPos)
            self.__checkByDeep(newPos, inSeconds - 1, inScore + self.__initGems[newPos[0]][newPos[1]], visitedPos)

        

    def resolve(self):
        self.__checkByDeep(self.__initPos, self.__initSec)

        return self.__maxScore

    def __init__(self, mainProcessPid, inLinePos, inGrid, inInitPos, inSec, inGems):
        self.__maxScore = 0
        self.__initPos = inInitPos
        self.__initSec = inSec
        self.__initGrid = inGrid

        self.__initGems = []
        for row in xrange(0, inGrid[1]):
            self.__initGems.append([0] * inGrid[0])

        for gem in inGems:
            self.__initGems[gem[0]][gem[1]] = gem[2]

        if self.__debug:
            print "-- New problem --"
            print "Grid: %s" % (inGrid)
            print "InitPos: %s" % (inInitPos)
            print "Seconds: %s" % (inSec)
            print "Gems: %s" % (self.__initGems)

        # Use a temporal file to store the output in order print it after finish the execution
        # in the correct order
        f = open("/tmp/out_%s_%s" % (mainProcessPid, inLinePos), 'w')
        f.write("%s\n" % (self.resolve()))
        f.close()

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]
    cpus = multiprocessing.cpu_count()

    for problem in xrange(0, int(lines[0])):
        gridInfo = map(int, lines[(problem * 5) + 1].split(','))
        initialPos = map(int, lines[(problem * 5) + 2].split(','))
        seconds = int(lines[(problem * 5) + 3])
        gems = int(lines[(problem * 5) + 4])
        gemsList = [map(int, gemInfo.split(',')) for gemInfo in lines[(problem * 5) + 5].split('#')]

        p = multiprocessing.Process(target = Problem, args = (os.getpid(), problem, gridInfo, initialPos, seconds, gemsList))
        p.start()

        while len(multiprocessing.active_children()) >= cpus:
            time.sleep(0.1)

    # Wait until all the process has finished
    while len(multiprocessing.active_children()) > 0:
        time.sleep(0.1)

    os.system("cat /tmp/out_%s_*" % (os.getpid()))
