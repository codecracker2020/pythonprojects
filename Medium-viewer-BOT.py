import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

for x in range(1000):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome('C:/Users/naveen/Downloads/chromedriver_win32 (1)/chromedriver.exe', chrome_options=options)
    url = "https://jstipsntricks.medium.com/copy-paste-symbols-for-social-media-posts-%E1%83%A6-97f7f37da5db"
    driver.get(url)
    SCROLL_PAUSE_TIME = 0.5
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    # give a delay for 10 seconds
    time.sleep(5)
    print('Views ', x)
    driver.close()
