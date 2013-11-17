# -*- coding: utf8 -*-

class assert_functor(object):
    def __call__(self, given, expected, msg=None):
        pass

assert_equal3 = assert_functor()


def assert3(given):
    assert_equal3(given, given)

def test3():
    for i in range(20):
        assert3(i)

