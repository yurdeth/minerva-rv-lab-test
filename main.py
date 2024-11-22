# main.py
import unittest

from DoLogins.Login import LoginTest
from LoadViews.LoadViews import LoadViewsTest


def callLoadTest():
    suite = unittest.TestLoader().loadTestsFromTestCase(LoadViewsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


def callLoginTest():
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


def main():
    callLoadTest()
    callLoginTest()


if __name__ == "__main__":
    main()
