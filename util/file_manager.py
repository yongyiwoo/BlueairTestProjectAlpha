import json
import base64

file_path = "../device/"
image_path = "../image/"


class FileManager(object):
    @staticmethod
    def read_file_lines(file_name):
        try:
            with open(file_path + file_name, "r") as device_file:
                device_strings = device_file.readlines()
                return device_strings
        except FileNotFoundError:
            print("File not found.")

    @staticmethod
    def read_json_string(json_string):
        try:
            device_info = json.loads(json_string)
            return device_info
        except ValueError:
            print("String error")

    @staticmethod
    def write_image_string(base64_string, file_name):
        # https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
        try:
            with open(image_path + file_name + ".png", "wb") as img:
                img.write(base64.decodebytes(base64_string.encode("utf-8")))
            return image_path + file_name + ".png"
        except IOError:
            print("File cannot be opened.")