import time
import unittest

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = 'http://127.0.0.1:8000/iniciar-sesion'
        self.api_url = 'http://127.0.0.1:8000/signin'
        self.credentials = [
            {'email': 'admin@admin.com', 'password': '$z*!P#6KXdmU4SNfC'},
            {'email': 'US21003@ues.edu.sv', 'password': 'hugo.ulloa.$R*V@2024'}
        ]
        self.driver.get(self.url)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_admin_login_valid_credentials(self):
        email_field = self.driver.find_element(By.ID, 'email')
        password_field = self.driver.find_element(By.ID, 'password')
        button = self.driver.find_element(By.ID, 'submitButton')

        email_field.send_keys('admin@admin.com')
        password_field.send_keys('$z*!P#6KXdmU4SNfC')
        button.click()
        time.sleep(3)
        self.driver.get('http://127.0.0.1:8000/logout')

    def test_user_login_valid_credentials(self):
        email_field = self.driver.find_element(By.ID, 'email')
        password_field = self.driver.find_element(By.ID, 'password')
        button = self.driver.find_element(By.ID, 'submitButton')

        email_field.send_keys('US21003@ues.edu.sv')
        password_field.send_keys('hugo.ulloa.$R*V@2024')
        button.click()
        time.sleep(3)
        self.driver.get('http://127.0.0.1:8000/logout')

    def test_login_wrong_mail(self):
        for creds in self.credentials:
            email_field = self.driver.find_element(By.ID, 'email')
            password_field = self.driver.find_element(By.ID, 'password')
            button = self.driver.find_element(By.ID, 'submitButton')

            email_field.send_keys('root@ues.edu.sv')
            password_field.send_keys(creds['password'])
            button.click()
            time.sleep(3)

            response = requests.get(self.api_url)
            self.assertEqual(200, response.status_code, f"Expected status code 200, but got {response.status_code}")
            self.driver.refresh()

    def test_login_wrong_password(self):
        for creds in self.credentials:
            email_field = self.driver.find_element(By.ID, 'email')
            password_field = self.driver.find_element(By.ID, 'password')
            button = self.driver.find_element(By.ID, 'submitButton')

            email_field.send_keys(creds['email'])
            password_field.send_keys('1234567890')
            button.click()
            time.sleep(3)

            response = requests.get(self.api_url)
            self.assertEqual(200, response.status_code, f"Expected status code 200, but got {response.status_code}")
            self.driver.refresh()

    def test_login_wrong_credentials(self):
        for creds in self.credentials:
            email_field = self.driver.find_element(By.ID, 'email')
            password_field = self.driver.find_element(By.ID, 'password')
            button = self.driver.find_element(By.ID, 'submitButton')

            email_field.send_keys('root@ues.edu.sv')
            password_field.send_keys('1234567890')
            button.click()
            time.sleep(3)

            response = requests.get(self.api_url)
            self.assertEqual(200, response.status_code, f"Expected status code 200, but got {response.status_code}")
            self.driver.refresh()

    def test_login_empty_credentials(self):
        for creds in self.credentials:
            email_field = self.driver.find_element(By.ID, 'email')
            password_field = self.driver.find_element(By.ID, 'password')
            button = self.driver.find_element(By.ID, 'submitButton')

            email_field.send_keys('')
            password_field.send_keys('')
            button.click()
            time.sleep(3)

            response = requests.get(self.api_url)
            self.assertEqual(200, response.status_code, f"Expected status code 200, but got {response.status_code}")
            self.driver.refresh()
