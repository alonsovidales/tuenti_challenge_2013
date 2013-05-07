#!/usr/bin/env pypy

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class Defense:
    __debug = False

    def __printCanyon(self, inCanyon):
        print "--- Canyon %d ---" % (len(inCanyon))
        for row in inCanyon:
            print row

    def __killThemAll(self, soldiers):
        """
        Return the number of seconds that you can resist with the given soldiers in the
        current scene or -1 if you can resist all the time
        """

        # If we have more soldiers than smelly Zorglings, we will win this battle!!!!
        if soldiers >= self.__widthHeight[0]:
            return -1

        # No, we can't win, no hope left, calculate the advancage speed of the Zorglings
        speed = self.__widthHeight[0] - soldiers
        # Calculate the max number of Zorglings that can fit intil the end of all...
        maxZorglings = self.__widthHeight[0] * (self.__widthHeight[1] - 1)

        # The time that we can resist if the number of Zorglings that fit in the canyon
        # divided by the speed that the number of Zorglings is increased
        return (maxZorglings / speed) + 1

    def resolve(self):
        #print self.__killThemAll(70)
        #exit()

        maxResistanceTime = 0
        for soldiers in xrange(0, (self.__gold / self.__soldierPrice) + 1):
            crematoriums = (self.__gold - (soldiers * self.__soldierPrice)) / self.__crematoriumPrice

            # Get how many time we can resist with the current soldiers
            timeByRound = self.__killThemAll(soldiers)

            if timeByRound == -1:
                return -1

            # We can resist the max time possible with the soldiers and launch the crematoriums to clean
            # the canyon and start again, then we can resist the time that we can resist with only the
            # soldiers by the number of crematoriums
            time = (timeByRound * (crematoriums + 1))
            if self.__debug:
                print "Soldiers: %d - Crematoriums %d - Time: %d" % (soldiers, crematoriums, time)
            if time > maxResistanceTime:
                maxResistanceTime = time

        return maxResistanceTime

    def __init__(self, inWidthHeight, inSoldierPrice, inCrematorium, inGold):
        self.__widthHeight = inWidthHeight
        self.__soldierPrice = inSoldierPrice
        self.__crematoriumPrice = inCrematorium
        self.__gold = inGold

        if self.__debug:
            print "Gold: %d" % (self.__gold)
            print "Prices: S: %d C: %d" % (self.__soldierPrice, self.__crematoriumPrice)
            print "Width: %d Height: %d" % (self.__widthHeight[0], self.__widthHeight[1])

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for problem in xrange(1, int(lines[0]) + 1):
        info = map(int, lines[problem].split())
        print "%s" % (Defense(
            [info[0], info[1]],
            info[2],
            info[3],
            info[4]).resolve())
