#-------------------------------------------------------------------------------
# Name:        6.9.7
# Purpose:     seconds counter
#
# Author:      bjmeloche
#
# Created:     02/10/2025
# Copyright:   (c) bjmeloche 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if True:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def to_secs(h,m,s):
    h *=3600
    m *= 60

    to_secs = s+m+h
    print(to_secs)

def test_suite():
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)

test_suite()
to_secs(2, 30, 10)
to_secs(2, 0, 0)
to_secs(0, 2, 0)
to_secs(0, 0, 42)
to_secs(0, -10, 10)
