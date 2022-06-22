from kata import *
import unittest


class Test_Range_Extraction(unittest.TestCase):
    def test1(self):    
        result = solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
        expected = '-6,-3-1,3-5,7-11,14,15,17-20'
        self.assertEqual(result, expected)

    def test2(self):    
        result = solution([-3,-2,-1,2,10,15,16,18,19,20])
        expected = '-3--1,2,10,15,16,18-20'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


'''
test.describe("Sample Test Cases")

test.it("Simple Tests")
test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')

'''