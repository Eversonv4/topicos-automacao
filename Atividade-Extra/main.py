from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

TOTAL = 100
MAIN_URL = 'https://www.folhadelondrina.com.br/?d=1'
FILE_OUTPUT = 'links.txt'

driver = webdriver.Chrome()

def get_robots_txt(base_url):
    robots_url = urljoin(base_url, 'robots.txt')
    driver.get(robots_url)
    time.sleep(1)
    return driver.find_element(By.TAG_NAME, 'pre').text

def is_url_allowed(url, robots_txt):
    rp = RobotFileParser()
    rp.parse(robots_txt.splitlines())
    return rp.can_fetch('*', url)

def extract_links():
    url_list = []

    driver.get(MAIN_URL)
    elements = driver.find_elements(By.TAG_NAME, 'a')

    for elem in elements:
        href = elem.get_attribute('href')
        if href and href not in url_list:
            url_list.append(href)

    return url_list

robots_txt = get_robots_txt(MAIN_URL)

if robots_txt and is_url_allowed(MAIN_URL, robots_txt):
    valid_links = []
    invalid_links = []
    links = extract_links()

    for link in links:
        if len(valid_links) >= TOTAL:
            break

        if is_url_allowed(link, robots_txt):
            valid_links.append(link)
        else:
            invalid_links.append(link)

    with open(FILE_OUTPUT, 'w') as f:
        for link in valid_links[:TOTAL]:
            f.write(link + '\n')

    print("Links salvos com sucesso, meu chapa! 😎")

    if invalid_links:
        print('Links proibidos:')
        for link in invalid_links:
            print(link)
else:
    print("Forneça uma URL válida até o arquivo \"robot.txt\".")
    driver.quit()