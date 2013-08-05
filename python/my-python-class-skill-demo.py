#!/usr/bin/python

# play around with this code to learn:
#   1.classc will have self.b
#   2.classd.run()
#   3.classdiff.run()

class classa:
    def __init__(self):
        self.a = "aaa"
        self.b = "bbb"
    def go(self):
        print self.a
    def gob(self):
        print self.b
    def gogo(self):
        self.run()

class classb(classa):
    def __init__(self):
        classa.__init__(self)
        self.a = "aaaaaa"
        self.c = "cccccc"


class classc(classa):
    def run(self):
        print self.a


class classd(classa):
    def run(self):
        print "try self.b %s " % self.b
        return classa.gob(self)

class classdiff:
    def __init__(self):
        self.a = "classdiffa"
    def run():
        print self.b
