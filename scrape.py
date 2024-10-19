import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

def scrape_website(website):
    print("Launching Chrome Browser.....")


    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("page loaded.....")
        html = driver.page_source

        return html
    finally:
        driver.quit()