import time
from time import sleep
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from Public.Pages.BaseView import BaseView
import logging
from Log.log import Logger


#日志类的实例化
logger =Logger("Bela",Cmdlevel=logging.INFO,Filelevel=logging.INFO)

class task(BaseView):



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
    taskElement = (By.XPATH,"//*[@text='任务打卡']")
    addElement = (By.ID,'com.teacher.boxfairy:id/ib_inner_right')
    check =(By.ID,'测试班级test')

    def intoObj(self):
        '''
        进入任务打卡
        '''
        deskBtn = self.find_element(*self.deskElement)
        deskBtn.click()
        taskBtn = self.find_element(*self.taskElement)
        taskBtn.click()
        addBtn = self.find_element(*self.addElement)
        addBtn.click()

        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("任务打卡 is Ok!")

    layout4 = (By.XPATH,"//*[@text='任意打卡']")
    layout3 = (By.XPATH,"//*[@text='动画配音']")
    layout5 = (By.XPATH, "//*[@text='绘本跟读']")
    layout1 =(  By.XPATH, "//*[@text='跟读练习']")

    content = (By.ID,  'com.teacher.boxfairy:id/ll_empty')
    finish = (By.XPATH, "//*[@text='完成']")

    emt1 = (By.XPATH, "//*[@text='K1-1']")
    emt2 = (By.XPATH,  "//*[@text='海尼曼GK']")
    emt3 = (By.XPATH, "//*[@text='小猪佩奇']")


    student = (By.ID,'测试人员')
    check1 = (By.ID, '课件跟读：打包作业测试')

    def add1Obj(self):
        '''
        添加课件跟读任务打卡
        '''
        layout1Btn = self.find_element(*self.layout1)
        layout1Btn.click()
        contentBtn = self.find_element(*self.content)
        contentBtn.click()
        emt1Btn = self.find_element(*self.emt1)
        emt1Btn.click()
        finishBtn = self.find_element(*self.finish)
        finishBtn.click()

        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("课件跟读任务打卡 is Ok!")

    def add2Obj(self):
        '''
        添加绘本跟读任务打卡
        '''
        layout2Btn = self.find_element(*self.layout5)
        layout2Btn.click()
        contentBtn = self.find_element(*self.content)
        contentBtn.click()
        emt2Btn = self.find_element(*self.emt2)
        emt2Btn.click()
        finishBtn = self.find_element(*self.finish)
        finishBtn.click()

        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("绘本跟读任务打卡 is Ok!")

    def add3Obj(self):
        '''
        添加动画配音任务打卡
        '''
        layout3Btn = self.find_element(*self.layout3)
        layout3Btn.click()
        contentBtn = self.find_element(*self.content)
        contentBtn.click()
        emt3Btn = self.find_element(*self.emt3)
        emt3Btn.click()
        finishBtn = self.find_element(*self.finish)
        finishBtn.click()

        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("动画配音任务打卡 is Ok!")


    lx1 =(By.ID, 'com.teacher.boxfairy:id/iv_1')
    picture =(By.XPATH, "//*[@text='从相册选择']")
    photo = (By.ID,'com.teacher.boxfairy:id/cb_photo_lpsi')
    done = (By.ID, 'com.teacher.boxfairy:id/btn_right_lh')

    content1 = (By.XPATH,"//*[@text='选择照片或视频']")
    def add4Obj(self):
        '''
        添加任意打卡任务打卡
        '''
        layout4Btn = self.find_element(*self.layout4)
        layout4Btn.click()
        time.sleep(2)
        contentBtn = self.find_element(*self.content1)
        contentBtn.click()
        lx1Btn = self.find_element(*self.lx1)
        lx1Btn.click()
        pictureBtn = self.find_element(*self.picture)
        pictureBtn.click()
        photoBtn = self.find_element(*self.photo)
        photoBtn.click()
        doneBtn = self.find_element(*self.done)
        doneBtn.click()
        self.swipe_elemen(500,200)

        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("任意打卡任务打卡 is Ok!")


    input1 = (By.XPATH, "//*[@text='请输入活动标题']")
    input2 = (By.XPATH,"//*[@text='请输入活动要求']")
    starttime =(By.XPATH,"//*[@text='请选择开始时间']")
    determine =(By.ID, 'com.teacher.boxfairy:id/btnSubmit')
    endtime =(By.XPATH,"//*[@text='请选择截止时间']")
    cover = (By.ID,'com.teacher.boxfairy:id/iv_title_page')
    book1 = (By.XPATH,"//*[@text='1']")
    confirm = (By.ID, 'com.teacher.boxfairy:id/bt_confirm')
    classmate = (By.ID,  'com.teacher.boxfairy:id/tv_class_name')
    task = (By.ID,   'com.teacher.boxfairy:id/tv_submit')

    def sendoutObj(self,text1,text2):
        '''
        输入要求
        '''
        self.input_text(text1,*self.input1)
        self.input_text(text2, *self.input2)
        
        starttimetn = self.find_element(*self.starttime)
        starttimetn.click()
        determineBtn = self.find_element(*self.determine)
        determineBtn.click()
        endtimeBtn = self.find_element(*self.endtime)
        endtimeBtn.click()
        determineBtn = self.find_element(*self.determine)
        determineBtn.click()
        self.swipe_elemen(1300,200)
        coverBtn = self.find_element(*self.cover)
        coverBtn.click()
        book1Btn = self.find_element(*self.book1)
        book1Btn.click()
        confirmBtn = self.find_element(*self.confirm)
        confirmBtn.click()
        classmateBtn = self.find_element(*self.classmate)
        classmateBtn.click()
        taskBtn = self.find_element(*self.task)
        taskBtn.click()

        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test', "进入作业", *self.check)
        logger.info("输入要求 is Ok!")

    input2 = (By.XPATH,"//*[@text='请输入活动要求']")
    delete =(By.XPATH, "//*[@text='删除']")
    def deleteObj(self):
        '''
        删除任务打卡
        '''
        self.swipe_elemen_max(800,300,100,300)
        deleteBtn = self.find_element(*self.delete)
        deleteBtn.click()


        # self.get_assert_text(*self.check)
        # self.assert_ele_in('测试班级test',"进入作业",*self.check)
        logger.info("删除任务打卡 is Ok!")
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
