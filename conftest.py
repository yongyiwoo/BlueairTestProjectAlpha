from util.driver_info import DriverInfo
from util.file_manager import FileManager
import pytest
import allure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    if rep.when == "call" and rep.outcome == "failed":
        common_driver = item.funcargs["common_driver"]
        allure.attach(
            common_driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )


# https://docs.pytest.org/en/stable/fixture.html#fixtures
@pytest.fixture(scope="session", params=[FileManager.read_json_string(device_string) for device_string in FileManager.read_file_lines("device.txt")])
def common_driver(request):
    """
    setup common drivers for different devices use based on device info
    a dictionary which consists necessary key value pairs for android or ios
    :return: the driver
    """
    driver = DriverInfo(request.param).get_driver_start()
    yield driver
    driver.quit()
