from page_object.new_device_connection_pages import NewDeviceConnectionPages
from selenium.common import exceptions

# constant string for HealthProtect/Protect image in Find your Device page

# Pixel 3a XL image
HEALTHPROTECT = "/wAA////AAAA////AAAA////AAAA////AAAA////AAAA//8AAAAA//8AAAAA//8AAAAA//8AAAAA//8AAAAA//8A/wAAAP//"

# Samsung S21 image


class HealthProtectConnectionPages(NewDeviceConnectionPages):
    def check_device_icon(self, device_index):
        """
        check the device image in Find your Device page, compare with the stored bas64 image string
        more details check crop_screenshot() method in base_page.py
        :param device_index: device order in the current UI page
        :return:
        """
        try:
            device_image_list_elements = self.locate_element_list(self.new_device_image_list)
            device_name_list_elements = self.locate_element_list(self.new_device_name_list)

            device_image_element_coordinates = self.get_element_coordinates(device_image_list_elements[device_index])
            width = device_image_element_coordinates["width"]
            height = device_image_element_coordinates["height"]
            # the image height width ratio is 1:1
            if (width / height) == 1:
                device_image_base64_string = self.crop_screenshot_and_compress_as_string(self.get_screenshot_base64(), device_image_element_coordinates)
                device_name_text = self.get_element_attribute(device_name_list_elements[device_index], "text")
                #print("device_icon_base64_string: " + device_image_base64_string)
                if device_name_text == "HealthProtect" or device_name_text == "Protect":
                    if device_image_base64_string == HEALTHPROTECT:
                        return True
                    else:
                        return False
                else:
                    return False
        except exceptions.TimeoutException:
            return False
