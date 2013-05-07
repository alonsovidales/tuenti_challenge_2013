#!/usr/bin/env pypy

import fileinput, os, Image, binascii, math

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-29"

class Problem:
    """
    First of all get all the frames in jpeg files with:
        ffmpeg -i video.avi -vcodec mjpeg video_frames/img-%08d.jpg
    After have all the frames on the directoy video_frames, execute the method "decodeImages"
    This mehod will give the string corresponding to the output of the leds
    Te output is:
        ?eT / HTTP/1.1
        Host: silence.contest.tuenti.net
        Connection: keep-alive
        Cache-Control: max-age=0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31
        Accept-Encoding: gzip,deflate,sdch
        Accept-Language: en-Us,en;q=0.8
        Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3
        Cookie: adminsession=true

    Then calling to the server with the cooke "adminsession" setted to "true", I obtained this result:
        For each input N return the sum of digits of N!
    And this is what the method "resolve" do for each string as input :)

    I'm a hacker MuahhahHAhaAAHa
    """

    __debug = False
    __videosDir = "video_frames"
    __pixelToStudy = [410, 344]
    __colorRedLimit = 50

    def resolve(self, inLine):
        """
        Calculate the factoria, and sum all the digits one by one
        """
        fact = str(math.factorial(int(inLine)))

        return sum(map(int, list(fact)))

    def decodeImages(self):
        """
        I divided the vide on frames using:
            ffmpeg -i video.avi -vcodec mjpeg video_frames/img-%08d.jpg
        Doing this I obtained a jpg frame by frame

        This method read all the images, and gets a pixel corresponding to the lights on each one
        If the light is on, add a one, if not add a zero, after all, convert the binary to 
        a string, and, you have the output :)
        """
        files = os.listdir(self.__videosDir)

        result = ''
        for video in files:
            img = Image.open("%s/%s" % (self.__videosDir, video))
            pix = img.load()

            pixel = pix[self.__pixelToStudy[0], self.__pixelToStudy[1]]
            if pixel[0] > self.__colorRedLimit:
                result += '1'
            else:
                result += '0'

        print binascii.unhexlify('%x' % result)

        if self.__debug:
            print "Position: %s" % (self.__groups) 


if __name__ == "__main__":
    problem = Problem()

    # Uncomment This line after obtain the frames with ffmpeg and it will show the output
    #problem.decodeImages()

    lines = [line.replace('\n', '') for line in fileinput.input()]

    for line in lines:
        print "%s" % (Problem().resolve(line))
