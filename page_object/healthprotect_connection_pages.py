from appium.webdriver.common.mobileby import MobileBy
from page_object.device_connection_pages import DeviceConnectionPages
from selenium.common import exceptions
import page_object.main_page
import time

class HealthProtectConnectionPages(DeviceConnectionPages):
    def __init__(self, common_driver):
        super(HealthProtectConnectionPages, self).__init__(common_driver)
        # device_name should be "HealthProtect"
        self.device_name = (MobileBy.ID, "com.blueair.android:id/name")
        # device_model should be "HealthProtect 7410i", "HealthProtect 7440i", "HealthProtect 7470i"
        self.device_model = (MobileBy.ID, "com.blueair.android:id/model")
        # need to return device_image to compare
        self.device_image = (MobileBy.ID, "com.blueair.android:id/device_img")
        # hard coded wifi_ssid_name: Yongyi
        self.wifi_ssid = (MobileBy.XPATH, "//android.widget.TextView[@text=" + "\"Yongyi\"" + "]")
        self.wifi_password = (MobileBy.ID, "com.blueair.android:id/editText")
        # self.password_visible = (MobileBy.ID, "com.blueair.android:id/text_input_end_icon")
        self.password_submit = (MobileBy.ID, "com.blueair.android:id/buttonNext")
        # should be text "Incorrect password"
        self.password_error = (MobileBy.ID, "com.blueair.android:id/textinput_error")
        self.custom_name = (MobileBy.ID, "com.blueair.android:id/customer_purifier_name_layout")
        self.input_name = (MobileBy.ID, "com.blueair.android:id/editText")
        self.save_name = (MobileBy.ID, "com.blueair.android:id/ok_view")
        # need to check the cancel button UI overlap issue
        self.cancel_name = (MobileBy.ID, "com.blueair.android:id/cancel_view")
        self.next_done = (MobileBy.ID, "com.blueair.android:id/buttonDone")
        self.retry_process = (MobileBy.ID, "com.blueair.android:id/button_restart")

    def tap_device_model(self):
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
                    screenshot_base64 = self.get_screenshot64()
                    self.save_image(screenshot_base64, self.tap_device_model.__name__ + "_model_name")
                    model_info[str(n)] = "Error"

                if model_name == "HealthProtect" or model_name == "DustMagnet":
                    try:
                        model_xpath_image_element = self.locate_element(model_xpath_image_info)
                        model_xpath_image_coordinates = self.get_element_coordinates(model_xpath_image_element)
                        screenshot_base64 = self.get_screenshot64()
                        model_image = self.crop_screenshot(screenshot_base64, model_xpath_image_coordinates)
                        model_info[model_name + "_image"] = model_image
                    except exceptions.TimeoutException:
                        screenshot_base64 = self.get_screenshot64()
                        self.save_image(screenshot_base64, self.tap_device_model.__name__ + "_model_image")
                        model_info[model_name + "_image"] = None

                # format: {"model_name": {"model_name": model_xpath_name_element, "model_name_image": model_image}}
                model_list[model_name] = model_info
                #print(model_list)
            # find out the "HealthProtect" device layout by device name
            model_element = model_list.get("HealthProtect", "No Such Device").get("HealthProtect")
            #print(model_element)
            if model_element != "No Such Device":
                self.tap_element(model_element)

            return model_list["HealthProtect"]

    def find_device_page(self):
        try:
            device_name_element = self.locate_element(self.device_name, waiting_time=10)
            device_name_text = self.get_element_attribute(device_name_element, "text")

            device_model_element = self.locate_element(self.device_model)
            device_model_text = self.get_element_attribute(device_model_element, "text")

            device_image_element = self.locate_element(self.device_image)
            device_image_coordinates = self.get_element_coordinates(device_image_element)
            screenshot_base64 = self.get_screenshot64()
            device_image_array = self.crop_screenshot(screenshot_base64, device_image_coordinates)

            # navigate to "connect to wifi" page
            self.tap_element(device_model_element)
            #print(device_name_text, device_model_text, device_image_array)
            return device_name_text, device_model_text, device_image_array
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot64()
            self.save_image(screenshot_base64, self.find_device_page.__name__)
            return None, None, None

    def connect_wifi_page(self, password: str, sleep_time=0):
        # if there are too many wifi around, try to find the correct one no more than 5 times by swiping up
        for _ in range(6):
            try:
                wifi_ssid_element = self.locate_element(self.wifi_ssid, waiting_time=30)

                # navigate to "enter wifi password" page
                self.tap_element(wifi_ssid_element)
                break
            except exceptions.TimeoutException:
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
        # set the sleep time to wait before input the wifi password, default is 0
        time.sleep(sleep_time)
        try:
            wifi_password_element = self.locate_element(self.wifi_password)
            self.set_element_text(wifi_password_element, password)
            # navigate to "enter wifi password" page
            password_submit_element = self.locate_element(self.password_submit)
            self.tap_element(password_submit_element)
            password_error_element = self.locate_element(self.password_error, waiting_time=10)
            return password_error_element
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot64()
            self.save_image(screenshot_base64, self.connect_wifi_page.__name__)
            password_error_element = None
            return password_error_element

    def name_device_page(self, name):
        try:
            custom_name_element = self.locate_element(self.custom_name, waiting_time=60)
            self.tap_element(custom_name_element)
            input_name_element = self.locate_element(self.input_name)
            self.set_element_text(input_name_element, name)
            save_name_element = self.locate_element(self.save_name)
            self.tap_element(save_name_element)
            next_done_element = self.locate_element(self.next_done)
            self.tap_element(next_done_element)
            return
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot64()
            self.save_image(screenshot_base64, self.name_device_page.__name__)
            retry_process_element = self.locate_element(self.retry_process, waiting_time=60)
            self.tap_element(retry_process_element)
            self.navigate_back(2)
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
