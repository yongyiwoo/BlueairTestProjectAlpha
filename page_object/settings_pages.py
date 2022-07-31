from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions
from appium import webdriver


class SettingsPages(BasePage):
    def __init__(self, common_driver):
        super(SettingsPages, self).__init__(common_driver)
        self.settings = (MobileBy.ID, "com.blueair.android:id/info_container")
        self.temperature = (MobileBy.ID, "com.blueair.android:id/temp_title")
        self.temperature_scale = (MobileBy.ID, "com.blueair.android:id/temp_pref")
        self.license_report = (MobileBy.ID, "com.blueair.android:id/tv_license")
        self.license_list = (MobileBy.ID, "com.blueair.android:id/license_list")

    def check_settings_page_appears(self):
        try:
            settings_element = self.locate_element(self.settings, waiting_time=20)
            if type(settings_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def change_temperature_scale(self, scale:str):
        """
        change temperature scale to either Celsius or Fahrenheit depends on the scale parameter
        :param scale:
        :return: string "Celsius" or "Fahrenheit"
        """
        try:
            temperature_scale_element = self.locate_element(self.temperature_scale)
            temperature_scale_text = self.get_element_attribute(temperature_scale_element, "text")
            if scale == temperature_scale_text:
                return temperature_scale_text
            else:
                self.tap_element(temperature_scale_element)
                temperature_scale_text = self.get_element_attribute(temperature_scale_element, "text")
                return temperature_scale_text
        except exceptions.TimeoutException:
            return False

    def tap_license_report(self):
        try:
            license_report_element = self.locate_element(self.license_report)
            self.tap_element(license_report_element)
        except exceptions.TimeoutException:
            return False

    def check_license_page_appears(self):
        try:
            license_list_element = self.locate_element(self.license_list, waiting_time=20)
            if type(license_list_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False
