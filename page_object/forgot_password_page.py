from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions


class ForgotPassword(BasePage):
    def __init__(self, common_driver):
        super(ForgotPassword, self).__init__(common_driver)
        self.back = (MobileBy.ID, "com.blueair.android:id/btnBack")
        self.close = (MobileBy.ID, "com.blueair.android:id/btnClose")
        self.email = (MobileBy.ID, "com.blueair.android:id/email")
        self.reset_password = (MobileBy.ID, "com.blueair.android:id/btnForgotPassword")
        self.invalid_text = (MobileBy.ID, "com.blueair.android:id/textinput_error")
        self.popup_text = (MobileBy.ID, "com.blueair.android:id/snackbar_text")

    def input_username_reset_password(self, email):
        """
        input the email address to reset the password
        :param email: the email address
        :return:
        """
        try:
            email_element = self.locate_element(self.email)
            self.tap_element(email_element)
            self.set_element_text(email_element, email)
            reset_password_element = self.locate_element(self.reset_password)
            self.tap_element(reset_password_element)
        except exceptions.TimeoutException:
            return False

    def wait_until_invalid_email_message_shows_up(self):
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

    def wait_until_unregistered_email_message_shows_up(self):
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

    def wait_until_password_reset_message_shows_up(self):
        """
        check if the password reset sent message shows up
        :return: True, if the message shows up
        """
        try:
            popup_text_element = self.locate_element(self.popup_text, waiting_time=20)
            password_reset= self.get_element_attribute(popup_text_element, "text")
            if password_reset == "A password reset link was sent to your email":
                return True
            else:
                return False # The popup text does not match incorrect_email
        except exceptions.TimeoutException:
            return False

    def close_forgot_password_page_use_close_button(self):
        """
        close the forgot password page by using close (X) button
        :return:
        """
        try:
            close_element = self.locate_element(self.close)
            self.tap_element(close_element)
        except exceptions.TimeoutException:
            return False

    def close_forgot_password_page_use_back_button(self):
        """
        clsoe the forgot password page by using back (<-) button
        :return:
        """
        try:
            back_element = self.locate_element(self.back)
            self.tap_element(back_element)
        except exceptions.TimeoutException:
            return False