import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the path of the ChromeDriver executable
chromedriver_path = 'PATH TO CHROME DRIVER'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromedriver_path)

# Navigate to the website to be tested
driver.get('http://192.168.1.8:8090/httpclient.html')

time.sleep(5)
# Find the search input element and enter a search query
search_input = driver.find_element('name','username')
search_input.send_keys('21610053')
time.sleep(5)
search_pass = driver.find_element('name','password')
search_pass.send_keys('7218913222')
time.sleep(5)
search_pass.send_keys(Keys.RETURN)
time.sleep(5)
# Assert that the search results page title contains the search query
#assert 'test query' in driver.title

# Close the browser
driver.quit()