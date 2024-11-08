from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from categories import categories

MAX_QUANTITY_OF_PRODUCTS = 10

def get_products_url(browser, url):
  browser.get(url)

  product_a_tags = browser.find_elements(By.CSS_SELECTOR, '[itemprop="url"]')
  product_a_tags = product_a_tags[:MAX_QUANTITY_OF_PRODUCTS]

  product_links = []

  for a_tag in product_a_tags:
    url = a_tag.get_attribute('href')
    product_links.append(url)

  return product_links

def fetch_product_and_get_data(browser, link, category_name):
  browser.get(link)
  time.sleep(2)

  try:
    product_price = browser.find_element(By.CSS_SELECTOR, '.font-title-s.color-primary').text
    product_name = browser.find_element(By.XPATH, '//*[@id="__layout"]/div/div/main/main/div[1]/section[1]/div[1]/div/div/div[2]/div[2]/header/h1').text
    image_url = browser.find_element(By.CSS_SELECTOR, '[datatest-id="main-img"]').get_attribute('src')

  except Exception as e:
    print("Produto está com informações incompletas")
    return None

  return {
    "Nome": product_name,
    "Preco": product_price,
    "Imagem": image_url,
    "Categoria": category_name
  }

def get_scraped_data(browser, category):
  products_data = []

  product_links = get_products_url(browser, category['url'])
  product_links = product_links[:MAX_QUANTITY_OF_PRODUCTS]

  for product_link in product_links:
    product_data = fetch_product_and_get_data(browser, product_link, category['category'])
    if product_data:
      products_data.append(product_data)

  return products_data

def save_scraped_data_as_cvs(data, category):
  with open(f'produtos_{category['category']}_petshop.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["Nome", "Preco", "Imagem", "Categoria"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for product in data:
        writer.writerow(product)


def main():
  url_site = "https://www.petlove.com.br/cachorro"
  browser = webdriver.Chrome()

  for category in categories:
    browser.get(category['url'])

    products_data = get_scraped_data(browser, category)
    save_scraped_data_as_cvs(products_data, category)

  browser.quit()

main()