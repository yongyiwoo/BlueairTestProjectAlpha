from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions
from appium import webdriver
import page_object.main_page
import time
import random

class SideMenuPages(BasePage):
    def __init__(self, common_driver):
        super(SideMenuPages, self).__init__(common_driver)
        self.blueair_logo = (MobileBy.ID, "com.blueair.android:id/blueair_icon_dot")
        self.blueair_title = (MobileBy.ID, "com.blueair.android:id/blueair_icon")

        self.close = (MobileBy.ID, "com.blueair.android:id/drawer_close_view")
        self.log_out = self.sign_in = (MobileBy.ID, "com.blueair.android:id/signin")

        self.log_out_confirm = (MobileBy.ID, "com.blueair.android:id/confirm_button")
        self.log_out_dismiss = (MobileBy.ID, "com.blueair.android:id/dismiss_button")
        # the elements in the side menu don't have IDs
        # may use resource id "com.blueair.android:id/design_menu_item_text"
        self.side_menu_list = (MobileBy.ID, "com.blueair.android:id/design_menu_item_text")
        self.touchable_area = (MobileBy.ID, "com.blueair.android:id/drawerLayout")
        self.side_menu_area = (MobileBy.ID, "com.blueair.android:id/drawer_relative_layout")

        self.air_quality_map = (MobileBy.ID, "com.blueair.android:id/map_container")
        self.blueair_store = self.support = self.policies = (MobileBy.ID, "com.blueair.android:id/web_container")
        self.voice_assistants = (MobileBy.ID, "com.blueair.android:id/info_container")

        self.app_version = (MobileBy.ID, "com.blueair.android:id/build")

    def check_blueair_logo_appears(self):
        """
        check if the logo appears
        :return: True, if appears, False, if disappears
        """
        try:
            blueair_logo_element = self.locate_element(self.blueair_logo)
            if type(blueair_logo_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_blueair_title_appears(self):
        """
        check if the title appears
        :return: True, if appears, False, if disappears
        """
        try:
            blueair_title_element = self.locate_element(self.blueair_title)
            if type(blueair_title_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_side_menu_appears(self):
        """
        check if the side menu appears
        :return: True, if appears, False, if disappears
        """
        try:
            side_menu_element = self.locate_element(self.side_menu_area)
            if type(side_menu_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_air_quality_map_appears(self):
        """
        check if the air quality map appears
        :return: True, if appears, False, if disappears
        """
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Air Quality Map":
                    return True
            return False
        except exceptions.TimeoutException:
            return False

    def tap_air_quality_map(self):
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Air Quality Map":
                    self.tap_element(side_menu_section_element)
                    break
        except exceptions.TimeoutException:
            return False

    def check_air_quality_map_page_appears(self):
        """
        This method should be in another page, but combine it with the side menu page
        :return:
        """
        try:
            air_quality_map_element = self.locate_element(self.air_quality_map, waiting_time=20)
            if type(air_quality_map_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_blueair_store_appears(self):
        """
        check if the profile appears
        :return: True, if appears, False, if disappears
        """
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Blueair Store":
                    return True
            return False
        except exceptions.TimeoutException:
            return False

    def tap_blueair_store(self):
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Blueair Store":
                    self.tap_element(side_menu_section_element)
                    break
        except exceptions.TimeoutException:
            return False

    def check_blueair_store_page_appears(self):
        """
        This method should be in another page, but combine it with the side menu page
        :return:
        """
        try:
            air_quality_map_element = self.locate_element(self.blueair_store, waiting_time=20)
            if type(air_quality_map_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_profile_appears(self):
        """
        check if the profile appears
        :return: True, if appears, False, if disappears
        """
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Profile":
                    return True
            return False
        except exceptions.TimeoutException:
            return False

    def tap_profile(self):
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Profile":
                    self.tap_element(side_menu_section_element)
                    break
        except exceptions.TimeoutException:
            return False

    def check_settings_appears(self):
        """
        check if the settings appears
        :return: True, if appears, False, if disappears
        """
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Settings":
                    return True
            return False
        except exceptions.TimeoutException:
            return False

    def tap_settings(self):
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Settings":
                    self.tap_element(side_menu_section_element)
                    break
        except exceptions.TimeoutException:
            return False

    def check_voice_assistants_appears(self):
        """
        check if the voice assistants appears
        :return: True, if appears, False, if disappears
        """
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Voice Assistants":
                    return True
            return False
        except exceptions.TimeoutException:
            return False

    def tap_voice_assistants(self):
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Voice Assistants":
                    self.tap_element(side_menu_section_element)
                    break
        except exceptions.TimeoutException:
            return False

    def check_voice_assistants_page_appears(self):
        """
        This method should be in another page, but combine it with the side menu page
        :return:
        """
        try:
            voice_assistants_element = self.locate_element(self.voice_assistants)
            if type(voice_assistants_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_support_appears(self):
        """
        check if the support appears
        :return: True, if appears, False, if disappears
        """
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Support":
                    return True
            return False
        except exceptions.TimeoutException:
            return False

    def tap_support(self):
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Support":
                    self.tap_element(side_menu_section_element)
                    break
        except exceptions.TimeoutException:
            return False

    def check_support_page_appears(self):
        """
        This method should be in another page, but combine it with the side menu page
        :return:
        """
        try:
            support_element = self.locate_element(self.support)
            if type(support_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_policies_appears(self):
        """
        check if the policies appears
        :return: True, if appears, False, if disappears
        """
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Policies":
                    return True
            return False
        except exceptions.TimeoutException:
            return False

    def tap_policies(self):
        try:
            side_menu_list_elements = self.locate_element_list(self.side_menu_list)
            for side_menu_section_element in side_menu_list_elements:
                side_menu_section_text = self.get_element_attribute(side_menu_section_element, "text")
                if side_menu_section_text == "Policies":
                    self.tap_element(side_menu_section_element)
                    break
        except exceptions.TimeoutException:
            return False

    def check_policies_page_appears(self):
        """
        This method should be in another page, but combine it with the side menu page
        :return:
        """
        try:
            policies_element = self.locate_element(self.policies)
            if type(policies_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_log_out_appears(self):
        """
        check if the log out appears
        :return: True, if appears, False, if disappears
        """
        try:
            log_out_element = self.locate_element(self.log_out)
            log_out_element_text = self.get_element_attribute(log_out_element, "text")
            if log_out_element_text == "Log out":
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_sign_in_appears(self):
        """
        check if the sign in appears
        :return: True, if appears, False, if disappears
        """
        try:
            sign_in_element = self.locate_element(self.sign_in)
            sign_in_element_text = self.get_element_attribute(sign_in_element, "text")
            if sign_in_element_text == "Sign in":
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def tap_log_out(self, confirm: bool):
        try:
            log_out_element = self.locate_element(self.log_out)
            self.tap_element(log_out_element)
            if confirm:
                log_out_confirm_element = self.locate_element(self.log_out_confirm)
                self.tap_element(log_out_confirm_element)
            else:
                log_out_dismiss_element = self.locate_element(self.log_out_dismiss)
                self.tap_element(log_out_dismiss_element)
        except exceptions.TimeoutException:
            return False

    def tap_sign_in(self):
        try:
            sign_in_element = self.locate_element(self.sign_in)
            self.tap_element(sign_in_element)
        except exceptions.TimeoutException:
            return False

    def check_app_version_appears(self):
        """
        check if the app version appears
        :return: True, if appears, False, if disappears
        """
        try:
            app_version_element = self.locate_element(self.app_version)
            if type(app_version_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def close_side_menu_use_close_button(self):
        try:
            close_side_menu_element = self.locate_element(self.close)
            self.tap_element(close_side_menu_element)
        except exceptions.TimeoutException:
            return False

    def close_side_menu_use_blank_space(self):
        """
        close the side menu by tapping other area
        :return:
        """
        try:
            side_menu_area_element = self.locate_element(self.side_menu_area)
            side_menu_area_element_coordinates = self.get_element_coordinates(side_menu_area_element)
            #print(side_menu_area_element_coordinates)
            touchable_area_element = self.locate_element(self.touchable_area)
            touchable_area_element_coordinates = self.get_element_coordinates(touchable_area_element)
            #print(touchable_area_element_coordinates)

            # calculate the x-axis, y-axis out of the side menu area
            x_axis_start_coordinate = side_menu_area_element_coordinates["width"] + 1
            x_axis_end_coordinate = touchable_area_element_coordinates["width"]
            y_axis_start_coordinate = side_menu_area_element_coordinates["y"] + 1
            y_axis_end_coordinate = touchable_area_element_coordinates["height"]

            touch_x_axis = random.randint(x_axis_start_coordinate, x_axis_end_coordinate)
            #print("touch_x_axis: " + str(touch_x_axis))
            touch_y_axis = random.randint(y_axis_start_coordinate, y_axis_end_coordinate)
            #print("touch_y_axis: " + str(touch_y_axis))

            self.tap_element(x=touch_x_axis,y=touch_y_axis)

        except exceptions.TimeoutException:
            return False
