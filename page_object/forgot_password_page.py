from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions
import imaplib


class ForgotPasswordPage(BasePage):
    def __init__(self, common_driver):
        super(ForgotPasswordPage, self).__init__(common_driver)
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

    def wait_until_password_reset_message_appears(self):
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

    def wait_until_check_internet_connection_message_appears(self):
        """
        check if the check internet connection message shows up
        :return: True, if the message shows up
        """
        try:
            popup_text_element = self.locate_element(self.popup_text, waiting_time=20)
            connection_lost= self.get_element_attribute(popup_text_element, "text")
            if connection_lost == "Please check your internet connection":
                return True
            else:
                return False # The popup text does not match
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

    @staticmethod
    def check_forgot_password_email():
        """
        check if there is a new email that sent from blueair with subject "How to reset your Blueair account password"
        currently use Apple icloud email service
        check the link of how to get the app-specific password https://support.apple.com/en-us/HT204397
        "username: test_forgot_password@icloud.com"
        "password: Qazwsx135."
        "app-pass: cpjb-xhhe-sccs-cnaw"
        :return:
        """
        username = "test_forgot_password@icloud.com"
        password = "cpjb-xhhe-sccs-cnaw"
        imap_server = "imap.mail.me.com"

        imap = imaplib.IMAP4_SSL(host=imap_server, port=993)
        imap.login(username, password)

        _, messages = imap.select("INBOX")
        _, items = imap.search(None, "ALL") # can also be "UNSEEN" for new email

        if items == [None]:
            return False
        else:
            # check fetch command https://datatracker.ietf.org/doc/html/rfc2060#section-6.4.5 for more parameters
            # e.g. "(BODY[TEXT])" means text body of the message
            # items[-1], "UTF-8": fetch the newest email and convert it to string
            _, data = imap.fetch(str(items[-1], "UTF-8").strip()[-1], "(BODY[TEXT])")

            if data == [None]:
                return False
            else:
                subject_string = 'name="subject" content="How to reset your Blueair account password"'
                whole_email = str(data[0][1],"UTF-8")
                if subject_string in whole_email:
                    return True
                else:
                    return False