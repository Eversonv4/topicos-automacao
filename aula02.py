from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
  browser = webdriver.Chrome()
  # browser = webdriver.Firefox()
  browser.get("https://huggingface.co/")

  elem = browser.find_element(By.XPATH, "/html/body/div/div[1]/header/div/div/div[1]/input")

  elem.click()

  elem.send_keys("Meta-Llama-3.1-8B-Instruct")

  time.sleep(2)

  first_item = browser.find_element(By.XPATH, "/html/body/div/div[1]/header/div/div/div[1]/div/ul[1]/li[2]/a")

  first_item.click()

  time.sleep(10)

main()