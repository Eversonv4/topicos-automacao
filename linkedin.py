import os
from dotenv import load_dotenv
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
  dotenv_path = Path('.env')
  load_dotenv(dotenv_path=dotenv_path)
  email = os.getenv("EMAIL")
  password = os.getenv("PASSWORD")

  browser = webdriver.Chrome()

  browser.get("https://www.linkedin.com/login/pt")

  username_input = browser.find_element(By.NAME, "session_key")
  password_input = browser.find_element(By.NAME, "session_password")
  submit_button = browser.find_element(By.CSS_SELECTOR, '[data-litms-control-urn="login-submit"]')

  username_input.send_keys(email)
  password_input.send_keys(password)
  submit_button.click()

  browser.execute_script("alert('Ihuuu')")

  time.sleep(6)

main()