# everything on the page UI, named ELEMENT!
from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions
import time
from appium import webdriver


class MainPage(BasePage):
    def __init__(self, common_driver):
        super(MainPage, self).__init__(common_driver)
        self.side_menu = (MobileBy.ACCESSIBILITY_ID, "Open navigation drawer")
        # when user logged in, this button is not displayed
        self.sign_in = (MobileBy.ID, "com.blueair.android:id/action_signin")
        self.outdoor_fold = (MobileBy.ID, "com.blueair.android:id/button_collapse")
        # when the location is enabled, this button is not displayed
        self.enable_location = (MobileBy.ID, "com.blueair.android:id/button_enable_location")
        self.device_empty = (MobileBy.ID, "com.blueair.android:id/textEmptyTitle")
        # when there is only 1 device, this text is not displayed
        self.device_count = (MobileBy.ID, "com.blueair.android:id/device_count")

        self.device_name = (MobileBy.ID, "com.blueair.android:id/textDeviceName")
        self.device_mode = (MobileBy.ID, "com.blueair.android:id/deviceModeLabel")
        self.device_aqi_level = (MobileBy.ID, "com.blueair.android:id/statusLabel")
        self.device_aqi_icon = (MobileBy.ID, "com.blueair.android:id/statusLabelIcon")
        self.device_offline_icon = (MobileBy.ID, "com.blueair.android:id/offline_view")
        self.device_clean_air_indication = (MobileBy.ID, "com.blueair.android:id/clear_air_in")
        self.device_clean_air_bar = (MobileBy.ID, "com.blueair.android:id/device_progress_bar")
        self.device_layout = (MobileBy.ID, "com.blueair.android:id/foregroundLayout")

        self.device_swipe_left = (MobileBy.ID, "com.blueair.android:id/leftview")
        self.device_swipe_right = (MobileBy.ID, "com.blueair.android:id/rightview")
        self.swipe_auto_mode = (MobileBy.ID, "com.blueair.android:id/automode_root")
        self.swipe_night_mode = (MobileBy.ID, "com.blueair.android:id/nightmode_root")
        self.swipe_standby_mode = (MobileBy.ID, "com.blueair.android:id/standby_mode_root")
        self.connect_product = (MobileBy.ID, "com.blueair.android:id/buttonConnectProduct")
        # DeviceConnectionPages object
        self.device_connection_pages = None

    def add_new_device(self):
        while True:
            try:
                connect_product_button = self.locate_element(self.connect_product)
                break
            except exceptions.TimeoutException:
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
        self.tap_element(connect_product_button)
        return self.device_connection_pages.tap_device_model()

    def get_devices_info(self, device="all", attr="all", scroll="yes", **kwargs):
        """
        device info format:
        ["device name", "device mode", "aqi level", "aqi icon", "offline icon", "clean air text", "clean air bar text"]
        device info list format:
        [[device info 1], [device info 2], [device info 3], ..., [device info n]]
        :param device: the device name user wants to return, default are all devices
        :param attr: the device attribute user wants to return, default are all attributes
        :param scroll: the current UI device without scrolling, default is to return the whole list by scrolling
        :param kwargs: waiting time for loading elements
        :return: the device info list
        """
        device_info_list = []

        # loop through the whole device list, when device list number < device count number
        while True:
            # device layout, need waiting_time to load
            try:
                device_layout_elements = self.locate_element_list(self.device_layout, kwargs["waiting_time"])
            except exceptions.TimeoutException:
                device_layout_elements = None

            # device name: aware, sense+, classic, g4, b4, icp
            try:
                device_name_elements = self.locate_element_list(self.device_name)
            except exceptions.TimeoutException:
                device_name_elements = None

            # device mode: fan speed %, auto, night, online(aware), offline, standby
            try:
                device_mode_elements = self.locate_element_list(self.device_mode)
            except exceptions.TimeoutException:
                device_mode_elements = None

            # aqi_level: excellent, good, moderate, polluted, very polluted
            try:
                device_aqi_level_elements = self.locate_element_list(self.device_aqi_level)
            except exceptions.TimeoutException:
                device_aqi_level_elements = None

            # aqi_icon: blue, green, yellow, orange, red
            try:
                device_aqi_icon_elements = self.locate_element_list(self.device_aqi_icon)
            except exceptions.TimeoutException:
                device_aqi_icon_elements = None

            # device offline
            try:
                device_offline_icon_elements = self.locate_element_list(self.device_offline_icon)
            except exceptions.TimeoutException:
                device_offline_icon_elements = None

            # device clean air indication: text
            try:
                device_clean_air_indication_elements = self.locate_element_list(self.device_clean_air_indication)
            except exceptions.TimeoutException:
                device_clean_air_indication_elements = None

            # device clean air bar: text 100.0
            try:
                device_clean_air_bar_elements = self.locate_element_list(self.device_clean_air_bar)
            except exceptions.TimeoutException:
                device_clean_air_bar_elements = None

            # organize device info into groups, iterate through devices
            if device_layout_elements:
                for device_layout_element in device_layout_elements:
                    device_layout_element_duplicate = False
                    device_info = []

                    device_layout_coordinates = self.get_element_coordinates(device_layout_element)
                    device_layout_x = device_layout_coordinates["x"]
                    device_layout_y = device_layout_coordinates["y"]
                    device_layout_w = device_layout_coordinates["x"] + device_layout_coordinates["width"]
                    device_layout_h = device_layout_coordinates["y"] + device_layout_coordinates["height"]

                    if device_name_elements:
                        device_name_element_no_inside = True
                        for device_name_element in device_name_elements:
                            device_name_element_duplicate = False
                            device_name_coordinates = self.get_element_coordinates(device_name_element)
                            device_name_x = device_name_coordinates["x"]
                            device_name_y = device_name_coordinates["y"]
                            device_name_w = device_name_coordinates["x"] + device_name_coordinates["width"]
                            device_name_h = device_name_coordinates["y"] + device_name_coordinates["height"]

                            device_name_text = self.get_element_attribute(device_name_element, "text")
                            # check if the name inside the layout
                            if device_layout_x <= device_name_x and device_layout_y <= device_name_y \
                                    and device_name_w <= device_layout_w and device_name_h <= device_layout_h:
                                device_name_element_no_inside = False
                                # check if the device name text already in the device info list
                                for device_info_list_element in device_info_list:
                                    # there is a device name text in the device info list, jump out the loop
                                    if device_name_text in device_info_list_element:
                                        device_name_element_duplicate = True
                                        device_layout_element_duplicate = True
                                        break
                                # there is a device name text in the device info list
                                # skip this device name element, go to the next
                                if device_name_element_duplicate:
                                    break
                                # check if there is no device name text, add it into device info
                                if not device_name_element_duplicate:
                                    device_info.append(device_name_text)
                                    break

                        # there is duplicated device name text in the current device layout, skip this layout
                        if device_layout_element_duplicate:
                            continue

                        # there is no device name in the current device layout, skip this layout
                        if device_name_element_no_inside:
                            continue

                    if device_mode_elements:
                        for device_mode_element in device_mode_elements:
                            device_mode_coordinates = self.get_element_coordinates(device_mode_element)
                            device_mode_x = device_mode_coordinates["x"]
                            device_mode_y = device_mode_coordinates["y"]
                            device_mode_w = device_mode_coordinates["x"] + device_mode_coordinates["width"]
                            device_mode_h = device_mode_coordinates["y"] + device_mode_coordinates["height"]

                            device_mode_text = self.get_element_attribute(device_mode_element, "text")
                            # check if the mode inside the layout
                            if device_layout_x <= device_mode_x and device_layout_y <= device_mode_y \
                                    and device_mode_w <= device_layout_w and device_mode_h <= device_layout_h:
                                device_info.append(device_mode_text)
                                break

                    if device_aqi_level_elements:
                        device_aqi_level_element_no_inside = True
                        for device_aqi_level_element in device_aqi_level_elements:
                            device_aqi_level_coordinates = self.get_element_coordinates(device_aqi_level_element)
                            device_aqi_level_x = device_aqi_level_coordinates["x"]
                            device_aqi_level_y = device_aqi_level_coordinates["y"]
                            device_aqi_level_w = device_aqi_level_coordinates["x"] + \
                                                 device_aqi_level_coordinates["width"]
                            device_aqi_level_h = device_aqi_level_coordinates["y"] + \
                                                 device_aqi_level_coordinates["height"]

                            device_aqi_level_text = self.get_element_attribute(device_aqi_level_element, "text")
                            # check if the device aqi level inside the layout
                            if device_layout_x <= device_aqi_level_x and device_layout_y <= device_aqi_level_y \
                                    and device_aqi_level_w <= device_layout_w and device_aqi_level_h <= device_layout_h:
                                device_aqi_level_element_no_inside = False
                                device_info.append(device_aqi_level_text)
                                break
                        if device_aqi_level_element_no_inside:
                            device_info.append(None)
                    else:
                        device_info.append(None)

                    if device_aqi_icon_elements:
                        device_aqi_icon_element_no_inside = True
                        for device_aqi_icon_element in device_aqi_icon_elements:
                            device_aqi_icon_coordinates = self.get_element_coordinates(device_aqi_icon_element)
                            device_aqi_icon_x = device_aqi_icon_coordinates["x"]
                            device_aqi_icon_y = device_aqi_icon_coordinates["y"]
                            device_aqi_icon_w = device_aqi_icon_coordinates["x"] + device_aqi_icon_coordinates["width"]
                            device_aqi_icon_h = device_aqi_icon_coordinates["y"] + device_aqi_icon_coordinates["height"]

                            # analyze the color of the device aqi icon
                            device_aqi_icon_image = self.analyze_screenshot_pixel_color(
                                self.crop_screenshot(self.get_screenshot64(), device_aqi_icon_coordinates))
                            # check if the device aqi icon inside the layout
                            if device_layout_x <= device_aqi_icon_x and device_layout_y <= device_aqi_icon_y \
                                    and device_aqi_icon_w <= device_layout_w and device_aqi_icon_h <= device_layout_h:
                                device_aqi_icon_element_no_inside = False
                                device_info.append(device_aqi_icon_image)
                                break
                        if device_aqi_icon_element_no_inside:
                            device_info.append(None)
                    else:
                        device_info.append(None)

                    if device_offline_icon_elements:
                        device_offline_icon_element_no_inside = True
                        for device_offline_icon_element in device_offline_icon_elements:
                            device_offline_icon_coordinates = self.get_element_coordinates(device_offline_icon_element)
                            device_offline_icon_x = device_offline_icon_coordinates["x"]
                            device_offline_icon_y = device_offline_icon_coordinates["y"]
                            device_offline_icon_w = device_offline_icon_coordinates["x"] + \
                                                    device_offline_icon_coordinates["width"]
                            device_offline_icon_h = device_offline_icon_coordinates["y"] + \
                                                    device_offline_icon_coordinates["height"]

                            if device_layout_x <= device_offline_icon_x and device_layout_y <= device_offline_icon_y \
                                    and device_offline_icon_w <= device_layout_w and \
                                    device_offline_icon_h <= device_layout_h:
                                device_offline_icon_element_no_inside = False
                                device_info.append("Offline")
                                break
                        if device_offline_icon_element_no_inside:
                            device_info.append(None)
                    else:
                        device_info.append(None)

                    if device_clean_air_indication_elements:
                        device_clean_air_indication_element_no_inside = True
                        for device_clean_air_indication_element in device_clean_air_indication_elements:
                            device_clean_air_indication_coordinates = self.get_element_coordinates(
                                device_clean_air_indication_element)
                            device_clean_air_indication_x = device_clean_air_indication_coordinates["x"]
                            device_clean_air_indication_y = device_clean_air_indication_coordinates["y"]
                            device_clean_air_indication_w = device_clean_air_indication_coordinates["x"] + \
                                                            device_clean_air_indication_coordinates["width"]
                            device_clean_air_indication_h = device_clean_air_indication_coordinates["y"] + \
                                                            device_clean_air_indication_coordinates["height"]

                            device_clean_air_indication_text = self.get_element_attribute(
                                device_clean_air_indication_element, "text")
                            # check if the device clean air indication inside the layout
                            if device_layout_x <= device_clean_air_indication_x \
                                    and device_layout_y <= device_clean_air_indication_y \
                                    and device_clean_air_indication_w <= device_layout_w \
                                    and device_clean_air_indication_h <= device_layout_h:
                                device_clean_air_indication_element_no_inside = False
                                device_info.append(device_clean_air_indication_text)
                                break
                        if device_clean_air_indication_element_no_inside:
                            device_info.append(None)
                    else:
                        device_info.append(None)

                    if device_clean_air_bar_elements:
                        device_clean_air_bar_element_no_inside = True
                        for device_clean_air_bar_element in device_clean_air_bar_elements:
                            device_clean_air_bar_coordinates = self.get_element_coordinates(
                                device_clean_air_bar_element)
                            device_clean_air_bar_x = device_clean_air_bar_coordinates["x"]
                            device_clean_air_bar_y = device_clean_air_bar_coordinates["y"]
                            device_clean_air_bar_w = device_clean_air_bar_coordinates["x"] + \
                                                     device_clean_air_bar_coordinates["width"]
                            device_clean_air_bar_h = device_clean_air_bar_coordinates["y"] + \
                                                     device_clean_air_bar_coordinates["height"]

                            device_clean_air_bar_text = self.get_element_attribute(device_clean_air_bar_element, "text")
                            # check if the device clean air bar inside the layout
                            if device_layout_x <= device_clean_air_bar_x \
                                    and device_layout_y <= device_clean_air_bar_y \
                                    and device_clean_air_bar_w <= device_layout_w \
                                    and device_clean_air_bar_h <= device_layout_h:
                                device_clean_air_bar_element_no_inside = False
                                device_info.append(device_clean_air_bar_text)
                                break
                        if device_clean_air_bar_element_no_inside:
                            device_info.append(None)
                    else:
                        device_info.append(None)

                    # append the device info into device info list
                    device_info_list.append(device_info)
                    # print(device_info_list)
            # delete the last element if the device current number < device count number
            try:
                connect_product_element = self.locate_element(self.connect_product)
            except exceptions.TimeoutException:
                connect_product_element = None

            if not connect_product_element:
                device_info_list = device_info_list[:-1]

            # loop until device count number equals device list number if it's needed
            if connect_product_element or scroll == "no":
                break
            else:
                # scroll up the screen to load more devices
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)

        #attr: "device_name", "device_mode", "aqi_level", "aqi_icon", "offline_icon", "clean_air_text", "clean_air_bar"
        if device == "all" and attr == "all":
            return device_info_list
        else:
            for list_element in device_info_list:
                if device in list_element:
                    if attr == "device_name":
                        return list_element[0]
                    elif attr == "device_mode":
                        return list_element[1]
                    elif attr == "aqi_level":
                        return list_element[2]
                    elif attr== "aqi_icon":
                        return list_element[3]
                    elif attr == "offline_icon":
                        return list_element[4]
                    elif attr == "clean_air_text":
                        return list_element[5]
                    elif attr == "clean_air_bar":
                        return list_element[6]
                    else:
                        return None
                else:
                    return None

    def swipe_device_layout_left(self, device: str, **kwargs):
        device_info_dict = {}
        device_layout_swipe_left_done = False

        while True:
            # device layout, need waiting_time to load
            try:
                device_layout_elements = self.locate_element_list(self.device_layout, kwargs["waiting_time"])
            except exceptions.TimeoutException:
                device_layout_elements = None

            # device name: aware, sense+, classic, g4, b4, icp
            try:
                device_name_elements = self.locate_element_list(self.device_name)
            except exceptions.TimeoutException:
                device_name_elements = None

            # iterate through devices to find the device name
            if device_name_elements:
                for device_name_element in device_name_elements:
                    device_name_text = self.get_element_attribute(device_name_element, "text")

                    if device_name_text == device:

                        device_name_coordinates = self.get_element_coordinates(device_name_element)
                        device_name_x = device_name_coordinates["x"]
                        device_name_y = device_name_coordinates["y"]
                        device_name_w = device_name_coordinates["x"] + device_name_coordinates["width"]
                        device_name_h = device_name_coordinates["y"] + device_name_coordinates["height"]

                        if device_layout_elements:
                            #iterate through layout
                            for device_layout_element in device_layout_elements:
                                device_layout_coordinates = self.get_element_coordinates(device_layout_element)
                                device_layout_x = device_layout_coordinates["x"]
                                device_layout_y = device_layout_coordinates["y"]
                                device_layout_w = device_layout_coordinates["x"] + device_layout_coordinates["width"]
                                device_layout_h = device_layout_coordinates["y"] + device_layout_coordinates["height"]

                                # check if the name inside the layout
                                if device_layout_x <= device_name_x and device_layout_y <= device_name_y \
                                        and device_name_w <= device_layout_w and device_name_h <= device_layout_h:
                                    device_info_dict[device_name_text] = device_layout_element
                                    # scroll the device_layout_element to the middle of the screen
                                    screen_vertical_center = self.get_screen_size()[1]
                                    print("float(device_layout_y / screen_vertical_center)", float(device_layout_y / screen_vertical_center))
                                    if 0.1 > float(device_layout_y / screen_vertical_center) or \
                                            float(device_layout_y / screen_vertical_center) > 0.9:
                                        start_position = (device_layout_x, device_layout_y)
                                        end_position = (device_layout_x, screen_vertical_center)
                                        self.scroll_screen(start_position, end_position)
                                    time.sleep(1)
                                    # relocate the device_layout_element
                                    device_layout_coordinates = self.get_element_coordinates(device_layout_element)
                                    device_layout_y = device_layout_coordinates["y"] + \
                                                      device_layout_coordinates["height"] // 2
                                    device_layout_w = device_layout_coordinates["x"] + \
                                                      device_layout_coordinates["width"]
                                    # start position is 20 percent of the whole width of the element
                                    start_position = (device_layout_w // 5, device_layout_y)
                                    end_position = (device_layout_w // 5 * 4, device_layout_y)
                                    while True:
                                        self.scroll_screen(start_position, end_position)
                                        try:
                                            self.locate_element(self.device_swipe_left)
                                            break
                                        except exceptions.TimeoutException:
                                            pass
                                    device_layout_swipe_left_done = True

            if device_layout_swipe_left_done:
                break

            try:
                connect_product_element = self.locate_element(self.connect_product)
            except exceptions.TimeoutException:
                connect_product_element = None

            # loop until device count number equals device list number if it's needed
            if connect_product_element:
                break
            else:
                # scroll up the screen to load more devices
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
                # print("scroll the screen")

        return device_info_dict

    def tap_auto_mode(self, press_status):
        """
        after swiping the device layout to the left, press the auto mode button
        can add image analyze by returning the result (white image/blue image) later
        :return:
        """
        try:
            auto_mode_element = self.locate_element(self.swipe_auto_mode)
            # get the pixel color
            while True:
                self.tap_element(auto_mode_element)
                auto_mode_element = self.locate_element(self.swipe_auto_mode)
                auto_mode_coordinates = self.get_element_coordinates(auto_mode_element)
                button_status = self.analyze_button_pixel_color(
                    self.crop_screenshot(self.get_screenshot64(), auto_mode_coordinates))
                if button_status == press_status:
                    break
            return True
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot64()
            self.save_image(screenshot_base64, self.tap_auto_mode.__name__)
            return False

    def tap_night_mode(self, press_status):
        """
        after swiping the device layout to the left, press the night mode button
        can add image analyze by returning the result (white image/blue image by analyzing white/blue pixel numbers) later
        :return:
        """
        try:
            night_mode_element = self.locate_element(self.swipe_night_mode)
            # get the pixel color
            while True:
                self.tap_element(night_mode_element)
                night_mode_element = self.locate_element(self.swipe_night_mode)
                night_mode_coordinates = self.get_element_coordinates(night_mode_element)
                button_status = self.analyze_button_pixel_color(
                    self.crop_screenshot(self.get_screenshot64(), night_mode_coordinates))
                if button_status == press_status:
                    break
            return True
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot64()
            self.save_image(screenshot_base64, self.tap_night_mode.__name__)
            return False

    def swipe_device_layout_left_back(self):
        """
        swipe back the left layout element
        :return:
        """
        device_swipe_left_layout = self.locate_element(self.device_swipe_left)
        device_swipe_left_coordinates = self.get_element_coordinates(device_swipe_left_layout)

        # relocate the device_layout_element
        device_layout_y = device_swipe_left_coordinates["y"] + \
                          device_swipe_left_coordinates["height"] // 2
        device_layout_w = device_swipe_left_coordinates["width"] // 10


        # start position is 80 percent of the whole width of the element,
        # end position is the start of the element, the left side of the screen
        start_position = (device_layout_w * 8, device_layout_y)
        end_position = (device_layout_w, device_layout_y)
        while True:
            self.scroll_screen(start_position, end_position)
            try:
                self.locate_element(self.device_swipe_left)
            except exceptions.TimeoutException:
                break

        try:
            if self.locate_element(self.device_swipe_left):
                return False
            else:
                return True
        except exceptions.TimeoutException:
            return True

    def swipe_device_layout_right(self, device: str, **kwargs):
        device_info_dict = {}
        device_layout_swipe_right_done = False

        while True:
            # print("locate elements start")
            # device layout, need waiting_time to load
            try:
                device_layout_elements = self.locate_element_list(self.device_layout, kwargs["waiting_time"])
            except exceptions.TimeoutException:
                device_layout_elements = None

            # device name: aware, sense+, classic, g4, b4, icp
            try:
                device_name_elements = self.locate_element_list(self.device_name)
                # print("device_name_coordinates")
            except exceptions.TimeoutException:
                device_name_elements = None

            # iterate through devices to find the device name
            if device_name_elements:
                for device_name_element in device_name_elements:
                    device_name_text = self.get_element_attribute(device_name_element, "text")

                    if device_name_text == device:

                        device_name_coordinates = self.get_element_coordinates(device_name_element)
                        device_name_x = device_name_coordinates["x"]
                        device_name_y = device_name_coordinates["y"]
                        device_name_w = device_name_coordinates["x"] + device_name_coordinates["width"]
                        device_name_h = device_name_coordinates["y"] + device_name_coordinates["height"]
                        # print("device_name_element")

                        if device_layout_elements:
                            # iterate through layout
                            for device_layout_element in device_layout_elements:
                                device_layout_coordinates = self.get_element_coordinates(device_layout_element)
                                device_layout_x = device_layout_coordinates["x"]
                                device_layout_y = device_layout_coordinates["y"]
                                device_layout_w = device_layout_coordinates["x"] + device_layout_coordinates["width"]
                                device_layout_h = device_layout_coordinates["y"] + device_layout_coordinates["height"]
                                # print("device_layout_element")

                                # check if the name inside the layout
                                if device_layout_x <= device_name_x and device_layout_y <= device_name_y \
                                        and device_name_w <= device_layout_w and device_name_h <= device_layout_h:
                                    device_info_dict[device_name_text] = device_layout_element
                                    # print("device_name_element in device_layout_element")
                                    # scroll the device_layout_element to the middle of the screen y axis
                                    screen_vertical_center = self.get_screen_size()[1]
                                    # print("screen_vertical_center: ", device_layout_y / screen_vertical_center)
                                    if 0.1 > float(device_layout_y / screen_vertical_center) or \
                                            float(device_layout_y / screen_vertical_center) > 0.9:
                                        start_position = (device_layout_x, device_layout_y)
                                        end_position = (device_layout_x, screen_vertical_center)
                                        self.scroll_screen(start_position, end_position)
                                    time.sleep(1)
                                    # relocate the device_layout_element
                                    device_layout_coordinates = self.get_element_coordinates(device_layout_element)
                                    device_layout_y = device_layout_coordinates["y"]
                                    device_layout_w = device_layout_coordinates["x"] + \
                                                      device_layout_coordinates["width"]
                                    # print("device_layout_element again")
                                    # start position is 80 percent of the whole width of the element
                                    start_position = (device_layout_w // 5 * 4, device_layout_y)
                                    end_position = (device_layout_w // 5, device_layout_y)
                                    while True:
                                        self.scroll_screen(start_position, end_position)
                                        try:
                                            self.locate_element(self.device_swipe_right)
                                            break
                                        except exceptions.TimeoutException:
                                            pass
                                    device_layout_swipe_right_done = True

            if device_layout_swipe_right_done:
                break

            try:
                connect_product_element = self.locate_element(self.connect_product)
            except exceptions.TimeoutException:
                connect_product_element = None

            # loop until device count number equals device list number if it's needed
            if connect_product_element:
                break
            else:
                # scroll up the screen to load more devices
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
                # print("scroll the screen")

        return device_info_dict

    def tap_standby_mode(self, press_status):
        """
        after swiping the device layout to the right, press the standby mode button
        can add image analyze by returning the result (white image/blue image) later
        :param press_status: True or False
        :return: True or False
        """
        try:
            standby_mode_element = self.locate_element(self.swipe_standby_mode)
            while True:
                self.tap_element(standby_mode_element)
                standby_mode_element = self.locate_element(self.swipe_standby_mode)
                standby_mode_coordinates = self.get_element_coordinates(standby_mode_element)
                button_status = self.analyze_button_pixel_color(
                    self.crop_screenshot(self.get_screenshot64(), standby_mode_coordinates))
                if button_status == press_status:
                    #print("pressed")
                    break
            return True
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot64()
            self.save_image(screenshot_base64, self.tap_standby_mode.__name__)
            return False

    def swipe_device_layout_right_back(self):
        """
        swipe back the right layout element
        :return:
        """
        device_swipe_right_layout = self.locate_element(self.device_swipe_right)
        device_swipe_right_coordinates = self.get_element_coordinates(device_swipe_right_layout)

        # relocate the device_layout_element
        device_layout_y = device_swipe_right_coordinates["y"] + \
                          device_swipe_right_coordinates["height"] // 2
        device_layout_w = (device_swipe_right_coordinates["width"] -
                           device_swipe_right_coordinates["x"]) // 5

        # start position is 20 percent of the whole width of the element,
        # end position is 80 percent of the element, the right side of the screen
        start_position = (device_swipe_right_coordinates["x"] + device_layout_w, device_layout_y)
        end_position = (device_swipe_right_coordinates["x"] + device_layout_w * 4, device_layout_y)
        while True:
            self.scroll_screen(start_position, end_position)
            try:
                self.locate_element(self.device_swipe_right)
            except exceptions.TimeoutException:
                break

        try:
            if self.locate_element(self.device_swipe_right):
                return False
            else:
                return True
        except exceptions.TimeoutException:
            return True

    def tap_device(self, device: str):
        device_name_dict = {}
        device_name_tap_done = False

        while True:
            # device name: aware, sense+, classic, g4, b4, icp
            try:
                device_name_elements = self.locate_element_list(self.device_name)
                # print("device_name_coordinates")
            except exceptions.TimeoutException:
                device_name_elements = None

            # iterate through devices to find the device name
            if device_name_elements:
                for device_name_element in device_name_elements:
                    device_name_text = self.get_element_attribute(device_name_element, "text")
                    # print(device_name_text)
                    if device_name_text == device:
                        while True:
                            self.tap_element(device_name_element)
                            device_name_dict[device_name_text] = device_name_element
                            device_name_tap_done = True
                            try:
                                # if the device name elements still can be seen, then go to the loop, tap the device name again
                                self.locate_element_list(self.device_name)
                                continue
                            except exceptions.TimeoutException:
                                # if the device name elements can not be found, then jump out the loop
                                return device_name_dict

            if device_name_tap_done:
                break

            try:
                connect_product_element = self.locate_element(self.connect_product)
            except exceptions.TimeoutException:
                connect_product_element = None

            # loop until device count number equals device list number if it's needed
            if connect_product_element:
                break
            else:
                # scroll up the screen to load more devices
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)

        return device_name_dict

    def tap_side_menu(self):
        """
        pressing the hamburger menu on the top left corner of the UI
        :return: a hamburger menu page object
        """
        try:
            side_menu_element = self.locate_element(self.side_menu, waiting_time=20)
            self.tap_element(side_menu_element)
            # side_menu = SideMenuPage(self.driver)
            # return side_menu
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot64()
            self.save_image(screenshot_base64, self.tap_side_menu.__name__)
            return

    def tap_user_login(self):
        """
        pressing the login menu on the top right corner of the UI
        :return: a login page object
        """
        try:
            user_login_element = self.locate_element(self.sign_in)
            self.tap_element(user_login_element)
            # user_login = LoginPage(self.driver)
            # return user_login
        except exceptions.TimeoutException:
            # screenshot_base64 = self.get_screenshot64()
            # self.save_image(screenshot_base64, self.tap_user_login.__name__)
            return False

    def check_login_appears(self):
        """
        check if the sign in button appears
        :return: True, if appears, False, if disappears
        """
        try:
            user_login_element = self.locate_element(self.sign_in, waiting_time=20)
            if type(user_login_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def check_side_menu_appears(self):
        """
        check if the side menu appears
        :return:
        """
        try:
            side_menu_element = self.locate_element(self.side_menu, waiting_time=20)
            if type(side_menu_element) is webdriver.WebElement:
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False

    def put_app_to_background(self, wait_time):
        """
        put the app to background if wait_time > 0, de-active the app if wait_time = -1
        :param wait_time: the waiting time in second
        :return:
        """
        self.put_background(wait_time)

    def active_app_to_foreground(self):
        """
        active the app to foreground if it's in de-active status or background
        :return:
        """
        self.put_foreground()

    def turn_on_screen(self):
        """
        DO NOTHING, more details can check self.unlock_screen()
        :return:
        """
        self.unlock_screen()

    def turn_off_screen(self):
        """
        DO NOTHING, more details can check self.lock_screen()
        :return:
        """
        self.lock_screen()

    # add more outdoor methods

    # about analyse the graph, can use opencv to calculate the total area of the graph, should be month > week > day