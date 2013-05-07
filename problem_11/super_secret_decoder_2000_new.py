#!/usr/bin/env pypy

import fileinput, binascii, Image

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class SuperSecretDecoder:
    __debug = False
    __color = (0, 0, 0)

    def __createTree(self, inCurrentBranch, inSecret, inRoute):
        print inRoute
        #print "Origin: %s" % (inCurrentBranch)
        #print inSecret
        for charPos in range(4):
            if inCurrentBranch[charPos] == 'p':
                inCurrentBranch[charPos] = inSecret.pop(0)
    
        #print "Final: %s" % (inCurrentBranch)
        #print inSecret
        for charPos in range(4):
            if type(inCurrentBranch[charPos]) == type([]):
                self.__createTree(inCurrentBranch[charPos], inSecret, inRoute + " %d" % (charPos))

    def __getTreeByLevelsDeep(self, inTree, inCurrentLevel, inLevels):
        if self.__debug:
            print "To Print: %s" % (inTree)

        if len(inLevels) <= inCurrentLevel:
            inLevels.append('')

        for char in inTree:
            if type(char) == type([]):
                inLevels[inCurrentLevel] += 'p'
                self.__getTreeByLevelsDeep(char, inCurrentLevel + 1, inLevels)
            else:
                inLevels[inCurrentLevel] += char

    def __getTreeByLevels(self, inTree):
        levels = []
        self.__getTreeByLevelsDeep(inTree, 0, levels)

        result = ''
        print levels
        for level in levels:
            print level
            result += ''.join(level)

        return result

    def __sumTrees(self, oldTree, newTree):
        newBranch = []

        if self.__debug:
            print "-- Check --"
            print oldTree[0]
            print newTree[0]

        # Go throw all the branches on this branch and:
        #   - If one of both are black, the result is black
        #   - If no black found, but one of both contains a branch, add the branch
        #   - If both are white, add the white
        for charPos in xrange(0, 4):
            if self.__debug:
                print "Checking: %s %s" % (oldTree[charPos], newTree[charPos])

            if oldTree[charPos] == 'b' or newTree[charPos] == 'b':
                newBranch.append('b')
            elif type(newTree[charPos]) == type([]) and type(oldTree[charPos]) == type([]):
                newBranch.append(self.__sumTrees(newTree[charPos], oldTree[charPos]))
            elif type(newTree[charPos]) == type([]):
                newBranch.append(newTree[charPos])
            elif type(oldTree[charPos]) == type([]):
                newBranch.append(oldTree[charPos])
            else:
                newBranch.append('w')

        if self.__debug:
            print "Result: %s" % (newBranch)

        return newBranch

    def __addPixel(self, inImage, inWidthHeight, inRoute):
        left = 0
        top = 0
        for routePos in xrange(0, len(inRoute)):
            if inRoute[routePos] == 0 or inRoute[routePos] == 3:
                left += inWidthHeight / (2 ** (routePos + 1))

            if inRoute[routePos] == 2 or inRoute[routePos] == 3:
                top += inWidthHeight / (2 ** (routePos + 1))

        widthHeight = inWidthHeight / (2 ** len(inRoute))

        for leftPos in xrange(left, left + widthHeight):
            for topPos in xrange(top, top + widthHeight):
               inImage[leftPos, topPos] = self.__color

    def __drawByDeep(self, inTree, inWidthHeight, inImage, inDeep, inRoute):
        for charPos in xrange(0, 4):
            if type(inTree[charPos]) == type([]):
                newRoute = inRoute[:]
                newRoute.append(charPos)
                self.__drawByDeep(inTree[charPos], inWidthHeight, inImage, inDeep + 1, newRoute)
            else:
                if inTree[charPos] == 'b':
                    self.__addPixel(inImage, inWidthHeight, inRoute + [charPos])

    def __draw(self, inTree, inProblem):
        #widthHeight = 2 ** (self.__getMaxDeep(inTree, 0, [0]) + 1)
        widthHeight = 5000

        if self.__debug:
            print "WidthHeight: %s" % (widthHeight)

        img = Image.new('RGB', (widthHeight, widthHeight), (255, 255, 255))
        pixels = img.load()

        self.__drawByDeep(inTree, widthHeight, pixels, 0, [])

        img.save("out_%d.png" % (inProblem))

    def resolve(self, inProblem):
        secretTrees = []
        for secret in self.__secrets:
            branch = secret.pop(0)
            self.__createTree(branch, secret, '')
            secretTrees.append(branch)

        #self.__draw(result, inProblem)
        origin = "ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppwwppwppbpppppwppwppppppppppppppppppppwpppppwppppbwppwpppppppbwppwwpbpppwppppppppppppppppbppppppppppwpppppppppppppppppppppppppppppppwppppppppwpppppbppppppppppppppppppbpppppwwppwwppppbpppppwwppwwwppwppppbbppwppwpppwpppppppppppppbppppwpppwwwpwwwwpwpppppwwwwbbwwbbwbbwwbbwwwbbwwbwwbbwwbbwwbbwwwbbwwbwwbbbwwbbwwbbwwbbwwbwbwwbwwwbbwbbbbwwbbwbwwbwbwbbwwbbwwwbwwbbwbbwwwbbbbwwbwbbbwwbbwwwbbwbwwbbbwwwbwbbwbbbwwwbwwwwbbwwbwwbwwbwwwwbwwbbbbwwwwwwbwbwwbwwwwwbwwbbwwbbwbbbwwbwwbbwwbwwbbbwwwwbbwbwbwbbbwbwbbwwbbwwbwbwwwbbbwbbwbbwwwbbwwbbwbbwwbbbwwbbwbbwwwbbwbbwwbbwwwbbwwbwwbbwwwbwwbbwbwwbwbbwwbbbwwwbbwbwwbbbwwwwbbwwwwbbwwwwbwbwwwbbwbwwwbbwwbbwwbbwwbbwwbwwwbwwwbbwbbwbbbwwbwbbbbbbwwwbwwbwbwbbbbwwwwbbwbbwwwwwbwwbwbbwwwbbwwbwwwbbwbbbwwwbwbbbwwbwbbwbbbbbwwbwwbwbbwbwwbwwwwbwwwbwwbwwwwbwwbbbwbwwwbwwwbbbwbbwwwbwwbwwwbbwwwbbwwbbwwbbwwbwwwbbwwbbwwbbwbbwwbbwwbbwwwbwwbbwwwwwbwbwbwwbbbwbwwwbwwbwwwwbbbwwwbwwwwbwwbwwwwbwwwbbwbwwwbbwwwbwwwwbwbbbwbwwwwbwwwwbwbwwbbwbwwbbwwwbwbwwwbbbwwwbwbbwwbbwbwwwbbwwbbbwwbbbwwbbwwbwwbbwbwbbwbwwwwbbwbbwwbwbwbbwwwbwwbbwwwbwwbwbbwbbwbwbbwwwbbbww"
        #self.__draw(result, inProblem)
        result = origin.replace('w', '1').replace('b', '0').replace('p', '')
        return binascii.unhexlify('%x' % int(result, 2))

        #print origin
        #print 'p' + aux
        exit()
        result = self.__getTreeByLevels(secretTrees[0]).replace('w', '1').replace('b', '0').replace('p', '')
        result = ''
        return binascii.unhexlify('%x' % int(result, 2))

        result = secretTrees.pop(0)
        self.__draw(result, int("%s1" % (inProblem)))
        
        for tree in secretTrees:
            self.__draw(tree, int("%s2" % (inProblem)))
            result = self.__sumTrees(result, tree)

        #self.__draw(result, inProblem)
        #result = self.__getTreeByLevels(result).replace('w', '1').replace('b', '0').replace('p', '')
        #result = ''
        #return binascii.unhexlify('%x' % int(result, 2))

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
