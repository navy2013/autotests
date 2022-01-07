#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/6 22:22
import unittest
class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print('testcase01')
        self.assertEqual(2,2,"判断相等")
        self.assertIn('h','this')

    def test_case02(self):
        print('testcase02')
        self.assertEqual(2, 2, "判断相等")
        self.assertIn('h', 'this')

    @unittest.skipIf(1+1==2,"跳过这条")
    def test_case03(self):
        print('testcase03')
        self.assertEqual(2,2,"判断相等")
        self.assertIn('h','this')


class demo1(unittest.TestCase):
    def test_demo1_case01(self):
        print("test_demo1 case01")

    def test_demo1_case02(self):
        print("test_demo1 case02")


class deomo2(unittest.TestCase):
    def test_demo2_case01(self):
        print("test_demo1 case01")

    def test_demo2_case01(self):
        print("test_demo1 case02")
if __name__ == '__main__':
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # suite.addTest(deomo1("test_demo1_case01"))
    #
    # unittest.TextTestRunner().run(suite)

    # suite = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    #
    # suiteall = unittest.TestSuite([suite,suite1])
    # unittest.TextTestRunner().run(suiteall)

    unittest.defaultTestLoader.discover("./",'test*.py')