# -*- coding: utf8 -*-

def assert4(given):
    assert given == given


def test4():
    for i in range(20):
        assert4(i)

