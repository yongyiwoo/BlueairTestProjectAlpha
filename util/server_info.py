from appium.webdriver.appium_service import AppiumService

class ServerInfo(object):
    def __init__(self, host="0.0.0.0", port="4723"):
        self.host = host
        self.port = port

    def start_server(self):
        #print("start server")
        service = AppiumService()
        service.start(args=["--address", self.host, "--port", self.port, "--base-path", "/wd/hub"])
