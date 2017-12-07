# my_first_python
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print('start!')
    def tearDown(self):
        time.sleep(2)
        print("end!")
    def test_1(self):
        print("执行测试用例1")
    def test_3(self):
        print("执行测试用例3")
    def test_2(self):
        print("执行测试用例2")
    def addtest(self):
        print("add方法")
    def test_equal(self):
        '''断言：assert,实际结果与期望结果对比'''
        self.assertEqual(4*5,21)
        print("2")
if __name__=="__main__":
    unittest.main()

'''
执行顺序，根据测试用例名称先后来执行：
start-执行测试用例1 end
start-执行测试用例2 end
start-执行测试用例3 end
输出：
start!
执行测试用例1
end!
start!
执行测试用例2
end!
start!
执行测试用例3
end!
'''
