import time

def test_check_card_presence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector(".btn-add-to-basket").is_displayed()
    assert button, 'Button is NOT FOUND'