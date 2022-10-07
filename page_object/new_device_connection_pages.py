from appium.webdriver.common.mobileby import MobileBy
from page_object.device_connection_pages import DeviceConnectionPages
from selenium.common import exceptions
from appium import webdriver
import page_object.main_page
import time


# constants from image to base64 string, more details check crop_screenshot() method in base_page.py
# the base64 string may vary according to phone font and display size
# below strings use font size large, display size large

# constant string for HealthProtect/Protect image in Find your Device page
# HEALTHPROTECT = "/wAA////AAAA////AAAA////AAAA////AAAA////AAAA//8AAAAA//8AAAAA//8AAAAA//8AAAAA//8AAAAA//8A/wAAAP//"

# below test scroll up screen sample
# HEALTHPROTECT = "/wAA////AAD/////AAAA////AAAA////AAAA////AAAA//8AAAAA//8AAAAA//8AAAAA//8AAAAA//8AAAAA//8A/wAAAP//"

# constant string for Dustmagnet image in Find your Device page
DUSTMAGNET = "AAAAAAD/AAAAAP8AAAAA//8AAAAA//8AAAAA//8AAAAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP8A//8A//8A////"


class NewDeviceConnectionPages(DeviceConnectionPages):
    def __init__(self, common_driver):
        super(NewDeviceConnectionPages, self).__init__(common_driver)
        # device info block (display device all info together in a block area)
        self.new_device_block_list = (MobileBy.ID, "com.blueair.android:id/root")

        # device_name should be "HealthProtect", "DustMagnet"
        self.new_device_name_list = (MobileBy.ID, "com.blueair.android:id/name")

        # device_model should be "HealthProtect 7xxxi", "DustMagnet 5xxxi"
        self.new_device_model_list = (MobileBy.ID, "com.blueair.android:id/model")

        # need to return device_image to compare
        self.new_device_image_list = (MobileBy.ID, "com.blueair.android:id/device_img")

        # mac address related
        self.mac_title_list = (MobileBy.ID, "com.blueair.android:id/mac_number_title")
        self.mac_hint_list = (MobileBy.ID, "com.blueair.android:id/question_mark")
        self.mac_address_list = (MobileBy.ID, "com.blueair.android:id/mac_number")

        # connected status
        self.connected_label_list = (MobileBy.ID, "com.blueair.android:id/connected_label") # Available, Connecting..., Connected to app
        self.connected_name_list = (MobileBy.ID, "com.blueair.android:id/connected_name")
        # already connected related
        self.already_connected_message = (MobileBy.ID, "android:id/message") # "The device is already connected, you need to delete it before it can be onboarded again"
        self.already_connected_close = (MobileBy.ID, "android:id/button2")

        # searching product message
        self.search_message = (MobileBy.ID, "com.blueair.android:id/scanning_msg") # message should disappear when press to connect the product
        self.search_icon = (MobileBy.ID, "com.blueair.android:id/progressBar") # icon should disappear when press to connect the product

        # connection lost
        self.connection_lost_title = (MobileBy.ID, "com.blueair.android:id/dialog_title")
        self.connection_lost_message = (MobileBy.ID, "com.blueair.android:id/dialog_msg")
        self.connection_lost_close = (MobileBy.ID, "com.blueair.android:id/buttonTryAgainLater")

        # bluetooth
        self.bluetooth_enable_title = (MobileBy.ID, "com.blueair.android:id/enable_title")
        self.bluetooth_enable = (MobileBy.ID, "com.blueair.android:id/ble_enable_btn")
        self.bluetooth_enable_ok = (MobileBy.ID, "com.blueair.android:id/ok_view")
        self.bluetooth_enable_not_allow = (MobileBy.ID, "com.blueair.android:id/cannotallow_view")


        # WiFi ssid
        self.wifi_ssid_list = (MobileBy.ID, "com.blueair.android:id/ssidName")
        self.wifi_password = (MobileBy.ID, "com.blueair.android:id/editText")
        self.password_visible = (MobileBy.ID, "com.blueair.android:id/text_input_end_icon")
        self.password_submit = (MobileBy.ID, "com.blueair.android:id/buttonNext")
        # should be text "Incorrect password"
        self.password_error = (MobileBy.ID, "com.blueair.android:id/textinput_error")


        # Setting up your air purifier page
        # Connecting to WiFi network "your_wifi_network_name"
        self.connecting_to_wifi_network = (MobileBy.ID, "com.blueair.android:id/textViewHeading")
        # Adding air purifier to your account
        self.adding_device_to_account = (MobileBy.ID, "com.blueair.android:id/progressText")
        # Failed messages
        # Please try again following the troubleshooting steps
        self.connecting_failed_title = (MobileBy.ID, "com.blueair.android:id/failure_title")
        # Please contact Blueair customer support
        self.connecting_failed_message = (MobileBy.ID, "com.blueair.android:id/failure_msg")
        # retry button, it will navigate to Find your Device page
        self.retry_process = (MobileBy.ID, "com.blueair.android:id/button_restart")
        # WiFi troubleshooting button, it will open support page
        self.wifi_troubleshooting = (MobileBy.ID, "com.blueair.android:id/button_support")


        self.predefined_name_list = (MobileBy.ID, "com.blueair.android:id/customer_purifier_name")
        self.custom_name = (MobileBy.ID, "com.blueair.android:id/add_name_right")
        self.input_name = (MobileBy.ID, "com.blueair.android:id/editText")
        self.save_name = (MobileBy.ID, "com.blueair.android:id/ok_view")
        self.cancel_name = (MobileBy.ID, "com.blueair.android:id/cancel_view")
        self.next_done = (MobileBy.ID, "com.blueair.android:id/buttonDone")


    def locate_device_by_mac_address(self, device_mac_address: str):
        """
        in Find your Device page, locate the device by provided mac address
        :param device_mac_address: device mac address
        :return: the index of the device in the current UI page or False
        """
        for _ in range(10): # try to scroll up the screen 10 times, should be enough
            try:
                mac_address_index = None
                mac_address_list_elements = self.locate_element_list(self.mac_address_list, waiting_time=20)
                #print(mac_address_list_elements)
                for mac_address_list_element in mac_address_list_elements:
                    mac_address_text = self.get_element_attribute(mac_address_list_element, "text")
                    #print("mac_address_text: " + mac_address_text)
                    if mac_address_text == device_mac_address:
                        mac_address_index = mac_address_list_elements.index(mac_address_list_element)
                        break
                #print("mac_address_index: " + str(mac_address_index))
                if mac_address_index is not None:
                    return mac_address_index
                else:
                    # if not found, scroll up the screen by setting the last block to the first
                    device_block_list_elements = self.locate_element_list(self.new_device_block_list)
                    # the first block coordinates 0
                    first_device_block_element_coordinates = self.get_element_coordinates(device_block_list_elements[0])
                    # the last block coordinates -1
                    last_device_block_element_coordinates = self.get_element_coordinates(device_block_list_elements[-1])

                    start_position = (
                        last_device_block_element_coordinates["x"], last_device_block_element_coordinates["y"])
                    # print(start_position)
                    end_position = (
                        first_device_block_element_coordinates["x"], first_device_block_element_coordinates["y"])
                    # print(end_position)
                    self.scroll_screen(start_position, end_position)
            except exceptions.TimeoutException:
                return False
        # after 10 times try still not found, return False
        return False

    def check_device_name(self, device_index):
        """
        check the device name status based on device_index
        :param device_index: the index of the device in the current UI page or False
        :return: the connected label text: "HealthProtect" or "DustMagnet"
        """
        try:
            device_name_list_elements = self.locate_element_list(self.new_device_name_list)
            device_name_text = self.get_element_attribute(device_name_list_elements[device_index], "text")
            return device_name_text
        except exceptions.TimeoutException:
            return False

    def check_model_name(self, device_index):
        """
        check the device model status based on device_index
        :param device_index: the index of the device in the current UI page or False
        :return: the connected label text: "HealthProtect 7xxxi" or "DustMagnet 5xxxi"
        """
        try:
            device_model_list_elements = self.locate_element_list(self.new_device_model_list)
            device_model_text = self.get_element_attribute(device_model_list_elements[device_index], "text")
            return device_model_text
        except exceptions.TimeoutException:
            return False

    def check_mac_title(self):
        """
        no need to check right now
        :return:
        """
        pass

    def tap_mac_hint(self):
        """
        no need to check right now
        :return:
        """
        pass

    def tap_mac_address(self, device_index):
        """
        tap the device mac address based on device_index
        :param device_index: the index of the device in the current UI page or False
        :return:
        """
        try:
            mac_address_list_elements = self.locate_element_list(self.mac_address_list, waiting_time=5)
            self.tap_element(mac_address_list_elements[device_index])
        except exceptions.TimeoutException:
            return False

    def check_connection_lost_appears(self):
        """
        sometimes there is a popup window saying "connection lost", that needs to be closed and re-tap the mac address
        :return:
        """
        try:
            connection_lost_element = self.locate_element(self.connection_lost_close, waiting_time=30)
            if type(connection_lost_element) is webdriver.WebElement:
                self.tap_element(connection_lost_element)
                #print("close connection lost")
                return True
        except exceptions.TimeoutException:
            return False


    def check_connected_label(self, device_index):
        """
        check the device connected label status based on device_index
        :param device_index: the index of the device in the current UI page or False
        :return: the connected label text: "Available", "Connecting..." or "Connected to app"
        """
        try:
            connected_label_list_elements = self.locate_element_list(self.connected_label_list, waiting_time=10)
            connected_label_text = self.get_element_attribute(connected_label_list_elements[device_index], "text")
            return connected_label_text
        except exceptions.TimeoutException:
            return False

    def check_connected_name(self, device_index):
        """
        check the device customized name status based on device_index
        :param device_index: the index of the device in the current UI page or False
        :return: the device customized name text
        """
        try:
            connected_label_list_elements = self.locate_element_list(self.connected_label_list)
            # connected name may cannot be found
            try:
                connected_name_list_elements = self.locate_element_list(self.connected_name_list)
            except exceptions.TimeoutException:
                return None
            
            # iterate the connected label to insert missing connected name, so it matches the mac address numbers
            for connected_label_list_element in connected_label_list_elements:
                if self.get_element_attribute(connected_label_list_element, "text") == "Available":
                    index_number = connected_label_list_elements.index(connected_label_list_element)
                    connected_name_list_elements.insert(index_number, None)
            connected_name_text = self.get_element_attribute(connected_name_list_elements[device_index], "text")
            return connected_name_text
        except exceptions.TimeoutException:
            return False
    '''
    def check_device_image(self, device_index):
        """
        check the device image in Find your Device page, compare with the stored bas64 image string
        more details check crop_screenshot() method in base_page.py
        :param device_index: device order in the current UI page
        :return:
        """

        try:
            device_image_list_elements = self.locate_element_list(self.device_image_list)
            device_name_list_elements = self.locate_element_list(self.device_name_list)

            device_image_element_coordinates = self.get_element_coordinates(device_image_list_elements[device_index])
            width = device_image_element_coordinates["width"]
            height = device_image_element_coordinates["height"]
            # the image height width ratio is 1:1
            if (width / height) == 1:
                device_image_base64_string = self.crop_screenshot(self.get_screenshot64(), device_image_element_coordinates)
                device_name_text = self.get_element_attribute(device_name_list_elements[device_index], "text")
                #print("device_image_base64_string" + device_image_base64_string)
                if device_name_text == "HealthProtect" or device_name_text == "Protect":
                    if device_image_base64_string == HEALTHPROTECT:
                        return True
                    else:
                        return False
                elif device_name_text == "DustMagnet":
                    if device_image_base64_string == DUSTMAGNET:
                        return True
                    else:
                        return False
                else:
                    return False
        except exceptions.TimeoutException:
            return False
    '''
    def check_search_message_appears(self):
        """
        the search message "Searching for products via Bluetooth..." disappears when tap any device
        :return:
        """
        try:
            search_message_element = self.locate_element(self.search_message)
            if type(search_message_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_search_icon_appears(self):
        """
        the search message icon disappears when tap any device
        :return:
        """
        try:
            search_icon_element = self.locate_element(self.search_icon)
            if type(search_icon_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    # some tooltips check needed

    def tap_wifi_ssid(self, ssid: str):
        """
        tap the ssid
        :param ssid: ssid that wants to connect
        :return:
        """
        # try 2 times refresh the wifi list
        for _ in range(2):
            #print("try to refresh the wifi list")
            # try 3 times scroll up to find the wifi in the wifi list
            for _ in range(3):
                #print("try to find the wifi")
                try:
                    wifi_ssid_list_elements = self.locate_element_list(self.wifi_ssid_list, waiting_time=10)
                    for wifi_ssid_list_element in wifi_ssid_list_elements:
                        if self.get_element_attribute(wifi_ssid_list_element, "text") == ssid:
                            self.tap_element(wifi_ssid_list_element)
                            return True
                except exceptions.TimeoutException:
                    # swipe up the screen
                    start_position_percent = self.set_position_on_screen((75, 75))
                    end_position_percent = self.set_position_on_screen((25, 25))
                    self.scroll_screen(start_position_percent, end_position_percent)

            # swipe down the screen to refresh
            start_position_percent = self.set_position_on_screen((50, 50))
            end_position_percent = self.set_position_on_screen((75, 75))
            self.scroll_screen(start_position_percent, end_position_percent)
        return False

    def input_wifi_password(self, password: str):
        try:
            wifi_password_element = self.locate_element(self.wifi_password)
            password_submit_element = self.locate_element(self.password_submit)
            self.tap_element(wifi_password_element)
            self.set_element_text(wifi_password_element, password)
            self.tap_element(password_submit_element)
        except exceptions.TimeoutException:
            return False

    def wait_until_incorrect_password_message_appears(self):
        """
        check if the incorrect password message appears
        :return: True, if the message appears
        """
        try:
            password_error_element = self.locate_element(self.password_error, waiting_time=20)
            password_error_text_element = self.get_element_attribute(password_error_element, "text")
            if password_error_text_element == "Incorrect password":
                return True
            else:
                return False # The text does not match "Incorrect password"
        except exceptions.TimeoutException:
            return False

    def input_device_name(self, name: str, save_name=True):
        """
        if the name is one of the 3: "Bedroom Purifier", "Kitchen Purifier" or "Living Room Purifier",
        it goes to predefined name, otherwise, it goes to custom name
        :param name: device name
        :param save_name: if save the custom name
        :return:
        """
        try:
            if name == "Bedroom Purifier" or name == "Kitchen Purifier" or name == "Living Room Purifier":
                #print("predefined name")
                predefined_name_elements = self.locate_element_list(self.predefined_name_list, waiting_time=60)
                if name == "Bedroom Purifier":
                    self.tap_element(predefined_name_elements[0])
                elif name == "Kitchen Purifier":
                    self.tap_element(predefined_name_elements[1])
                else:
                    self.tap_element(predefined_name_elements[2])
            else:
                #print("customized name")
                custom_name_element = self.locate_element(self.custom_name, waiting_time=60)
                self.tap_element(custom_name_element)
                input_name_element = self.locate_element(self.input_name)
                self.tap_element(input_name_element)
                # re-locate the element because of the keyboard pops up and the element location changed
                input_name_element = self.locate_element(self.input_name)
                self.set_element_text(input_name_element, name, hide_kb=False) # don't hide the keyboard
                # save the name
                save_custom_name_element = self.locate_element(self.save_name)
                cancel_custom_name_element = self.locate_element(self.cancel_name)
                if save_name:
                    self.tap_element(save_custom_name_element)
                else:
                    self.tap_element(cancel_custom_name_element)
                # go to next step
                next_button_element = self.locate_element(self.next_done)
                self.tap_element(next_button_element)
        except exceptions.TimeoutException:
            return False









