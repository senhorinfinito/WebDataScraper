from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-setuid-sandbox")

chromeOptions.add_argument("--remote-debugging-port=9222")  # this

chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")

b = webdriver.Chrome(chrome_options=chromeOptions)
keyword = 'smartphone'
b.get(f'https://www.airlinequality.com/review-pages/a-z-airline-reviews/')
b.find_element_by_class_name('item').click()

# b.quit()
