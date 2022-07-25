from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions
from appium import webdriver
import page_object.main_page

class LoginPage(BasePage):
    def __init__(self, common_driver):
        super(LoginPage, self).__init__(common_driver)
        self.title = (MobileBy.ID, "com.blueair.android:id/appCompatTextView")
        self.close = (MobileBy.ID, "com.blueair.android:id/btnClose")
        self.email = (MobileBy.ID, "com.blueair.android:id/email")
        self.password = (MobileBy.ID, "com.blueair.android:id/password")
        self.show_password = (MobileBy.ID, "com.blueair.android:id/text_input_end_icon")
        self.forget_password = (MobileBy.ID, "com.blueair.android:id/btnForgotPassword")
        self.log_in = (MobileBy.ID, "com.blueair.android:id/btnLogin")
        self.popup_text = (MobileBy.ID, "com.blueair.android:id/snackbar_text")
        self.invalid_text = (MobileBy.ID, "com.blueair.android:id/textinput_error")
        self.register = (MobileBy.ID, "com.blueair.android:id/btnRegister")
        self.facebook_login = (MobileBy.ID, "com.blueair.android:id/btnFacebook")
        self.google_login = (MobileBy.ID, "com.blueair.android:id/btnGoogle")
        self.google_account = (MobileBy.ID, "com.google.android.gms:id/account_name")
        self.terms_of_service = (MobileBy.ID, "com.blueair.android:id/txtTerms")
        self.terms_and_conditions = (MobileBy.ID, "com.blueair.android:id/info_container")
        self.privacy_policy = (MobileBy.ID, "com.blueair.android:id/txtPrivacy")
        self.privacy_notice = (MobileBy.ID, "com.blueair.android:id/info_container")

    def input_username_password_login(self, email, password):
        """
        input the email address and the password to login
        :param email: the email address
        :param password: the password
        :return:
        """
        try:
            email_element = self.locate_element(self.email)
            self.tap_element(email_element)
            self.set_element_text(email_element, email)
            password_element = self.locate_element(self.password)
            self.tap_element(password_element)
            self.set_element_text(password_element, password)
            login_element = self.locate_element(self.log_in)
            self.tap_element(login_element)
        except exceptions.TimeoutException:
            return False

    def main_page_login_status(self):
        """
        check if the app is logged in or not
        :return: True, if logged in
        """
        try:
            main_page = page_object.main_page.MainPage(self.driver)
            side_menu_status = main_page.check_side_menu_status()
            login_status = main_page.check_login_status()
            return side_menu_status, login_status
        except exceptions.TimeoutException:
            return False # There is no Sign in button

    def wait_until_unregistered_email_message_appears(self):
        """
        check if the unregistered email message shows up
        :return: True, if the message shows up
        """
        try:
            popup_text_element = self.locate_element(self.popup_text, waiting_time=20)
            unregistered_email= self.get_element_attribute(popup_text_element, "text")
            if unregistered_email == "There is no user with that email":
                return True
            else:
                return False # The popup text does not match incorrect_email
        except exceptions.TimeoutException:
            return False

    def wait_until_invalid_email_message_appears(self):
        """
        check if the invalid email message shows up
        :return: True, if the message shows up
        """
        try:
            email_invalid_text_element = self.locate_element(self.invalid_text, waiting_time=20)
            invalid_email= self.get_element_attribute(email_invalid_text_element, "text")
            if invalid_email == "Email is invalid":
                return True
            else:
                return False # The popup text does not match invalid_email
        except exceptions.TimeoutException:
            return False

    def wait_until_complexity_password_message_appears(self):
        """
        check if the meet complexity password message shows up
        :return: True, if the message shows up
        """
        try:
            password_complexity_text_element = self.locate_element(self.invalid_text, waiting_time=20)
            non_complexity_password= self.get_element_attribute(password_complexity_text_element, "text")
            if non_complexity_password == "The password doesn’t meet complexity requirements":
                return True
            else:
                return False # The popup text does not match non_complexity_password
        except exceptions.TimeoutException:
            return False

    def wait_until_invalid_password_message_appears(self):
        """
        check if the invalid password message shows up
        :return: True, if the message shows up
        """
        try:
            password_invalid_text_element = self.locate_element(self.popup_text, waiting_time=20)
            invalid_password= self.get_element_attribute(password_invalid_text_element, "text")
            if invalid_password == "Invalid credentials":
                return True
            else:
                return False # The popup text does not match invalid_password
        except exceptions.TimeoutException:
            return False

    def wait_until_connection_lost_message_appears(self):
        """
        check if the connection lost message shows up
        :return: True, if the message shows up
        """
        try:
            popup_text_element = self.locate_element(self.popup_text, waiting_time=20)
            connection_lost= self.get_element_attribute(popup_text_element, "text")
            if connection_lost == "The Internet connection appears to be offline.":
                return True
            else:
                return False # The popup text does not match
        except exceptions.TimeoutException:
            return False

    def close_login_page(self):
        """
        close the login page
        :return:
        """
        try:
            close_element = self.locate_element(self.close)
            self.tap_element(close_element)
        except exceptions.TimeoutException:
            return False

    def tap_register(self):
        """
        go to register page
        :return:
        """
        try:
            register_element = self.locate_element(self.register)
            self.tap_element(register_element)
        except exceptions.TimeoutException:
            return False

    def tap_continue_with_facebook(self):
        """
        login with facebook account

        * there is a webview of giving the permission with facebook account,
        * when login with facebook account for the first time
        * it is hard to automate and happens only once
        * so it is better to give the permission manually
        * then test the facebook login by automation testing

        :return:
        """
        try:
            facebook_login_element = self.locate_element(self.facebook_login)
            self.tap_element(facebook_login_element)
        except exceptions.TimeoutException:
            return False

    def tap_continue_with_google(self):
        """
        login with google account
        :return:
        """
        try:
            google_login_element = self.locate_element(self.google_login)
            self.tap_element(google_login_element)
            google_account_element = self.locate_element(self.google_account, waiting_time=5)
            self.tap_element(google_account_element)
        except exceptions.TimeoutException:
            return False

    def check_terms_of_service(self):
        """
        check terms of service availability
        :return: Ture, if terms of service page shows up
        """
        try:
            terms_of_service_element = self.locate_element(self.terms_of_service)
            self.tap_element(terms_of_service_element)
            terms_and_conditions_element = self.locate_element(self.terms_and_conditions, waiting_time=10)
            if type(terms_and_conditions_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_privacy_policy(self):
        """
        check privacy policy availability
        :return: Ture, if privacy policy page shows up
        """
        try:
            privacy_policy_element = self.locate_element(self.privacy_policy)
            self.tap_element(privacy_policy_element)
            privacy_notice_element = self.locate_element(self.privacy_notice)
            if type(privacy_notice_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_login_page_status(self):
        """
        check if the login page (the tile text) appears
        :return:
        """
        try:
            login_title_element = self.locate_element(self.title, waiting_time=20)
            login_title_text = self.get_element_attribute(login_title_element, "text")
            if login_title_text == "Log In":
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def tap_forgot_password(self):
        """
        go to forgot password page
        :return:
        """
        try:
            forgot_password_element = self.locate_element(self.forget_password)
            self.tap_element(forgot_password_element)
        except exceptions.TimeoutException:
            return False

    def retrieve_password(self):
        pass