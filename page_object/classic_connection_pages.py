from appium.webdriver.common.mobileby import MobileBy
from page_object.device_connection_pages import DeviceConnectionPages
from selenium.common import exceptions
from util.servo_control import ServoControl
import page_object.main_page
import time

class ClassicConnectionPages(DeviceConnectionPages):
    def __init__(self, common_driver):
        super(ClassicConnectionPages, self).__init__(common_driver)

        # connect my device next/active device wifi next/connect to network next/name your device next/setup done next
        self.next_page = (MobileBy.ID, "com.blueair.android:id/buttonNext")
        # self.wifi_ssid = (MobileBy.ID, "com.blueair.android:id/editTextSSID")
        self.wifi_password = (MobileBy.ID, "com.blueair.android:id/editTextPassword")
        self.input_name = (MobileBy.ID, "com.blueair.android:id/editTextDeviceName")


    def tap_device_name(self):
        """
        tap the device model: "HealthProtect", "DustMagnet", "Classic", "Sense+", "Aware", "Cabin Air P2i"
        :return: model with name and image (if possible)
        """
        model_list = {}
        model_name = ""
        try:
            # get the number of model from list (based on different regions, model list will be different)
            xpath_elements = self.locate_element_list(self.model_list)
            model_number = len(xpath_elements)
        except exceptions.TimeoutException:
            return model_list
        else:
            # iterate through different models
            for n in range(1, model_number + 1):
                model_info = {}
                # for saving each device info
                model_xpath_base_string = self.model_list[1] + "[" + str(n) + "]"
                model_xpath_extend_string = "/android.widget.TextView"
                # device image string
                model_xpath_extend_string2 = "/android.widget.ImageView"

                # get model name
                model_xpath_name_string = model_xpath_base_string + model_xpath_extend_string
                model_xpath_name_info = (MobileBy.XPATH, model_xpath_name_string)
                # get model image
                model_xpath_image_string = model_xpath_base_string + model_xpath_extend_string2
                model_xpath_image_info = (MobileBy.XPATH, model_xpath_image_string)

                try:
                    model_xpath_name_element = self.locate_element(model_xpath_name_info)
                    model_name = self.get_element_attribute(model_xpath_name_element, "text")
                    model_info[model_name] = model_xpath_name_element
                except exceptions.TimeoutException:
                    screenshot_base64 = self.get_screenshot_base64()
                    self.save_image(screenshot_base64, self.tap_device_name.__name__ + "_model_name")
                    model_info[str(n)] = "Error"

                if model_name == "HealthProtect" or model_name == "DustMagnet":
                    try:
                        model_xpath_image_element = self.locate_element(model_xpath_image_info)
                        model_xpath_image_coordinates = self.get_element_coordinates(model_xpath_image_element)
                        screenshot_base64 = self.get_screenshot_base64()
                        model_image = self.crop_screenshot_and_compress_as_string(screenshot_base64, model_xpath_image_coordinates)
                        model_info[model_name + "_image"] = model_image
                    except exceptions.TimeoutException:
                        screenshot_base64 = self.get_screenshot_base64()
                        self.save_image(screenshot_base64, self.tap_device_name.__name__ + "_model_image")
                        model_info[model_name + "_image"] = None

                # format: {"model_name": {"model_name": model_xpath_name_element, "model_name_image": model_image}}
                model_list[model_name] = model_info
                #print(model_list)
            # find out the "HealthProtect" device layout by device name
            model_element = model_list.get("Classic", "No Such Device").get("Classic")
            #print(model_element)
            if model_element != "No Such Device":
                self.tap_element(model_element)

            return model_list["Classic"]

    def find_device_page(self):
        try:
            next_page_element = self.locate_element(self.next_page)
            # navigate to "active wifi" page
            self.tap_element(next_page_element)
            # navigate to "connect to network" page
            # need to wait a second
            time.sleep(1)
            self.tap_element(next_page_element)
            return True
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.find_device_page.__name__)
            return None

    def connect_wifi_page(self, password: str, sleep_time=0):
        time.sleep(sleep_time)
        servo_byte_string = ServoControl.servo_control("192.168.1.101", 65000, b"3SPRS")
        print(servo_byte_string)
        if servo_byte_string == b'3 seconds press done\n':
            try:
                wifi_password_element = self.locate_element(self.wifi_password)
                self.set_element_text(wifi_password_element, password)
                # navigate to "enter wifi password" page
                next_page_element = self.locate_element(self.next_page)
                self.tap_element(next_page_element)
                return
            except exceptions.TimeoutException:
                screenshot_base64 = self.get_screenshot_base64()
                self.save_image(screenshot_base64, self.connect_wifi_page.__name__)
                return

    def name_device_page(self, name):
        # need to wait couple of seconds, dont know why the waiting_time=60 doesnt work
        #time.sleep(30)
        try:
            input_name_element = self.locate_element(self.input_name, waiting_time=120)
            self.set_element_text(input_name_element, name)
            next_page_element = self.locate_element(self.next_page)
            # navigate to "setup complete" page
            self.tap_element(next_page_element)
            # need to wait couple of seconds
            time.sleep(5)
            # navigate to main page
            self.tap_element(next_page_element)
            return
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.name_device_page.__name__)
            return

    def finalize_device_page(self, name):
        try:
            # use page_object.main_page.MainPage because of circular import
            main_page_device_list = page_object.main_page.MainPage(self.driver)
            added_device = main_page_device_list.get_devices_info(device=name, attr="device_name", scroll="yes",waiting_time=60)
            return added_device
        except exceptions.TimeoutException:
            added_device = None
            return added_device
