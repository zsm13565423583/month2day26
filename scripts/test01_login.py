from tools.get_driver import GetDriver
from page.page_login import PageLogin
from parameterized import parameterized
import pytest
from tools.get_yaml import get_yaml
from tools.get_log import GetLogger
log = GetLogger.get_logger()
class TestLogin():

    def setup_class(self):
        self.driver = GetDriver.get_app_driver()
        self.page = PageLogin(self.driver)
        #调用关闭稍后升级对象
        self.page.page_click_close_alter()
        #调用点击我的对象
        self.page.page_click_my()
        #调用点击登录/注册对象
        self.page.page_click_login_reg()
    def teardown_class(self):
        GetDriver.quit_app_driver()

    @pytest.mark.parametrize("phone,pwd,expect",get_yaml("login.yaml"))
    def test02_login(self,phone,pwd,expect):
        #调用登录业务操作
        self.page.page_login(phone,pwd)
        #获取登录按钮是否可以操作
        result=self.page.page_get_attribute("clickable")
        print("按钮可点",result)
        try:
            assert result == "false"
        except Exception as e:
            #日志
            log.error(e)
            #截图
            self.page.base_get_img()
            #抛异常
            raise



