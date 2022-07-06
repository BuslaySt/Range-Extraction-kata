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

    def test3(self):    
        result = solution([-70,-68,-66,-63--61,-59,-56,-54,-51--48,-46,-43,-40,-39,-37,-34,-31,-28--28])
        expected = '-70,-68,-66,-63--61,-59,-56,-54,-51--48,-46,-43,-40,-39,-37,-34,-31,-28'
        self.assertEqual(result, expected)
    
    def test4(self):    
        result = solution([-83,-81,-78,-76,-75,-73,-71,-70,-68,-65,-64,-61--58,-56,-53,-50,-47--45,-43,-42,-40,-38,-36,-33,-32,-29,-26])
        expected = '-83,-81,-78,-76,-75,-73,-71,-70,-68,-65,-64,-61--58,-56,-53,-50,-47--45,-43,-42,-40,-38,-36,-33,-32,-29,-26--26'
        self.assertEqual(result, expected)
    
    def test5(self):    
        result = solution([-59,-56,-53,-51,-48,-45,-43,-41,-38--36,-34,-31,-29])
        expected = '-59,-56,-53,-51,-48,-45,-43,-41,-38--36,-34,-31,-29--29'
        self.assertEqual(result, expected)
    
    def test6(self):    
        result = solution([-54--52,-50,-48,-45,-44,-41,-38,-35,-32,-31,-28,-26,-23,-21,-18,-17,-15,-13--10,-7,-5])
        expected = '-54--52,-50,-48,-45,-44,-41,-38,-35,-32,-31,-28,-26,-23,-21,-18,-17,-15,-13--10,-7,-5--5'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


'''

'''