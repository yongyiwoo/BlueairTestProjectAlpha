from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage

class DeviceConnectionPages(BasePage):
    def __init__(self, common_driver):
        super(DeviceConnectionPages, self).__init__(common_driver)
        self.model_list = (MobileBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")

    def tap_device_model(self):
        pass

    def find_device_page(self):
        pass

    def connect_wifi_page(self, password):
        pass

    def name_device_page(self, name):
        pass

    def finalize_device_page(self, name):
        pass