
from time import sleep
from selenium.webdriver.common.by import By
from Public.Pages.BaseView import BaseView
import logging
from Log.log import Logger


#日志类的实例化
logger =Logger("Bela",Cmdlevel=logging.INFO,Filelevel=logging.INFO)

class practive(BaseView):


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
    
    def intohomeworkObj(self):
        '''
        进入已完成作业
        '''
        practiceElementBtn = self.find_element(*self.practiceElement)
        practiceElementBtn.click()
        homeworktElementBtn = self.find_element(*self.homeworktElement)
        homeworktElementBtn.click()
        menuElementBtn = self.find_element(*self.menuElement)
        menuElementBtn.click()
        addpractiveBtn = self.find_element(*self.addpractive)
        addpractiveBtn.click()
        logger.info("进入完成作业 is Ok!")
        self.getScreenShot()


    input= (By.ID,'com.teacher.boxfairy:id/et_input')
    leftBtnElement = (By.ID,'com.teacher.boxfairy:id/bt_left')
    backElement = (By.ID,'com.teacher.boxfairy:id/back')
    libraryElement = (By.ID,'com.teacher.boxfairy:id/ll_practice_library')

    def addpracticeObj(self,value):
        '''
        加入到练习库
        '''
        inputBtn = self.find_element(*self.input)
        inputBtn.clear()
        inputBtn.send_keys(value)
        leftBtnElementBtn = self.find_element(*self.leftBtnElement)
        leftBtnElementBtn.click()
        backElementBtn = self.find_element(*self.backElement)
        backElementBtn.click()
        libraryElementBtn = self.find_element(*self.libraryElement)
        libraryElementBtn.click()
        logger.info("加入练习库 is Ok!")
        self.getScreenShot()

    
    edit= (By.ID,'com.teacher.boxfairy:id/tv_lib_edit')  

    def intopracticeObj(self):
        '''
        进入到练习库
        '''
        practiceElementBtn = self.find_element(*self.practiceElement)
        practiceElementBtn.click()
        libraryElementBtn = self.find_element(*self.libraryElement)
        libraryElementBtn.click()

        logger.info("进入练习库 is Ok!")
        self.getScreenShot()

    content= (By.ID,'com.teacher.boxfairy:id/et_content')
    
    def contentObj(self,text):
        editBtn = self.find_element(*self.edit)
        editBtn.click()
        self.swipe_elemen(1300,200)
        '''
        输入要求
        '''
        contentTx = self.find_element(*self.content)
        contentTx.clear()
        contentTx.send_keys(text)
        logger.info("输入要求 is Ok!")
        self.getScreenShot()

    save= (By.ID,'com.teacher.boxfairy:id/tv_save')
    def saveObj(self):
        '''
        保存
        '''
        saveBtn = self.find_element(*self.save)
        saveBtn.click()
        logger.info("保存 is Ok!")
        self.getScreenShot()

    savenew= (By.ID,'com.teacher.boxfairy:id/tv_save_new')

    def savenewObj(self):
        '''
        另保存
        '''
        savenewBtn = self.find_element(*self.savenew)
        savenewBtn.click()
        logger.info("另保存 is Ok!")
        self.getScreenShot()

    assignment= (By.ID,'com.teacher.boxfairy:id/tv_lib_assignment')

    def assignmentObj(self):
        '''
        进入布置界面
        '''
        assignmentBtn = self.find_element(*self.assignment)
        assignmentBtn.click()
        self.swipe_elemen(1300,200)
     
    classname=(By.ID,'com.teacher.boxfairy:id/tv_class_name')
    content = (By.ID,'com.teacher.boxfairy:id/et_content')
    startTime =(By.XPATH,"//*[@text='请选择开始时间']") 
    endTime =(By.XPATH,"//*[@text='请选择截止时间']") 
    insidesubmit= (By.ID,'com.teacher.boxfairy:id/btnSubmit')
    outsidesubmit = (By.ID,'com.teacher.boxfairy:id/tv_submit')

    def practivehomeworkObj(self,value):
        '''
        发布打包作业
        '''
        contentBtn = self.find_element(*self.content)
        contentBtn.send_keys(value)
        startTimeBtn = self.find_element(*self.startTime)
        startTimeBtn.click()
        insidesubmitBtn = self.find_element(*self.insidesubmit)
        insidesubmitBtn.click()
        endTimeBtn = self.find_element(*self.endTime)
        endTimeBtn.click()
        insidesubmitBtn.click()
        classnameBtn = self.find_element(*self. classname)
        classnameBtn.click()
        outsidesubmitBtn = self.find_element(*self. outsidesubmit)
        outsidesubmitBtn.click()


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
