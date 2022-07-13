from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions
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
        # may use ID "com.blueair.android:id/nav_view"

    def tap_log_out(self):
        try:
            log_out_element = self.locate_element(self.log_out)
            self.tap_element(log_out_element)
            log_out_confirm_element = self.locate_element(self.log_out_confirm)
            self.tap_element(log_out_confirm_element)
        except exceptions.TimeoutException:
            return False

    def close_side_menu(self):
        try:
            close_hamburger_menu_element = self.locate_element(self.close)
            self.tap_element(close_hamburger_menu_element)
        except exceptions.TimeoutException:
            return False
