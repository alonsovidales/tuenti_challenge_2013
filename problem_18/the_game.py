#!/usr/bin/env pypy

import fileinput, sys

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class TheGame:
    """
    This solution try to find loops inside the graph checking from each of the nodes
    and when we have a loop, we only should to check if this loop generated anergy or not.
    """
    __debug = False

    def __searchByDeep(self, inInitialLocation, inPathsToSearch, inVisitedLocations, inCurrentEnergy, inFoundInfinite):
        if self.__debug:
            print "Origin: %s Visited: %s" % (inInitialLocation, inVisitedLocations)

        # Check if any other path checked previously was infinite, in this case, don't continue checking
        if not inFoundInfinite[0]:
            # Go by all the patch inside the current node checking them
            for target, energy in inPathsToSearch.items():
                if target not in inVisitedLocations:
                    # If the next node to visit is the origin, don't cotinue, we have a loop, simply check
                    # if the energy now is bigger than the original energy
                    if inInitialLocation == target:
                        if (inCurrentEnergy * energy) > 1:
                            inFoundInfinite[0] = True
                        if self.__debug:
                            print "Origin: %s" % (inCurrentEnergy * energy)
                    else:
                        # Add the next node to the visited nodes in order to avoid repeated paths, and
                        # continue with it
                        inVisitedLocations.add(target)
                        if target in self.__pathVariations:
                            self.__searchByDeep(inInitialLocation, self.__pathVariations[target], inVisitedLocations, inCurrentEnergy * energy, inFoundInfinite)

    def resolve(self):
        found = [False]
        for location, paths in self.__pathVariations.items():
            self.__searchByDeep(location, paths, set(), 1, found)

        return found[0]

    def __init__(self, inLocations, inMovements, inVariations):
        self.__locations = inLocations
        self.__movements = inMovements
        self.__pathVariations = {}
        # The graph with the amounth of energy, the main key is the origin, the internal keys are the
        # destinations, and the value, the tmies one, is easy to work with this inestead of percentages
        for variation in inVariations:
            if variation[0] in self.__pathVariations:
                self.__pathVariations[variation[0]][variation[1]] = 1 + float(variation[2]) / 100
            else:
                self.__pathVariations[variation[0]] = {variation[1]: 1 + float(variation[2]) / 100}

        if self.__debug:
            print "Locations: %s" % (self.__locations) 
            print "Movements: %s" % (self.__movements) 
            print "Variations: %s" % (self.__pathVariations) 

if __name__ == "__main__":
    # We need more recursion XD
    sys.setrecursionlimit(100000000)

    problems = int(raw_input())

    for problem in range(problems):
        locations = int(raw_input())
        movements = int(raw_input())
        variations = []
        for variation in range(movements):
            variations.append(map(int, raw_input().split()))

        print "%s" % (TheGame(locations, movements, variations).resolve())
