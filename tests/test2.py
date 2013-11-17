# -*- coding: utf8 -*-

def assert_equal2(given, expected, msg=None):
    pass

def assert2(given):
    assert_equal2(given, given)

def test2():
    for i in range(20):
        assert2(i)
