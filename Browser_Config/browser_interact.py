import time
from selenium import webdriver


def launch_website(browser_name, url):
    try:
        if browser_name.lower() == 'chrome':
            driver = webdriver.Chrome()
            driver.maximize_window()
            print("Chrome launched")
        elif browser_name.lower() == 'firefox':
            driver = webdriver.Firefox()
            print("Firefox launched")
        elif browser_name.lower() == 'edge':
            driver = webdriver.Edge()
            driver.maximize_window()
            print("Edge launched")

        try:
            driver.get(url)
            time.sleep(3)
        except Exception as e:
            print("Failed to launch. Invalid URI %s" % url)

    except Exception as e:
        print("Exception Type: ", type(e).__name__)


launch_website('firefox', 'https://www.google.com')
# browser_list = ['chrome', 'firefox', 'edge']
#
# for browser in browser_list:
#     launch_website(browser, 'https://www.google.com')
