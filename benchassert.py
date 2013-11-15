# -*- coding: utf8 -*-

assert_equal1 = lambda given, expected, msg=None: None

def assert_equal2(given, expected, msg=None):
    pass

class assert_functor(object):
    def __call__(self, given, expected, msg=None):
        pass

assert_equal3 = assert_functor()


def assert1(given):
    assert_equal1(given, given)

def assert2(given):
    assert_equal2(given, given)

def assert3(given):
    assert_equal3(given, given)

def assert4(given):
    assert given == given


def test1():
    for i in range(20):
        assert1(i)

def test2():
    for i in range(20):
        assert2(i)

def test3():
    for i in range(20):
        assert3(i)

def test4():
    for i in range(20):
        assert4(i)

import timeit
import cProfile

print("Test 1 - null lambda:")
cProfile.run('test1()')
print(timeit.timeit("test1()", setup="from __main__ import test1"))
print('')

print("Test 2 - null def:")
cProfile.run('test2()')
print(timeit.timeit("test2()", setup="from __main__ import test2"))
print('')

print("Test 3 - functor object:")
cProfile.run('test3()')
print(timeit.timeit("test3()", setup="from __main__ import test3"))
print('')

print("Test 4 - assert:")
cProfile.run('test4()')
print(timeit.timeit("test4()", setup="from __main__ import test4"))
print('')
