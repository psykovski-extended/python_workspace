import json
import time
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
settings = {"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}],
            "selectedDestinationId": "Save as PDF", "version": 2}
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')

driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe', options=chrome_options)
driver.get('https://digi4school.at/')

username = driver.find_element_by_name('email')
username.clear()
username.send_keys(input('Your Email:\n'))

with open('C:\\Users\\' + os.environ['USERNAME'] + '\\pw.txt', 'r') as pw:
    passW = pw.readline()

password = driver.find_element_by_name('password')
password.clear()
password.send_keys(passW)
password.submit()

del passW

time.sleep(3)

ancker = driver.find_elements_by_tag_name('a')
english = ancker[4]
mathe = ancker[5]
nw = ancker[6]
e = mathe.click()
time.sleep(3)

c = driver.current_window_handle
driver.switch_to.window(driver.window_handles[1])

for i in range(1, 340):
    # driver.get('https://a.hpthek.at/ebook/164/' + str(i) + '/' + str(i) + '.svg')
    driver.get('https://a.hpthek.at/ebook/164/' + str(i) + '.svg')
    driver.execute_script('window.print();')

driver.quit()
