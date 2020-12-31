from appium import webdriver


class DriverInfo(object):
    def __init__(self, desired_caps):
        """
        a driver object with desired_caps attribute
        :param desired_caps: a dictionary which consists necessary key value pairs for android or ios
        """
        self.desired_caps = desired_caps

    def get_driver_start(self):
        """
        initialize the connection to the server
        :return: the driver
        """
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        return driver
