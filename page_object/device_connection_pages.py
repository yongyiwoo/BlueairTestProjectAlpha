from appium.webdriver.common.mobileby import MobileBy
from selenium.common import exceptions
from page_object.base_page import BasePage
from appium import webdriver


# constants from image to base64 string, more details check crop_screenshot() method in base_page.py
# constant string for HealthProtect/Protect image in Blueair products page
HEALTHPROTECT = "/wAA////AAAA////AAAA////AAAA////AAAA////AAAA//8AAAAA//8AAAAA//8AAAAA//8AAAAA//8AAAAA//8A/wAAAP//"
# constant string for Dustmagnet image in Blueair products page
DUSTMAGNET = "AAAAAAD/AAAAAP8AAAAA//8AAAAA//8AAAAA//8AAAAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP8A//8A//8A////"
# constant string for Classic image in Blueair products page
CLASSIC = "AAAAAAAA////////////////////////////////////////////////////////////////////////////////////////"
# constant string for Sense+ image in Blueair products page
SENSEPLUS = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
# constant string for Aware image in Blueair products page
AWARE = "////////////////AP////8A//////8AAP////8AAP////8AAP////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAAAAAA"
# constant string for Cabin Air P2i image in Blueair products page
P2I = "AAAAAAD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAAAAAAAAAAAAAA/wAAAAAA/wAAAAAA/wAAAAAA/wAAAAAA/wAAAAAA"


class DeviceConnectionPages(BasePage):
    def __init__(self, common_driver):
        super(DeviceConnectionPages, self).__init__(common_driver)
        self.all_device_name_list = (MobileBy.ID, "com.blueair.android:id/model_name")
        self.all_device_image_list = (MobileBy.ID, "com.blueair.android:id/model_image")
        self.select_device_page_tile = (MobileBy.ID, "com.blueair.android:id/add_device_appbar")
        self.select_device_page_close = (MobileBy.ID, "com.blueair.android:id/add_device_close")
        # for healthprotect and dustmagnet need to give permissions of location and nearby devices
        # some elements may need to be added later

    def tap_device_name(self, device_model: str):
        """
        tap the device name
        :param device_model: "HealthProtect/Protect", "DustMagnet", "Classic", "Sense+", "Aware" or "Cabin Air P2i"
        :return: True, if select the model; None, if error
        """
        # when having a small screen phone, the products at the bottom of the list may not be seen
        # extra scroll up the screen may be needed
        for _ in range(2):
            try:
                # get models from the list (based on different regions, model list will be different)
                device_name_list_elements = self.locate_element_list(self.all_device_name_list)
                # iterate to find the air purifier
                for device_name_list_element in device_name_list_elements:
                    device_name_text = self.get_element_attribute(device_name_list_element, "text")
                    if device_name_text == device_model:
                        self.tap_element(device_name_list_element)
                        return True
            except exceptions.TimeoutException:
                # swipe up the screen
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((25, 25))
                self.scroll_screen(start_position_percent, end_position_percent)
        return False

    def check_device_image(self, device_name: str):
        """
        check the device image in Blueair products page, compare with the stored bas64 image string
        more details check crop_screenshot() method in base_page.py
        :param device_name: "HealthProtect/Protect", "DustMagnet", "Classic", "Sense+", "Aware", "Cabin Air P2i"
        :return:
        """
        try:
            # get the whole image of the product by scroll up the screen
            for _ in range(2):
                device_image_index = None
                # get models from the list (based on different regions, model list will be different)
                device_name_list_elements = self.locate_element_list(self.all_device_name_list)
                # iterate to find the air purifier
                for device_name_list_element in device_name_list_elements:
                    device_name_text = self.get_element_attribute(device_name_list_element, "text")
                    if device_name_text == device_name:
                        device_image_index = device_name_list_elements.index(device_name_list_element)
                        break
                #print(device_image_index)

                if device_image_index is not None:
                    device_image_list_elements = self.locate_element_list(self.all_device_image_list)
                    #for model_image_list_element in model_image_list_elements:
                    device_image_element_coordinates = self.get_element_coordinates(device_image_list_elements[device_image_index])
                    width = device_image_element_coordinates["width"]
                    height = device_image_element_coordinates["height"]
                    # the image height:width ratio is not correct, scroll up the screen
                    if (width / height) > 1.1:
                        start_position_percent = self.set_position_on_screen((75, 75))
                        end_position_percent = self.set_position_on_screen((25, 25))
                        self.scroll_screen(start_position_percent, end_position_percent)
                    else:
                        device_image_base64_string = self.crop_screenshot_and_compress_as_string(self.get_screenshot_base64(), device_image_element_coordinates)
                        #print("device_image_base64_string: " + device_image_base64_string)
                        if device_name == "HealthProtect" or device_name == "Protect":
                            if device_image_base64_string == HEALTHPROTECT:
                                return True
                            else:
                                return False
                        elif device_name == "DustMagnet":
                            if device_image_base64_string == DUSTMAGNET:
                                return True
                            else:
                                return False
                        elif device_name == "Classic":
                            if device_image_base64_string == CLASSIC:
                                return True
                            else:
                                return False
                        elif device_name == "Sense+":
                            if device_image_base64_string == SENSEPLUS:
                                return True
                            else:
                                return False
                        elif device_name == "Aware":
                            if device_image_base64_string == AWARE:
                                return True
                            else:
                                return False
                        elif device_name == "Cabin Air P2i":
                            if device_image_base64_string == P2I:
                                return True
                            else:
                                return False
                        else:
                            return False
            return False
        except exceptions.TimeoutException:
            return False

    def check_select_device_page_appears(self):
        """
        check if the device connection page appear
        :return: True, if the page appears
        """
        try:
            device_connection_page_title_element = self.locate_element(self.select_device_page_tile)
            if type(device_connection_page_title_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def close_select_device_page(self):
        """
        because the system navigate back doesn't work on device connection page, so have to use this close button
        :return:
        """
        try:
            close_device_connection_page_element = self.locate_element(self.select_device_page_close)
            print("close device connection page")
            self.tap_element(close_device_connection_page_element)
        except exceptions.TimeoutException:
            return False
