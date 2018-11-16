from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
print(type(browser))


def openurl():
    browser.get('http://google.com')

def click():
    browser.get('http://inventwithpython.com')
    linkElem = browser.find_element_by_link_text('Automate the Boring Stuff with Python')
    type(linkElem)
    print(linkElem)
    linkElem.click()

def forms():
    browser.get('https://mail.yahoo.com')
    emailElem = browser.find_elements_by_id('login-username')[0]
    emailElem.send_keys('iammajor1')
    emailElem.submit()
    # Not sure how to capture yahoo's redirect page
    browser.implicitly_wait(5)
    print(browser.current_url)
    passwordElem = browser.find_element_by_id('login-passwd')
    passwordElem.send_keys('TEST432523626')
    passwordElem.submit()

def specialkeys():
    from selenium.webdriver.common.keys import keys
    browser.get('http://nostarch.com')
    htmlElem = browser.find_element_by_tag_name('html')
    htmlElem.send_keys(Keys.END) # Scrolls to the bottom
    htmlElem.send_keys(Keys.HOME) # Scrolls to the top of the page
    # the <html> tag is the base tag in HTML files: the full content of the HTML file is enclosed within <html></html>
    # calling browser.find_element_by_tagh_name('html') is a good place to send keys to the general web page

def browserbuttons():
    browser.back()
    browser.forward()
    browser.refresh()
    browser.quit()

forms()