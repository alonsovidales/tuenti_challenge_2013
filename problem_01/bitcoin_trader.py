#!/usr/bin/env pypy

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class BitcoinTrader:
    __debug = False

    def getBestChangeRation(self, inEuros, inBitCoins, inRates, inLastActionWasBuy = False):
        if inEuros >= self.__maxEuros:
            # Use a class property in order to keep the max value along all the calls
            self.__maxEuros = inEuros

        if len(inRates) == 0:
            return

        # Sell all if the last action was buy, or buy all the possible
        # bitcoins if the last action was sell
        if inLastActionWasBuy:
            # Check selling all the bitcoins at the maximun rate
            rates = inRates[:]
            currentRate = rates.pop(0)
            while len(rates) > 0 and currentRate <= rates[0]:
                currentRate = rates.pop(0)

            if self.__debug:
                print "MAX: E: %s B: %s R: %s" % (inEuros, inBitCoins, currentRate)
                print "AFt: E: %s B: %s R: %s" % (inEuros + (inBitCoins * currentRate), 0, currentRate)

            self.getBestChangeRation(
                inEuros + (inBitCoins * currentRate),
                0,
                rates,
                False)
        else:
            # Check buying all the possible bitcoins with the euros that we have
            rates = inRates[:]
            currentRate = rates.pop(0)
            while len(rates) > 0 and currentRate >= rates[0]:
                currentRate = rates.pop(0)

            if self.__debug:
                print "MIN: E: %s B: %s R: %s" % (inEuros, inBitCoins, currentRate)
                print "AFT: E: %s B: %s R: %s" % (inEuros % currentRate, inBitCoins + (inEuros / currentRate), currentRate)

            self.getBestChangeRation(
                inEuros % currentRate,
                inBitCoins + (inEuros / currentRate),
                rates,
                True)

    def resolve(self):
        self.getBestChangeRation(self.__euros, 0, self.__rates)

        return self.__maxEuros

    def __init__(self, inBitCoins, inRates):
        self.__euros = inBitCoins
        self.__rates = inRates
        self.__maxEuros = 0

        if self.__debug:
            print "-- BitcoinTrader --"
            print "Euros: %s" % (self.__euros) 
            print "Rates: %s" % (self.__rates) 

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    # Go one by one solving all the problems
    for problem in xrange(0, int(lines[0])):
        print "%s" % (BitcoinTrader(
            int(lines[(problem * 2) + 1]),
            map(int, lines[(problem * 2) + 2].split()),
        ).resolve())
