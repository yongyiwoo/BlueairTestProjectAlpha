from page_object.main_page import MainPage
from page_object.dustmagnet_connection_pages import DustMagnetConnectionPages
from page_object.dustmagnet_detail_pages import DustMagnetDetailPages
from page_object.healthprotect_connection_pages import HealthProtectConnectionPages
from page_object.classic_connection_pages import ClassicConnectionPages
import pytest
import allure
import time
import datetime
import re


@allure.feature("test the main user interface")    #
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


    def test_add_g4_device(self, common_driver):   # add g4
        main_page = MainPage(common_driver)
        healthprotect_connection_pages = HealthProtectConnectionPages(common_driver)
        main_page.device_connection_pages = healthprotect_connection_pages
        healthprotect_select_page = main_page.add_new_device()
        device_image_template = healthprotect_select_page.get("HealthProtect_image")
        find_device_info = healthprotect_connection_pages.find_device_page()
        if find_device_info is not None:
            device_model_type = find_device_info[1]
            device_image_small = find_device_info[2]
        else:
            device_model_type = None
            device_image_small = None
        image_compare_result = healthprotect_connection_pages.compare_screenshot(device_image_template, device_image_small)
        healthprotect_connection_pages.connect_wifi_page("28116194")
        healthprotect_connection_pages.name_device_page("g4_7710i")
        device_added_result = healthprotect_connection_pages.finalize_device_page("g4_7710i")

        assert device_model_type == "HealthProtect 7710i"
        assert image_compare_result is True
        assert device_added_result == "g4_7710i"
    '''

    #####################################################################################

    @allure.story("test onboard b4 device")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_onboard_b4_device(self, common_driver):   # add B4
        main_page = MainPage(common_driver)
        dustmagnet_connection_pages = DustMagnetConnectionPages(common_driver)
        main_page.device_connection_pages = dustmagnet_connection_pages
        dustmagnet_select_page = main_page.add_new_device()
        device_image_template = dustmagnet_select_page.get("DustMagnet_image")
        find_device_info = dustmagnet_connection_pages.find_device_page()
        if find_device_info is not None:
            device_model_type = find_device_info[1]
            device_image_small = find_device_info[2]
        else:
            device_model_type = None
            device_image_small = None
        image_compare_result = dustmagnet_connection_pages.compare_screenshot(device_image_template, device_image_small)
        dustmagnet_connection_pages.connect_wifi_page("28116194", sleep_time=30)
        dustmagnet_connection_pages.name_device_page("b4_5210i")
        time.sleep(30)  # firmware issue, the wifi module needs to restart
        device_added_result = dustmagnet_connection_pages.finalize_device_page("b4_5210i")

        assert device_model_type == "DustMagnet 5210i"
        assert image_compare_result is True
        assert device_added_result == "b4_5210i"
    '''
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
    '''
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
        #time.sleep(60)  # sensor warm up time
        assert device_mode == "Fan Speed 12%"

    @allure.story("test navigate to b4")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_b4(self, common_driver):   # refactoring, sometimes the b4 device page doesn't show up
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
    def test_be_device_delete(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        device = dustmagnet_detail_pages.delete_onboarded_device("delete")
        assert device is None

if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_main_page.py"]) # use pytest test_main_page.py
    # pytest -v -s --alluredir="/Users/yongyi/PycharmProjects/BlueairTestProjectAlpha/test_report" test_main_page.py
    # allure serve /Users/yongyi/PycharmProjects/BlueairTestProjectAlpha/test_report