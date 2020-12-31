from util.driver_info import DriverInfo
from util.file_manager import FileManager
import pytest


@pytest.fixture(scope="module")
# https://docs.pytest.org/en/stable/fixture.html#fixtures
def common_driver():
    """
    setup common drivers for different devices use based on device info
    a dictionary which consists necessary key value pairs for android or ios
    :return: the driver
    """
    FileManager.device_file_path = "./device/"
    device_strings = FileManager.read_file_lines("device.txt")
    for device_string in device_strings:
        device_info = FileManager.read_json_string(device_string)
        driver = DriverInfo(device_info).get_driver_start()
        yield driver
        driver.quit()
