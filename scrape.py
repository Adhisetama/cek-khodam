# Author: martabakmenari
# NOTE: Install webdriver untuk chrome, taruh .exe nya di directory ini

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

# buat nyimpen khodam
khodams = set()
iterations = 1000



try:
    url = 'https://check-your-khodam.vercel.app'
    driver.get(url)

    for i in range(iterations):
        # 1. Ketik nama
        text_input = driver.find_element(By.TAG_NAME, 'input')
        text_input.clear()
        text_input.send_keys('hirasawa yui')

        # 2. Klik tombol cek khodam
        submit_button = driver.find_element(By.ID, 'btn-check')
        submit_button.click()

        # 3. Tunggu sampe dapet khodam
        wait = WebDriverWait(driver, 10)
        div_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'result-text')))

        # 4. Ambil teksnya
        result_text = div_element.text

        # 5. Print & save
        try:
            print(i, result_text)
        except UnicodeEncodeError:
            print(i, '<error bang gabisa ngeprint emoji>')
        khodams.add(result_text)

        driver.refresh()

finally:
    driver.quit()

    with open('khodam.txt', 'w', encoding='unicode_escape') as khodam_file:
        for khodam in khodams:
            khodam_file.write(f'{khodam}\n')