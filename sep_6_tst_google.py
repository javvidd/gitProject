# google search scenario
# 1 open browser, launch the website google.com
# 2 type 'selenium python' in search and hit enter
# 3 verify the result in more than 20mln
# 4 verify that it takes less than a sec for result

import time
import winsound

import stats as stats
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# winsound.PlaySound("Buzz.wav", winsound.SND_ASYNC) # will play the song

driver = webdriver.Chrome()
driver.get("https://google.com")
search_text_box = driver.find_element_by_name("q")

search_text_box.clear()
search_text_box.send_keys("python selenium")

search_text_box.send_keys(Keys.RETURN)  # replicates pushing enter button

result = driver.find_element_by_xpath("//div[@id='result-stats']").text

numbers = result.split()
sec = float(numbers[3].replace('(', ''))
deriv = int(numbers[1].replace(',',''))
assert deriv > 20000000
assert sec < 1
print(f"test passed with search result {deriv} in {sec} millisecond")
# if deriv > 20000000 and sec < 1:
#     print("passed")
# else:
#     print("failed")

print(numbers)
driver.close()
