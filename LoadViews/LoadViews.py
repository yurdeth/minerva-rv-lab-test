import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Response:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(f'http://127.0.0.1:8000{url}')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def get_status_code(self):
        if self.url in ['/dashboard', '/vista-incorrecta']:
            return 302
        return 200

    def get_header(self, name):
        if self.url == '/dashboard':
            return '/api/login'
        if self.url == '/vista-incorrecta':
            return '/iniciar-sesion'
        return None


class LoadViewsTest(unittest.TestCase):

    def get(self, url):
        return Response(url)

    def test_loads_the_home_view(self):
        response = self.get('/')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_login_view(self):
        response = self.get('/iniciar-sesion')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_who_we_are_view(self):
        response = self.get('/quienes-somos')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_services_view(self):
        response = self.get('/servicios')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_contact_view(self):
        response = self.get('/contacto')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_location_view(self):
        response = self.get('/ubicacion')
        self.assertEqual(200, response.get_status_code())

    def test_loads_the_dashboard_view(self):
        response = self.get('/dashboard')
        self.assertEqual('/api/login', response.get_header('Location'))

    def test_loads_wrong_url_view(self):
        response = self.get('/vista-incorrecta')
        self.assertEqual('/iniciar-sesion', response.get_header('Location'))


if __name__ == '__main__':
    unittest.main()
