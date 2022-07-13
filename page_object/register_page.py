from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from selenium.common import exceptions
from appium import webdriver
import page_object.login_page

class RegisterPage(BasePage):
    def __init__(self, common_driver):
        super(RegisterPage, self).__init__(common_driver)
        self.cose = (MobileBy.ID, "com.blueair.android:id/btnClose")
        self.back = (MobileBy.ID, "com.blueair.android:id/btnBack")
        self.first_name = (MobileBy.ID, "com.blueair.android:id/firstName")
        self.last_name = (MobileBy.ID, "com.blueair.android:id/lastName")
        self.email = (MobileBy.ID, "com.blueair.android:id/email")
        self.phone_number = (MobileBy.ID, "com.blueair.android:id/phoneNumber")
        self.password = (MobileBy.ID, "com.blueair.android:id/password")
        self.confirm_password = (MobileBy.ID, "com.blueair.android:id/confirmPassword")
        self.age_limit = (MobileBy.ID, "com.blueair.android:id/cbYears")
        self.blueair_subscription = (MobileBy.ID, "com.blueair.android:id/cbSubscribe")
        self.unilever_data_share = (MobileBy.ID, "com.blueair.android:id/cbConsent")
        self.agree_documents = (MobileBy.ID, "com.blueair.android:id/cbPrivacy")
        self.terms_of_service = (MobileBy.ID, "com.blueair.android:id/txtTerms")
        self.terms_and_conditions = (MobileBy.ID, "com.blueair.android:id/info_container")
        self.privacy_policy = (MobileBy.ID, "com.blueair.android:id/txtPrivacy")
        self.privacy_notice = (MobileBy.ID, "com.blueair.android:id/info_container")
        self.register = (MobileBy.ID, "com.blueair.android:id/btnRegister")

    def 

