from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from categories import categories

def main():
  browser = webdriver.Chrome()
  browser.get("https://www.petlove.com.br/cachorro")

  products_data = []

  product_a_tags = browser.find_elements(By.CSS_SELECTOR, '[itemprop="url"]')

  product_links = []

  for a_tag in product_a_tags:
    url = a_tag.get_attribute('href')
    product_links.append(url)

  for link in product_links:
    browser.get(link)
    time.sleep(2)

    try:
      print(link)

      product_price = browser.find_element(By.CSS_SELECTOR, '.font-title-s.color-primary').text
      product_name = browser.find_element(By.CSS_SELECTOR, '.mt-5.font-title-xs.font-medium.color-neutral-darkest').text
      image_url = browser.find_element(By.CSS_SELECTOR, '[datatest-id="main-img"]').get_attribute('src')
      categoria = "Cachorro"
      print(image_url)

    except Exception as e:
      print("Produto está com informações incompletas")
      continue

    products_data.append({
      "Nome": product_name,
      "Preço": product_price,
      "Imagem": image_url,
      "Categoria": categoria
    })

main()