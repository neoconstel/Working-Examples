import json
import re
import os


def save_cookies(driver, location):

    json.dump(driver.get_cookies(), open(location, "w"))


def load_cookies(driver, location, url):

    if not os.path.exists(location):
        driver.get(url)
        return

    cookies = json.load(open(location, "r"))
    	
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which. but good to make it your intended url
    driver.get(url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):#Checks if the instance expiry a float 
            cookie['expiry'] = int(cookie['expiry'])# it converts expiry cookie to a int 
        driver.add_cookie(cookie)


def delete_cookies(driver, domains=None):

    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  # if cookies changed, we will update them
            # deleting everything and adding the modified cookie object
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()


def domain_from_url(url):
    domain_regex = re.compile("(\w+\.\w+\.[^/]+)|(\w+\.[^/]+)")
    domain_match = re.search(domain_regex, url)

    if not domain_match:
        return

    return domain_match.group()
