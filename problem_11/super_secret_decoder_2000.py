#!/usr/bin/env pypy

import fileinput, Image, binascii

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class SuperSecretDecoder:
    __debug = False
    __color = (0, 0, 0)

    def __createTree(self, inCurrentBranch, inSecret):
        result = []

        for char in inCurrentBranch:
            if char == 'p':
                result.append(self.__createTree(inSecret.pop(0), inSecret))
            else:
                result.append(char)

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

    def __printTree(self, inTree):
        if self.__debug:
            print "To Print: %s" % (inTree)

        result = ''
        toAdd = []
        for char in inTree:
            if type(char) == type([]):
                toAdd.append(char)
                result += 'p'
            else:
                result += char

        for tree in toAdd:
            result += self.__printTree(tree)

        return result

    def __getMaxDeep(self, inTree, inDeep, inMaxDeep):
        if inDeep >= inMaxDeep[0]:
            print inTree
            inMaxDeep[0] = inDeep

        for charPos in xrange(0, 4):
            if type(inTree[charPos]) == type([]):
                self.__getMaxDeep(inTree[charPos], inDeep + 1, inMaxDeep)

        return inMaxDeep[0]

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
                    inImage.append('1')
                else:
                    inImage.append('0')
                #if inTree[charPos] == 'b':
                #    print ' '.join(map(str, inRoute + [charPos]))
                #if inTree[charPos] == 'b':
                #    self.__addPixel(inImage, inWidthHeight, inRoute + [charPos])

    def __draw(self, inTree, inProblem):
        #widthHeight = 2 ** (self.__getMaxDeep(inTree, 0, [0]) + 1)
        widthHeight = 5000

        if self.__debug:
            print "WidthHeight: %s" % (widthHeight)

        #img = Image.new('RGB', (widthHeight, widthHeight), (255, 255, 255))
        #pixels = img.load()

        pixels = []
        self.__drawByDeep(inTree, widthHeight, pixels, 0, [])

        binText = '' + ''.join(pixels)
        print ''.join(chr(int(binText[i:i+8], 2)) for i in xrange(0, len(binText), 8))

        #img.save("out_%d.png" % (inProblem))

    def resolve(self, inProblem):
        secretTrees = []
        for secret in self.__secrets:
            secretTrees.append(self.__createTree(secret[0], secret[1:]))

        result = secretTrees.pop(0)
        for tree in secretTrees:
            result = self.__sumTrees(result, tree)

        if self.__debug:
            self.__draw(result, inProblem)
        self.__draw(result, inProblem)

        return 'p' + self.__printTree(result)

    def __init__(self, inSecrets):
        self.__secrets = []
        for secret in inSecrets:
            newSecret = []
            for part in xrange(0, (len(secret) - 1) / 4):
                newSecret.append(secret[1 + (part * 4): 5 + (part * 4)])

            self.__secrets.append(newSecret)

        if self.__debug:
            print "Secrets: %s" % (self.__secrets) 

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for problem in xrange(1, int(lines[0]) + 1):
        print "%s" % (SuperSecretDecoder(lines[problem].split()).resolve(problem))
