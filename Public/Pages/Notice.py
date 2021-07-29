import time
from time import sleep
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import By

from Public.Pages.BaseView import BaseView
import logging
from Log.log import Logger


#日志类的实例化
logger =Logger("Bela",Cmdlevel=logging.INFO,Filelevel=logging.INFO)

class notice(BaseView):


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


    deskElement = (By.XPATH,"//*[@text='办公桌']")
    taskElement = (By.XPATH,"//*[@text='班级通知']")
    addElement = (By.XPATH,"//*[@text='新建']")
    check =(By.XPATH,"//*[@text='测试班级test']")

    def intoObj(self):
        '''
        进入班级通知
        '''
        deskBtn = self.find_element(*self.deskElement)
        deskBtn.click()
        taskBtn = self.find_element(*self.taskElement)
        taskBtn.click()
        addBtn = self.find_element(*self.addElement)
        addBtn.click()

        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("进入班级通知 is Ok!")

    addtext = (By.ID,'com.teacher.boxfairy:id/et_add_comment')
    addimage = (By.ID,"com.teacher.boxfairy:id/iv_avatar")
    add = (By.ID,"com.teacher.boxfairy:id/btn_pick_photo")
    picture1 = (By.ID, "com.teacher.boxfairy:id/iv_photo_lpsi")
    done = (By.ID, "com.teacher.boxfairy:id/btn_right_lh")

    def addObj(self,text):
        '''
        添加班级通知
        '''
        addtextBtn = self.find_element(*self.addtext)
        self.input_text(text,*self.addtext)
        addimageBtn = self.find_element(*self.addimage)
        addimageBtn.click()
        addBtn = self.find_element(*self.add)
        addBtn.click()
        picture1Btn = self.find_element(*self.picture1)
        picture1Btn.click()
        doneBtn = self.find_element(*self.done)
        doneBtn.click()

        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("添加班级通知 is Ok!")


    video = (By.XPATH, "//*[@bounds='[46,1024][310,1184]']")
    videoElement = (By.ID, "com.teacher.boxfairy:id/btn_pick_photo")
    
    classmate = (By.XPATH,"//*[@text='测试班级test(4人)']")
    sendout = (By.XPATH,"//*[@text='发送']")

    def addvideoObj(self):
        '''
        添加视频
        '''
        videoBtn = self.find_element(*self.video)
        videoBtn.click()
        videoElementBtn = self.find_element(*self.videoElement)
        videoElementBtn.click()
        self.TouchAction_elemen_perform()


        classmateBtn = self.find_element(*self.classmate)
        classmateBtn.click()
        sendoutBtn = self.find_element(*self.sendout)
        sendoutBtn.click()
        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("添加视频 is Ok!")



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
