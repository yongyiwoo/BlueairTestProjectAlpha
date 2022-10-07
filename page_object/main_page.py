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

        # the device display area, when swipe up the device list, the area will show all the devices
        self.device_display_area = (MobileBy.ID, "com.blueair.android:id/content_container")

        self.device_name_list = (MobileBy.ID, "com.blueair.android:id/textDeviceName")
        self.device_mode_list = (MobileBy.ID, "com.blueair.android:id/deviceModeLabel")
        self.device_aqi_level_list = (MobileBy.ID, "com.blueair.android:id/statusLabel")
        self.device_aqi_icon_list = (MobileBy.ID, "com.blueair.android:id/statusLabelIcon")
        self.device_offline_icon_list = (MobileBy.ID, "com.blueair.android:id/offline_view")
        self.device_clean_air_list = (MobileBy.ID, "com.blueair.android:id/clear_air_in")
        self.device_clean_air_bar_list = (MobileBy.ID, "com.blueair.android:id/device_progress_bar")
        self.device_welcome_home_list = (MobileBy.ID, "com.blueair.android:id/device_welcome_home")
        self.device_block_list = (MobileBy.ID, "com.blueair.android:id/foregroundLayout")

        self.device_swipe_left = (MobileBy.ID, "com.blueair.android:id/leftview")
        self.device_swipe_right = (MobileBy.ID, "com.blueair.android:id/rightview")
        self.swipe_auto_mode = (MobileBy.ID, "com.blueair.android:id/automode_root")
        self.swipe_night_mode = (MobileBy.ID, "com.blueair.android:id/nightmode_root")
        self.swipe_standby_mode = (MobileBy.ID, "com.blueair.android:id/standby_mode_root")
        self.connect_product = (MobileBy.ID, "com.blueair.android:id/buttonConnectProduct")
        # DeviceConnectionPages object
        self.device_connection_pages = None

    # find the device
    def find_the_device(self, device_name: str):
        """
        try to find the device based on the given device_name
        :param device_name:
        :return: device name element
        """
        # try to scroll up the screen 10 times, so it can cover all devices in the list
        for _ in range(10):
            try:
                device_name_elements = self.locate_element_list(self.device_name_list, waiting_time=10)
                # find the device name
                for device_name_element in device_name_elements:
                    device_name_text_element = self.get_element_attribute(device_name_element, "text")
                    if device_name_text_element == device_name:
                        device_name_element_coordinates = self.get_element_coordinates(device_name_element)
                        # print(device_name_element_coordinates)
                        # print(self.set_position_on_screen((90, 90)))
                        # the name element should not be too close to the bottom of the screen
                        if device_name_element_coordinates["y"] < self.set_position_on_screen((90, 90))[1]:
                            return device_name_element
                # if not found, scroll up the screen by 25% of the screen height
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
            except exceptions.TimeoutException:
                return False
        # doesn't find anything after 10 times try, return false
        return False

    # center the device
    def center_the_device(self, device_name_element):
        try:
            if type(device_name_element) is webdriver.WebElement:
                # move the device name to the middle of the screen
                device_name_element_coordinates = self.get_element_coordinates(device_name_element)
                # swipe the device name element into the center of the screen
                start_position = (device_name_element_coordinates["x"], device_name_element_coordinates["y"])
                end_position = self.set_position_on_screen((50, 50))
                if abs(start_position[1] - end_position[1]) > 100:
                    self.scroll_screen(start_position, end_position)
        except exceptions.TimeoutException:
            return False

    # refind the device
    def refind_the_device(self, device_name: str):
        try:
            device_name_elements = self.locate_element_list(self.device_name_list, waiting_time=10)
            # find the device name again
            for device_name_element in device_name_elements:
                device_name_text_element = self.get_element_attribute(device_name_element, "text")
                if device_name_text_element == device_name:
                    return device_name_element
        except exceptions.TimeoutException:
            return False

    # get the device name coordinates
    def get_device_name_coordinates(self, device_name_element):
        try:
            if type(device_name_element) is webdriver.WebElement:
                device_name_coordinates = self.get_element_coordinates(device_name_element)
                return device_name_coordinates
        except exceptions.TimeoutException:
            return False

    # find the device block
    def find_device_block(self, device_name_coordinates):
        try:
            if (type(device_name_coordinates) is not None) and device_name_coordinates:
                device_block_elements = self.locate_element_list(self.device_block_list)
                for device_block_element in device_block_elements:
                    device_block_coordinates = self.get_element_coordinates(device_block_element)
                    # measure the name element position within the block element position
                    # x is the difference the x start point between the name and the block
                    # y is the difference the y start point between the name and the block
                    # w is the difference the x end point between the name and the block
                    # h is the difference the y end point between the name and the block
                    x = device_name_coordinates["x"] - device_block_coordinates["x"]
                    y = device_name_coordinates["y"] - device_block_coordinates["y"]
                    h = -y + device_block_coordinates["height"] - device_name_coordinates["height"]
                    w = -x + device_block_coordinates["width"] - device_name_coordinates["width"]
                    # the name element is inside the block element
                    if x > 0 and y > 0 and h > 0 and w > 0:
                        return device_block_element
                # if no finding, return None
                return None
        except exceptions.TimeoutException:
            return False

    # get the device block coordinates
    def get_device_block_coordinates(self, device_block_element):
        try:
            if type(device_block_element) is webdriver.WebElement:
                device_block_coordinates = self.get_element_coordinates(device_block_element)
                return device_block_coordinates
        except exceptions.TimeoutException:
            return False

    # find the device mode
    def find_device_mode(self, device_block_coordinates):
        try:
            if (type(device_block_coordinates) is not None) and device_block_coordinates:
                device_mode_elements = self.locate_element_list(self.device_mode_list)
                for device_mode_element in device_mode_elements:
                    device_mode_coordinates = self.get_element_coordinates(device_mode_element)
                    # measure the device mode element position within the block element position
                    # x is the difference the x start point between the device mode and the block
                    # y is the difference the y start point between the device mode and the block
                    # w is the difference the x end point between the device mode and the block
                    # h is the difference the y end point between the device mode and the block
                    x = device_mode_coordinates["x"] - device_block_coordinates["x"]
                    y = device_mode_coordinates["y"] - device_block_coordinates["y"]
                    h = -y + device_block_coordinates["height"] - device_mode_coordinates["height"]
                    w = -x + device_block_coordinates["width"] - device_mode_coordinates["width"]
                    # the device mode element is inside the block element
                    if x > 0 and y > 0 and h > 0 and w > 0:
                        device_mode_text = self.get_element_attribute(device_mode_element, "text")
                        return device_mode_text
                # if no finding, return None
                return None
        # if there is no device mode element
        except exceptions.TimeoutException:
            return None
        else:
            return False

    # find aqi level
    def find_aqi_level(self, device_block_coordinates):
        try:
            if (type(device_block_coordinates) is not None) and device_block_coordinates:
                aqi_level_elements = self.locate_element_list(self.device_aqi_level_list)
                for aqi_level_element in aqi_level_elements:
                    aqi_level_coordinates = self.get_element_coordinates(aqi_level_element)
                    # measure the device aqi level element position within the block element position
                    # x is the difference the x start point between the aqi level and the block
                    # y is the difference the y start point between the aqi level and the block
                    # w is the difference the x end point between the aqi level and the block
                    # h is the difference the y end point between the aqi level and the block
                    x = aqi_level_coordinates["x"] - device_block_coordinates["x"]
                    y = aqi_level_coordinates["y"] - device_block_coordinates["y"]
                    h = -y + device_block_coordinates["height"] - aqi_level_coordinates["height"]
                    w = -x + device_block_coordinates["width"] - aqi_level_coordinates["width"]

                    # the device aqi level element is inside the block element
                    if x > 0 and y > 0 and h > 0 and w > 0:
                        aqi_level_text = self.get_element_attribute(aqi_level_element, "text")
                        return aqi_level_text
                # if no finding, return None
                return None
        # if there is no aqi level element
        except exceptions.TimeoutException:
            return None
        else:
            return False

    # find aqi icon
    def find_aqi_icon(self, device_block_coordinates):
        try:
            if (type(device_block_coordinates) is not None) and device_block_coordinates:
                aqi_icon_elements = self.locate_element_list(self.device_aqi_icon_list)
                for aqi_icon_element in aqi_icon_elements:
                    aqi_icon_coordinates = self.get_element_coordinates(aqi_icon_element)
                    # measure the device aqi icon element position within the block element position
                    # x is the difference the x start point between the aqi icon and the block
                    # y is the difference the y start point between the aqi icon and the block
                    # w is the difference the x end point between the aqi icon and the block
                    # h is the difference the y end point between the aqi icon and the block
                    x = aqi_icon_coordinates["x"] - device_block_coordinates["x"]
                    y = aqi_icon_coordinates["y"] - device_block_coordinates["y"]
                    h = -y + device_block_coordinates["height"] - aqi_icon_coordinates["height"]
                    w = -x + device_block_coordinates["width"] - aqi_icon_coordinates["width"]
                    # the device aqi level element is inside the block element
                    if x > 0 and y > 0 and h > 0 and w > 0:
                        aqi_icon_coordinates = self.get_element_coordinates(aqi_icon_element)
                        # get the device aqi icon color
                        aqi_icon_color = self.analyze_screenshot_pixel_color(
                            self.crop_screenshot_and_convert_as_array(self.get_screenshot_base64(), aqi_icon_coordinates))
                        return aqi_icon_color
                # if no finding, return None
                return None
        # if there is no aqi icon element
        except exceptions.TimeoutException:
            return None
        else:
            return False

    # find the device offline icon
    def find_offline_icon(self, device_block_coordinates, turn_online=False):
        try:
            if (type(device_block_coordinates) is not None) and device_block_coordinates:
                offline_icon_elements = self.locate_element_list(self.device_offline_icon_list)
                for offline_icon_element in offline_icon_elements:
                    offline_icon_coordinates = self.get_element_coordinates(offline_icon_element)
                    # measure the device aqi icon element position within the block element position
                    # x is the difference the x start point between the offline icon and the block
                    # y is the difference the y start point between the offline icon and the block
                    # w is the difference the x end point between the offline icon and the block
                    # h is the difference the y end point between the offline icon and the block
                    x = offline_icon_coordinates["x"] - device_block_coordinates["x"]
                    y = offline_icon_coordinates["y"] - device_block_coordinates["y"]
                    h = -y + device_block_coordinates["height"] - offline_icon_coordinates["height"]
                    w = -x + device_block_coordinates["width"] - offline_icon_coordinates["width"]
                    # the device aqi level element is inside the block element
                    if x > 0 and y > 0 and h > 0 and w > 0:
                        # check if the device offline icon disappears
                        if turn_online:
                            if self.get_element_disappearance(offline_icon_element, waiting_time=20):
                                device_offline_icon_result = "Turn Online"
                                #print("device_offline_icon_result: " + str(device_offline_icon_result))
                                return device_offline_icon_result
                        # device offline icon appears
                        device_offline_icon_result = "Offline"
                        #print("device_offline_icon_result: " + str(device_offline_icon_result))
                        return device_offline_icon_result
                # if no finding, return None
                return None
        # if there is no offline icon element
        except exceptions.TimeoutException:
            return None
        else:
            return False

    # find the device clean air indication text
    def find_clean_air(self, device_block_coordinates):
        try:
            if (type(device_block_coordinates) is not None) and device_block_coordinates:
                clean_air_elements = self.locate_element_list(self.device_clean_air_list)
                for clean_air_element in clean_air_elements:
                    clean_air_coordinates = self.get_element_coordinates(clean_air_element)
                    # measure the device aqi icon element position within the block element position
                    # x is the difference the x start point between the offline icon and the block
                    # y is the difference the y start point between the offline icon and the block
                    # w is the difference the x end point between the offline icon and the block
                    # h is the difference the y end point between the offline icon and the block
                    x = clean_air_coordinates["x"] - device_block_coordinates["x"]
                    y = clean_air_coordinates["y"] - device_block_coordinates["y"]
                    h = -y + device_block_coordinates["height"] - clean_air_coordinates["height"]
                    w = -x + device_block_coordinates["width"] - clean_air_coordinates["width"]
                    # the device clean air element is inside the block element
                    if x > 0 and y > 0 and h > 0 and w > 0:
                        clean_air_text = self.get_element_attribute(clean_air_element, "text")
                        return clean_air_text
                # if no finding, return None
                return None
        # if there is no clean air element
        except exceptions.TimeoutException:
            return None
        else:
            return False

    # find the device clean air bar
    def find_clean_air_bar(self, device_block_coordinates):
        try:
            if (type(device_block_coordinates) is not None) and device_block_coordinates:
                clean_air_bar_elements = self.locate_element_list(self.device_clean_air_bar_list)
                for clean_air_bar_element in clean_air_bar_elements:
                    clean_air_bar_coordinates = self.get_element_coordinates(clean_air_bar_element)
                    # measure the device aqi icon element position within the block element position
                    # x is the difference the x start point between the offline icon and the block
                    # y is the difference the y start point between the offline icon and the block
                    # w is the difference the x end point between the offline icon and the block
                    # h is the difference the y end point between the offline icon and the block
                    x = clean_air_bar_coordinates["x"] - device_block_coordinates["x"]
                    y = clean_air_bar_coordinates["y"] - device_block_coordinates["y"]
                    h = -y + device_block_coordinates["height"] - clean_air_bar_coordinates["height"]
                    w = -x + device_block_coordinates["width"] - clean_air_bar_coordinates["width"]
                    # the device clean air bar element is inside the block element
                    if x >= 0 and y >= 0 and h >= 0 and w >= 0:
                        clean_air_bar_text = self.get_element_attribute(clean_air_bar_element, "text")
                        return clean_air_bar_text
                # if no finding, return None
                return None
        # if there is no clean air bar element
        except exceptions.TimeoutException:
            return None
        else:
            return False

    # find the device welcome home
    def find_welcome_home(self, device_block_coordinates):
        try:
            if (type(device_block_coordinates) is not None) and device_block_coordinates:
                welcome_home_elements = self.locate_element_list(self.device_welcome_home_list)
                for welcome_home_element in welcome_home_elements:
                    welcome_home_coordinates = self.get_element_coordinates(welcome_home_element)
                    # measure the device aqi icon element position within the block element position
                    # x is the difference the x start point between the offline icon and the block
                    # y is the difference the y start point between the offline icon and the block
                    # w is the difference the x end point between the offline icon and the block
                    # h is the difference the y end point between the offline icon and the block
                    x = welcome_home_coordinates["x"] - device_block_coordinates["x"]
                    y = welcome_home_coordinates["y"] - device_block_coordinates["y"]
                    h = -y + device_block_coordinates["height"] - welcome_home_coordinates["height"]
                    w = -x + device_block_coordinates["width"] - welcome_home_coordinates["width"]
                    # the device welcome home element is inside the block element
                    if x > 0 and y > 0 and h > 0 and w > 0:
                        welcome_home_result = self.get_element_attribute(welcome_home_element, "text")
                        return welcome_home_result
                # if no finding, return None
                return None
        # if there is no welcome home element
        except exceptions.TimeoutException:
            return None
        else:
            return False

    def get_device_status(self, device_name: str, **status_info):
        """
        return the device status in one block
        include aqi level, aqi icon, offline icon, mode, clean air, clean air bar, welcome home
        based on device name
        :return:
        """
        try:
            device_mode_result = aqi_level_result = aqi_icon_result = offline_icon_result = \
                clean_air_result = clean_air_bar_result = welcome_home_result = None
            self.center_the_device(self.find_the_device(device_name))
            block_coordinates = self.get_device_block_coordinates(
                self.find_device_block(self.get_device_name_coordinates(self.refind_the_device(device_name))))

            if status_info.get("device_mode"):
                device_mode_result = self.find_device_mode(block_coordinates)

            if status_info.get("aqi_level"):
                aqi_level_result = self.find_aqi_level(block_coordinates)

            if status_info.get("offline_icon"):
                # need to add something to check if the offline icon does appear or disappear or change from those 2 status
                offline_icon_result = self.find_offline_icon(block_coordinates, turn_online=True)

            if status_info.get("aqi_icon"):
                aqi_icon_result = self.find_aqi_icon(block_coordinates)

            if status_info.get("clean_air"):
                clean_air_result = self.find_clean_air(block_coordinates)

            if status_info.get("clean_air_bar"):
                clean_air_bar_result = self.find_clean_air_bar(block_coordinates)

            if status_info.get("welcome_home"):
                welcome_home_result = self.find_welcome_home(block_coordinates)

            return device_name, device_mode_result, aqi_level_result, aqi_icon_result, \
                   offline_icon_result, clean_air_result, clean_air_bar_result, welcome_home_result
        except exceptions.TimeoutException:
            return False

    def tap_connect_product(self):
        # may have a long device list, it needs to scroll down to find connect product button
        for _ in range(10): # try 10 times scroll in case of long device list
            try:
                connect_product_button = self.locate_element(self.connect_product)
                self.tap_element(connect_product_button)
                return True
            except exceptions.TimeoutException:
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((25, 25))
                self.scroll_screen(start_position_percent, end_position_percent)
        return False

    def swipe_device_layout_left(self, device: str, **kwargs):
        device_info_dict = {}
        device_layout_swipe_left_done = False

        while True:
            # device layout, need waiting_time to load
            try:
                device_layout_elements = self.locate_element_list(self.device_block_list, kwargs["waiting_time"])
            except exceptions.TimeoutException:
                device_layout_elements = None

            # device name: aware, sense+, classic, g4, b4, icp
            try:
                device_name_elements = self.locate_element_list(self.device_name_list)
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
                    self.crop_screenshot_and_compress_as_string(self.get_screenshot_base64(), auto_mode_coordinates))
                if button_status == press_status:
                    break
            return True
        except exceptions.TimeoutException:
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
                    self.crop_screenshot_and_compress_as_string(self.get_screenshot_base64(), night_mode_coordinates))
                if button_status == press_status:
                    break
            return True
        except exceptions.TimeoutException:
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
                device_layout_elements = self.locate_element_list(self.device_block_list, kwargs["waiting_time"])
            except exceptions.TimeoutException:
                device_layout_elements = None

            # device name: aware, sense+, classic, g4, b4, icp
            try:
                device_name_elements = self.locate_element_list(self.device_name_list)
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
                    self.crop_screenshot_and_compress_as_string(self.get_screenshot_base64(), standby_mode_coordinates))
                if button_status == press_status:
                    #print("pressed")
                    break
            return True
        except exceptions.TimeoutException:
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
                device_name_elements = self.locate_element_list(self.device_name_list)
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
                                self.locate_element_list(self.device_name_list)
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

    def check_side_menu_icon_appears(self):
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