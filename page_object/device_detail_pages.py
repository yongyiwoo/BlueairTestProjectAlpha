from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage

class DeviceDetailPages(BasePage):
    def __init__(self, common_driver):
        super(DeviceDetailPages, self).__init__(common_driver)