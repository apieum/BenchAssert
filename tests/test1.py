# -*- coding: utf8 -*-

assert_equal1 = lambda given, expected, msg=None: None

def assert1(given):
    assert_equal1(given, given)


def test1():
    for i in range(20):
        assert1(i)

