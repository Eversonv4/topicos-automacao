from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
  browser = webdriver.Chrome()
  browser.get("https://huggingface.co/google/gemma-2-2b-it")

  # elem = browser.find_element(By.XPATH, '/html/body/div/main/div[2]/section[2]/div[5]/div/form/div[4]/div/span/span/input')

  elem = browser.find_element(By.CSS_SELECTOR, '[placeholder="Your sentence here..."]')

  time.sleep(2)

  elem.click()

  time.sleep(2)

  elem.send_keys("Welcome to selenium")

  time.sleep(5)

main()