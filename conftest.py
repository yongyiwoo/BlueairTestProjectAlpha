from util.driver_info import DriverInfo
from util.file_manager import FileManager
import pytest


# https://docs.pytest.org/en/stable/fixture.html#fixtures
@pytest.fixture(scope="module", params=[FileManager.read_json_string(device_string) for device_string in FileManager.read_file_lines("device.txt")])
def common_driver(request):
    """
    setup common drivers for different devices use based on device info
    a dictionary which consists necessary key value pairs for android or ios
    :return: the driver
    """
    driver = DriverInfo(request.param).get_driver_start()
    yield driver
    driver.quit()
