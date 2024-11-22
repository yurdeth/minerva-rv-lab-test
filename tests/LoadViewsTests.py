import unittest
from unittest.mock import patch

from LoadViews.LoadViews import Response


class TestLoadViewsTest(unittest.TestCase):

    @patch('LoadViews.LoadViewsTest.webdriver.Chrome')
    def setUp(self, MockWebDriver):
        self.mock_driver = MockWebDriver.return_value

    def test_loads_the_home_view(self):
        response = Response('/')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_login_view(self):
        response = Response('/iniciar-sesion')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_who_we_are_view(self):
        response = Response('/quienes-somos')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_services_view(self):
        response = Response('/servicios')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_contact_view(self):
        response = Response('/contacto')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_location_view(self):
        response = Response('/ubicacion')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_dashboard_view(self):
        response = Response('/dashboard')
        self.assertEqual('/api/login', response.get_header('Location'))

    def test_loads_wrong_url_view(self):
        response = Response('/vista-incorrecta')
        self.assertEqual('/iniciar-sesion', response.get_header('Location'))

    def tearDown(self):
        self.mock_driver.quit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
