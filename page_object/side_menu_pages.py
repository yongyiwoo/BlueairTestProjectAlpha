from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions
from appium import webdriver
import page_object.main_page
import time

class SideMenuPages(BasePage):
    def __init__(self, common_driver):
        super(SideMenuPages, self).__init__(common_driver)
        self.close = (MobileBy.ID, "com.blueair.android:id/drawer_close_view")
        self.log_out = (MobileBy.ID, "com.blueair.android:id/signin")
        self.log_out_confirm = (MobileBy.ID, "com.blueair.android:id/confirm_button")
        self.log_out_dismiss = (MobileBy.ID, "com.blueair.android:id/dismiss_button")
        # the elements in the hamburger menu don't have IDs
        # may use resource id "com.blueair.android:id/design_menu_item_text"
        self.side_menu_section = (MobileBy.ID, "com.blueair.android:id/design_menu_item_text")

        self.email = (MobileBy.ID, "com.blueair.android:id/email")
        # two ids below need to be added on Android
        #self.first_name = (MobileBy.ID, "com.blueair.android:id/FirstName")
        #self.last_name = (MobileBy.ID, "com.blueair.android:id/LastName")
        self.phone_number = (MobileBy.ID, "com.blueair.android:id/phoneNumber")


    def tap_log_out(self):
        try:
            log_out_element = self.locate_element(self.log_out)
            self.tap_element(log_out_element)
            log_out_confirm_element = self.locate_element(self.log_out_confirm)
            self.tap_element(log_out_confirm_element)
        except exceptions.TimeoutException:
            return False

    def check_log_out_status(self):
        """
        check if the log out appears
        :return: True, if appears, False, if disappears
        """
        try:
            log_out_element = self.locate_element(self.log_out)
            if type(log_out_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_profile_status(self):
        """
        check if the profile appears
        :return: True, if appears, False, if disappears
        """
        try:
            side_menu_section_elements = self.locate_element_list(self.side_menu_section)
            for side_menu_section_element in side_menu_section_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Profile":
                    return True
            return False
        except exceptions.TimeoutException:
            return False

    def check_voice_assistants_status(self):
        """
        check if the voice assistants appears
        :return: True, if appears, False, if disappears
        """
        try:
            side_menu_section_elements = self.locate_element_list(self.side_menu_section)
            for side_menu_section_element in side_menu_section_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Voice Assistants":
                    return True
            return False
        except exceptions.TimeoutException:
            return False

    def tap_profile(self):
        try:
            side_menu_section_elements = self.locate_element_list(self.side_menu_section)
            for side_menu_section_element in side_menu_section_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Profile":
                    self.tap_element(side_menu_section_element)
                    break
        except exceptions.TimeoutException:
            return False

    def close_side_menu(self):
        try:
            close_hamburger_menu_element = self.locate_element(self.close)
            self.tap_element(close_hamburger_menu_element)
        except exceptions.TimeoutException:
            return False

    def get_profile_email(self):
        """
        get the email in account section on the profile page
        :return: the email address
        """
        try:
            profile_email_element = self.locate_element(self.email)
            profile_email_text = self.get_element_attribute(profile_email_element, "text")
            return profile_email_text
        except exceptions.TimeoutException:
            return False
    '''
    def get_profile_first_name(self):
        """
        get the first name in account section on the profile page
        :return: the first name
        """
        try:
            profile_first_name_element = self.locate_element(self.first_name)
            profile_first_name_text = self.get_element_attribute(profile_first_name_element, "text")
            return profile_first_name_text
        except exceptions.TimeoutException:
            return False
            
    def get_profile_last_name(self):
        """
        get the last name in account section on the profile page
        :return: the last name
        """
        try:
            profile_last_name_element = self.locate_element(self.last_name)
            profile_last_name_text = self.get_element_attribute(profile_last_name_element, "text")
            return profile_last_name_text
        except exceptions.TimeoutException:
            return False
    '''

    def get_profile_phone_number(self):
        """
        get the phone number in account section on the profile page
        :return: the phone number
        """
        try:
            profile_phone_number_element = self.locate_element(self.phone_number)
            profile_phone_number_text = self.get_element_attribute(profile_phone_number_element, "text")
            return profile_phone_number_text
        except exceptions.TimeoutException:
            return False