from appium.webdriver.common.mobileby import MobileBy
from page_object.device_connection_pages import DeviceConnectionPages
from selenium.common import exceptions
import page_object.main_page
import time

class DustMagnetConnectionPages(DeviceConnectionPages):
    def __init__(self, common_driver):
        super(DustMagnetConnectionPages, self).__init__(common_driver)
        # device_name should be "DustMagnet"
        # self.device_name = (MobileBy.ID, "com.blueair.android:id/name")
        # device_model may be "DustMagnet 5410i", "DustMagnet 5210i", "DustMagnet 5440i", "DustMagnet 5240i"
        self.device_model = (MobileBy.ID, "com.blueair.android:id/model")
        # need to return device_image to compare
        # self.device_image = (MobileBy.ID, "com.blueair.android:id/device_img")
        self.wifi_ssid = (MobileBy.ID, "com.blueair.android:id/ssidName")
        self.wifi_password = (MobileBy.ID, "com.blueair.android:id/editText")
        # self.password_visible = (MobileBy.ID, "com.blueair.android:id/text_input_end_icon")
        self.password_submit = (MobileBy.ID, "com.blueair.android:id/buttonNext")
        # should be text "Incorrect password"
        self.password_error = (MobileBy.ID, "com.blueair.android:id/textinput_error")
        self.custom_name = (MobileBy.ID, "com.blueair.android:id/customer_purifier_name_layout")
        self.input_name = (MobileBy.ID, "com.blueair.android:id/editText")
        self.save_name = (MobileBy.ID, "com.blueair.android:id/ok_view")
        # need to check the cancel button UI overlap issue
        # self.cancel_name = (MobileBy.ID, "com.blueair.android:id/cancel_view")
        self.next_done = (MobileBy.ID, "com.blueair.android:id/buttonDone")
        #self.retry_process = (MobileBy.ID, "com.blueair.android:id/button_restart")

    def tap_device_model(self):
        """
        tap the device model: "HealthProtect", "DustMagnet", "Classic", "Sense+", "Aware", "Cabin Air P2i"
        :return: True, if select the model; None, if error
        """
        counter = 0
        while True:
            try:
                # get models from the list (based on different regions, model list will be different)
                model_name_list_elements = self.locate_element_list(self.model_name_list)
                # iterate to find the air purifier
                for model_name_list_element in model_name_list_elements:
                    model_name_text = self.get_element_attribute(model_name_list_element, "text")
                    if model_name_text == "DustMagnet":
                        self.tap_element(model_name_list_element)
                        return True
            except exceptions.TimeoutException:
                # swipe up the screen
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
            # to stop the loop in 3 times
            counter += 1
            if counter > 2:
                break
            # print("Class: {} method: {} has an error".format(self.__class__.__name__, self.tap_device_model.__name__))
            return None

    def find_device_page(self):
        """
        Tap the device needs to be connected
        :return: the device model name
        """
        try:
            #device_name_element = self.locate_element(self.device_name, waiting_time=10)
            #device_name_text = self.get_element_attribute(device_name_element, "text")

            #device_image_element = self.locate_element(self.device_image)
            #device_image_coordinates = self.get_element_coordinates(device_image_element)
            #screenshot_base64 = self.get_screenshot64()
            #device_image_array = self.crop_screenshot(screenshot_base64, device_image_coordinates)

            device_model_element = self.locate_element(self.device_model)
            device_model_text = self.get_element_attribute(device_model_element, "text")
            # navigate to "connect to wifi" page
            self.tap_element(device_model_element)
            return device_model_text #device_name_text, device_image_array
        except exceptions.TimeoutException:
            #print("Class: {} method: {} has an error".format(self.__class__.__name__, self.find_device_page.__name__))
            return None

    def connect_wifi_page(self, ssid: str, password: str, sleep_time=0):
        """
        select the WIFI based on the SSID, input the password
        :param ssid: the WIFI ssid
        :param password: the WIFI password
        :param sleep_time: wait time before input the password
        :return: True, if success; None, if fail; Error password message, if the password is wrong
        """
        # if there are too many wifi around, try to find the correct one no more than 5 times by swiping up
        counter = 0
        while True:
            try:
                wifi_ssid_elements = self.locate_element_list(self.wifi_ssid, waiting_time=30)
                for wifi_ssid_element in wifi_ssid_elements:
                    wifi_ssid_text = self.get_element_attribute(wifi_ssid_element, "text")
                    if wifi_ssid_text == ssid:
                        # navigate to "enter wifi password" page
                        self.tap_element(wifi_ssid_element)
                        break
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
            except exceptions.TimeoutException:
            # print("Class: {} method: {} step 1 has an error".format(self.__class__.__name__, self.connect_wifi_page.__name__))
                break
            # to stop the loop in 5 times
            counter += 1
            if counter > 4:
                # print("Class: {} method: {} step 1 has an error".format(self.__class__.__name__, self.connect_wifi_page.__name__))
                break
        # set the sleep time to wait before input the wifi password, default is 0
        time.sleep(sleep_time)
        try:
            wifi_password_element = self.locate_element(self.wifi_password)
            self.set_element_text(wifi_password_element, password)
            # navigate to "enter wifi password" page
            password_submit_element = self.locate_element(self.password_submit)
            self.tap_element(password_submit_element)
            try:
                password_error_element = self.locate_element(self.password_error, waiting_time=10)
                password_error_text = self.get_element_attribute(password_error_element, "text")
                return password_error_text # "Incorrect password"
            except exceptions.TimeoutException:
                pass
            return True
        except exceptions.TimeoutException:
            #print("Class: {} method: {} step 2 has an error".format(self.__class__.__name__, self.connect_wifi_page.__name__))
            return None

    def name_device_page(self, name):
        """
        input the device name
        :param name: device name
        :return: True, if success; False, if fail
        """
        try:
            custom_name_element = self.locate_element(self.custom_name, waiting_time=60)
            self.tap_element(custom_name_element)
            input_name_element = self.locate_element(self.input_name)
            self.set_element_text(input_name_element, name, hide_kb=False)
            save_name_element = self.locate_element(self.save_name)
            self.tap_element(save_name_element)
            next_done_element = self.locate_element(self.next_done)
            self.tap_element(next_done_element)
            return True
        except exceptions.TimeoutException:
            # print("Class: {} method: {} has an error".format(self.__class__.__name__, self.name_device_page.__name__))
            #retry_process_element = self.locate_element(self.retry_process, waiting_time=60)
            #self.tap_element(retry_process_element)
            #self.navigate_back(2)
            return False

    def finalize_device_page(self, name):   # this method needs to move to the main_page
        """
        check if the onboarded device is in device list
        :param name: the onboarded device name
        :return: the device name, if success, None, if fail
        """
        try:
            # use page_object.main_page.MainPage because of circular import
            main_page_device_list = page_object.main_page.MainPage(self.driver)
            added_device = main_page_device_list.get_devices_info(device=name, attr="device_name", scroll="yes",waiting_time=60)
            return added_device
        except exceptions.TimeoutException:
            # print("Class: {} method: {} has an error".format(self.__class__.__name__, self.finalize_device_page.__name__))
            return None
