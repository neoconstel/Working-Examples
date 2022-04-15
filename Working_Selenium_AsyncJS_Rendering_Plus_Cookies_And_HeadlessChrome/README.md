# Selenium Async JavaScript-Rendering Example -- Along with Selenium Cookies and Headless Chrome

This example shows the working way to:

- use python selenium to crawl through JavaScript-loaded HTML pages in chrome headless mode (that is -- without the Chrome browser UI)
- make chrome headless mode undetectable by sites which block headless webcrawlers (an example is Udemy)
	> this is because although the normal selenium chrome mode works easily, the headless mode might be detected as a bot and thus blocked
- work with cookies in selenium (save, load and delete cookies)
- bonus: take snapshots of the webpage even in headless mode for use in diagnosing what the problem might be if webcrawling is failing
- bonus: a good exposure on setting important chrome options (such as disabling extensions) which make it easier to successfully render a webpage speedily

