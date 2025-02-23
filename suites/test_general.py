import unittest

# from HtmlTestRunner import HTMLTestRunner

from test_objects import test_login, test_product_sort, test_checkout

def suite_general():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(test_login.Test_Login))
    suite.addTest(unittest.makeSuite(test_product_sort.Test_Product))
    suite.addTest(unittest.makeSuite(test_checkout.Test_Checkout))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner = runner.run(suite_general())
    # runner = HTMLTestRunner(
    #     combine_reports=True,
    #     report_title='Swag Labs Test Automation Reports',
    #     open_in_browser=True
    # )
    # runner.run(suite_general())
