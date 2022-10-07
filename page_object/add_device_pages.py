from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
import page_object.main_page
from selenium.common import exceptions
import re

class AddDevicePages(BasePage):
    def __init__(self, common_driver):
        super(AddDevicePages, self).__init__(common_driver)

    def add_device_process(self):
        pass

class AddDustmagnetPages(AddDevicePages):
    def __init__(self, common_driver):
        super(AddDevicePages, self).__init__(common_driver)
        self.device_name = (MobileBy.ID, "com.blueair.android:id/name")
        # need to be a model with some numbers
        self.device_model = (MobileBy.ID, "com.blueair.android:id/model")
        self.device_image = (MobileBy.ID, "com.blueair.android:id/device_img")
        # wifi_ssid_name: Yongyi
        self.wifi_ssid = (MobileBy.XPATH, "//android.widget.TextView[@text=" + "\"Yongyi\"" + "]")
        self.wifi_password = (MobileBy.ID, "com.blueair.android:id/editText")
        # self.password_visible = (MobileBy.ID, "com.blueair.android:id/text_input_end_icon")
        self.password_submit = (MobileBy.ID, "com.blueair.android:id/buttonNext")
        # should show text "Incorrect password"
        self.password_error = (MobileBy.ID, "com.blueair.android:id/textinput_error")
        self.custom_name = (MobileBy.ID, "com.blueair.android:id/customer_purifier_name_layout")
        self.input_name = (MobileBy.ID, "com.blueair.android:id/editText")
        self.save_name = (MobileBy.ID, "com.blueair.android:id/ok_view")
        # need to check the cancel button UI overlap issue
        self.cancel_name = (MobileBy.ID, "com.blueair.android:id/cancel_view")
        self.next_done = (MobileBy.ID, "com.blueair.android:id/buttonDone")

    def add_device_process(self):
        # get the device name text: "DustMagnet"
        try:
            device_name_element = self.locate_element(self.device_name)
            device_name_text = self.get_element_attribute(device_name_element, "text")
            if device_name_text == "DustMagnet":
                device_name_text_result = True
            else:
                device_name_text_result = False
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.add_device_process.__name__ + "_device_name")
            device_name_text_result = None

        try:
            device_model_element = self.locate_element(self.device_model)
            device_model_text = self.get_element_attribute(device_model_element, "text")
            device_model_text_match = re.match("DustMagnet 5[0-9]{3}i", device_model_text)
            if device_model_text_match:
                device_model_text_result = True
            else:
                device_model_text_result = False
            # navigate to "connect to wifi" page
            self.tap_element(device_model_element)
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.add_device_process.__name__ + "_device_model")
            device_model_text_result = None

        try:
            device_image_element = self.locate_element(self.device_image)
            device_image_bin = self.get_screenshotpng()
            print(device_image_bin)
            device_image_base64 = self.get_screenshot_base64(device_image_element)
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.add_device_process.__name__ + "_device_image")


        while True:
            try:
                wifi_ssid_element = self.locate_element(self.wifi_ssid, waiting_time=30)

                # navigate to "enter wifi password" page
                self.tap_element(wifi_ssid_element)
                break
            except exceptions.TimeoutException:
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)

        try:
            wifi_password_element = self.locate_element(self.wifi_password)
            # wifi_ssid_password: 28116194
            self.set_element_text(wifi_password_element, "28116194")

            # navigate to "enter wifi password" page
            password_submit_element = self.locate_element(self.password_submit)
            self.tap_element(password_submit_element)
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.add_device_process.__name__ + "_wifi")

        try:
            custom_name_element = self.locate_element(self.custom_name, waiting_time=60)
            self.tap_element(custom_name_element)
            input_name_element = self.locate_element(self.input_name)
            self.set_element_text(input_name_element, "b4_5410i")   # hardcoded name, can change it later
            save_name_element = self.locate_element(self.save_name)
            self.tap_element(save_name_element)
            next_done_element = self.locate_element(self.next_done)
            self.tap_element(next_done_element)
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.add_device_process.__name__ + "_custom_name")
        try:
            # use page_object.main_page.MainPage because of circular import
            main_page_device_list = page_object.main_page.MainPage(self.driver)
            added_device = main_page_device_list.get_devices_info(device="b4_5410i", attr="device_name", scroll="yes",waiting_time=60)

            if added_device:
                added_device_result = True
            else:
                added_device_result = False
        except exceptions.TimeoutException:
            added_device_result = None

        return device_name_text_result, device_model_text_result, added_device_result
