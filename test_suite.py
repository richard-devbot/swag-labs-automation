import unittest

from test_login import Test_Login
from test_product_sort import Test_Product

def suite_general():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_Login))
    suite.addTest(unittest.makeSuite(Test_Product))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_general())