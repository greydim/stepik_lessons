from selenium import webdriver

simple_user_email = "nabetag654@200cai.com"
simple_user_password = "qYO5Cj7BX"

login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

email_input_locator = "#id_login-username"
password_input_locator = "#id_login-password"
login_button_locator = "button[name='login_submit']"


def test_successful_login():
    # Data
    login_message_locator = "div.alertinner.wicon"
    successful_login_text = "Рады видеть вас снова"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_page_link)

        email_input = browser.find_element_by_css_selector(email_input_locator)
        email_input.clear()

        # Act
        email_input.send_keys(simple_user_email)
        password_input = browser.find_element_by_css_selector(password_input_locator)
        password_input.clear()
        password_input.send_keys(simple_user_password)
        login_button = browser.find_element_by_css_selector(login_button_locator)
        login_button.click()

        # Assert
        login_message = browser.find_element_by_css_selector(login_message_locator)
        login_message_text = login_message.text
        assert successful_login_text in login_message.text, \
            f"В приветственном сообщении текст:{login_message_text}, должен быть:{successful_login_text}"

    finally:
        browser.quit()


test_successful_login()
