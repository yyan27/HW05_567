# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Yulong Yan
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_right_triangle_a(self):
        """
        check if it can be a right triangle
        """
        self.assertEqual(classifyTriangle(3,4,5),'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """
        check if it can be a right triangle
        """
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test_equilateral_triangle(self):
        """
        check if it can be a equilateral triangle
        """
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_isoceles_triangle(self):
        """
        check if it can be a isoceles triangle
        """
        self.assertEqual(classifyTriangle(6,6,4),'Isoceles','6,6,4 should be Isoceles')

    def test_scalene_triangle(self):
        """
        check if it can be a scalene triangle
        """
        self.assertEqual(classifyTriangle(2,8,9),'Scalene','2,8,9 should be Scalene')

    def test_notTriangle_a(self):
        """
        check if it can be a invalid triangle
        """
        self.assertEqual(classifyTriangle(6,6,14),'NotATriangle','6,6,14 should be NotATriangle')

    def test_notTriangle_b(self):
        """
        check if it can be a invalid triangle
        """
        self.assertEqual(classifyTriangle(2,4,2),'NotATriangle','2,4,2 should be NotATriangle')

    def test_invalid_a(self):
        """
        check if it can be a invalid triangle
        """
        self.assertEqual(classifyTriangle(2.1,3.1,4.1),'InvalidInput','2.1,3.1,4.1 is InvalidInput')

    def test_invlaid_b(self):
        """
        check if it can be a invalid triangle
        """
        self.assertEqual(classifyTriangle(-3,-4,-5),
                        'InvalidInput',
                        '-3,-4,-5 should be InvalidInput')

    def test_invlaid_c(self):
        """
        check if it can be a invalid triangle
        """
        self.assertEqual(classifyTriangle(300,500,600),
                        'InvalidInput',
                        '300,500,600 should be InvalidInput')

    def test_invalid_d(self):
        """
        check if it can be a invalid triangle
        """
        self.assertEqual(classifyTriangle(0,2,3),'InvalidInput','0,2,3 should be InvalidInput')

    def test_invalid_e(self):
        """
        check if it can be a invalid triangle
        """
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 should be InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
