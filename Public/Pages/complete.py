import time
from time import sleep
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from Public.Pages.BaseView import BaseView
import logging
from Log.log import Logger


#日志类的实例化
logger =Logger("Bela",Cmdlevel=logging.INFO,Filelevel=logging.INFO)

class complete(BaseView):


    # MobileTextElement = (By.XPATH,'//XCUIElementTypeOther[@name=\"欢迎来到盒精灵教师端\"]/XCUIElementTypeTextField[1]')
    # VerifyCodeTextElement = (By.XPATH,'//XCUIElementTypeOther[@name=\"欢迎来到盒精灵教师端\"]/XCUIElementTypeTextField[2]')
    # LoginBtnElement = (By.XPATH,'(//XCUIElementTypeStaticText[@name=\"登录\"])[1]"')
    #
    #
    # def LoginBtnObj(self,mobilevalue):
    #     '''
    #     登录测试账号
    #     '''
    #     self.implicitly_wait(30)
    #     MobileText = self.find_element(*self.MobileTextElement)
    #     MobileText.send_keys(mobilevalue)
    #     VerifyCodeText = self.find_element(*self.VerifyCodeTextElement)
    #     VerifyCodeText.send_keys("111222")
    #
    #     LoginBtn = self.find_element(*self.LoginBtnElement)
    #     LoginBtn.click()
    #     logger.info("LoginBtn is click!")

    practiceElement = (MobileBy.ACCESSIBILITY_ID,"练习")
    wholeElement = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]')
    studentElement = (MobileBy.ACCESSIBILITY_ID,'测试班级test（3人）')
    check =(MobileBy.ACCESSIBILITY_ID,'测试班级test')
    def intoObj(self):
        '''
        进入作业
        '''
        practiceBtn = self.find_element(*self.practiceElement)
        practiceBtn.click()
        wholeBtn = self.find_element(*self.wholeElement)
        wholeBtn.click()
        studentBtn = self.find_element(*self.studentElement)
        studentBtn.click()

        self.get_assert_text(*self.check)
        self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("进入作业 is Ok!")

    layout1 = (By.XPATH,"(//XCUIElementTypeStaticText[@name=\"练习 1：跟读练习\"])[1]")
    layout2 = (MobileBy.XPATH,'(//XCUIElementTypeStaticText[@name="练习 1：视频拍摄"])[1]')
    layout3 = (By.XPATH, "(//XCUIElementTypeStaticText[@name=\"练习 1：动画配音\"])[1]")
    layout4 = (By.XPATH, "(//XCUIElementTypeStaticText[@name=\"练习 1：课后练\"])[1]")
    student = (MobileBy.ACCESSIBILITY_ID,'测试人员')
    check1 = (MobileBy.ACCESSIBILITY_ID, '课件跟读：打包作业测试')

    def details_1_Obj(self):
        '''
        作业详情 跟读练习
        '''
        layout1Btn = self.find_element(*self.layout1)
        layout1Btn.click()
        self.ios_swipe_elemen_up()
        student1Btn = self.find_element(*self.student)
        student1Btn.click()
        self.get_assert_text(*self.check1)
        self.assert_ele_in('课件跟读：打包作业测试',"作业详情",*self.check1)
        logger.info("作业详情 is Ok!")

    def details_2_Obj(self):
        '''
        作业详情 视频拍摄
        '''
        layout2Btn = self.find_element(*self.layout2)
        layout2Btn.click()
        self.ios_swipe_elemen_up()
        student1Btn = self.find_element(*self.student)
        student1Btn.click()



        self.get_assert_text(*self.check1)
        self.assert_ele_in('课件跟读：打包作业测试',"作业详情",*self.check1)
        logger.info("作业详情 is Ok!")

    def details_3_Obj(self):
        '''
        作业详情 动画配音
        '''
        layout3Btn = self.find_element(*self.layout3)
        layout3Btn.click()
        self.ios_swipe_elemen_up()
        student1Btn = self.find_element(*self.student)
        student1Btn.click()



        self.get_assert_text(*self.check1)
        self.assert_ele_in('课件跟读：打包作业测试',"作业详情",*self.check1)
        logger.info("作业详情 is Ok!")

    def details_4_Obj(self):
        '''
        作业详情 课后练
        '''
        layout4Btn = self.find_element(*self.layout4)
        layout4Btn.click()
        self.ios_swipe_elemen_up()
        student1Btn = self.find_element(*self.student)
        student1Btn.click()



        self.get_assert_text(*self.check1)
        self.assert_ele_in('课件跟读：打包作业测试',"作业详情",*self.check1)
        logger.info("作业详情 is Ok!")

    comment1 = (By.XPATH,'//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextView')
    sound = (MobileBy.ACCESSIBILITY_ID,"点击录制(2分钟)")
    sound1 = (MobileBy.XPATH, "//XCUIElementTypeButton[@name=\"  点击录制(2分钟)\"]")
    Star = (MobileBy.ACCESSIBILITY_ID,"Rating")
    comment = (By.XPATH,"//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeTextView")
    Submit = (By.XPATH,"//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]")

    def CorrectionObj(self,text1,text2):
        '''
        批改作业
        '''

        comment1Btn = self.find_element(*self.comment1)
        self.input_text(text1,*self.comment1)
        self.ios_swipe_elemen_down()
        self.ios_swipe_elemen_up()
        soundBtn = self.find_element(*self.sound)
        soundBtn.click()
        time.sleep(3)
        self.TouchAction_elemen_perform(200,400)
        StarBtn = self.find_element(*self.Star)
        StarBtn.click()
        self.ios_swipe_elemen_up()
        commentBtn= self.find_element(*self.comment)
        self.input_text(text2,*self.comment)
        self.ios_swipe_elemen_up()
        sound1Btn = self.find_element(*self.sound1)
        sound1Btn.click()
        SubmitBtn = self.find_element(*self.Submit)
        SubmitBtn.click()

        logger.info("批改作业 is Ok!")

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
