#!/usr/bin/env pypy

import fileinput, binascii, Image

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class SuperSecretDecoder:
    __debug = False

    def __buildTree(self, inTree, inRemaingLeafs):
        result = []
        for leaf in inTree:
            if leaf == 'p':
                result.append(self.__buildTree(inRemaingLeafs.pop(0), inRemaingLeafs))
            else:
                result.append(leaf)

        #for leafPos in range(4):
        #    if type(result[leafPos]) == type([]):
        #        result[leafPos] = self.__buildTree(result[leafPos], inRemaingLeafs)

        return result

    def __getBinFromTree(self, inTree):
        result = "%s" % (inTree)
        return ''.join(result.replace('[', '').replace(']', '').replace('b', '0').replace('w', '1')).replace(', ', '').replace('\'', '')[::-1]

    def resolve(self, inProblem):
        print self.__secrets
        binStr = self.__getBinFromTree(self.__buildTree(self.__secrets[0].pop(0), self.__secrets[0]))
        print binStr
        return binascii.unhexlify('%x' % int(binStr, 2))
        exit()

        return 'p' + self.__getTreeByLevels(result)

    def __init__(self, inSecrets):
        self.__secrets = []
        for secret in inSecrets:
            newSecret = []
            for part in xrange(0, (len(secret) - 1) / 4):
                newSecret.append(list(secret[1 + (part * 4): 5 + (part * 4)]))

            self.__secrets.append(newSecret)

        if self.__debug:
            print "Secrets: %s" % (self.__secrets) 

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for problem in xrange(1, int(lines[0]) + 1):
        print "%s" % (SuperSecretDecoder(lines[problem].split()).resolve(problem))
