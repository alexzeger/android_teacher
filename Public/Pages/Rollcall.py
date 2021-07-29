import time
from time import sleep
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from Public.Pages.BaseView import BaseView
import logging
from Log.log import Logger


#日志类的实例化
logger =Logger("Bela",Cmdlevel=logging.INFO,Filelevel=logging.INFO)

class rollcall(BaseView):


    
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
    rollcallElement = (By.XPATH,"//*[@text='点名']")
    check =(By.XPATH,'测试班级test')

    def intoObj(self):
        '''
        进入点名
        '''
        deskBtn = self.find_element(*self.deskElement)
        deskBtn.click()
        rollcallBtn = self.find_element(*self.rollcallElement)
        rollcallBtn.click()

        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("进入点名 is Ok!")

        
    layout1 =(By.XPATH,"//*[@text='09:00 - 11:00']")
    Live1 = (By.ID, "(//XCUIElementTypeStaticText[@name=\"课堂实况发送\"])[1]")
    Live2 = (By.ID, "(//XCUIElementTypeStaticText[@name=\"课堂实况发送\"])[2]")
    Live3 = (By.ID, "(//XCUIElementTypeStaticText[@name=\"课堂实况发送\"])[3]")

    content = (By.XPATH,"//*[@text='编辑']")


    emt1 = (By.ID,'com.teacher.boxfairy:id/ll_name')
    emt2 = (By.ID,'com.teacher.boxfairy:id/tv_course_content')
    # emt3 = (By.XPATH, '上课时间')
    # emt4 = (By.XPATH, '下课时间')
    # emt5 = (By.XPATH, '消耗课时')
    save = (By.XPATH,"//*[@text='保存']")
    text1 = (By.ID,'com.teacher.boxfairy:id/et_course_name')
    text2 = (By.ID,'com.teacher.boxfairy:id/et_content')

    student = (By.XPATH,'测试人员')
    check1 = (By.XPATH,'课件跟读：打包作业测试')

    def editObj(self,txt1,txt2):
        '''
        编辑课次信息
        '''
        layout1Btn = self.find_element(*self.layout1)
        layout1Btn.click()
        contentBtn = self.find_element(*self.content)
        contentBtn.click()
        self.input_text(txt1,*self.text1)
        saveBtn = self.find_element(*self.save)
        saveBtn.click()

        emt2Btn = self.find_element(*self.emt2)
        emt2Btn.click()
        self.input_text(txt2,*self.text2)

        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("编辑课次信息 is Ok!")

    image1 = (By.ID, "com.teacher.boxfairy:id/iv_avatar")
    add = (By.ID,"com.teacher.boxfairy:id/btn_pick_photo")
    picture1 = (By.ID, "com.teacher.boxfairy:id/iv_photo_lpsi")
    done = (By.ID, "com.teacher.boxfairy:id/btn_right_lh")
    
    video = (By.XPATH,"//*[@bounds='[52,960][312,1120]']")
    videoElement = (By.ID, "com.teacher.boxfairy:id/btn_pick_photo")
    save=(By.ID, "com.teacher.boxfairy:id/tv_inner_right")
    black = (By.ID, "com.teacher.boxfairy:id/back")
    close = (By.ID, "com.teacher.boxfairy:id/iv_delete")
    def MediaObj(self):
        '''
        编辑课次多媒体
        '''

        image1Btn = self.find_element(*self.image1)
        image1Btn.click()
        addBtn = self.find_element(*self.add)
        addBtn.click()
        picture1Btn = self.find_element(*self.picture1)
        picture1Btn.click()
        doneBtn = self.find_element(*self.done)
        doneBtn.click()
        videoBtn = self.find_element(*self.video)
        videoBtn.click()

        videoElementBtn = self.find_element(*self.videoElement)
        videoElementBtn.click()
        self.TouchAction_elemen_perform()
        saveBtn = self.find_element(*self.save)
        saveBtn.click()
        time.sleep(2)
        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("编辑课次多媒体 is Ok!")


    def Media1Obj(self):
        '''
        编辑课次多媒体
        '''

        closeBtn = self.find_element(*self.close)
        closeBtn.click()
        time.sleep(2)
        closeBtn.click()
        image1Btn = self.find_element(*self.image1)
        image1Btn.click()
        addBtn = self.find_element(*self.add)
        addBtn.click()
        picture1Btn = self.find_element(*self.picture1)
        picture1Btn.click()
        doneBtn = self.find_element(*self.done)
        doneBtn.click()
        videoBtn = self.find_element(*self.video)
        videoBtn.click()

        videoElementBtn = self.find_element(*self.videoElement)
        videoElementBtn.click()
        self.TouchAction_elemen_perform()
        closeBtn = self.find_element(*self.close)
        closeBtn.click()
        time.sleep(2)
        closeBtn.click()
        saveBtn = self.find_element(*self.save)
        saveBtn.click()
        time.sleep(2)
        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("编辑课次多媒体 is Ok!")
        

    classemt = (By.ID, "com.teacher.boxfairy:id/ll_course_content")
    record =(By.XPATH,"//*[@text='上课记录']")

    def checkObj(self):
        '''
        检查断言
        '''
        blackBtn = self.find_element(*self.black)
        blackBtn.click()
        recordBtn = self.find_element(*self.record)
        recordBtn.click()
        self.swipe_elemen(200,1000)
        classemtBtn = self.find_element(*self.classemt)
        classemtBtn.click()
        time.sleep(2)
        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("检查断言 is Ok!")





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
