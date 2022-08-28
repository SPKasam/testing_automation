from selenium import webdriver
chrome = webdriver.Chrome()
chrome.get('https://demo.anhtester.com/basic-first-form-demo.html')

user_msg = chrome.find_element('xpath','//*[@id="user-message"]')
user_btn = chrome_brower.find_element('xpath','//*[@id="get-input"]/button')
user_msg.clear()
user_msg.send_keys('Testing Testing')
user_btn.click()
output_box = chrome_browser.find_element('xpath','//*[@id="display"]')
assert "Testing Testing" in output_box.text
print('testing passed!')