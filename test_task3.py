#!/usr/bin/env python

import unittest
import task3


class CircleTest(unittest.TestCase):
    def test_circle(self):
        p1 = task3.circle("UDLR")
        p2 = task3.circle("UR")
        self.assertTrue(p1)
        self.assertFalse(p2)


if __name__ == '__main__':
    unittest.main()
