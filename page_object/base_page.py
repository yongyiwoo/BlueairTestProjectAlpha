from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.touch_action import TouchAction
from util.file_manager import FileManager
import base64
import numpy as np
import cv2
# from selenium.common import exceptions


class BasePage(object):
    def __init__(self, common_driver):
        self.driver = common_driver

    def locate_element(self, element_id: tuple, waiting_time=1):
        """
        when check the element is enabled or displayed and need to wait a longer time
        like load the element from the internet
        :param element_id: element id
        :param waiting_time: waiting time for the element being loaded, the default time is 1 second
        :return: the element
        """
        element = WebDriverWait(self.driver, waiting_time).until(ec.visibility_of_element_located(element_id))
        return element

    def locate_element_list(self, element_id: tuple, waiting_time=1):
        element_list = WebDriverWait(self.driver, waiting_time).until(ec.visibility_of_all_elements_located(element_id))
        return element_list

    def get_screen_size(self):
        screen_size = self.driver.get_window_size()

        screen_size_x = screen_size["width"]
        screen_size_y = screen_size["height"]

        return screen_size_x, screen_size_y

    def set_position_on_screen(self, position: tuple):
        percent_x, percent_y = position
        screen_x, screen_y = self.get_screen_size()

        position_x = screen_x * percent_x / 100
        position_y = screen_y * percent_y / 100

        return position_x, position_y

    def tap_element(self, element=None, x=None, y=None):
        TouchAction(self.driver).tap(element, x, y).perform()

    def scroll_screen(self, original: tuple, destination: tuple):
        original_x, original_y = original
        destination_x, destination_y = destination

        TouchAction(self.driver).press(x=original_x, y=original_y).wait(1600). \
            move_to(x=destination_x, y=destination_y).release().perform()

    def get_screenshot64(self):
        """
        get a screenshot of the current UI as a base64 string
        :return: base64 string
        """
        screen_image = self.driver.get_screenshot_as_base64()
        #screen_image_decode = base64.b64decode(screen_image)
        #screen_image_array = np.frombuffer(screen_image_decode, np.uint8)
        return screen_image

    def navigate_back(self, n=1):
        """
        navigate back n times, default is 1 time
        :param n: times
        """
        for _ in range(n):
            self.driver.back()

    def put_background(self, wait_time=-1):
        """
        put the app to the background for wait_time seconds
        if wait_time = -1 means de-active the app
        :return:
        """
        self.driver.background_app(wait_time)

    def put_foreground(self):
        """
        active the app to the foreground when it's not active
        :return:
        """
        self.driver.launch_app()

    def unlock_screen(self):
        """
        unlock the screen (intend to do nothing, but keep the session alive between the client and the server)
        :return:
        """
        self.driver.unlock()

    def lock_screen(self):
        """
        lock the screen (intend to do nothing, but keep the session alive between the client and the server)
        :return:
        """
        self.driver.lock()

    def get_phone_settings(self):
        """
        For example:
        {'platform': 'LINUX', 'webStorageEnabled': False, 'takesScreenshot': True, 'javascriptEnabled': True,
        'databaseEnabled': False, 'networkConnectionEnabled': True, 'locationContextEnabled': False,
        'warnings': {}, 'desired': {'platformName': 'Android', 'platformVersion': '11', 'deviceName': 'Pixel 3a XL',
        'udid': '95QAX0G370', 'noReset': True, 'newCommandTimeout': 800, 'appPackage': 'com.blueair.android',
        'appActivity': 'com.blueair.android.activity.HomeActivity'}, 'platformName': 'Android',
        'platformVersion': '11', 'deviceName': '95QAX0G370', 'udid': '95QAX0G370', 'noReset': True,
        'newCommandTimeout': 800, 'appPackage': 'com.blueair.android',
        'appActivity': 'com.blueair.android.activity.HomeActivity', 'deviceUDID': '95QAX0G370',
        'deviceApiLevel': 30, 'deviceScreenSize': '1080x2160', 'deviceScreenDensity': 446,
        'deviceModel': 'Pixel 3a XL', 'deviceManufacturer': 'Google', 'pixelRatio': 2.7875001,
        'statBarHeight': 67, 'viewportRect': {'left': 0, 'top': 67, 'width': 1080, 'height': 1959}}
        :return:
        """
        return self.driver.desired_capabilities

    @staticmethod
    def crop_screenshot(base64_image, coordinates):
        """
        use numpy to convert base64 image to an array and crop it according to the coordinates
        :param base64_image: base64 image
        :param coordinates: cropped image coordinates
        :return: a numpy array
        """
        x = int(coordinates["x"])
        y = int(coordinates["y"])
        h = int(coordinates["height"])
        w = int(coordinates["width"])
        screen_image_decode = base64.b64decode(base64_image)
        screen_image_array = np.frombuffer(screen_image_decode, np.uint8)
        image = cv2.imdecode(screen_image_array, cv2.IMREAD_COLOR)
        cropped_image_array = image[y:y+h, x:x+w]
        return cropped_image_array

    @staticmethod
    def compare_screenshot(image_array_big, image_array_small):
        if image_array_big is None or image_array_small is None:
            return False
        # set the big image ration to 1:1, already know height < width
        if image_array_big.shape[0] != image_array_big.shape[1]:
            if image_array_big.shape[1] > image_array_big.shape[0]:
                before = (image_array_big.shape[1] - image_array_big.shape[0]) // 2
                after = image_array_big.shape[1] - before
                image_array_big_reshape = image_array_big[:, before:after, :]
            else:
                before = (image_array_big.shape[0] - image_array_big.shape[1]) // 2
                after = image_array_big.shape[0] - before
                image_array_big_reshape = image_array_big[before:after, :, :]
        else:
            image_array_big_reshape = image_array_big

        if image_array_big_reshape.shape != image_array_small.shape:
            height = image_array_small.shape[0]
            width = image_array_small.shape[1]
            dimension = (width, height)
            image_array_big_resize = cv2.resize(image_array_big_reshape, dimension)
        else:
            image_array_big_resize = image_array_big
        return np.allclose(image_array_big_resize, image_array_small, atol=2, rtol=1)

    @staticmethod
    def analyze_screenshot_pixel_color(image_array):
        # cv2.imwrite("image_array.jpg",image_array)
        # image height
        image_height = image_array.shape[0]
        image_width = image_array.shape[1]
        image_center_pixel = image_array[image_height // 2, image_width // 2]
        image_center_pixel_color = None
        # AQI: Color [B G R]
        # Excellent: Blue [228 180   0]
        # Good: Green [172 194  55]
        # Moderate: Yellow [123 231 239]
        # Polluted: Orange [118 149 239]
        # Very Polluted: Red [116  86 239]
        if image_center_pixel[0] > 200:
            image_center_pixel_color = "Blue"
        if 200 > image_center_pixel[0] > 100 and 200 > image_center_pixel[1] > 100 and image_center_pixel[2] < 100:
            image_center_pixel_color = "Green"
        if image_center_pixel[1] > 200 and image_center_pixel[2] > 200:
            image_center_pixel_color = "Yellow"
        if 200 > image_center_pixel[0] > 100 and 200 > image_center_pixel[1] > 100 and image_center_pixel[2] > 200:
            image_center_pixel_color = "Orange"
        if 200 > image_center_pixel[0] > 100 and image_center_pixel[1] < 100 and image_center_pixel[2] > 200:
            image_center_pixel_color = "Red"
        #print(image_center_pixel)
        return image_center_pixel_color

    @staticmethod
    def analyze_button_pixel_color(image_array):
        """
        Analyze button image center pixel color to get the result if it's a blue(pressed) or white(unpressed) image icon
        pressed status [85 40 0]
        unpressed status [255 255 255]
        :param image_array:
        :return: True or False
        """
        # cv2.imwrite("image_array.jpg", image_array)
        image_height = image_array.shape[0]
        image_width = image_array.shape[1]
        image_center_pixel = image_array[image_height // 2, image_width // 2]
        image_center_pixel_color = None
        if image_center_pixel[2] == 255:
            image_center_pixel_color = False
        if image_center_pixel[2] == 0:
            image_center_pixel_color = True
        return image_center_pixel_color

    @staticmethod
    def save_image(image_base64, image_name):
        image_path_string = FileManager.write_image_string(image_base64, image_name)
        return image_path_string

    @staticmethod
    def get_element_attribute(element, attribute: str):
        attribute_value = element.get_attribute(attribute)
        return attribute_value

    @staticmethod
    def get_element_coordinates(element):
        coordinate_value = element.rect
        return coordinate_value

    def set_element_text(self, element, text: str, hide_kb=True):
        element.click()
        element.clear()
        element.send_keys(text)
        if hide_kb:
            self.driver.hide_keyboard()

    @staticmethod
    def clear_element_text(element):
        element.click()
        element.clear()


    @staticmethod
    def pause_to_confirm():
        return input("Please type 'yes' to confirm your operation: ")

