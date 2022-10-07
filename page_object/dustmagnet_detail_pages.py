from appium.webdriver.common.mobileby import MobileBy
from page_object.device_detail_pages import DeviceDetailPages
from selenium.common import exceptions
import page_object.main_page
import time

class DustMagnetDetailPages(DeviceDetailPages):
    def __init__(self, common_driver):
        super(DustMagnetDetailPages, self).__init__(common_driver)
        self.device_title = (MobileBy.ID, "com.blueair.android:id/device_name")
        self.sensor_bar = (MobileBy.ID, "com.blueair.android:id/sensor_tabs")
        self.sensor_type = (MobileBy.ID, "com.blueair.android:id/sensor_label")
        self.sensor_value = (MobileBy.ID, "com.blueair.android:id/sensor_val")
        self.sensor_icon = (MobileBy.ID, "com.blueair.android:id/sensor_color")
        # graph
        self.graph_sensor = (MobileBy.ID, "com.blueair.android:id/value_label")
        self.graph_level = (MobileBy.ID, "com.blueair.android:id/severity_label")
        self.graph_icon = (MobileBy.ID, "com.blueair.android:id/severity_color")
        self.graph_chart = (MobileBy.ID, "com.blueair.android:id/lineChart")
        # fan speed
        # fan speed 0 text = 0.0, fan speed 1 text = 33.0, fan speed 2 text = 66.0, fan speed 3 text = 99.0
        # press increase or decrease the fan speed changes 3.3
        self.standby_message = (MobileBy.ID, "com.blueair.android:id/standby_message_view")
        self.mode_name = (MobileBy.ID, "com.blueair.android:id/mode_title")
        self.fanspeed_decrease = (MobileBy.ID, "com.blueair.android:id/decrease_imageview")
        self.fanspeed_bar = (MobileBy.ID, "com.blueair.android:id/fan_speed_seekbar")
        self.fanspeed_increase = (MobileBy.ID, "com.blueair.android:id/increase_imageview")
        self.fanspeed_0 = (MobileBy.ID, "com.blueair.android:id/fanspeed_0")
        #self.fanspeed_1 = (MobileBy.ID, "com.blueair.android:id/fanspeed_1")
        #self.fanspeed_2 = (MobileBy.ID, "com.blueair.android:id/fanspeed_2")
        self.fanspeed_3 = (MobileBy.ID, "com.blueair.android:id/fanspeed_3")
        # clean air in progress bar text shows 100.0
        self.clean_air = (MobileBy.ID, "com.blueair.android:id/clear_air_min_view")
        self.clean_air_bar = (MobileBy.ID, "com.blueair.android:id/progress")

        self.standby_mode = (MobileBy.ID, "com.blueair.android:id/standby_mode_root")
        self.manual_mode = (MobileBy.ID, "com.blueair.android:id/manual_mode_root")
        self.auto_mode = (MobileBy.ID, "com.blueair.android:id/automode_root")
        self.night_mode = (MobileBy.ID, "com.blueair.android:id/nightmode_root")

        # filter
        # self.filter_status = (MobileBy.ID, "com.blueair.android:id/attribute_title")
        self.filter_option = (MobileBy.ID, "com.blueair.android:id/learn_more_view")
        self.filter_percentage = (MobileBy.ID, "com.blueair.android:id/filter_time_percent_view")
        self.filter_bar = (MobileBy.ID, "com.blueair.android:id/progress")

        # schedule
        self.schedule_title = (MobileBy.ID, "com.blueair.android:id/device_schedule_title")
        self.add_schedule = (MobileBy.ID, "com.blueair.android:id/button_add")
        self.add_more_schedule = (MobileBy.ID, "com.blueair.android:id/add_schedule")
        self.schedule_name = (MobileBy.ID, "com.blueair.android:id/name")
        self.schedule_mode = (MobileBy.ID, "com.blueair.android:id/mode")
        self.schedule_icon = (MobileBy.ID, "com.blueair.android:id/mode_icon")
        self.schedule_time = (MobileBy.ID, "com.blueair.android:id/schedule_times")

        # schedule page
        self.schedule_save = (MobileBy.ID, "com.blueair.android:id/save_btn")
        self.schedule_overlap_cancel = (MobileBy.ID, "com.blueair.android:id/confirm_button")
        self.schedule_cancel = (MobileBy.ID, "com.blueair.android:id/cancel_btn")
        self.schedule_start_time = (MobileBy.ID, "com.blueair.android:id/button_start_time")
        self.schedule_end_time = (MobileBy.ID, "com.blueair.android:id/button_end_time")
        self.schedule_manual_mode_image = (MobileBy.ID, "com.blueair.android:id/manual_mode_imageview")
        self.schedule_manual_mode_text = (MobileBy.ID, "com.blueair.android:id/manual_mode_titleview")
        self.schedule_auto_mode_image = (MobileBy.ID, "com.blueair.android:id/automode_imageview")
        self.schedule_auto_mode_text = (MobileBy.ID, "com.blueair.android:id/automode_titleview")
        self.schedule_night_mode_image = (MobileBy.ID, "com.blueair.android:id/nightmode_imageview")
        self.schedule_night_mode_text = (MobileBy.ID, "com.blueair.android:id/nightmode_imageview")
        self.schedule_repeat = (MobileBy.ID, "com.blueair.android:id/text_view_selected_days")
        self.schedule_repeat_days = (MobileBy.ID, "com.blueair.android:id/day")
        self.schedule_label = (MobileBy.ID, "com.blueair.android:id/edit_text_label")
        self.schedule_delete = (MobileBy.ID, "com.blueair.android:id/button_delete_schedule")
        self.schedule_delete_confirm = (MobileBy.ID, "com.blueair.android:id/confirm_button")
        self.schedule_delete_cancel = (MobileBy.ID, "com.blueair.android:id/dismiss_button")

        # for schedule and settings led brightness
        self.led_brightness = (MobileBy.ID, "com.blueair.android:id/brightness_seekbar")

        # schedule set time subpage
        self.input_time_mode = (MobileBy.ID, "android:id/toggle_mode")
        self.input_hour = (MobileBy.ID, "android:id/input_hour")
        self.input_minute = (MobileBy.ID, "android:id/input_minute")
        self.input_time_ok = (MobileBy.ID, "android:id/button1")
        # change time format to 24 http://appium.io/docs/en/commands/mobile-command/
        # adb shell settings put system time_12_24 24
        self.schedule_am_pm = (MobileBy.ID, "android:id/am_pm_spinner")
        self.schedule_am_pm_set = (MobileBy.ID, "android:id/text1")

        # product settings
        self.device_settings = (MobileBy.ID, "com.blueair.android:id/buttonProductSettings")
        self.settings_names = (MobileBy.ID, "com.blueair.android:id/setting_title")
        self.settings_values = (MobileBy.ID, "com.blueair.android:id/setting_value")
        self.settings_childlock = (MobileBy.ID, "com.blueair.android:id/setting_switch")
        self.delete_device = (MobileBy.ID, "com.blueair.android:id/buttonDeleteProduct")

        self.device_name = (MobileBy.ID, "com.blueair.android:id/editText")
        # change name and delete device
        self.device_confirm_ok = (MobileBy.ID, "com.blueair.android:id/ok_view")
        self.device_confirm_cancel = (MobileBy.ID, "com.blueair.android:id/cancel_view")

        self.device_detail_info_name = (MobileBy.ID, "com.blueair.android:id/info_title")
        self.device_detail_info_value = (MobileBy.ID, "com.blueair.android:id/info_view")

    def get_sensor_info(self, sensor="all", scroll="yes", **kwargs):
        sensor_number = 1   # hardcoded
        sensor_info_list = []
        # loop through the whole sensor info list (B4 only has 1 PM2.5 sensor)
        # sensor type
        try:
            sensor_type_elements = self.locate_element_list(self.sensor_type)
        except exceptions.TimeoutException:
            sensor_type_elements = None
        # sensor value, need waiting_time to load
        try:
            sensor_value_elements = self.locate_element_list(self.sensor_value, kwargs["waiting_time"])
        except exceptions.TimeoutException:
            sensor_value_elements = None
        # sensor icon
        try:
            sensor_icon_elements = self.locate_element_list(self.sensor_icon)
        except exceptions.TimeoutException:
            sensor_icon_elements = None

        counter = 0
        while True:
            if sensor_type_elements:
                for i in range(len(sensor_type_elements)):
                    sensor_info = []
                    # get sensor type
                    sensor_type_text = self.get_element_attribute(sensor_type_elements[i], "text")
                    sensor_info.append(sensor_type_text)
                    # get sensor value
                    sensor_value_text = self.get_element_attribute(sensor_value_elements[i], "text")
                    sensor_info.append(sensor_value_text)
                    # get sensor icon (implement later)

                    # append the sensor info into sensor info list
                    sensor_info_list.append(sensor_info)

            # loop until sensor count number greater than a PM2.5 (PM1, PM2.5, PM10, TVOC, TEMP, HUM)
            if len(sensor_type_elements) < sensor_number or scroll == "no":
                break
            else:
                # swipe right the screen to load more sensors
                sensor_bar_element = self.locate_element(self.sensor_bar)
                # start position is 10 percent of the whole width of the element
                start_position_percent = (self.get_element_coordinates(sensor_bar_element)["width"] // 2,
                                  self.get_element_coordinates(sensor_bar_element)["y"])
                end_position_percent = (self.get_element_coordinates(sensor_bar_element)["x"],
                                self.get_element_coordinates(sensor_bar_element)["y"])

                self.scroll_screen(start_position_percent, end_position_percent)

            # to stop the loop in 10 times
            counter += 1
            if counter > 9:
                break

        if sensor == "all":
            return sensor_info_list
        else:
            for sensor_info_retval in sensor_info_list:
                if sensor_info_retval[0] == sensor:
                    return sensor_info_retval

            return None

    def get_graph_sensor(self):
        """
        get the sensor data which on top of the graph
        :return: the sensor data
        """
        graph_sensor_text = None
        try:
            graph_sensor_element = self.locate_element(self.graph_sensor)
            graph_sensor_text = self.get_element_attribute(graph_sensor_element, "text")
            return graph_sensor_text
        except exceptions.TimeoutException:
            return graph_sensor_text

    def get_graph_level(self):
        """
        get the air quality level which on top right of the graph
        :return: the air quality level
        """
        graph_level_text = None
        try:
            graph_level_element = self.locate_element(self.graph_level)
            graph_level_text = self.get_element_attribute(graph_level_element, "text")
            return graph_level_text
        except exceptions.TimeoutException:
            return graph_level_text

    def get_graph_icon(self):
        """
        get the air quality icon which on top right of the graph
        :return: the icon color
        """
        graph_icon_image = None
        try:
            graph_icon_element = self.locate_element(self.graph_icon)
            graph_icon_coordinates = self.get_element_coordinates(graph_icon_element)
            # analyze the color of the device aqi icon
            graph_icon_image = self.analyze_screenshot_pixel_color(
                self.crop_screenshot_and_compress_as_string(self.get_screenshot_base64(), graph_icon_coordinates))
            return graph_icon_image
        except exceptions.TimeoutException:
            return graph_icon_image

    def get_graph_chart(self):
        # need to implement later by using opencv
        pass

    def get_mode_info(self):
        """
        get the mode title info in manual, auto and night mode, get the message in standby mode
        :return: mode title
        """
        direction = "down"

        counter = 0
        while True:
            # test if it's in standby mode
            try:
                standby_message_element = self.locate_element(self.standby_message)
                standby_message_text = self.get_element_attribute(standby_message_element, "text")
                #print("standby_message_element")
                return standby_message_text
            except exceptions.TimeoutException:
                pass

            # test if it's in manual, auto or night mode
            try:
                mode_element = self.locate_element(self.mode_name)
                mode_text = self.get_element_attribute(mode_element, "text")
                #print("mode_element")
                return mode_text
            except exceptions.TimeoutException:
                pass

            # the end of the device details view
            try:
                self.locate_element(self.device_settings)
                #print("device_settings")
                direction = "up"
            except exceptions.TimeoutException:
                pass

            # the top of the device details view
            try:
                self.locate_element(self.sensor_bar)
                #print("device_title")
                direction = "down"
            except exceptions.TimeoutException:
                pass

            # if it's end of the page, scroll up, if not, scroll down
            if direction == "up":
                #print("scroll up")
                self.locate_element(self.device_settings)
                start_position_percent = self.set_position_on_screen((50, 50))
                end_position_percent = self.set_position_on_screen((75, 75))
                self.scroll_screen(start_position_percent, end_position_percent)
            if direction == "down":
                #print("scroll down")
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)

            # to stop the loop in 10 times
            counter += 1
            if counter > 9:
                break

    def get_manual_mode_info(self):
        # get fan speed
        try:
            mode_name_element = self.locate_element(self.mode_name)
            mode_name_text = self.get_element_attribute(mode_name_element, "text")
            fanspeed_bar_element = self.locate_element(self.fanspeed_bar)
            fanspeed_text = self.get_element_attribute(fanspeed_bar_element, "text")
            clean_air_element = self.locate_element(self.clean_air)
            clean_air_text = self.get_element_attribute(clean_air_element, "text")
            clean_air_bar_element = self.locate_element(self.clean_air_bar)
            clean_air_bar_text = self.get_element_attribute(clean_air_bar_element, "text")

            return mode_name_text, fanspeed_text, clean_air_text, clean_air_bar_text
        except exceptions.TimeoutException:
            return None

    def tap_standby_mode(self, press_status):
        """
        press the standby mode button
        image analyze by returning the result (white image/blue image)
        :return: True: pressed; False: unpressed
        """
        try:
            standby_mode_element = self.locate_element(self.standby_mode)
            # get the pixel color
            counter = 0
            while True:
                self.tap_element(standby_mode_element)
                standby_mode_element = self.locate_element(self.standby_mode)
                standby_mode_coordinates = self.get_element_coordinates(standby_mode_element)
                button_status = self.analyze_button_pixel_color(
                    self.crop_screenshot_and_compress_as_string(self.get_screenshot_base64(), standby_mode_coordinates))
                if button_status == press_status:
                    break
                # to stop the loop in 10 times
                counter += 1
                if counter > 9:
                    break
            return True
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.tap_standby_mode.__name__)
            return False

    def tap_manual_mode(self, press_status):
        """
        press the manual mode button
        image analyze by returning the result (white image/blue image)
        :return: True: pressed; False: unpressed
        """
        try:
            manual_mode_element = self.locate_element(self.manual_mode)

            counter = 0
            while True:
                self.tap_element(manual_mode_element)
                manual_mode_element = self.locate_element(self.manual_mode)
                manual_mode_coordinates = self.get_element_coordinates(manual_mode_element)
                button_status = self.analyze_button_pixel_color(
                    self.crop_screenshot_and_compress_as_string(self.get_screenshot_base64(), manual_mode_coordinates))
                if button_status == press_status:
                    break

                # to stop the loop in 10 times
                counter += 1
                if counter > 9:
                    break
            return True
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.tap_manual_mode.__name__)
            return False

    def set_manual_mode_by_button(self, set_fanspeed: str):
        """
        set manual mode fan speed by tap buttons
        fan speed 0 text = 0.0, fan speed 1 text = 33.0, fan speed 2 text = 66.0, fan speed 3 text = 99.0
        press increase or decrease the fan speed changes 3.3
        :param set_fanspeed: fan speed string between 0.0 and 99.0
        :return: fan speed text
        """
        try:
            fanspeed_increase_element = self.locate_element(self.fanspeed_increase)
            fanspeed_bar_element = self.locate_element(self.fanspeed_bar)
            fanspeed_bar_text = self.get_element_attribute(fanspeed_bar_element, "text")
            fanspeed_decrease_element = self.locate_element(self.fanspeed_decrease)

            change_fanspeed = float(set_fanspeed) - float(fanspeed_bar_text)

            counter = 0
            while change_fanspeed != 0.0:
                if change_fanspeed > 0.0:
                    self.tap_element(fanspeed_increase_element)
                    time.sleep(1)
                else:
                    self.tap_element(fanspeed_decrease_element)
                    time.sleep(1)
                # refresh the fanspeed bar text
                fanspeed_bar_text = self.get_element_attribute(fanspeed_bar_element, "text")
                change_fanspeed = float(set_fanspeed) - float(fanspeed_bar_text)

                # to stop the loop in 30 times
                counter += 1
                if counter > 30:
                    break

            return fanspeed_bar_text
        except exceptions.TimeoutException:
            return None

    def set_manual_mode_by_bar(self, set_fanspeed: str):
        """
        set manual mode fan speed by swipe the bar
        :param set_fanspeed: fan speed string between 0.0 and 99.0
        :return: fan speed text
        """
        try:
            fanspeed_bar_element = self.locate_element(self.fanspeed_bar)
            fanspeed_0_element = self.locate_element(self.fanspeed_0)
            #fanspeed_1_element = self.locate_element(self.fanspeed_1)
            #fanspeed_2_element = self.locate_element(self.fanspeed_2)
            fanspeed_3_element = self.locate_element(self.fanspeed_3)
            fanspeed_bar_text = self.get_element_attribute(fanspeed_bar_element, "text")

            factor = (int(self.get_element_coordinates(fanspeed_3_element)["x"] +
                          self.get_element_coordinates(fanspeed_3_element)["width"]) -
                      int(self.get_element_coordinates(fanspeed_0_element)["x"] +
                          self.get_element_coordinates(fanspeed_0_element)["width"])) / 99

            fanspeed_bar_start_x = int(self.get_element_coordinates(fanspeed_0_element)["x"] +
                                       self.get_element_coordinates(fanspeed_0_element)["width"] +
                                       factor * float(fanspeed_bar_text))
            fanspeed_bar_start_y = int(self.get_element_coordinates(fanspeed_bar_element)["y"])



            fanspeed_bar_end_x = int(self.get_element_coordinates(fanspeed_0_element)["x"] +
                                     self.get_element_coordinates(fanspeed_0_element)["width"] +
                                     factor * float(set_fanspeed))
            fanspeed_bar_end_y = int(self.get_element_coordinates(fanspeed_bar_element)["y"])

            self.scroll_screen((fanspeed_bar_start_x, fanspeed_bar_start_y), (fanspeed_bar_end_x, fanspeed_bar_end_y))
            fanspeed_bar_text = self.get_element_attribute(fanspeed_bar_element, "text")

            return fanspeed_bar_text
        except exceptions.TimeoutException:
            return None

    def tap_auto_mode(self, press_status):
        """
        press the auto mode button
        image analyze by returning the result (white image/blue image)
        :return: True: pressed; False: unpressed
        """
        try:
            auto_mode_element = self.locate_element(self.auto_mode)

            counter = 0
            while True:
                self.tap_element(auto_mode_element)
                auto_mode_element = self.locate_element(self.auto_mode)
                auto_mode_coordinates = self.get_element_coordinates(auto_mode_element)
                button_status = self.analyze_button_pixel_color(
                    self.crop_screenshot_and_compress_as_string(self.get_screenshot_base64(), auto_mode_coordinates))
                if button_status == press_status:
                    break

                # to stop the loop in 10 times
                counter += 1
                if counter > 9:
                    break
            return True
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.tap_auto_mode.__name__)
            return False

    def tap_night_mode(self, press_status):
        """
        press the night mode button
        image analyze by returning the result (white image/blue image)
        :return: True: pressed; False: unpressed
        """
        try:
            night_mode_element = self.locate_element(self.night_mode)

            counter = 0
            while True:
                self.tap_element(night_mode_element)
                night_mode_element = self.locate_element(self.night_mode)
                night_mode_coordinates = self.get_element_coordinates(night_mode_element)
                button_status = self.analyze_button_pixel_color(
                    self.crop_screenshot_and_compress_as_string(self.get_screenshot_base64(), night_mode_coordinates))
                if button_status == press_status:
                    break

                # to stop the loop in 10 times
                counter += 1
                if counter > 9:
                    break
            return True
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.tap_night_mode.__name__)
            return False

    def get_filter_info(self):
        """
        when getting the filter info
        otherwise, the filter bar will have the same id
        :return: filter_percentage_text, filter_bar_text
        """
        counter = 0
        while True:
            try:
                filter_percentage_element = self.locate_element(self.filter_percentage)
                filter_percentage_text = self.get_element_attribute(filter_percentage_element, "text")
                filter_percentage_coordinates_y = int(self.get_element_coordinates(filter_percentage_element)["y"])
                filter_bar_elements = self.locate_element_list(self.filter_bar)
                filter_bar_text = None
                for filter_bar_element in filter_bar_elements:
                    filter_bar_coordinates_y = int(self.get_element_coordinates(filter_bar_element)["y"])
                    if filter_bar_coordinates_y > filter_percentage_coordinates_y:
                        filter_bar_text = self.get_element_attribute(filter_bar_element, "text")
                if filter_percentage_text and filter_bar_text:
                    break
            except exceptions.TimeoutException:
                # swipe up the screen
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)

            # to stop the loop in 10 times
            counter += 1
            if counter > 9:
                filter_bar_text = None
                filter_percentage_text = None
                break
        if filter_percentage_text and filter_bar_text:
            return filter_percentage_text[:2], filter_bar_text[:2]
        else:
            return filter_percentage_text, filter_bar_text

    def tap_filter_option(self):
        """
        tap the "Learn more" link to navigate to filter detail page
        :return: None
        """
        try:
            filter_option_element = self.locate_element(self.filter_option)
            self.tap_element(filter_option_element)
            return
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.set_new_schedule.__name__)
            return

    def filter_detail_page(self):
        """
        get the sensor data which on top of the graph
        :return: the filter usage percentage text and filter bar text
        """
        try:
            filter_percentage_element = self.locate_element(self.filter_percentage)
            filter_percentage_text = self.get_element_attribute(filter_percentage_element, "text")
            filter_bar_element = self.locate_element(self.filter_bar)
            filter_bar_text = self.locate_element(filter_bar_element, "text")
            return filter_percentage_text, filter_bar_text
        except exceptions.TimeoutException:
            return None, None

    def tap_add_schedule(self):
        counter = 0
        while True:
        # for small screen, try to find the add schedule button by swiping up
            try:
                add_schedule_element = self.locate_element(self.add_schedule)
                self.tap_element(add_schedule_element)
                return True
            except exceptions.TimeoutException:
                # swipe up the screen
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
            # to stop the loop in 10 times
            counter += 1
            if counter > 2:
                break
        # if more than 3 times swiping cannot find the add schedule, trigger the error
        screenshot_base64 = self.get_screenshot_base64()
        self.save_image(screenshot_base64, self.tap_add_schedule.__name__)
        return False

    def tap_add_more_schedule(self):
        counter = 0
        while True:
        # for small screen, try to find the add schedule button by swiping up
            try:
                add_more_schedule_element = self.locate_element(self.add_more_schedule)
                self.tap_element(add_more_schedule_element)
                return True # add new schedule page?
            except exceptions.TimeoutException:
                # swipe up the screen
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
            # to stop the loop in 3 times
            counter += 1
            if counter > 2:
                break
        # if more than 3 times swiping cannot find the add schedule, trigger the error
        screenshot_base64 = self.get_screenshot_base64()
        self.save_image(screenshot_base64, self.tap_add_more_schedule.__name__)
        return None

    def set_new_schedule(self, start_time: str, end_time: str, mode: str, repeat: list, schedule_label: str,
                         result_action: str, am_pm=None, fanspeed=None, led=None):
        """
        set the new schedule
        :param start_time: the start time of the schedule, format "hh:mm"
        :param end_time: the end time of the schedule, format "hh:mm"
        :param mode: the air purifier mode, "manual", "auto", "night"
        :param repeat: a list from Sunday as 0 to Saturday as 6, [0, 1, 2, 3, 4, 5, 6]
        :param schedule_label: the schedule name
        :param result_action: the action to finish this schedule, "save" or "cancel"
        :param am_pm: 24 hour format if am_pm is None, "AM" and "PM" for 12 hour format
        :param fanspeed: fan speed string, like "33.0", "66.0", "99.0"
        :param led: an approximate value of the led brightness, "50.0"
        :return: a schedule info tuple
        """
        schedule_label_text = None
        mode_text = None
        mode_image = None

        try:
            start_time_element = self.locate_element(self.schedule_start_time)
            self.tap_element(start_time_element)
            input_time_element = self.locate_element(self.input_time_mode)
            self.tap_element(input_time_element)
            input_hour_element = self.locate_element(self.input_hour)
            input_minute_element = self.locate_element(self.input_minute)
            self.set_element_text(input_hour_element, start_time.split(":")[0], hide_kb=False)
            self.set_element_text(input_minute_element, start_time.split(":")[1], hide_kb=False)
            if am_pm is not None:
                schedule_am_pm_element = self.locate_element(self.schedule_am_pm)
                self.tap_element(schedule_am_pm_element)
                if am_pm == "AM":
                    schedule_am_element = self.locate_element_list(self.schedule_am_pm_set, waiting_time=5)[0]
                    #print(schedule_am_element)
                    self.tap_element(schedule_am_element)
                if am_pm == "PM":
                    schedule_pm_element = self.locate_element_list(self.schedule_am_pm_set, waiting_time=5)[1]
                    #print(schedule_pm_element)
                    self.tap_element(schedule_pm_element)
            input_time_ok_element = self.locate_element(self.input_time_ok, waiting_time=5)
            self.tap_element(input_time_ok_element)
            start_time_element = self.locate_element(self.schedule_start_time, waiting_time=5)
            start_time_text = self.get_element_attribute(start_time_element, "text")
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.set_new_schedule.__name__)
            return None

        try:
            end_time_element = self.locate_element(self.schedule_end_time)
            self.tap_element(end_time_element)
            input_time_element = self.locate_element(self.input_time_mode)
            self.tap_element(input_time_element)
            input_hour_element = self.locate_element(self.input_hour)
            self.set_element_text(input_hour_element, end_time.split(":")[0], hide_kb=False)
            input_minute_element = self.locate_element(self.input_minute)
            self.set_element_text(input_minute_element, end_time.split(":")[1], hide_kb=False)
            if am_pm is not None:
                schedule_am_pm_element = self.locate_element(self.schedule_am_pm)
                self.tap_element(schedule_am_pm_element)
                if am_pm == "AM":
                    schedule_am_element = self.locate_element_list(self.schedule_am_pm_set, waiting_time=5)[0]
                    self.tap_element(schedule_am_element)
                if am_pm == "PM":
                    schedule_pm_element = self.locate_element_list(self.schedule_am_pm_set, waiting_time=5)[1]
                    self.tap_element(schedule_pm_element)
            input_time_ok_element = self.locate_element(self.input_time_ok, waiting_time=5)
            self.tap_element(input_time_ok_element)
            end_time_element = self.locate_element(self.schedule_end_time, waiting_time=5)
            end_time_text = self.get_element_attribute(end_time_element, "text")
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.set_new_schedule.__name__)
            return None

        try:
            if mode == "auto":
                schedule_auto_mode_image_element = self.locate_element(self.schedule_auto_mode_image)
                self.tap_element(schedule_auto_mode_image_element)
                # crop the auto mode icon
                schedule_auto_mode_coordinates = self.get_element_coordinates(schedule_auto_mode_image_element)
                screenshot_base64 = self.get_screenshot_base64()
                schedule_auto_mode_image = self.crop_screenshot_and_compress_as_string(screenshot_base64, schedule_auto_mode_coordinates)
                mode_image = schedule_auto_mode_image
                schedule_auto_mode_text_element = self.locate_element(self.schedule_auto_mode_text)
                schedule_auto_mode_text = self.get_element_attribute(schedule_auto_mode_text_element, "text")
                mode_text = schedule_auto_mode_text
            if mode == "night":
                schedule_night_mode_image_element = self.locate_element(self.schedule_night_mode_image)
                self.tap_element(schedule_night_mode_image_element)
                # crop the night mode icon
                schedule_night_mode_coordinates = self.get_element_coordinates(schedule_night_mode_image_element)
                screenshot_base64 = self.get_screenshot_base64()
                schedule_night_mode_image = self.crop_screenshot_and_compress_as_string(screenshot_base64, schedule_night_mode_coordinates)
                mode_image = schedule_night_mode_image
                schedule_night_mode_text_element = self.locate_element(self.schedule_night_mode_text)
                schedule_night_mode_text = self.get_element_attribute(schedule_night_mode_text_element, "text")
                mode_text = schedule_night_mode_text
            if mode == "manual":
                schedule_manual_mode_image_element = self.locate_element(self.schedule_manual_mode_image)
                self.tap_element(schedule_manual_mode_image_element)
                # crop the manual mode icon
                schedule_manual_mode_coordinates = self.get_element_coordinates(schedule_manual_mode_image_element)
                screenshot_base64 = self.get_screenshot_base64()
                schedule_manual_mode_image = self.crop_screenshot_and_compress_as_string(screenshot_base64, schedule_manual_mode_coordinates)
                mode_image = schedule_manual_mode_image
                schedule_manual_mode_text_element = self.locate_element(self.schedule_manual_mode_text)
                schedule_manual_mode_text = self.get_element_attribute(schedule_manual_mode_text_element, "text")
                mode_text = schedule_manual_mode_text
                self.set_manual_mode_by_button(fanspeed)
                # self.set_manual_mode_by_bar(fanspeed)
                # the led brightness is an approximate value, cannot control accurately
                led_brightness_element = self.locate_element(self.led_brightness)
                factor = int(self.get_element_coordinates(led_brightness_element)["width"] / 100)
                brightness_bar_start_x = int(self.get_element_coordinates(led_brightness_element)["x"])
                brightness_bar_start_y = int(self.get_element_coordinates(led_brightness_element)["y"])
                brightness_bar_end_x = int(self.get_element_coordinates(led_brightness_element)["x"] +
                                           factor * int(led))
                brightness_bar_end_y = int(self.get_element_coordinates(led_brightness_element)["y"])
                self.scroll_screen((brightness_bar_start_x, brightness_bar_start_y),
                                   (brightness_bar_end_x, brightness_bar_end_y))
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.set_new_schedule.__name__)
            return None

        try:
            # repeat is [0, 1, 2, 3, 4, 5 ,6] presents Sunday, Monday ... Saturday
            schedule_repeat_element = self.locate_element(self.schedule_repeat)
            self.tap_element(schedule_repeat_element)
            counter = 0
            while True:
                schedule_repeat_days_elements = self.locate_element_list(self.schedule_repeat_days)
                if len(schedule_repeat_days_elements) != 7:
                    # swipe up the screen
                    start_position_percent = self.set_position_on_screen((75, 75))
                    end_position_percent = self.set_position_on_screen((50, 50))
                    self.scroll_screen(start_position_percent, end_position_percent)
                else:
                    for i in [x for x in range(6) if x not in repeat]:
                        self.tap_element(schedule_repeat_days_elements[i])
                    break
                # to stop the loop in 10 times
                counter += 1
                if counter > 9:
                    break
            schedule_repeat_text = self.get_element_attribute(schedule_repeat_element, "text")
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.set_new_schedule.__name__)
            return None

        # put a name for the schedule
        name_counter = 0
        while True:
            try:
                schedule_label_element = self.locate_element(self.schedule_label)
                self.set_element_text(schedule_label_element, schedule_label, hide_kb=False)
                schedule_label_text = self.get_element_attribute(schedule_label_element, "text")
                break
            except exceptions.TimeoutException:
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
            # to stop the loop in 3 times
            name_counter += 1
            if name_counter > 2:
                break

        try:
            if result_action == "save":
                schedule_save_element = self.locate_element(self.schedule_save, waiting_time=5)
                self.tap_element(schedule_save_element)
                # the schedule time overlap
                try:
                    schedule_overlap_cancel_element = self.locate_element(self.schedule_overlap_cancel)
                    self.tap_element(schedule_overlap_cancel_element)
                    schedule_overlap_cancelled = "overlap_cancelled"
                    return schedule_overlap_cancelled
                except exceptions.TimeoutException:
                    pass
            if result_action == "cancel":
                schedule_cancel_element = self.locate_element(self.schedule_cancel, waiting_time=5)
                self.tap_element(schedule_cancel_element)
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.set_new_schedule.__name__)
            return None

        try:
            schedule_title_element = self.locate_element(self.schedule_title, waiting_time=10)
            schedule_title_text = self.get_element_attribute(schedule_title_element, "text")
            if schedule_title_text:
                return schedule_label_text, mode_text, mode_image, schedule_repeat_text + " " + start_time_text + " - " + end_time_text
        except exceptions.TimeoutException:
            return None

    def get_schedule_info(self):
        """
        get the schedule info as a list
        :return: a schedule list, element consists of tuple
        """
        schedule_list = []
        counter = 0
        while True:
            try:
                schedule_name_elements = self.locate_element_list(self.schedule_name)
                schedule_mode_elements = self.locate_element_list(self.schedule_mode)
                schedule_icon_elements = self.locate_element_list(self.schedule_icon)
                schedule_time_elements = self.locate_element_list(self.schedule_time)

                for i in range(len(schedule_name_elements)):
                    schedule_name_element = schedule_name_elements[i]
                    schedule_name_text = self.get_element_attribute(schedule_name_element, "text")
                    #print("schedule_name_text", schedule_name_text)
                    schedule_mode_element = schedule_mode_elements[i]
                    schedule_mode_text = self.get_element_attribute(schedule_mode_element, "text")
                    #print("schedule_mode_text", schedule_mode_text)
                    schedule_icon_element = schedule_icon_elements[i]
                    schedule_icon_coordinates = self.get_element_coordinates(schedule_icon_element)
                    screenshot_base64 = self.get_screenshot_base64()
                    schedule_icon_image = self.crop_screenshot_and_compress_as_string(screenshot_base64, schedule_icon_coordinates)
                    schedule_time_element = schedule_time_elements[i]
                    schedule_time_text = self.get_element_attribute(schedule_time_element, "text")
                    #print("schedule_time_text", schedule_time_text)
                    schedule_list.append((schedule_name_text, schedule_mode_text, schedule_icon_image, schedule_time_text))
                return schedule_list
            except exceptions.TimeoutException:
                try:
                    product_settings_element = self.locate_element(self.device_settings)
                    #print("product_settings_element", product_settings_element)
                    if product_settings_element:
                        break
                except exceptions.TimeoutException:
                    # scroll up the screen to load more devices
                    #print("scroll up")
                    start_position_percent = self.set_position_on_screen((75, 75))
                    end_position_percent = self.set_position_on_screen((50, 50))
                    self.scroll_screen(start_position_percent, end_position_percent)
            # to stop the loop in 10 times
            counter += 1
            if counter > 9:
                break

    def change_schedule_info(self, schedule_label: str, start_time: str, end_time: str, mode: str, repeat: list,
                             new_schedule_label: str, result_action: str, am_pm=None, fanspeed=None, led=None):
        try:
            schedule_name_elements = self.locate_element_list(self.schedule_name)
            for schedule_name_element in schedule_name_elements:
                schedule_name_text = self.get_element_attribute(schedule_name_element, "text")
                if schedule_name_text == schedule_label:
                    self.tap_element(schedule_name_element)
        except exceptions.TimeoutException:
            return None

        # change the schedule
        self.set_new_schedule(start_time, end_time, mode, repeat, new_schedule_label, result_action,
                              am_pm, fanspeed, led)

    def delete_schedule_info(self, schedule_label: str, confirm_delete: str):
        """
        find the schedule and delete it
        :param schedule_label: the name of the schedule
        :param confirm_delete: if it's "delete", delete the schedule, if it's "cancel", do NOT delete the schedule
        :return: True or False if delete the schedule
        """
        schedule_counter = 0
        while True:
            try:
                tap_schedule_name_confirm = None
                schedule_name_elements = self.locate_element_list(self.schedule_name)
                for schedule_name_element in schedule_name_elements:
                    schedule_name_text = self.get_element_attribute(schedule_name_element, "text")
                    if schedule_name_text == schedule_label:
                        self.tap_element(schedule_name_element)
                        tap_schedule_name_confirm = True
                        break
                # break to jump out of the while loop
                if tap_schedule_name_confirm:
                    break

            except exceptions.TimeoutException:
                # swipe up the screen
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)

            # to stop the loop in 10 times
            schedule_counter += 1
            if schedule_counter > 9:
                break

        delete_counter = 0
        while True:
            try:
                schedule_delete_element = self.locate_element(self.schedule_delete)
                self.tap_element(schedule_delete_element)
                break
            except exceptions.TimeoutException:
                start_position_percent = self.set_position_on_screen((75, 75))
                end_position_percent = self.set_position_on_screen((50, 50))
                self.scroll_screen(start_position_percent, end_position_percent)
            # to stop the loop in 10 times
            delete_counter += 1
            if delete_counter > 9:
                break

        try:
            if confirm_delete == "delete":
                schedule_delete_confirm_element = self.locate_element(self.schedule_delete_confirm)
                self.tap_element(schedule_delete_confirm_element)
            if confirm_delete == "cancel":
                schedule_delete_cancel_element = self.locate_element(self.schedule_delete_cancel)
                self.tap_element(schedule_delete_cancel_element)
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.set_new_schedule.__name__)
            return None

        try:
            schedule_title_element = self.locate_element(self.schedule_title, waiting_time=10)
            schedule_title_text = self.get_element_attribute(schedule_title_element, "text")
            if schedule_title_text:
                return True
        except exceptions.TimeoutException:
            return None

    def tap_device_settings(self):
        counter = 0
        # for small screen, try to find the product settings button by swiping up
        while True:
            try:
                device_settings_element = self.locate_element(self.device_settings)
                self.tap_element(device_settings_element)
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
        # if more than 3 times swiping cannot find the add schedule, return None
        screenshot_base64 = self.get_screenshot_base64()
        self.save_image(screenshot_base64, self.tap_add_schedule.__name__)
        return None

    def set_device_name(self, new_name: str, confirm_save="save"):
        try:
            settings_names_elements = self.locate_element_list(self.settings_names)
            for settings_name_element in settings_names_elements:
                settings_name_text = self.get_element_attribute(settings_name_element, "text")
                if settings_name_text == "Custom Name":
                    settings_name_index = settings_names_elements.index(settings_name_element)
                    self.tap_element(settings_name_element)
                    device_name_element = self.locate_element(self.device_name)
                    self.set_element_text(device_name_element, new_name, hide_kb=False)
                    if confirm_save == "save":
                        device_name_save_element = self.locate_element(self.device_confirm_ok)
                        self.tap_element(device_name_save_element)
                        settings_values_elements = self.locate_element_list(self.settings_values)
                        settings_value_element = settings_values_elements[settings_name_index]
                        settings_value_text = self.get_element_attribute(settings_value_element, "text")
                        return settings_value_text

                    if confirm_save == "cancel":
                        device_name_cancel_element = self.locate_element(self.device_confirm_cancel)
                        self.tap_element(device_name_cancel_element)
                        return
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.set_device_name.__name__)
            return None

    def get_device_name(self):
        """
        get the device name from the device detail page, on the top of the page view beside the device icon
        :return: the device name
        """
        try:
            device_name_element = self.locate_element(self.device_title)
            device_name_text = self.get_element_attribute(device_name_element, "text")
            return device_name_text
        except exceptions.TimeoutException:
            return None

    def set_device_location(self):
        pass

    def set_device_led(self, led: str):
        """
        adjust led brightness in settings
        :param led: from 0% to 100%
        :return:
        """
        try:
            # the led brightness is an approximate value, cannot control accurately
            settings_led_bar_element = self.locate_element(self.led_brightness)
            factor = int(self.get_element_coordinates(settings_led_bar_element)["width"] / 100)
            brightness_bar_start_x = int(self.get_element_coordinates(settings_led_bar_element)["x"])
            brightness_bar_start_y = int(self.get_element_coordinates(settings_led_bar_element)["y"])
            brightness_bar_end_x = int(self.get_element_coordinates(settings_led_bar_element)["x"] +
                                       factor * int(led))
            brightness_bar_end_y = int(self.get_element_coordinates(settings_led_bar_element)["y"])
            self.scroll_screen((brightness_bar_start_x, brightness_bar_start_y),
                               (brightness_bar_end_x, brightness_bar_end_y))

            settings_names_elements = self.locate_element_list(self.settings_names)
            for settings_name_element in settings_names_elements:
                settings_name_text = self.get_element_attribute(settings_name_element, "text")
                if settings_name_text == "LED Brightness":
                    settings_name_index = settings_names_elements.index(settings_name_text)
                    settings_values_elements = self.locate_element_list(self.settings_values)
                    settings_value_element = settings_values_elements[settings_name_index]
                    settings_value_text = self.get_element_attribute(settings_value_element, "text")
                    return settings_value_text
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.set_device_led.__name__)
            return None

    def set_device_childlock(self, status: str):
        """
        set the child lock for the device
        :param status: status should be either "on" or "off"
        :return:
        """
        try:
            settings_childlock_element = self.locate_element(self.settings_childlock)
            settings_childlock_text = self.get_element_attribute(settings_childlock_element, "text")
            if settings_childlock_text != status.upper():
                self.tap_element(settings_childlock_element)
                settings_childlock_text = self.get_element_attribute(settings_childlock_element, "text")
                return settings_childlock_text
            else:
                return settings_childlock_text
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.set_device_childlock.__name__)
            return None

    def get_device_detail_info(self):
        # maybe need to scroll the screen
        try:
            settings_names_elements = self.locate_element_list(self.settings_names)
            for settings_name_element in settings_names_elements:
                settings_name_text = self.get_element_attribute(settings_name_element, "text")
                if settings_name_text == "Product Information":
                    self.tap_element(settings_name_element)
                    device_detail_info_names = self.locate_element_list(self.device_detail_info_name)
                    device_detail_info_names_texts = [self.get_element_attribute(device_detail_info_name, "text") for
                                                      device_detail_info_name in device_detail_info_names]
                    device_detail_info_values = self.locate_element_list(self.device_detail_info_value)
                    device_detail_info_values_texts = [self.get_element_attribute(device_detail_info_value, "text") for
                                                      device_detail_info_value in device_detail_info_values]
                    return {device_detail_info_names_texts[i]: device_detail_info_values_texts[i]
                            for i in range (len(device_detail_info_names))}
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.get_device_detail_info.__name__)
            return None

    def delete_onboarded_device(self, name: str, confirm_delete: str):
        try:
            delete_device_element = self.locate_element(self.delete_device)
            self.tap_element(delete_device_element)
            if confirm_delete == "delete":
                device_delete_ok_element = self.locate_element(self.device_confirm_ok)
                self.tap_element(device_delete_ok_element)
                main_page_device_list = page_object.main_page.MainPage(self.driver)
                device_list = main_page_device_list.get_devices_info(device=name, attr="device_name", scroll="yes", waiting_time=60)
                return device_list
            if confirm_delete == "cancel":
                device_delete_cancel_element = self.locate_element(self.device_confirm_cancel)
                self.tap_element(device_delete_cancel_element)
                return
        except exceptions.TimeoutException:
            screenshot_base64 = self.get_screenshot_base64()
            self.save_image(screenshot_base64, self.get_device_detail_info.__name__)
            return None