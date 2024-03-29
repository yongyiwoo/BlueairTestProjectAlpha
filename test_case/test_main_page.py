import os
import sys
sys.path.insert(0, "./")


from page_object.main_page import MainPage
from page_object.login_page import LoginPage
from page_object.forgot_password_page import ForgotPasswordPage
from page_object.register_page import RegisterPage
from page_object.side_menu_pages import SideMenuPages
from page_object.settings_pages import SettingsPages
from page_object.profile_page import ProfilePage
from page_object.dustmagnet_connection_pages import DustMagnetConnectionPages
from page_object.dustmagnet_detail_pages import DustMagnetDetailPages

#from page_object.device_connection_pages import DeviceConnectionPages
#from page_object.new_device_connection_pages import NewDeviceConnectionPages
from page_object.healthprotect_connection_pages import HealthProtectConnectionPages

from page_object.classic_connection_pages import ClassicConnectionPages
from util.file_manager import FileManager
import pytest
import allure
import time
from datetime import datetime
import re


@allure.feature("test the login feature")
class TestMainPage(object):
    '''
    def test_auto_add_classic_device(self, common_driver):  # auto add classic
        main_page = MainPage(common_driver)
        classic_connection_pages = ClassicConnectionPages(common_driver)
        main_page.device_connection_pages = classic_connection_pages
        main_page.add_new_device()
        classic_connection_pages.find_device_page()
        #classic_connection_pages.connect_wifi_page("28116194", sleep_time=30) # need to press wifi button on the unit

        classic_connection_pages.connect_wifi_page("28116194", sleep_time=10)
        classic_connection_pages.name_device_page("classic")
        device_added_result = classic_connection_pages.finalize_device_page("classic")

        assert device_added_result == "classic"

    '''
    def test_onboard_healthprotect_device(self, common_driver):
        main_page = MainPage(common_driver)
        healthprotect_connection_pages = HealthProtectConnectionPages(common_driver)

        main_page.tap_connect_product()

        # Blueair products page
        device_image_result = healthprotect_connection_pages.check_device_image("HealthProtect")
        healthprotect_connection_pages.tap_device_name("HealthProtect")

        # Find your Device page
        hp_7410i_index = healthprotect_connection_pages.locate_device_by_mac_address("A8:03:2A:EC:94:8C")
        device_icon_result = healthprotect_connection_pages.check_device_icon(hp_7410i_index)
        
        device_name = healthprotect_connection_pages.check_device_name(hp_7410i_index)

        device_model_type = healthprotect_connection_pages.check_model_name(hp_7410i_index)

        device_connected_label = healthprotect_connection_pages.check_connected_label(hp_7410i_index)

        device_connected_name = healthprotect_connection_pages.check_connected_name(hp_7410i_index)

        search_message_status = healthprotect_connection_pages.check_search_message_appears()

        search_icon_status = healthprotect_connection_pages.check_search_icon_appears()

        # tap the device to onboard
        healthprotect_connection_pages.tap_mac_address(hp_7410i_index)
        device_connected_label_pressed = healthprotect_connection_pages.check_connected_label(hp_7410i_index)

        search_message_status_pressed = healthprotect_connection_pages.check_search_message_appears()

        search_icon_status_pressed = healthprotect_connection_pages.check_search_icon_appears()

        # Wifi page
        healthprotect_connection_pages.tap_wifi_ssid("Yongyi")
        healthprotect_connection_pages.input_wifi_password("28116194")

        # naming page
        healthprotect_connection_pages.input_device_name("test7410i")

        # navigate back to the main if the main page does not appear
        while not main_page.check_side_menu_icon_appears():
            if healthprotect_connection_pages.check_select_device_page_appears():
                healthprotect_connection_pages.close_select_device_page()
            else:
                healthprotect_connection_pages.navigate_back()

        # wait until the device is online then check the device status
        device_onboard_status = main_page.get_device_status("test7410i", device_mode=True, aqi_level=True, offline_icon=True, aqi_icon=True,
                                                                clean_air=True, clean_air_bar=True, welcome_home=True)

        assert device_image_result is True
        assert device_icon_result is True
        assert device_name == "HealthProtect"
        assert device_model_type == "HealthProtect 7410i"
        assert device_connected_label == "Available"
        assert device_connected_name is None
        assert search_message_status is True
        assert search_icon_status is True
        assert device_connected_label_pressed == "Connecting…"
        assert search_message_status_pressed is False
        assert search_icon_status_pressed is False
        assert device_onboard_status == ("test7410i", "Fan Speed 0%", "Excellent", "Blue", None, "Your air is clean!", "100.0", None)

    '''
    @allure.story("test onboard b4 device")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_onboard_b4_device(self, common_driver):
        main_page = MainPage(common_driver)
        dustmagnet_connection_pages = DustMagnetConnectionPages(common_driver)
        main_page.device_connection_pages = dustmagnet_connection_pages
        main_page.add_new_device()
        dustmagnet_connection_pages.find_device_page()
        wifi_config_text = FileManager.read_file_lines("wifi.txt")[0]
        ssid = FileManager.read_json_string(wifi_config_text)["ssid"]
        password = FileManager.read_json_string(wifi_config_text)["password"]
        dustmagnet_connection_pages.connect_wifi_page(ssid, password, sleep_time=10)
        dustmagnet_connection_pages.name_device_page("b4_5210i")
        time.sleep(30)  # firmware issue, the wifi module needs to restart
        device_added_result = dustmagnet_connection_pages.finalize_device_page("b4_5210i")

        assert device_added_result == "b4_5210i"

    @allure.story("test b4 online status")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_online_status(self, common_driver):
        """
        b4 device online status check
        """
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        device_online_count = 0
        for check_times in range(3):    # check online status times in range()
            device_mode = main_page.get_devices_info(device, "device_mode", waiting_time=10)
            if device_mode != "Offline":
                device_online_count += 1
            main_page.put_background(-1)
            for idle_time in range(1):  # idle time in range(minute) for de-active the app in the background
                main_page.turn_on_screen()
                time.sleep(60)
            main_page.put_foreground()
        assert device_online_count == 3

    @allure.story("test swipe device layout left manual to night mode")
    @allure.severity(allure.severity_level.NORMAL)
    def test_swipe_device_layout_left_manual_to_night_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_left(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_night_mode(True)
        main_page.swipe_device_layout_left_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        assert device_mode == "Night"

    @allure.story("test swipe device layout left night to manual mode")
    @allure.severity(allure.severity_level.NORMAL)
    def test_swipe_device_layout_left_night_to_manual_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_left(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_night_mode(False)
        main_page.swipe_device_layout_left_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        assert device_mode == "Fan Speed 12%"

    @allure.story("test swipe device layout left manual to auto mode")
    @allure.severity(allure.severity_level.NORMAL)
    def test_swipe_device_layout_left_manual_to_auto_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_left(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_auto_mode(True)
        main_page.swipe_device_layout_left_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        assert device_mode == "Auto"

    @allure.story("test swipe device layout left auto to manual mode")
    @allure.severity(allure.severity_level.NORMAL)
    def test_swipe_device_layout_left_auto_to_manual_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_left(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_auto_mode(False)
        main_page.swipe_device_layout_left_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        assert device_mode == "Fan Speed 12%"

    @allure.story("test swipe device layout right manual to standby mode")
    @allure.severity(allure.severity_level.NORMAL)
    def test_swipe_device_layout_right_manual_to_standby_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_right(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_standby_mode(True)
        main_page.swipe_device_layout_right_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        assert device_mode == "Standby"

    @allure.story("test swipe device layout left standby to manual mode")
    @allure.severity(allure.severity_level.NORMAL)
    def test_swipe_device_layout_left_standby_to_manual_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_right(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_standby_mode(False)
        main_page.swipe_device_layout_right_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        time.sleep(60)  # sensor warm up time
        assert device_mode == "Fan Speed 12%"

    @allure.story("test navigate to b4")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_b4(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        # need to wait for 10 seconds to load the main UI
        time.sleep(10)
        navi_result = main_page.tap_device(device)
        assert navi_result

    @allure.story("test b4 auto mode on")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_auto_mode_on(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_auto_mode(True)
        mode_info = dustmagnet_detail_pages.get_mode_info()
        assert mode_info == "Auto Mode"

    @allure.story("test b4 auto mode off")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_auto_mode_off(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_auto_mode(False)
        mode_info = dustmagnet_detail_pages.get_manual_mode_info()
        assert mode_info[0] == "Fan speed" and mode_info[1] == "33.0"

    @allure.story("test b4 night mode on")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_night_mode_on(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_night_mode(True)
        mode_info = dustmagnet_detail_pages.get_mode_info()
        assert mode_info == "Night Mode"

    @allure.story("test b4 night mode off")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_night_mode_off(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_night_mode(False)
        mode_info = dustmagnet_detail_pages.get_manual_mode_info()
        assert mode_info[0] == "Fan speed" and mode_info[1] == "33.0"

    @allure.story("test b4 standby mode on")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_standby_mode_on(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_standby_mode(False)
        mode_info = dustmagnet_detail_pages.get_mode_info()
        assert mode_info == "Air purifier is turned off at the moment"

    @allure.story("test b4 standby mode off")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_standby_mode_off(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_standby_mode(True)
        mode_info = dustmagnet_detail_pages.get_manual_mode_info()
        assert mode_info[0] == "Fan speed" and mode_info[1] == "33.0"

    @allure.story("test b4 manual mode fan speed 0")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_manual_mode_fanspeed_0(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("0.0")
        time.sleep(5)
        assert fan_speed == "0.0"

    @allure.story("test b4 manual mode fan speed 1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_manual_mode_fanspeed_1(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("33.0")
        time.sleep(5)
        assert fan_speed == "33.0"

    @allure.story("test b4 manual mode fan speed 1.5")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_manual_mode_fanspeed_1_5(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("51.0")
        time.sleep(5)
        assert fan_speed == "51.0"

    @allure.story("test b4 manual mode fan speed 2")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_manual_mode_fanspeed_2(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("66.0")
        time.sleep(5)
        assert fan_speed == "66.0"

    @allure.story("test b4 manual mode fan speed 2.5")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_manual_mode_fanspeed_2_5(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("84.0")
        time.sleep(5)
        assert fan_speed == "84.0"

    @allure.story("test b4 manual mode fan speed 3")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_manual_mode_fanspeed_3(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("99.0")
        time.sleep(5)
        assert fan_speed == "99.0"

    @allure.story("test b4 manual mode fan speed 1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_back_manual_mode_fanspeed_1(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("33.0")
        time.sleep(5)
        assert fan_speed == "33.0"

    @allure.story("test b4 filter usage check")
    @allure.severity(allure.severity_level.MINOR)
    def test_b4_filter_usage(self, common_driver):  # can't do exact compare the filter
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        filter_usage = dustmagnet_detail_pages.get_filter_info()
        assert filter_usage[0] == filter_usage[1]
    
    @allure.story("test b4 navigate to schedule auto")
    @allure.severity(allure.severity_level.NORMAL)
    def test_b4_navigate_to_schedule_auto(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        tap_result = dustmagnet_detail_pages.tap_add_schedule()
        assert tap_result
    
    @allure.story("test b4 set schedule auto")
    @allure.severity(allure.severity_level.NORMAL)
    def test_b4_set_schedule_auto(self, common_driver): # need a file to read all the schedule settings
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        start_time = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(minutes=2), "%H:%M")
        end_time = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(minutes=4), "%H:%M")
        schedule_result = dustmagnet_detail_pages.set_new_schedule(start_time, end_time, "auto", [0, 1, 2, 3, 4, 5 ,6],
                                                                   "b4_schedule_auto" , "save")
        assert schedule_result

    @allure.story("test b4 check schedule auto on")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_check_schedule_auto_on(self, common_driver):
        schedule_mode = None
        schedule_end_time = None

        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        schedule_result_list = dustmagnet_detail_pages.get_schedule_info()
        for schedule_result in schedule_result_list:
            schedule_name = schedule_result[0]
            if schedule_name == "b4_schedule_auto":
                schedule_mode = schedule_result[1]
                schedule_end_time = re.findall("[0-9][0-9]:[0-9][0-9]", schedule_result[-1])[0]
                break

        if schedule_end_time:
            current_time = datetime.datetime.strptime(datetime.datetime.strftime(datetime.datetime.now(), "%H:%M"),
                                                      "%H:%M")
            schedule_time = datetime.datetime.strptime(schedule_end_time, "%H:%M")
            time.sleep(int(datetime.timedelta.total_seconds(schedule_time - current_time) + 60))

        mode_info = dustmagnet_detail_pages.get_mode_info().split(" ")[0]

        assert schedule_mode == mode_info and mode_info is not None

    @allure.story("test b4 check schedule auto off")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_check_schedule_auto_off(self, common_driver):
        schedule_mode = None
        schedule_end_time = None

        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        schedule_result_list = dustmagnet_detail_pages.get_schedule_info()
        for schedule_result in schedule_result_list:
            schedule_name = schedule_result[0]
            if schedule_name == "b4_schedule_auto":
                schedule_mode = schedule_result[1]
                schedule_end_time = re.findall("[0-9][0-9]:[0-9][0-9]", schedule_result[-1])[-1]
                break

        if schedule_end_time:
            current_time = datetime.datetime.strptime(datetime.datetime.strftime(datetime.datetime.now(), "%H:%M"),
                                                      "%H:%M")
            schedule_time = datetime.datetime.strptime(schedule_end_time, "%H:%M")
            # wait 1 more minute (+ 60) till the schedule is done
            time.sleep(int(datetime.timedelta.total_seconds(schedule_time - current_time)) + 60)

        mode_info = dustmagnet_detail_pages.get_mode_info().split(" ")[0]
        fan_speed = dustmagnet_detail_pages.get_manual_mode_info()[1]

        assert schedule_mode != mode_info and mode_info is not None and fan_speed == "33.0"

    @allure.story("test b4 navigate to schedule manual2")
    @allure.severity(allure.severity_level.NORMAL)
    def test_b4_navigate_to_schedule_manual2(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        tap_result = dustmagnet_detail_pages.tap_add_more_schedule()
        assert tap_result

    @allure.story("test b4 set schedule manual2")
    @allure.severity(allure.severity_level.NORMAL)
    def test_b4_set_schedule_manual2(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        start_time = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(minutes=2), "%H:%M")
        end_time = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(minutes=4), "%H:%M")
        schedule_result = dustmagnet_detail_pages.set_new_schedule(start_time, end_time, "manual",
                                                                   [0, 1, 2, 3, 4, 5 ,6], "b4_schedule_manual2" ,
                                                                   "save", fanspeed="66.0", led="50")
        assert schedule_result

    @allure.story("test b4 check schedule manual2 on")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_check_schedule_manual2_on(self, common_driver):
        schedule_mode = None
        schedule_end_time = None

        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        schedule_result_list = dustmagnet_detail_pages.get_schedule_info()
        for schedule_result in schedule_result_list:
            schedule_name = schedule_result[0]
            if schedule_name == "b4_schedule_manual2":
                schedule_mode = schedule_result[1]
                schedule_end_time = re.findall("[0-9][0-9]:[0-9][0-9]", schedule_result[-1])[0]
                break

        if schedule_end_time:
            current_time = datetime.datetime.strptime(datetime.datetime.strftime(datetime.datetime.now(), "%H:%M"),
                                                      "%H:%M")
            schedule_time = datetime.datetime.strptime(schedule_end_time, "%H:%M")
            time.sleep(int(datetime.timedelta.total_seconds(schedule_time - current_time)) + 60)

        mode_info = dustmagnet_detail_pages.get_mode_info()
        fan_speed = dustmagnet_detail_pages.get_manual_mode_info()[1]

        assert schedule_mode == mode_info and mode_info is not None and fan_speed == "66.0"
    
    @allure.story("test b4 check schedule auto off")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_check_schedule_manual2_off(self, common_driver):  # need to read from a file with all the schedule settings
        schedule_mode = None
        schedule_end_time = None

        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        schedule_result_list = dustmagnet_detail_pages.get_schedule_info()
        for schedule_result in schedule_result_list:
            schedule_name = schedule_result[0]
            if schedule_name == "b4_schedule_manual2":
                schedule_mode = schedule_result[1]
                schedule_end_time = re.findall("[0-9][0-9]:[0-9][0-9]", schedule_result[-1])[-1]
                break

        if schedule_end_time:
            current_time = datetime.datetime.strptime(datetime.datetime.strftime(datetime.datetime.now(), "%H:%M"),
                                                      "%H:%M")
            schedule_time = datetime.datetime.strptime(schedule_end_time, "%H:%M")
            # wait 1 more minutes (+ 60) till the schedule is done
            time.sleep(int(datetime.timedelta.total_seconds(schedule_time - current_time)) + 60)

        mode_info = dustmagnet_detail_pages.get_mode_info()
        fan_speed = dustmagnet_detail_pages.get_manual_mode_info()[1]

        assert schedule_mode == mode_info and mode_info is not None and fan_speed == "33.0"
    
    @allure.story("test b4 delete schedule auto")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_delete_schedule_auto(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        delete_schedule_result = dustmagnet_detail_pages.delete_schedule_info("b4_schedule_auto", "delete")
        assert delete_schedule_result

    @allure.story("test b4 delete schedule manual2")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_delete_schedule_manual2(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        delete_schedule_result = dustmagnet_detail_pages.delete_schedule_info("b4_schedule_manual2", "delete")
        assert delete_schedule_result

    @allure.story("test b4 change device name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b4_change_name(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_device_settings()
        changed_name = dustmagnet_detail_pages.set_device_name("b4_5210i_change")
        dustmagnet_detail_pages.navigate_back()
        device_name = dustmagnet_detail_pages.get_device_name()
        assert changed_name == device_name

    @allure.story("test b4 device info")
    @allure.severity(allure.severity_level.NORMAL)
    def test_b4_device_info(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_device_settings()
        info = dustmagnet_detail_pages.get_device_detail_info()
        dustmagnet_detail_pages.navigate_back()
        # need to get the value from a config file
        assert info == {"Product Type": "DustMagnet 5210i", "MAC Address": "a8:03:2a:e5:8b:d4",
                        "Serial Number": "110590900001110110000142", "WiFi Firmware": "2.2.3", "MCU Firmware": "2.2.3"}

    @allure.story("test b4 delete onboarded device")
    @allure.severity(allure.severity_level.NORMAL)
    def test_b4_device_delete(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        device = dustmagnet_detail_pages.delete_onboarded_device("b4_5210i", "delete")
        assert device is None

    
    @allure.story("test onboard b4 device restart the app before ssid")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_onboard_b4_before_ssid(self, common_driver):
        main_page = MainPage(common_driver)
        dustmagnet_connection_pages = DustMagnetConnectionPages(common_driver)
        main_page.device_connection_pages = dustmagnet_connection_pages
        dustmagnet_select_page = main_page.add_new_device()
        dustmagnet_select_page.get("DustMagnet_image")
        dustmagnet_connection_pages.find_device_page()
        dustmagnet_connection_pages.put_background()
        time.sleep(30)   # wait for 30 seconds to restart the app
        dustmagnet_connection_pages.put_foreground()
        device_onboard_result = main_page.get_devices_info("b4_5210i")
        assert device_onboard_result is None

    @allure.story("test onboard b4 device restart the app after ssid")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_onboard_b4_before_ssid(self, common_driver):
        main_page = MainPage(common_driver)
        dustmagnet_connection_pages = DustMagnetConnectionPages(common_driver)
        main_page.device_connection_pages = dustmagnet_connection_pages
        dustmagnet_select_page = main_page.add_new_device()
        dustmagnet_select_page.get("DustMagnet_image")
        dustmagnet_connection_pages.find_device_page()
        dustmagnet_connection_pages.connect_wifi_page("28116194")
        time.sleep(10)  # wait for 10 seconds to let the app react with the password
        dustmagnet_connection_pages.put_background()
        time.sleep(30)   # wait for 30 seconds to restart the app
        dustmagnet_connection_pages.put_foreground()
        device_onboard_result = main_page.get_devices_info("b4_5210i")
        assert device_onboard_result is None
    
    '''
    ####################################################################################################
    #                                          login test cases                                        #
    ####################################################################################################

    @allure.story("01 test login with unregistered username and a password")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_unregistered_username_and_a_password(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. input an unregistered username and a password and press log in button
        4. wait for 20 seconds, to check the popup text
        5. go back to the main page
        result:
        1. the app shows message: "There is no user with that email"
        2. user has NOT logged in and back to the main page
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        login_pages.input_username_password_login("unregistered@mailinator.com", "Abcd1234.")

        message_shows_up_result = login_pages.wait_until_unregistered_email_message_appears()
        login_pages.close_login_page()
        # sometimes checking needs more time, so to make sure back to the main page
        if not main_page.check_side_menu_icon_appears():
            login_pages.navigate_back()

        assert message_shows_up_result == True

    @allure.story("02 test login with invalid username and a password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_invalid_username_and_a_password(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. input an invalid username and a password and press log in button
        4. wait for 20 seconds, to check the popup text
        5. go back to the main page
        result:
        1. the app shows message: "Email is invalid"
        2. user has NOT logged in and back to the main page
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        login_pages.input_username_password_login("test@mailinator", "Abcd1234.")

        message_shows_up_result = login_pages.wait_until_invalid_email_message_appears()
        login_pages.close_login_page()
        # sometimes checking needs more time, so to make sure back to the main page
        if not main_page.check_side_menu_icon_appears():
            login_pages.navigate_back()

        assert message_shows_up_result == True

    @allure.story("03 test login with blank username and a password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_blank_username_and_a_password(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. input a blank username and a password and press log in button
        4. go back to the main page
        result:
        1. user has NOT logged in and back to the main page
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        login_pages.input_username_password_login("", "Abcd1234.")

        login_pages.close_login_page()

        login_result = main_page.check_login_appears()
        side_menu_result = main_page.check_side_menu_icon_appears()

        assert (login_result, side_menu_result) == (True, True)

    @allure.story("04 test login with correct username and not complex password") # password is less than 6 characters
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_correct_username_and_not_complex_password(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. input a username and a password that less than 8 characters and press log in button
        4. wait for 20 seconds, to check the popup text
        5. go back to the main page
        result:
        1. the app shows message: "The password doesn’t meet complexity requirements"
        2. user has NOT logged in and back to the main page
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        login_pages.input_username_password_login("test_202202@mailinator.com", "12345")

        message_shows_up_result = login_pages.wait_until_complexity_password_message_appears()
        login_pages.close_login_page()

        assert message_shows_up_result == True

    @allure.story("05 test login with correct username and incorrect password")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_correct_username_and_incorrect_password(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. input a username and an incorrect password and press log in button
        4. go back to the main page
        result:
        1. the app shows message: "Email is invalid"
        2. user has NOT logged in and back to the main page
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        login_pages.input_username_password_login("test_202202@mailinator.com", "incorrect_password")

        message_shows_up_result = login_pages.wait_until_invalid_password_message_appears()
        login_pages.navigate_back()
        # sometimes checking needs more time, so to make sure back to the main page
        if not main_page.check_side_menu_icon_appears():
            login_pages.navigate_back()

        assert message_shows_up_result == True

    @allure.story("06 test login without network")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_without_network(self, common_driver):
        """
        steps:
        1. turn off the phone wifi
        2. in the app main page, press the sign in button
        3. navigate to the login page
        4. input a username and an incorrect password and press log in button
        5. go back to the main page
        result:
        1. the app shows message: "The Internet connection appears to be offline."
        2. user has NOT logged in and back to the main page
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.set_connection(0)
        main_page.tap_user_login()
        login_pages.input_username_password_login("test_202202@mailinator.com", "Abcd1234.")

        message_shows_up_result = login_pages.wait_until_connection_lost_message_appears()
        login_pages.close_login_page()
        main_page.set_connection(6)
        # sometimes checking needs more time, so to make sure back to the main page
        if not main_page.check_side_menu_icon_appears():
            login_pages.navigate_back()

        assert message_shows_up_result == True
    
    @allure.story("07 test login with correct username and blank password")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_correct_username_and_blank_password(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. input a username and a blank password and press log in button
        4. go back to the main page
        result:
        1. user has NOT logged in and back to the main page
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        login_pages.input_username_password_login("test_202202@mailinator.com", "")

        login_pages.close_login_page()

        login_result = main_page.check_login_appears()
        side_menu_result = main_page.check_side_menu_icon_appears()

        assert (login_result, side_menu_result) == (True, True)
    
    @allure.story("08 test login with correct username and password")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_correct_username_and_password(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. input the correct username and password and press log in button
        4. wait for 20 seconds
        result:
        1. user has logged in
        2. the app goes back to the main page
        :param common_driver:
        :return: pass if sign in button disappeared
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        login_pages.input_username_password_login("test_202202@mailinator.com", "Abcd1234.")

        login_result = main_page.check_login_appears()
        side_menu_result = main_page.check_side_menu_icon_appears()

        assert (login_result, side_menu_result) == (False, True)

    @allure.story("09 test log out with app")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_logout_with_app(self, common_driver):
        """
        steps:
        1. in the app main page, press side menu
        2. in the side menu, press log out
        3. in the popup window, press yes
        result:
        1. the app logs out
        2. the app goes back to the main page
        :param common_driver:
        :return: pass, terms of service shows
        """
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)

        # check if test case login with blueair account pass
        if main_page.check_login_appears():
            login_result = False
            side_menu_result = False
        else:
            main_page.tap_side_menu()
            side_menu_pages.tap_log_out(True)
            side_menu_pages.close_side_menu_use_close_button()

            login_result = main_page.check_login_appears()
            side_menu_result = main_page.check_side_menu_icon_appears()

        assert (login_result, side_menu_result) == (True, True)

    @allure.story("10 test login with facebook account")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_facebook_account(self, common_driver):
        """
        steps:
        1. in the app main page, press sign in button
        2. navigate to the login page
        3. press continue with facebook button
        result:
        1. user has logged in with preset facebook account
        2. the app goes back to the main page
        :param common_driver:
        :return: pass, if sign in button disappeared
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_continue_with_facebook()

        login_result = main_page.check_login_appears()
        side_menu_result = main_page.check_side_menu_icon_appears()
        # sometimes facebook has some issues and cannot login, so to make sure back to the main page
        if not main_page.check_side_menu_icon_appears():
            login_pages.navigate_back()

        assert (login_result, side_menu_result) == (True, False)

    @allure.story("11 test log out with facebook")
    @allure.severity(allure.severity_level.NORMAL)
    def test_logout_with_facebook(self, common_driver):
        """
        steps:
        1. in the app main page, press side menu
        2. in the side menu, press log out
        3. in the popup window, press yes
        result:
        1. the app logs out
        2. the app goes back to the main page
        :param common_driver:
        :return: pass, terms of service shows
        """
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)

        # check if test case login with facebook account pass
        if main_page.check_login_appears():
            login_result = False
            side_menu_result = False
        else:
            main_page.tap_side_menu()
            side_menu_pages.tap_log_out(True)
            side_menu_pages.close_side_menu_use_close_button()

            login_result = main_page.check_login_appears()
            side_menu_result = main_page.check_side_menu_icon_appears()

        assert (login_result, side_menu_result) == (True, True)

    @allure.story("12 test login with google account")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_google_account(self, common_driver):
        """
        steps:
        1. in the app main page, press sign in button
        2. navigate to the login page
        3. press continue with google button
        4. then press google account
        result:
        1. user has logged in with google account
        2. the app goes back to the main page
        :param common_driver:
        :return: pass, if sign in button disappeared
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_continue_with_google()

        login_result = main_page.check_login_appears()
        side_menu_result = main_page.check_side_menu_icon_appears()

        # sometimes google has some issues and cannot login, so to make sure back to the main page
        if not main_page.check_side_menu_icon_appears():
            login_pages.navigate_back()

        assert (login_result, side_menu_result) == (False, True)

    @allure.story("13 test log out with google")
    @allure.severity(allure.severity_level.NORMAL)
    def test_logout_with_google(self, common_driver):
        """
        steps:
        1. in the app main page, press side menu
        2. in the side menu, press log out
        3. in the popup window, press yes
        result:
        1. the app logs out
        2. the app goes back to the main page
        :param common_driver:
        :return: pass, terms of service shows
        """
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)

        # check if test case login with google account pass
        if main_page.check_login_appears():
            login_result = False
            side_menu_result = False
        else:
            main_page.tap_side_menu()
            side_menu_pages.tap_log_out(True)
            side_menu_pages.close_side_menu_use_close_button()

            login_result = main_page.check_login_appears()
            side_menu_result = main_page.check_side_menu_icon_appears()

        assert (login_result, side_menu_result) == (True, True)

    @allure.story("14 test terms of service")
    @allure.severity(allure.severity_level.MINOR)
    def test_login_terms_of_service(self, common_driver):
        """
        steps:
        1. in the app main page, press sign in button
        2. navigate to the login page
        3. press terms of service
        4. go back to the main page
        result:
        1. the app shows terms of services
        2. the app goes back to the main page
        :param common_driver:
        :return: pass, terms of service shows
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        terms_of_service_result = login_pages.check_terms_of_service()

        login_pages.navigate_back(2) # navigate back to login page then to main page

        assert terms_of_service_result == True

    @allure.story("15 test privacy policy")
    @allure.severity(allure.severity_level.MINOR)
    def test_login_privacy_policy(self, common_driver):
        """
        steps:
        1. in the app main page, press sign in button
        2. navigate to the login page
        3. press privacy policy
        4. go back to the main page
        result:
        1. the app shows privacy policy
        2. the app goes back to the main page
        :param common_driver:
        :return: pass, privacy policy shows
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)

        main_page.tap_user_login()
        privacy_policy_result = login_pages.check_privacy_policy()

        login_pages.navigate_back(2)  # navigate back to login page then to main page

        assert privacy_policy_result == True

    ####################################################################################################
    #                                    forgot password test cases                                    #
    ####################################################################################################

    @allure.story("16 test forgot password reset success")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_forgot_password_reset_success(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. in the login page, press the forgot password link
        4. navigate to the forgot password page
        5. input the correct username (test_forgot_password@icloud.com) and press reset password button
        4. wait for 20 seconds, check the popup text
        5. go back to the login page
        result:
        1. the app goes back to login page
        2. the app shows message: "A password reset link was sent to your email"
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        forgot_password_page = ForgotPasswordPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_forgot_password()
        forgot_password_page.input_username_reset_password("test_forgot_password@icloud.com")

        message_result = forgot_password_page.wait_until_password_reset_message_appears()
        login_page_result = login_pages.check_login_page_status()

        login_pages.navigate_back()

        # wait for 1 minutes to check if there is a forgot password email
        time.sleep(60)
        email_result = forgot_password_page.check_forgot_password_email()

        assert (message_result, login_page_result, email_result) == (True, True, True)

    @allure.story("17 test forgot password with invalid username")
    @allure.severity(allure.severity_level.NORMAL)
    def test_forgot_password_with_invalid_username(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. in the login page, press the forgot password link
        4. navigate to the forgot password page
        5. input the invalid username and press reset password button
        6. check the popup text
        7. go back to the login page
        result:
        1. the app goes back to main page
        2. the app shows message: "Email is invalid"
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        forgot_password_page = ForgotPasswordPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_forgot_password()
        forgot_password_page.input_username_reset_password("test_202202@mailinator")

        message_shows_up_result = forgot_password_page.wait_until_invalid_email_message_appears()

        forgot_password_page.close_forgot_password_page_use_close_button()
        main_page_status_result = main_page.check_login_appears()

        assert message_shows_up_result, main_page_status_result == (True, True)

    @allure.story("18 test forgot password with unregistered username")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_forgot_password_with_unregistered_username(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. in the login page, press the forgot password link
        4. navigate to the forgot password page
        5. input an unregistered username and press reset password button
        4. check the popup text
        5. go back to the login page
        result:
        1. the app shows message: "There is no user with that email"
        2. the app goes back to login page
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        forgot_password_page = ForgotPasswordPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_forgot_password()
        forgot_password_page.input_username_reset_password("unregistered@mailinator.com")

        message_shows_up_result = forgot_password_page.wait_until_unregistered_email_message_appears()

        forgot_password_page.close_forgot_password_page_use_back_button()
        login_page_status_result = login_pages.check_login_page_status()

        assert message_shows_up_result, login_page_status_result == (True, True)

    @allure.story("19 test forgot password without network")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_forgot_password_without_network(self, common_driver):
        """
        steps:
        1. turn off the phone wifi
        2. in the app main page, press the sign in button
        3. navigate to the login page
        4. press the forgot password link
        5. input a valid username and press reset password button
        6. check out the popup text
        5. go back to the login page
        result:
        1. the app shows message: "Please check your internet connection"
        2. the app goes back to login page
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        forgot_password_page = ForgotPasswordPage(common_driver)

        main_page.set_connection(0)
        main_page.tap_user_login()
        login_pages.tap_forgot_password()
        forgot_password_page.input_username_reset_password("test_202202@mailinator.com")

        message_shows_up_result = forgot_password_page.wait_until_check_internet_connection_message_appears()
        login_pages.close_login_page()
        main_page.set_connection(6)
        # sometimes checking needs more time, so to make sure back to the main page
        if not main_page.check_side_menu_icon_appears():
            login_pages.navigate_back()

        assert message_shows_up_result == True

    ####################################################################################################
    #                                        register test cases                                       #
    ####################################################################################################

    @allure.story("20 test register without filling required fields")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_without_filling_required_fields(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. in the login page, press the register link
        4. navigate to the register page
        5. leave the required fields blank and tick the required checkboxes and press register button
        6. wait for several seconds, check if the error messages show up
        7. close the register page and back to the main page
        result:
        1. the error messages show up in register page
        2. the app goes back to the main page with Sign in link
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        register_page = RegisterPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_register()
        register_page.input_required_fields_register("", "", "", "", "", "", True, False, False, True)

        first_name_error_message_result = register_page.check_enter_your_first_name_message_appears()
        last_name_error_message_result = register_page.check_enter_your_last_name_message_appears()
        email_error_message_result = register_page.check_enter_your_email_message_appears()
        password_error_message_result = register_page.check_enter_your_password_message_appears()
        error_message_appears_result = (first_name_error_message_result, last_name_error_message_result,
                                         email_error_message_result, password_error_message_result)


        date_time = datetime.today().strftime('%Y%m%d%H%M%S')
        register_page.input_required_fields_register("Firstname", "Lastname", date_time + "@mailinator.com", "",
                                                     "Abcd1234.", "", False, False, False, False)

        # there are several redundant scroll up, because of trying to find error messages (but error messages disappear)
        first_name_error_message_result = register_page.check_enter_your_first_name_message_appears()
        last_name_error_message_result = register_page.check_enter_your_last_name_message_appears()
        email_error_message_result = register_page.check_enter_your_email_message_appears()
        password_error_message_result = register_page.check_enter_your_password_message_appears()
        error_message_disappears_result = (first_name_error_message_result, last_name_error_message_result,
                                           email_error_message_result, password_error_message_result)

        register_result = (error_message_appears_result, error_message_disappears_result)

        register_page.close_register_page_use_close_button()

        assert register_result == ((True, True, True, True), (False, False, False, False))

    @allure.story("21 test register password match")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_password_match(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. in the login page, press the register link
        4. navigate to the register page
        5. fill the password with valid format and leave other required fields blank
        6. tick the required checkboxes and press register button
        7. wait for several seconds, check if the password doesn't match message appears
        8. fill the password and confirm password with the same valid format
        9. press register button, check if the password doesn't match message disappears
        10. fill the password and confirm password with different valid format
        11. press register button, check if the password doesn't match message appears
        12. close the register page and back to the main page
        result:
        1. the password doesn't match message appears in register page
        2. the password doesn't match message disappears in register page
        3. the password doesn't match message appears in register page
        4. the app goes back to the main page with Sign in link
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        register_page = RegisterPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_register()
        register_page.input_required_fields_register("", "", "", "", "Abcd1234.", "", True, False, False, True)

        password_match_error_message_result = register_page.check_password_does_not_match_message_appears()
        error_message_appears_result_with_empty_password = password_match_error_message_result

        # change the password field to blank because don't need to input anything
        # need to refactor, refer to test_register_without_filling_required_fields
        register_page.input_required_fields_register("", "", "", "", "", "Abcd1234.", False, False, False, False)

        # there are several redundant scroll up, because of trying to find error messages (but error messages disappear)
        password_match_error_message_result = register_page.check_password_does_not_match_message_appears()
        error_message_disappears_result = password_match_error_message_result

        # change the password field to blank because don't need to input anything
        # need to refactor, refer to test_register_without_filling_required_fields
        register_page.input_required_fields_register("", "", "", "", "", "Abcd1234..", False, False, False,
                                                     False)
        password_match_error_message_result = register_page.check_password_does_not_match_message_appears()
        error_message_appears_result_with_different_password = password_match_error_message_result

        register_result = (error_message_appears_result_with_empty_password, error_message_disappears_result,
                           error_message_appears_result_with_different_password)

        register_page.close_register_page_use_close_button()

        assert register_result == (True, False, True)

    @allure.story("22 test register password complexity")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_password_complexity(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. in the login page, press the register link
        4. navigate to the register page
        5. fill the password with invalid format below
           5.1. less than 8 characters (Abc123.)
           5.2. at least 8 characters with lower case, at least 1 number, 0 special symbol (abcd1234)
           5.3. at least 8 characters with upper case, at least 1 number, 0 special symbol (ABCD1234)
           5.4. at least 8 characters with upper and lower case, 0 number, 0 special symbol (ABCDabcd)
           5.5. at least 8 characters with lower case, 0 number, at least 1 special symbol (abcd.,-?)
           5.6. at least 8 characters with upper case, 0 number, at least 1 special symbol (ABCD.,-?)
           5.7. at least 8 characters without letter, at least 1 number, at least 1 special symbol (1234.,-?)
        6. leave other required fields blank
        7. tick the required checkboxes and press register button
        8. close the register page and back to the main page
        result:
        1. the password doesn't meet complexity requirements message appears in register page
        2. the password doesn't meet complexity requirements message disappears in register page
        3. the app goes back to the main page with Sign in link
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        register_page = RegisterPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_register()
        # 5.1. less than 8 characters (Abc123.)
        register_page.input_required_fields_register("", "", "", "", "Abc123.", "", True, False, False, True)
        less_than_8_char = register_page.check_password_does_not_meet_complexity_requirements_message_appears()

        # 5.2. at least 8 characters with lower case, at least 1 number, 0 special symbol (abcd1234)
        register_page.input_required_fields_register("", "", "", "", "abcd1234", "", False, False, False, False)
        lower_case_number = register_page.check_password_does_not_meet_complexity_requirements_message_appears()

        # 5.3. at least 8 characters with upper case, at least 1 number, 0 special symbol (ABCD1234)
        register_page.input_required_fields_register("", "", "", "", "ABCD1234", "", False, False, False, False)
        upper_case_number = register_page.check_password_does_not_meet_complexity_requirements_message_appears()

        # 5.4. at least 8 characters with upper and lower case, 0 number, 0 special symbol (ABCDabcd)
        register_page.input_required_fields_register("", "", "", "", "ABCDabcd", "", False, False, False, False)
        upper_case_lower_case = register_page.check_password_does_not_meet_complexity_requirements_message_appears()

        # 5.5. at least 8 characters with lower case, 0 number, at least 1 special symbol (abcd.,-?)
        register_page.input_required_fields_register("", "", "", "", "abcd.,-?", "", False, False, False, False)
        lower_case_symbol = register_page.check_password_does_not_meet_complexity_requirements_message_appears()

        # 5.6. at least 8 characters with upper case, 0 number, at least 1 special symbol (ABCD.,-?)
        register_page.input_required_fields_register("", "", "", "", "ABCD.,-?", "", False, False, False, False)
        upper_case_symbol = register_page.check_password_does_not_meet_complexity_requirements_message_appears()

        # 5.7. at least 8 characters without letter, at least 1 number, at least 1 special symbol (1234.,-?)
        register_page.input_required_fields_register("", "", "", "", "1234.,-?", "", False, False, False, False)
        number_symbol = register_page.check_password_does_not_meet_complexity_requirements_message_appears()

        # fill with valid password
        register_page.input_required_fields_register("", "", "", "", "Abcd1234.", "", False, False, False, False)
        valid_password = register_page.check_password_does_not_meet_complexity_requirements_message_appears()

        register_result = (less_than_8_char, lower_case_number, upper_case_number, upper_case_lower_case,
                           lower_case_symbol, upper_case_symbol, number_symbol, valid_password)

        register_page.close_register_page_use_close_button()

        assert register_result == (True, True, True, True, True, True, True, False)

    @allure.story("22 test register already registered email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_email_already_exists(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. in the login page, press the register link
        4. navigate to the register page
        5. input an already registered email
        5. input all other fields and tick all the checkboxes and press register button
        6. wait for several seconds, check if the already exists email message appears
        7. close the register page and back to the main page
        result:
        1. the already exists email message appears
        2. the app goes back to the main page with Sign in link
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        register_page = RegisterPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_register()
        # use an already exist email to fill, here use "test_202202@mailinator.com"
        register_page.input_required_fields_register("Firstname", "Lastname", "test_202202@mailinator.com", "",
                                                     "Abcd1234.", "Abcd1234.", True, False, False, True)

        email_already_exists_result = register_page.wait_until_email_already_exists_message_appears()

        register_page.close_register_page_use_close_button()

        assert email_already_exists_result == True
    
    @allure.story("23 test register terms of service")
    @allure.severity(allure.severity_level.NORMAL)
    def test_register_terms_of_service(self, common_driver):
        """
        steps:
        1. in the app main page, press sign in button
        2. navigate to the login page
        3. in the login page, press the register link
        4. navigate to the register page
        3. press terms of service
        4. go back to the main page
        result:
        1. the app shows terms of services
        2. the app goes back to the main page
        :param common_driver:
        :return: pass, terms of service appears
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        register_page = RegisterPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_register()
        terms_of_service_result = register_page.check_terms_of_service()

        register_page.navigate_back(3)  # navigate back to main page

        assert terms_of_service_result == True

    @allure.story("24 test register privacy policy")
    @allure.severity(allure.severity_level.NORMAL)
    def test_register_privacy_policy(self, common_driver):
        """
        steps:
        1. in the app main page, press sign in button
        2. navigate to the login page
        3. in the login page, press the register link
        4. navigate to the register page
        3. press privacy policy
        4. go back to the main page
        result:
        1. the app shows privacy policy
        2. the app goes back to the main page
        :param common_driver:
        :return: pass, privacy policy appears
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        register_page = RegisterPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_register()
        privacy_policy_result = register_page.check_privacy_policy()

        register_page.navigate_back(3)  # navigate back to main page

        assert privacy_policy_result == True

    @allure.story("25 test register with invalid email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_register_with_invalid_username(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. in the login page, press the register link
        4. navigate to the register page
        5. input the invalid email (test_202202@mailinator)
        6. fill other fields and press register button
        7. check the popup text
        8. go back to the login page
        result:
        1. the app shows message: "Email is invalid"
        2. the app goes back to main page
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        register_page = RegisterPage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_register()
        register_page.input_required_fields_register("", "", "test_202202@mailinator", "", "", "",
                                                     True, False, False, True)

        message_shows_up_result = register_page.check_email_is_invalid_message_appears()

        register_page.close_register_page_use_back_button()
        login_pages.close_login_page()

        assert message_shows_up_result == True
    
    @allure.story("26 test register without network")
    @allure.severity(allure.severity_level.NORMAL)
    def test_register_without_network(self, common_driver):
        """
        steps:
        1. turn off the phone wifi
        2. in the app main page, press the sign in button
        3. navigate to the login page
        4. press the register link
        5. input a valid username and press reset password button
        6. check out the popup text
        5. go back to the login page
        result:
        1. the app shows message: "Please check your internet connection"
        2. the app goes back to login page
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        register_page = RegisterPage(common_driver)

        main_page.set_connection(0)
        main_page.tap_user_login()
        login_pages.tap_register()
        date_time = datetime.today().strftime('%Y%m%d%H%M%S')
        register_page.input_required_fields_register("Firstname", "Lastname", date_time + "@mailinator.com", "",
                                                     "Abcd1234.", "Abcd1234.", True, False, False, True)

        message_shows_up_result = register_page.wait_until_check_internet_connection_message_shows_up()
        register_page.close_register_page_use_close_button()
        main_page.set_connection(6)

        assert message_shows_up_result == True

    @allure.story("27 test register new user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_new_user(self, common_driver):
        """
        steps:
        1. in the app main page, press the sign in button
        2. navigate to the login page
        3. in the login page, press the register link
        4. navigate to the register page
        5. input all the fields and tick all the checkboxes and press register button
        6. wait for several seconds, check if the registration is successful (checking profile in side menu)
        7. log out
        result:
        1. the app accepts the new registration
        2. the app goes back to the main page with logged in
        3. the app logged out
        :param common_driver:
        :return: pass, if not logged in
        """
        main_page = MainPage(common_driver)
        login_pages = LoginPage(common_driver)
        register_page = RegisterPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)
        profile_page = ProfilePage(common_driver)

        main_page.tap_user_login()
        login_pages.tap_register()
        date_time = datetime.today().strftime('%Y%m%d%H%M%S')
        register_page.input_required_fields_register("Firstname", "Lastname", date_time + "@mailinator.com",
                                                     "1234567890", "Abcd1234.", "Abcd1234.", True, True, True, True)

        login_button_result = main_page.check_login_appears()
        side_menu_result = main_page.check_side_menu_icon_appears()

        main_page.tap_side_menu()
        side_menu_pages.tap_profile()
        profile_email_text = profile_page.get_email_info()
        if profile_email_text == date_time + "@mailinator.com":
            profile_email_result = True
        else:
            profile_email_result = False
            
        profile_first_name_text = profile_page.get_first_name_info()
        if profile_first_name_text == "Firstname":
            profile_first_name_result = True
        else:
            profile_first_name_result = False
            
        profile_last_name_text = profile_page.get_last_name_info()
        if profile_last_name_text == "Lastname":
            profile_last_name_result = True
        else:
            profile_last_name_result = False
            
        profile_phone_number_text = profile_page.get_phone_number_info()
        if profile_phone_number_text == "1234567890":
            profile_phone_number_result = True
        else:
            profile_phone_number_result = False
        side_menu_pages.navigate_back()

        main_page.tap_side_menu()
        log_out_button_result = side_menu_pages.check_log_out_appears()
        side_menu_pages.tap_log_out(True)
        side_menu_pages.close_side_menu_use_close_button()

        register_result = (login_button_result, side_menu_result, profile_email_result, profile_first_name_result, 
                           profile_last_name_result, profile_phone_number_result, log_out_button_result)
        assert register_result == (False, True, True, True, True, True, True)

    ####################################################################################################
    #                                       side menu test cases                                       #
    ####################################################################################################

    @allure.story("28 test side menu open close")
    @allure.severity(allure.severity_level.NORMAL)
    def test_side_menu_open_close(self, common_driver):
        """
        steps:
        1. in the app main page, press the side menu button
        2. tap the close button in side menu
        3. in the app main page, press the side menu button
        4. tap other area than the side menu
        result:
        1. the side menu opens
        2. the side menu closes
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)

        main_page.tap_side_menu()
        side_menu_pages.close_side_menu_use_close_button()
        #time.sleep(5) # wait for 5 seconds to let the code checks side menu disappears

        close_button_result = side_menu_pages.check_side_menu_appears()

        main_page.tap_side_menu()
        side_menu_pages.close_side_menu_use_blank_space()
        #time.sleep(5)  # wait for 5 seconds to let the code checks side menu disappears

        blank_space_result = side_menu_pages.check_side_menu_appears()

        assert (close_button_result, blank_space_result) == (False, False)

    @allure.story("29 test side menu air quality map")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_side_menu_air_quality_map(self, common_driver):
        """
        steps:
        1. in the app main page, press the side menu button
        2. tap the air quality map button
        3. navigate to the main page
        result:
        1. the air quality map page opens
        2. the app goes back to the main page with logged in
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)

        main_page.tap_side_menu()
        side_menu_pages.tap_air_quality_map()
        air_quality_map_result = side_menu_pages.check_air_quality_map_page_appears()

        side_menu_pages.navigate_back()

        assert air_quality_map_result == True

    @allure.story("30 test side menu blueair store")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_side_menu_blueair_store(self, common_driver):
        """
        steps:
        1. in the app main page, press the side menu button
        2. tap the blueair store button
        3. navigate to the main page
        result:
        1. the blueair store page opens
        2. the app goes back to the main page with logged in
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)

        main_page.tap_side_menu()
        side_menu_pages.tap_blueair_store()
        blueair_store_result = side_menu_pages.check_blueair_store_page_appears()

        side_menu_pages.navigate_back()

        assert blueair_store_result == True

    @allure.story("31 test side menu profile")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_side_menu_profile(self, common_driver):
        """
        steps:
        1. in the app main page, press the side menu button
        2. tap the profile button
        3. navigate to the main page
        result:
        1. the profile page opens
        2. the app goes back to the main page with logged in
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        login_page = LoginPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)
        profile_page = ProfilePage(common_driver)

        # check if the app is logged in, profile only appears with logged in
        if main_page.check_login_appears():
            main_page.tap_user_login()
            login_page.input_username_password_login("test_202202@mailinator.com", "Abcd1234.")

        main_page.tap_side_menu()
        side_menu_pages.tap_profile()
        profile_result = profile_page.check_profile_page_appears()

        # check side_menu appears, close the side menu if True
        if side_menu_pages.check_side_menu_appears():
            side_menu_pages.close_side_menu_use_close_button()
        else:
            profile_page.navigate_back()

        if not main_page.check_login_appears():
            main_page.tap_side_menu()
            side_menu_pages.tap_log_out(True)
            side_menu_pages.close_side_menu_use_close_button()

        assert profile_result == True

    @allure.story("32 test side menu settings")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_side_menu_settings(self, common_driver):
        """
        steps:
        1. in the app main page, press the side menu button
        2. tap the settings button
        3. navigate to the main page
        result:
        1. the settings page opens
        2. the app goes back to the main page with logged in
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)
        settings_pages = SettingsPages(common_driver)

        main_page.tap_side_menu()
        side_menu_pages.tap_settings()
        settings_result = settings_pages.check_settings_page_appears()

        side_menu_pages.navigate_back()

        assert settings_result == True

    @allure.story("33 test side menu voice assistants")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_side_menu_voice_assistants(self, common_driver):
        """
        steps:
        1. in the app main page, press the side menu button
        2. tap the voice assistants button
        3. navigate to the main page
        result:
        1. the voice assistants page opens
        2. the app goes back to the main page with logged in
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        login_page = LoginPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)

        # check if the app is logged in, voice assistants only appears with logged in
        if main_page.check_login_appears():
            main_page.tap_user_login()
            login_page.input_username_password_login("test_202202@mailinator.com", "Abcd1234.")

        main_page.tap_side_menu()
        side_menu_pages.tap_voice_assistants()
        voice_assistants_result = side_menu_pages.check_voice_assistants_page_appears()

        # check side_menu appears, close the side menu if True
        if side_menu_pages.check_side_menu_appears():
            side_menu_pages.close_side_menu_use_close_button()
        else:
            side_menu_pages.navigate_back()

        if not main_page.check_login_appears():
            main_page.tap_side_menu()
            side_menu_pages.tap_log_out(True)
            side_menu_pages.close_side_menu_use_close_button()

        assert voice_assistants_result == True

    @allure.story("34 test side menu support")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_side_menu_support(self, common_driver):
        """
        steps:
        1. in the app main page, press the side menu button
        2. tap the support button
        3. navigate to the main page
        result:
        1. the support page opens
        2. the app goes back to the main page with logged in
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)

        main_page.tap_side_menu()
        side_menu_pages.tap_support()
        support_result = side_menu_pages.check_support_page_appears()

        side_menu_pages.navigate_back()

        assert support_result == True

    @allure.story("35 test side menu policies")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_side_menu_policies(self, common_driver):
        """
        steps:
        1. in the app main page, press the side menu button
        2. tap the policies button
        3. navigate to the main page
        result:
        1. the policies page opens
        2. the app goes back to the main page with logged in
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)

        main_page.tap_side_menu()
        side_menu_pages.tap_support()
        policies_result = side_menu_pages.check_policies_page_appears()

        side_menu_pages.navigate_back()

        assert policies_result == True
    
    @allure.story("36 test side menu logout")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_side_menu_logout(self, common_driver):
        """
        steps:
        1. in the app main page, press the side menu button
        2. tap the logout button
        3. in the popup window, press no
        4. tap the logout button again
        5. in the popup window, press yes
        6. close the side menu
        result:
        1. the app stays with logged in
        2. the app logged out
        3. sign in button appears, log out button replaces by sign in button in side menu
        4. additional sections disappear (profile, voice assistants, subscriptions, warranty) depends on the region
        :param common_driver:
        :return:
        """
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)
        login_page = LoginPage(common_driver)

        if main_page.check_login_appears():
            main_page.tap_user_login()
            login_page.input_username_password_login("test_202202@mailinator.com", "Abcd1234.")

        main_page.tap_side_menu()
        side_menu_pages.tap_log_out(False)
        side_menu_pages.tap_log_out(True)

        sign_in_result = side_menu_pages.check_sign_in_appears()
        log_out_result = side_menu_pages.check_log_out_appears()
        profile_result = side_menu_pages.check_profile_appears()
        voice_assistants_result = side_menu_pages.check_voice_assistants_appears()

        side_menu_pages.close_side_menu_use_close_button()

        login_result = main_page.check_login_appears()

        assert (login_result, sign_in_result, log_out_result, profile_result, voice_assistants_result) == \
               (True, True, False, False, False)

    @allure.story("37 test side menu login logout ui")
    @allure.severity(allure.severity_level.NORMAL)
    def test_side_menu_login_logout_ui(self, common_driver):
        main_page = MainPage(common_driver)
        side_menu_pages = SideMenuPages(common_driver)
        login_page = LoginPage(common_driver)

        main_page.tap_side_menu()

        if side_menu_pages.check_log_out_appears():
            side_menu_pages.tap_log_out(True)

        logout_ui_result = (side_menu_pages.check_blueair_logo_appears(),
                            side_menu_pages.check_blueair_title_appears(),
                            side_menu_pages.check_air_quality_map_appears(),
                            side_menu_pages.check_blueair_store_appears(),
                            side_menu_pages.check_profile_appears(),
                            side_menu_pages.check_settings_appears(),
                            side_menu_pages.check_voice_assistants_appears(),
                            side_menu_pages.check_support_appears(),
                            side_menu_pages.check_policies_appears(),
                            side_menu_pages.check_sign_in_appears(),
                            side_menu_pages.check_log_out_appears(),
                            side_menu_pages.check_app_version_appears())

        side_menu_pages.tap_sign_in()
        login_page.input_username_password_login("test_202202@mailinator.com", "Abcd1234.")

        main_page.tap_side_menu()
        login_ui_result = (side_menu_pages.check_blueair_logo_appears(),
                           side_menu_pages.check_blueair_title_appears(),
                           side_menu_pages.check_air_quality_map_appears(),
                           side_menu_pages.check_blueair_store_appears(),
                           side_menu_pages.check_profile_appears(),
                           side_menu_pages.check_settings_appears(),
                           side_menu_pages.check_voice_assistants_appears(),
                           side_menu_pages.check_support_appears(),
                           side_menu_pages.check_policies_appears(),
                           side_menu_pages.check_sign_in_appears(),
                           side_menu_pages.check_log_out_appears(),
                           side_menu_pages.check_app_version_appears())

        side_menu_pages.tap_log_out(True)
        side_menu_pages.close_side_menu_use_close_button()

        assert (logout_ui_result, login_ui_result) == \
               ((True, True, True, True, False, True, False, True, True, True, False, True),
                (True, True, True, True, True, True, True, True, True, False, True, True))

if __name__ == "__main__":
    pytest.main(["-v", "-s", "--alluredir","./test_results"]) # use pytest test_main_page.py
    # os.system("allure generate ./test_results -o ./test_report")
    # allure serve /Users/yongyi/PycharmProjects/BlueairTestProjectAlpha/test_report