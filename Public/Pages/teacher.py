from time import sleep
from selenium.webdriver.common.by import By
from Public.Pages.BaseView import BaseView
import logging
from Log.log import Logger

#日志类的实例化
logger =Logger("Bela",Cmdlevel=logging.INFO,Filelevel=logging.INFO)

class Teacher(BaseView):
    MobileTextElement = (By.ID,'com.teacher.boxfairy:id/et_phone')
    VerifyCodeTextElement = (By.ID,'com.teacher.boxfairy:id/et_verifyCode')
    LoginBtnElement = (By.ID,'com.teacher.boxfairy:id/rl_login')

    def MobileTextObj(self,mobilevalue):
        '''
        输入手机号
        '''
        MobileText = self.find_element(*self.MobileTextElement)
        MobileText.send_keys(mobilevalue)
        logger.info("MobileText is sendValues!")
        self.getScreenShot()


    def VerifyCodeTextObj(self):
        '''
        输入验证码
        '''
        VerifyCodeText = self.find_element(*self.VerifyCodeTextElement)
        VerifyCodeText.send_keys("111222")
        logger.info("VerifyCodeText is sendValues!")
        self.getScreenShot()


    def LoginBtnObj(self):
        '''
        登录按钮
        '''
        LoginBtn = self.find_element(*self.LoginBtnElement)
        LoginBtn.click()
        logger.info("LoginBtn is click!")





# ################################################
# 如下为测试代码，正式运行时（run.py）,需要注释到
# ################################################
#from Public.common.Desired_caps import desired
#from Public.common.DoExcel import ReadExcel
#if __name__ == "__main__":
#    driver = desired()
#    teacher = Teacher(driver)

#    teacher.waitActivity("com.teacher.boxfairy.mvp.ui.activity.login.LoginActivity",100)
#    mobilevalue =int(ReadExcel("Data.xls","Sheet1").read_excel(1,0))
#    print(mobilevalue)
#    teacher.MobileTextObj(mobilevalue)
#    teacher.VerifyCodeTextObj()
#    teacher.LoginBtnObj()
