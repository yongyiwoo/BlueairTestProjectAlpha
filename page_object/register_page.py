from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions
from appium import webdriver
import page_object.login_page

class RegisterPage(BasePage):
    def __init__(self, common_driver):
        super(RegisterPage, self).__init__(common_driver)
        self.close = (MobileBy.ID, "com.blueair.android:id/btnClose")
        self.back = (MobileBy.ID, "com.blueair.android:id/btnBack")
        self.first_name = (MobileBy.ID, "com.blueair.android:id/firstName")
        self.last_name = (MobileBy.ID, "com.blueair.android:id/lastName")
        self.email = (MobileBy.ID, "com.blueair.android:id/email")
        self.phone_number = (MobileBy.ID, "com.blueair.android:id/phoneNumber")
        self.password = (MobileBy.ID, "com.blueair.android:id/password")
        self.confirm_password = (MobileBy.ID, "com.blueair.android:id/confirmPassword")
        self.age_limit = (MobileBy.ID, "com.blueair.android:id/cbYears")
        self.blueair_subscription = (MobileBy.ID, "com.blueair.android:id/cbSubscribe")
        self.unilever_data_share = (MobileBy.ID, "com.blueair.android:id/cbConsent")
        self.agree_documents = (MobileBy.ID, "com.blueair.android:id/cbPrivacy")
        self.terms_of_service = (MobileBy.ID, "com.blueair.android:id/txtTerms")
        self.terms_and_conditions = (MobileBy.ID, "com.blueair.android:id/info_container")
        self.privacy_policy = (MobileBy.ID, "com.blueair.android:id/txtPrivacy")
        self.privacy_notice = (MobileBy.ID, "com.blueair.android:id/info_container")
        self.register = (MobileBy.ID, "com.blueair.android:id/btnRegister")
        self.text_input_error = (MobileBy.ID, "com.blueair.android:id/textinput_error")
        self.email_already_exists = (MobileBy.ID, "com.blueair.android:id/snackbar_text")

    def input_required_fields_register(self, first_name, last_name, email, phone_number, password, confirm_password,
                                       age_limit: bool, blueair_subscription: bool, unilever_data_share: bool,
                                       agree_documents: bool):
        """
        input and check the fields to register
        :param first_name:
        :param last_name:
        :param email:
        :param phone_number:
        :param password:
        :param confirm_password:
        :param age_limit: tick, if True, un-tick, if False
        :param blueair_subscription: tick, if True, un-tick, if False
        :param unilever_data_share: tick, if True, un-tick, if False
        :param agree_documents: tick, if True, un-tick, if False
        :return:
        """
        try:
            if first_name != "":
                first_name_element = self.locate_element(self.first_name)
                self.tap_element(first_name_element)
                self.set_element_text(first_name_element, first_name)
            if last_name != "":
                last_name_element = self.locate_element(self.last_name)
                self.tap_element(last_name_element)
                self.set_element_text(last_name_element, last_name)
            if email != "":
                email_element = self.locate_element(self.email)
                self.tap_element(email_element)
                self.set_element_text(email_element, email)
            if phone_number != "":
                phone_number_element = self.locate_element(self.phone_number)
                self.tap_element(phone_number_element)
                self.set_element_text(phone_number_element, phone_number)
            if password != "":
                password_element = self.locate_element(self.password)
                self.tap_element(password_element)
                self.set_element_text(password_element, password)
            if confirm_password != "":
                confirm_password_element = self.locate_element(self.confirm_password)
                self.tap_element(confirm_password_element)
                self.set_element_text(confirm_password_element, confirm_password)
        except exceptions.TimeoutException:
            pass

        # for register page, because there are more than one screen fields to fill,
        # so it needs to swipe up to find the element.
        if age_limit is True:
            # swipe 2 times to find the age limit element
            for _ in range(2):
                try:
                    age_limit_element = self.locate_element(self.age_limit)
                    self.tap_element(age_limit_element)
                    break
                except exceptions.TimeoutException:
                    start_position_percent = self.set_position_on_screen((75, 75))
                    end_position_percent = self.set_position_on_screen((25, 25))
                    self.scroll_screen(start_position_percent, end_position_percent)

        if blueair_subscription is True:
            # swipe 2 times to find the subscription element
            for _ in range(2):
                try:
                    #print("blueair subscription tap")
                    blueair_subscription_element = self.locate_element(self.blueair_subscription)
                    self.tap_element(blueair_subscription_element)
                    break
                except exceptions.TimeoutException:
                    #print("blueair subscription scroll")
                    start_position_percent = self.set_position_on_screen((75, 75))
                    end_position_percent = self.set_position_on_screen((25, 25))
                    self.scroll_screen(start_position_percent, end_position_percent)

        if unilever_data_share is True:
            # swipe 2 times to find the data share element
            for _ in range(2):
                try:
                    #print("unilever data share tap")
                    unilever_data_share_element = self.locate_element(self.unilever_data_share)
                    self.tap_element(unilever_data_share_element)
                    break
                except exceptions.TimeoutException:
                    #print("unilever data share scroll")
                    start_position_percent = self.set_position_on_screen((75, 75))
                    end_position_percent = self.set_position_on_screen((25, 25))
                    self.scroll_screen(start_position_percent, end_position_percent)

        if agree_documents is True:
            # swipe 2 times to find agree documents element
            for _ in range(2):
                try:
                    #print("agree documents tap")
                    agree_documents_element = self.locate_element(self.agree_documents)
                    self.tap_element(agree_documents_element)
                    break
                except exceptions.TimeoutException:
                    #print("agree documents scroll")
                    start_position_percent = self.set_position_on_screen((75, 75))
                    end_position_percent = self.set_position_on_screen((25, 25))
                    self.scroll_screen(start_position_percent, end_position_percent)

                    # swipe 2 times to find agree documents element
        for _ in range(2):
            try:
                register_element = self.locate_element(self.register)
                self.tap_element(register_element)
                break
            except exceptions.TimeoutException:
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((25, 25))
                self.scroll_screen(start_position_percent, end_position_percent)

    def close_register(self):
        try:
            close_register_element = self.locate_element(self.close)
            self.tap_element(close_register_element)
        except exceptions.TimeoutException:
            return False

    def check_enter_your_first_name_message_appears(self):
        """
        check if Enter your first name message appears
        :return: True, if appears, False, if disappears
        """
        try:
            # scroll up 2 times (if needed) to find text input error element
            for _ in range(2):
                text_input_error_elements = self.locate_element_list(self.text_input_error)
                for text_input_error_element in text_input_error_elements:
                    text_input_error_text = self.get_element_attribute(text_input_error_element, "text")
                    if text_input_error_text == "Enter your first name":
                        return True
                start_position_percent = self.set_position_on_screen((25, 25))
                end_position_percent = self.set_position_on_screen((75, 75))
                self.scroll_screen(start_position_percent, end_position_percent)
            return False
        except exceptions.TimeoutException:
            return False

    def check_enter_your_last_name_message_appears(self):
        """
        check if Enter your last name message appears
        :return: True, if appears, False, if disappears
        """
        try:
            # scroll up 2 times (if needed) to find text input error element
            for _ in range(2):
                text_input_error_elements = self.locate_element_list(self.text_input_error)
                for text_input_error_element in text_input_error_elements:
                    text_input_error_text = self.get_element_attribute(text_input_error_element, "text")
                    if text_input_error_text == "Enter your last name":
                        return True
                start_position_percent = self.set_position_on_screen((25, 25))
                end_position_percent = self.set_position_on_screen((75, 75))
                self.scroll_screen(start_position_percent, end_position_percent)

            return False
        except exceptions.TimeoutException:
            return False

    def check_enter_your_email_message_appears(self):
        """
        check if Enter your email message appears
        :return: True, if appears, False, if disappears
        """
        try:
            # scroll up 2 times (if needed) to find text input error element
            for _ in range(2):
                text_input_error_elements = self.locate_element_list(self.text_input_error)
                for text_input_error_element in text_input_error_elements:
                    text_input_error__text = self.get_element_attribute(text_input_error_element, "text")
                    if text_input_error__text == "Enter your email":
                        return True
                start_position_percent = self.set_position_on_screen((25, 25))
                end_position_percent = self.set_position_on_screen((75, 75))
                self.scroll_screen(start_position_percent, end_position_percent)
            return False
        except exceptions.TimeoutException:
            return False

    def check_enter_your_password_message_appears(self):
        """
        check if Enter your password message appears
        :return: True, if appears, False, if disappears
        """
        try:
            # scroll up 2 times (if needed) to find text input error element
            for _ in range(2):
                text_input_error_elements = self.locate_element_list(self.text_input_error)
                for text_input_error_element in text_input_error_elements:
                    text_input_error__text = self.get_element_attribute(text_input_error_element, "text")
                    if text_input_error__text == "Enter your password":
                        return True
                start_position_percent = self.set_position_on_screen((25, 25))
                end_position_percent = self.set_position_on_screen((75, 75))
                self.scroll_screen(start_position_percent, end_position_percent)
            return False
        except exceptions.TimeoutException:
            return False

    def check_password_does_not_match_message_appears(self):
        """
        check if password doesn't match message appears
        :return: True, if appears, False, if disappears
        """
        try:
            # scroll up 2 times (if needed) to find text input error element
            for _ in range(2):
                text_input_error_elements = self.locate_element_list(self.text_input_error)
                for text_input_error_element in text_input_error_elements:
                    text_input_error__text = self.get_element_attribute(text_input_error_element, "text")
                    if text_input_error__text == "Password doesn't match":
                        return True
                start_position_percent = self.set_position_on_screen((25, 25))
                end_position_percent = self.set_position_on_screen((75, 75))
                self.scroll_screen(start_position_percent, end_position_percent)
            return False
        except exceptions.TimeoutException:
            return False

    def check_password_does_not_meet_complexity_requirements_message_appears(self):
        """
        check if password doesn't meet complexity requirements message appears
        :return: True, if appears, False, if disappears
        """
        try:
            # scroll up 2 times (if needed) to find text input error element
            for _ in range(2):
                text_input_error_elements = self.locate_element_list(self.text_input_error)
                for text_input_error_element in text_input_error_elements:
                    text_input_error__text = self.get_element_attribute(text_input_error_element, "text")
                    if text_input_error__text == "The password doesn’t meet complexity requirements":
                        # print("can see the error message")
                        return True
                start_position_percent = self.set_position_on_screen((25, 25))
                end_position_percent = self.set_position_on_screen((75, 75))
                self.scroll_screen(start_position_percent, end_position_percent)
            return False
        except exceptions.TimeoutException:
            return False

    def wait_until_email_already_exists_message_appears(self):
        """
        check if the email already exists message appears
        :return: True, if the message appears
        """
        try:
            email_already_exists_text_element = self.locate_element(self.email_already_exists, waiting_time=20)
            email_already_exists= self.get_element_attribute(email_already_exists_text_element, "text")
            if email_already_exists == "Looks like an account with such email already exists":
                return True
            else:
                return False # The popup text does not match invalid_password
        except exceptions.TimeoutException:
            return False