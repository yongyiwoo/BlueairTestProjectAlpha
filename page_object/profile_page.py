from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions
from appium import webdriver

class ProfilePage(BasePage):
    def __init__(self, common_driver):
        super(ProfilePage, self).__init__(common_driver)
        #self.profile = (MobileBy.ID, "android:id/content") # shouldn't use this element
        self.profile_account = (MobileBy.ID, "com.blueair.android:id/txtAccountTitle")
        self.profile_address = (MobileBy.ID, "com.blueair.android:id/txtAddressTitle")
        self.email = (MobileBy.ID, "com.blueair.android:id/email")
        self.first_name = (MobileBy.ID, "com.blueair.android:id/firstName")
        self.last_name = (MobileBy.ID, "com.blueair.android:id/lastName")
        self.phone_number = (MobileBy.ID, "com.blueair.android:id/phoneNumber")

    def check_profile_page_appears(self):
        try:
            profile_account_element = self.locate_element(self.profile_account, waiting_time=20)
            profile_address_element = self.locate_element(self.profile_address, waiting_time=20)
            if type(profile_account_element) is webdriver.WebElement and \
                    type(profile_address_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def get_email_info(self):
        """
        get the email in the profile page
        :return: the email address
        """
        try:
            profile_email_element = self.locate_element(self.email)
            # sometimes page loading needs some time
            while True:
                profile_email_text = self.get_element_attribute(profile_email_element, "text")
                if profile_email_text != "Email":
                    break
            return profile_email_text
        except exceptions.TimeoutException:
            return False  # #

    def get_first_name_info(self):
        """
        get the first name on the profile page
        :return: the first name
        """
        try:
            profile_first_name_element = self.locate_element(self.first_name)
            profile_first_name_text = self.get_element_attribute(profile_first_name_element, "text")
            return profile_first_name_text
        except exceptions.TimeoutException:
            return False

    def get_last_name_info(self):
        """
        get the last name on the profile page
        :return: the last name
        """
        try:
            profile_last_name_element = self.locate_element(self.last_name)
            profile_last_name_text = self.get_element_attribute(profile_last_name_element, "text")
            return profile_last_name_text
        except exceptions.TimeoutException:
            return False

    def get_phone_number_info(self):
        """
        get the phone number on the profile page
        :return: the phone number
        """
        try:
            profile_phone_number_element = self.locate_element(self.phone_number)
            profile_phone_number_text = self.get_element_attribute(profile_phone_number_element, "text")
            return profile_phone_number_text
        except exceptions.TimeoutException:
            return False