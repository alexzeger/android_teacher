from time import sleep
from selenium.webdriver.common.by import By
from Public.Pages.BaseView import BaseView
import logging
from Log.log import Logger


#日志类的实例化
logger =Logger("Bela",Cmdlevel=logging.INFO,Filelevel=logging.INFO)

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

    practiceElement = (By.XPATH,"//*[@text='练习']")
    addhomeworktElement = (By.ID,'com.teacher.boxfairy:id/iv_add_homework')
    statusnodataElement = (By.ID,'com.teacher.boxfairy:id/rl_status_no_data')

    def intohomeworkObj(self):
        '''
        进入打包练习
        '''
        publishpracticeBtn = self.find_element(*self.practiceElement)
        publishpracticeBtn.click()
        addhomeworkBtn = self.find_element(*self.addhomeworktElement)
        addhomeworkBtn.click()
        logger.info("进入打包练习 is Ok!")
         #self.assert_ele_in()

    def addhomeworkObj(self):
        '''
        点击添加练习
        '''
        statusnodataBtn = self.find_element(*self.statusnodataElement)
        statusnodataBtn.click()
        logger.info("添加打包练习 is Ok!")
         #self.assert_ele_in()

    homework1 = (By.XPATH,"//*[@text='练习 1']")
    layout1 = (By.ID,'com.teacher.boxfairy:id/ll_layout1')
    empty = (By.ID,'com.teacher.boxfairy:id/ll_empty')

    homework1 = (By.XPATH,"//*[@text='练习 1']")
    homework2 = (By.XPATH,"//*[@text='练习 2']")
    homework3 = (By.XPATH,"//*[@text='练习 3']")
    homework4 = (By.XPATH,"//*[@text='练习 4']")
    homework5 = (By.XPATH,"//*[@text='练习 5']")

    def sethomeworkObj1(self):
        '''
        点击添加练习
        '''
        homeworkBtn = self.find_element(*self.homework1)
        homeworkBtn.click()
    def sethomeworkObj2(self):
        '''
        点击添加练习
        '''
        homeworkBtn = self.find_element(*self.homework2)
        homeworkBtn.click()
    def sethomeworkObj2(self):
        '''
        点击添加练习
        '''
        homeworkBtn = self.find_element(*self.homework2)
        homeworkBtn.click()
    def sethomeworkObj3(self):
        '''
        点击添加练习
        '''
        homeworkBtn = self.find_element(*self.homework3)
        homeworkBtn.click()
    def sethomeworkObj4(self):
        '''
        点击添加练习
        '''
        homeworkBtn = self.find_element(*self.homework4)
        homeworkBtn.click()
    def sethomeworkObj5(self):
        '''
        点击添加练习
        '''
        homeworkBtn = self.find_element(*self.homework5)
        homeworkBtn.click()

    choose1 = (By.ID,'com.teacher.boxfairy:id/iv_1')
    booksimple = (By.XPATH,"//*[@text='K1-1']")
    unit1 = (By.XPATH,"//*[@text='1-1']")
    confirm = (By.ID,'com.teacher.boxfairy:id/bt_confirm')

    def simpleObj(self):
        '''
        单句
        '''  
        layout1Btn = self.find_element(*self.layout1)
        layout1Btn.click()
        emptyBtn = self.find_element(*self.empty)
        emptyBtn.click()
        choose1Btn = self.find_element(*self.choose1)
        choose1Btn.click()
        booksimpleBtn = self.find_element(*self.booksimple)
        booksimpleBtn.click()
        unit1Btn = self.find_element(*self.unit1)
        unit1Btn.click()
        confirmBtn = self.find_element(*self.confirm)
        confirmBtn.click()

        logger.info("单句 is Ok!")
         #self.assert_ele_in()

    choose1 = (By.ID,'com.teacher.boxfairy:id/iv_1')
    bookmany = (By.XPATH,"//*[@text='鲁教版三年级上册']")
    page1 = (By.XPATH,"//*[@text='Greetings']")
    page2 = (By.XPATH,"//*[@text='Introduction']")
 
    def manyObj(self):
        '''
        多句
        '''
                
        layout1Btn = self.find_element(*self.layout1)
        layout1Btn.click()
        emptyBtn = self.find_element(*self.empty)
        emptyBtn.click()
        choose1Btn = self.find_element(*self.choose1)
        choose1Btn.click()

        self.swipe_elemen(1500,200)
        self.swipe_elemen(1500,200)
        self.swipe_elemen(1500,200)
        self.swipe_elemen(1500,200)
        self.swipe_elemen(1500,200)

        bookmanyBtn = self.find_element(*self.bookmany)
        bookmanyBtn.click()
        page1Btn = self.find_element(*self.page1)
        page1Btn.click()
        page2Btn = self.find_element(*self.page2)
        page2Btn.click()
        unit1Btn = self.find_element(*self.unit1)
        unit1Btn.click()
        confirmBtn = self.find_element(*self.confirm)
        confirmBtn.click()

        logger.info("多句 is Ok!")
         #self.assert_ele_in()

    layout2 = (By.ID,'com.teacher.boxfairy:id/ll_layout2')
    picture = (By.XPATH,"//*[@text='从相册选择']")
    page1 = (By.XPATH,"//*[@text='Greetings']")    
    photol = (By.ID,'com.teacher.boxfairy:id/cb_photo_lpsi')
    right_lh = (By.ID,'com.teacher.boxfairy:id/btn_right_lh')
    

    def pictureObj(self):
        '''
        选择照片
        '''
        layout2Btn = self.find_element(*self.layout2)
        layout2Btn.click()
        emptyBtn = self.find_element(*self.empty)
        emptyBtn.click()
        logger.info("选择练习内容 is Ok!")
         #self.assert_ele_in()

        choose1Btn = self.find_element(*self.choose1)
        choose1Btn.click()
        pictureBtn = self.find_element(*self.picture)
        pictureBtn.click()

        photolBtn = self.find_element(*self.photol)
        photolBtn.click()
        right_lhBtn = self.find_element(*self.right_lh)
        right_lhBtn.click()
        logger.info("选择照片 is Ok!")

         #self.assert_ele_in()
    send = (By.ID,'com.teacher.boxfairy:id/et_input')
    outsidesubmit = (By.ID,'com.teacher.boxfairy:id/tv_submit')

    layout3 = (By.ID,'com.teacher.boxfairy:id/ll_layout3')
    bookanimation=(By.XPATH,"//*[@text='小猪佩奇']")
    def animationObj(self):
        '''
        动画配音
        '''  
        layout3Btn = self.find_element(*self.layout3)
        layout3Btn.click()
        emptyBtn = self.find_element(*self.empty)
        emptyBtn.click()
        bookanimationBtn = self.find_element(*self.bookanimation)
        bookanimationBtn.click()
        unit1Btn = self.find_element(*self.unit1)
        unit1Btn.click()
        confirmBtn = self.find_element(*self.confirm)
        confirmBtn.click()

        logger.info("动画配音 is Ok!")
         #self.assert_ele_in()

    def requirementsObj(self,input):
        '''
        输入要求
        '''
        sendText = self.find_element(*self.send)
        sendText.send_keys(input)
        outsidesubmitBtn = self.find_element(*self. outsidesubmit)
        outsidesubmitBtn.click()

        logger.info("输入要求 is Ok!")
         #self.assert_ele_in()

    classname=(By.ID,'com.teacher.boxfairy:id/tv_class_name')
    content = (By.ID,'com.teacher.boxfairy:id/et_content')
    startTime =(By.XPATH,"//*[@text='请选择开始时间']") 
    endTime =(By.XPATH,"//*[@text='请选择截止时间']") 
    insidesubmit= (By.ID,'com.teacher.boxfairy:id/btnSubmit')
    def publishhomeworkObj(self,value):
        '''
        发布打包练习
        '''
        self.swipe_elemen(900,200)
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

        logger.info("发布打包练习 is Ok!")
         #self.assert_ele_in()

    




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
