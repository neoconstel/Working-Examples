from selenium import webdriver

from bs4 import BeautifulSoup
import time
from cookie_functions import * # this is a custom module

cookie_path = "cookies.json"
use_cookies = True


# options
options = webdriver.ChromeOptions()

# set user agent -- this makes the browser appear to be a real user, not a bot. EXTREMELY IMPORTANT for bot-blocking sites
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

options.add_argument("--disable-extensions") # Important to speed up page rendering, but can also work without it (but much better chance with it)
options.add_argument("--window-size=1920,1080") # set window dimensions to desktop
options.add_argument("--start-maximized") # start with maximized window
options.add_argument('--headless') # run without UI

# the rest of these options are not really necessary, but may possibly come in handy

# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--allow-running-insecure-content")

# end of options

# create the driver with the configured options
driver = webdriver.Chrome(options=options)

# getting a webpage
url = "https://www.udemy.com/course/complete-davinci-resolve-17-megacourse-beginner-to-expert/"

# load_cookies also gets the url (for mandatory reasons), so DO NOT do another driver.get(url) if cookie is loaded
if use_cookies:
    load_cookies(driver=driver, location=cookie_path, url=url)
    save_cookies(driver=driver, location=cookie_path)
else:
    driver.get(url)
    

# sleep a bit for page to render properly
time.sleep(10)

# NOW FOR THE MAIN STUFF

# execute a javascript code to get the entire html
html = driver.execute_script("return document.documentElement.outerHTML")

# turn the html into a beautifulsoup object
html_soup = BeautifulSoup(html, "lxml")

# find an element -- in this case the "Buy" button of an Udemy course. This
# button is an async element and can only be found if the javascript has been 
# rendered in the DOM
buy_btns = html_soup.select(".styles--btn--express-checkout--28jN4")
print(buy_btns)

# drop a screenshot of the page after everything, for proper diagnosis of what
# the headless browser 'saw'.
driver.get_screenshot_as_file("screenshot.png")

# close browser after our manipulations
# driver.close()
