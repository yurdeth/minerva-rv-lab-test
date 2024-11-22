import unittest
from unittest.mock import patch, MagicMock

from selenium.webdriver.common.by import By

from DoLogins.Login import LoginTest


class TestLoginTest(unittest.TestCase):

    @patch('DoLogins.LoginTest.webdriver.Chrome')
    def setUp(self, MockWebDriver):
        self.mock_driver = MockWebDriver.return_value
        self.login_test = LoginTest(
            url='http://127.0.0.1:8000/iniciar-sesion',
            api_url='http://127.0.0.1:8000/signin',
            email='admin@admin.com',
            password='$z*!P#6KXdmU4SNfC',
            token='YOUR_ACCESS_TOKEN'
        )

    def test_open_page(self):
        self.login_test.open_page()
        self.mock_driver.get.assert_called_once_with('http://127.0.0.1:8000/iniciar-sesion')

    def test_perform_login(self):
        self.mock_driver.find_element.return_value = MagicMock()
        self.login_test.perform_admin_login_valid_credentials()
        self.mock_driver.find_element.assert_any_call(By.ID, 'email')
        self.mock_driver.find_element.assert_any_call(By.ID, 'password')
        self.mock_driver.find_element.assert_any_call(By.ID, 'submitButton')

    @patch('DoLogins.LoginTest.requests.get')
    def test_get_api_response(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"token": "test_token", "redirect_to": "/home"}'
        mock_response.json.return_value = {"token": "test_token", "redirect_to": "/home"}
        mock_get.return_value = mock_response

        self.login_test.get_api_response()
        mock_get.assert_called_once_with(
            'http://127.0.0.1:8000/signin',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
            }
        )

    def close_browser(self):
        driver = self.mock_driver
        driver.quit()

    def tearDown(self):
        self.login_test.close_browser()
        self.mock_driver.quit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
