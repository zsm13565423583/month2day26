from time import sleep

from selenium import webdriver
import appium.webdriver



class GetDriver:
    __app_driver = None

    # 获取app应用 driver
    @classmethod
    def get_app_driver(cls):
        cap = {}
        if cls.__app_driver is None:
            # server 启动参数
            # 设备信息
            cap['platformName'] = 'Android'
            cap['platformVersion'] = '5.1'
            cap['deviceName'] = 'emulator-5554'
            # app的信息
            cap['appPackage'] = "com.bjcsxq.chat.carfriend"

            cap['appActivity'] = ".module_main.activity.MainActivity"

            # 中文
            cap['unicodeKeyboard'] = True
            cap['resetKeyboard'] = True
            # 不重置应用
            # cap['noReset'] = False
            cls.__app_driver = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
        return cls.__app_driver

    # 关闭app应用 driver
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None
