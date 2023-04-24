import unittest

from HtmlTestRunner import HTMLTestRunner

from test_login import Test_Login
from test_product_sort import Test_Product
from test_checkout import Test_Checkout

def suite_general():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(Test_Login))
    suite.addTest(unittest.makeSuite(Test_Product))
    suite.addTest(unittest.makeSuite(Test_Checkout))

    return suite

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(
        combine_reports=True,
        report_title='Swag Labs Test Automation Reports',
        open_in_browser=True
    )
    runner.run(suite_general())