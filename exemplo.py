from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

url = "https://popularpet.com.br/produtos/cachorro/"

driver.get(url)
time.sleep(3)

products_data = []

product_links = driver.find_elements(By.CLASS_NAME, 'woocommerce-loop-product__link')

print(product_links.to)

# for link in product_links:
#     product_url = link.get_attribute('href')
#     driver.get(product_url)

#     try:
#         name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.product-title'))).text
#         price = driver.find_element(By.CSS_SELECTOR, 'span.woocommerce-Price-currencySymbol').text
#         image_url = driver.find_element(By.CSS_SELECTOR, 'img.product-image').get_attribute('src')
#         category = "Cachorro"
#         description = driver.find_element(By.CSS_SELECTOR, 'div.product-description').text

#         products_data.append({
#             "Nome": name,
#             "Preço": price,
#             "Imagem": image_url,
#             "Categoria": category,
#             "Descrição": description,
#         })

#     except Exception as e:
#         print(f"Erro ao coletar dados do produto: {e}")

#     driver.back()
#     time.sleep(2)

# with open('produtos_petshop.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ["Nome", "Preço", "Imagem", "Categoria", "Descrição"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for product in products_data:
#         writer.writerow(product)

# driver.quit()
