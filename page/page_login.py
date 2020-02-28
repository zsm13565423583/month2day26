import page
from base.base import Base
from tools.get_log import GetLogger
log = GetLogger.get_logger()
class PageLogin(Base):

    #
    def page_click_close_alter(self):
        self.base_click_ele(page.login_close_alter)

    def page_click_my(self):
        self.base_click_ele(page.login_my_button)

    def page_click_login_reg(self):
        self.base_click_ele(page.login_login_button_reg)

    def page_input_phone(self,phone):
        self.base_input_ele(page.login_input_phone,phone)

    def page_input_pwd(self,pwd):
        self.base_input_ele(page.login_input_pwd,pwd)

    def page_click_login(self):
        self.base_click_ele(page.login_login)

    def page_get_attribute(self,att):
        return self.base_get_ele_attribute(page.login_login,att)

    def page_login(self,phone,pwd):
        log.info("正在调用登录业务方法，账号为{}，密码为：{}".format(phone,pwd))
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login()
