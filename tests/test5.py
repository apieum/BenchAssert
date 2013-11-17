# -*- coding: utf8 -*-
def assert_equal5(given, expected, msg=None):
    if given == expected: return
    raise AssertionError("%s != %s" % (given, expected))

def assert5(given):
    __debug__ and assert_equal5(given, given)

def test5():
    for i in range(20):
        assert5(i)
