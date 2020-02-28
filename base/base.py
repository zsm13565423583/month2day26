import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLogger

log = GetLogger.get_logger()
class Base:

    #初始化
    def __init__(self,driver):
        log.info("正在初始化driver对象，driver：{}".format(driver))
        self.driver = driver
    #查找元素
    def base_find_ele(self,loc,time = 20,poll = 0.5):
        log.info("正在查找:{}元素".format(loc))
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_element(*loc))



    #点击操作
    def base_click_ele(self,loc):
        log.info("正在对{}元素进行点击操作".format(loc))

        self.base_find_ele(loc).click()
        log.info("{}元素点击完成".format(loc))

    #输入操作
    def base_input_ele(self,loc,value):
        #查找元素
        ele = self.base_find_ele(loc)
        #清空
        log.info("正在对{}元素进清空击操作".format(loc))
        ele.clear()
        #输入
        log.info("正在对:{}元素进输入操作，输入内容为:value".format(loc,value))
        ele.send_keys(value)
        log.info("{}元素输入操作完成".format(loc))

    #获取属性值
    def base_get_ele_attribute(self,loc,value):

        #获取元素
        ele= self.base_find_ele(loc)
        #返回属性值
        log.info("正在获取:{}元素的属性值".format(loc))
        return ele.get_attribute(value)

    #截图
    def base_get_img(self):
        #调用截图方法
        log.error("正在进行截图操作")
        self.driver.get_screenshot_as_file("./image/err.png")
        #调用写入报告方法
        self.__base_write_img()

    #把截图写入报告
    def __base_write_img(self):
        #获取获取图片文件流
        log.error("正在将图片写入报告")
        with open("./image/err.png","rb") as f:

        #调用allure方法
            allure.attach("错误原因",f.read(),allure.attach_type.PNG)