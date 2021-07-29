from time import sleep
from selenium.webdriver.common.by import By
from Public.Pages.BaseView import BaseView
import logging
from Log.log import Logger
from Public.common.desired_caps import desired
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
#日志类的实例化
logger =Logger("Bela",Cmdlevel=logging.INFO,Filelevel=logging.INFO)

driver = desired()
driver.implicitly_wait(30)    
class Publish(BaseView):


    MobileTextElement = (By.ID,'com.teacher.boxfairy:id/et_phone')
    VerifyCodeTextElement = (By.ID,'com.teacher.boxfairy:id/et_verifyCode')
    LoginBtnElement = (By.ID,'com.teacher.boxfairy:id/rl_login')

    def LoginBtnObj(self,mobilevalue):
        '''
        登录测试账号
        '''
        MobileText = self.find_element(*self.MobileTextElement)
        MobileText.send_keys(mobilevalue)
        VerifyCodeText = self.find_element(*self.VerifyCodeTextElement)
        VerifyCodeText.send_keys("111222")

        LoginBtn = self.find_element(*self.LoginBtnElement)
        LoginBtn.click()
        logger.info("LoginBtn is click!")

    practiceElement =(By.XPATH,"//*[@text='练习']")
    homeworktElement = (By.XPATH,"//*[@text='测试班级test']")
    menuElement = (By.ID,'com.teacher.boxfairy:id/rl_show_more_menu')
    addpractive = (By.XPATH,"//*[@text='加入练习库']")
    
    def addpracticeObj():

        driver.find_element_by_id('com.teacher.boxfairy:id/et_phone').send_keys("18961520996")
        driver.find_element_by_id('com.teacher.boxfairy:id/et_verifyCode').send_keys("111222")
        driver.find_element_by_id('com.teacher.boxfairy:id/rl_login').click()
        sleep(2)
        #转到练习界面
        driver.find_element_by_xpath("//*[@text='练习']").click()
        #进入完成作业
        driver.find_element_by_xpath("//*[@text='测试班级test']").click()
        #弹出下拉菜单
        driver.find_element_by_id("com.teacher.boxfairy:id/rl_show_more_menu").click()
        #加入练习库
        driver.find_element_by_xpath("//*[@text='加入练习库']").click()
        #添加到练习库
        driver.find_element_by_id("com.teacher.boxfairy:id/et_input").clear()
        driver.find_element_by_id("com.teacher.boxfairy:id/et_input").send_keys("测试作业练习库")
        driver.find_element_by_id("com.teacher.boxfairy:id/bt_left").click()
        sleep(2)
        driver.find_element_by_id("com.teacher.boxfairy:id/back").click()
        #进入练习库
        driver.find_element_by_id("com.teacher.boxfairy:id/ll_practice_library").click()
        alertText =driver.find_element_by_id("com.teacher.boxfairy:id/tv_title") 
        name = str(alertText.text)
        

    input= (By.ID,'com.teacher.boxfairy:id/et_input')
    leftBtnElement = (By.ID,'com.teacher.boxfairy:id/bt_left')
    backElement = (By.ID,'com.teacher.boxfairy:id/back')
    libraryElement = (By.ID,'com.teacher.boxfairy:id/ll_practice_library')


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
