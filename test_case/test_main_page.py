from page_object.main_page import MainPage
from page_object.dustmagnet_connection_pages import DustMagnetConnectionPages
from page_object.dustmagnet_detail_pages import DustMagnetDetailPages
from page_object.healthprotect_connection_pages import HealthProtectConnectionPages
from page_object.classic_connection_pages import ClassicConnectionPages
import pytest
import time


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
    
    def test_add_b4_device(self, common_driver):   # add B4
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
        device_added_result = dustmagnet_connection_pages.finalize_device_page("b4_5210i")

        assert device_model_type == "DustMagnet 5210i"
        assert image_compare_result is True
        assert device_added_result == "b4_5210i"

    def test_swipe_device_layout_left(self, common_driver):
        device = "b4_5410i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_left(device, waiting_time=5)
        time.sleep(5)
        main_page.tap_night_mode()
        r = main_page.swipe_device_layout_left_back()
        assert False

    def test_swipe_device_layout_right(self, common_driver):
        device = "b4_5410i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_right(device, waiting_time=5)
        time.sleep(5)
        main_page.tap_standby_mode()
        r = main_page.swipe_device_layout_right_back()
        assert False

    def test_b4_device_info(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        # need to wait for 5 seconds
        time.sleep(5)
        main_page.tap_device(device, waiting_time=5)
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_device_settings()
        info = dustmagnet_detail_pages.get_device_detail_info()
        print(info)
        assert False

    def test_b4_fanspeed_mode(self, common_driver):
        device = "b4_5410i"
        main_page = MainPage(common_driver)
        # need to wait for 5 seconds
        time.sleep(5)
        main_page.tap_device(device)
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.set_manual_mode_by_button("0.0")
        time.sleep(10)
        assert False

    def test_b4_fanspeed_mode(self, common_driver):
        device = "b4_5410i"
        main_page = MainPage(common_driver)
        # need to wait for 5 seconds
        time.sleep(5)
        main_page.tap_device(device)
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.set_manual_mode_by_bar("55.0")
        time.sleep(5)
        assert False
    
    def test_device_info(self, common_driver):
        main_page = MainPage(common_driver)
        device_status = main_page.get_devices_info(waiting_time=10)
        print(device_status)
        assert False

    def test_b4_device_info(self, common_driver):
        device = "b4_5410i"
        main_page = MainPage(common_driver)
        # need to wait for 5 seconds
        time.sleep(5)
        main_page.tap_device(device)
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_device_settings()
        info = dustmagnet_detail_pages.get_device_detail_info()
        print(info)
        assert False

    
    def test_b4_schedule(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_add_schedule()
        dustmagnet_detail_pages.set_new_schedule("10:00", "10:01", "manual", [0, 2, 5, 6], "test", "save", am_pm="PM", fanspeed="60", led="20")
        assert False


    #####################################################################################

    def test_add_b4_device(self, common_driver):   # add B4
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
        device_added_result = dustmagnet_connection_pages.finalize_device_page("b4_5210i")

        assert device_model_type == "DustMagnet 5210i"
        assert image_compare_result is True
        assert device_added_result == "b4_5210i"

    def test_b4_online_status(self, common_driver):
        """
        b4 device online status check
        """
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        device_online_count = 0
        for check_times in range(4):    # check online status times in range()
            device_mode = main_page.get_devices_info(device, "device_mode", waiting_time=10)
            if device_mode != "Offline":
                device_online_count += 1
            main_page.put_background(-1)
            for idle_time in range(30):  # idle time in range(minute) for de-active the app in the background
                main_page.turn_on_screen()
                time.sleep(60)
            main_page.put_foreground()
        assert device_online_count == 4

    def test_swipe_device_layout_left_manual_to_night_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_left(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_night_mode(True)
        main_page.swipe_device_layout_left_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        assert device_mode == "Night"

    def test_swipe_device_layout_left_night_to_manual_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_left(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_night_mode(False)
        main_page.swipe_device_layout_left_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        assert device_mode == "Fan Speed 12%"


    def test_swipe_device_layout_left_manual_to_auto_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_left(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_auto_mode(True)
        main_page.swipe_device_layout_left_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        assert device_mode == "Auto"

    def test_swipe_device_layout_left_auto_to_manual_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_left(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_auto_mode(False)
        main_page.swipe_device_layout_left_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        assert device_mode == "Fan Speed 12%"

    def test_swipe_device_layout_right_manual_to_standby_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_right(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_standby_mode()
        main_page.swipe_device_layout_right_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        assert device_mode == "Standby"

    def test_swipe_device_layout_left_standby_to_manual_mode(self, common_driver):
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        main_page.swipe_device_layout_right(device, waiting_time=5)
        time.sleep(2)
        main_page.tap_standby_mode()
        main_page.swipe_device_layout_right_back()
        device_mode = main_page.get_devices_info(device, "device_mode", "no", waiting_time=10)
        #time.sleep(60)  # sensor warm up time
        assert device_mode == "Fan Speed 12%"

    '''
    def test_navigate_to_b4(self, common_driver):   # refactoring, sometimes the b4 device page doesn't show up
        device = "b4_5210i"
        main_page = MainPage(common_driver)
        # need to wait for 10 seconds to load the main UI
        time.sleep(10)
        navi_result = main_page.tap_device(device)
        assert navi_result
    '''
    def test_b4_manual_mode_fanspeed_1(self, common_driver):
        #device = "b4_5210i"
        #main_page = MainPage(common_driver)
        # need to wait for 10 seconds to load the main UI
        #time.sleep(10)
        #main_page.tap_device(device)
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("33.0")
        time.sleep(5)
        assert fan_speed == "33.0"

    def test_b4_manual_mode_fanspeed_1_5(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("51.0")
        time.sleep(5)
        assert fan_speed == "51.0"

    def test_b4_manual_mode_fanspeed_2(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("66.0")
        time.sleep(5)
        assert fan_speed == "66.0"

    def test_b4_manual_mode_fanspeed_2_5(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("84.0")
        time.sleep(5)
        assert fan_speed == "84.0"

    def test_b4_manual_mode_fanspeed_3(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("99.0")
        time.sleep(5)
        assert fan_speed == "99.0"

    def test_b4_back_manual_mode_fanspeed_1(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("33.0")
        time.sleep(5)
        assert fan_speed == "33.0"

    def test_b4_manual_mode_fanspeed_0(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        fan_speed = dustmagnet_detail_pages.set_manual_mode_by_button("0.0")
        time.sleep(5)
        assert fan_speed == "0.0"
    
    def test_b4_filter_usage(self, common_driver):  # can't do exact compare the filter
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        filter_usage = dustmagnet_detail_pages.get_filter_info()
        assert filter_usage is not None
    
    def test_b4_auto_mode(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_auto_mode(True)
        mode_info = dustmagnet_detail_pages.get_mode_info()
        assert mode_info == "Auto Mode"

    def test_b4_night_mode(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_night_mode(True)
        mode_info = dustmagnet_detail_pages.get_mode_info()
        assert mode_info == "Night Mode"

    def test_b4_standby_mode(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        dustmagnet_detail_pages.tap_standby_mode(False)
        mode_info = dustmagnet_detail_pages.get_mode_info()
        assert mode_info == "Air purifier is turned off at the moment"
    '''
    def test_b4_navigate_to_schedule(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        tap_result = dustmagnet_detail_pages.tap_add_schedule()
        assert tap_result

    def test_b4_set_schedule_auto(self, common_driver):
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        start_hour = time.strftime("%H", time.localtime())  # refactoring if time is 17:59
        start_minute = str(int(time.strftime("%M", time.localtime())) + 2)
        start_time = start_hour + ":" + start_minute
        end_hour = time.strftime("%H", time.localtime())
        end_minute = str(int(time.strftime("%M", time.localtime())) + 4)
        end_time = end_hour + ":" + end_minute
        schedule_result = dustmagnet_detail_pages.set_new_schedule(start_time, end_time, "auto", [0, 1, 2, 3, 4, 5 ,6], "b4_auto_schedule" , "save")
        assert schedule_result

    def test_b4_check_schedule_auto(self, common_driver):
        schedule_name = None
        schedule_mode = None
        schedule_hour = None
        schedule_minute = None
        mode_info = None
        wait_hour = 0
        wait_minute = 0
        dustmagnet_detail_pages = DustMagnetDetailPages(common_driver)
        schedule_result_list = dustmagnet_detail_pages.get_schedule_info()
        for schedule_result in schedule_result_list:
            # if schedule_name = "******"
            schedule_mode = schedule_result[1]
            schedule_hour = schedule_result[-1].split(":")[-2]
            schedule_minute = schedule_result[-1].split(":")[-1]  # the schedule end time minute

        if time.strftime("%M", time.localtime()) != schedule_minute:
            if time.strftime("%H", time.localtime()) > schedule_hour:
                wait_hour = int(time.strftime("%H", time.localtime())) - int(schedule_hour)
            # wait_minute -1 means that the checking happens 1 minute before it ends
            wait_minute = wait_hour * 60 + int(schedule_minute) - int(time.strftime("%M", time.localtime())) -1
            time.sleep(60 * wait_minute)
        mode_info = dustmagnet_detail_pages.get_mode_info().split(" ")[0]

        assert schedule_mode == mode_info and mode_info is not None

if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_main_page.py"]) # use pytest test_main_page.py
