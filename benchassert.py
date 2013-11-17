# -*- coding: utf8 -*-
import timeit
import cProfile
from tests import test1, test2, test3, test4, test5

def runTest(num, title):
    print("Test %s - %s:" % (num, title))
    func = 'test%s()' % num
    cProfile.run(func)
    time = timeit.timeit(func, setup="from __main__ import test%s" % num)
    print("Test %s lasts: %s" %(num, time))
    print('')


runTest(1, "null lambda")
runTest(2, "null def")
runTest(3, "functor")
runTest(4, "assert")
runTest(5, "def with __debug__")


