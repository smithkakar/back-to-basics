#!/usr/local/bin/env python3
from nose.tools import assert_equal


class TestReverse(object):

    def test_rev(self, solution):
        assert_equal(solution('hello'), 'olleh')
        assert_equal(solution('hello world'), 'dlrow olleh')
        assert_equal(solution('123456789'), '987654321')
        print('PASSED ALL TEST CASES!')


def reverse(s):
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


test = TestReverse()
test.test_rev(reverse)
