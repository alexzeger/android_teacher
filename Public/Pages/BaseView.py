from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import os
import time
import random
import unittest
from Log.log import Logger
from Config import globalconfig

img_path = globalconfig.img_path
import logging
logger = Logger("Bela",Cmdlevel= logging.WARNING,Filelevel=logging.WARNING)

class BaseView():
    def __init__(self,driver):
        self.driver = driver
    def implicitly_wait(self,time):
        '''
        将webdriver提供的implicitly_wait方法进行二次封装
        :param implicitly_wait：
        :param time：
        :return：
        '''
        self.driver.implicitly_wait(time)

    def waitActivity(self,waitActivity,time):
        '''
        将webdriver提供的wait_activity方法进行二次封装
        :param waitActivity：
        :param time：
        :return：
        '''
        self.driver.wait_activity(waitActivity,time)
        AC = self.driver.current_activity
        # print(AC)

    #     # 自定义一个元素查找方法
    # def find_element(self, *loc):
    #     #*loc代表任意数量的位置参数（带个星号的参数）
    #     try:
    #         WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(loc))
    #         return self.driver.find_element(*loc)
    #     except:
    #         print("%s 该activity中未找到 %s 元素" % (self.loc))

    # 自定义一个元素查找方法
    def find_element(self, *loc):
        try:
            # 元素可见时，返回查找到的元素；以下入参为元组的元素，需要加*
            WebDriverWait(self.driver,30).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)

        except selenium.common.exceptions.NoSuchElementException:
            # logging.warning('Can not find element: %s' % loc[1])
            logger.warning('Can not find element: %s' %loc[1] )
            raise
        except selenium.common.exceptions.TimeoutException:
            logger.warning('Can not find element: %s' %loc[1] )
            raise

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_elements(*loc))
            return self.driver.find_elements(*loc)

        except selenium.common.exceptions.NoSuchElementException:
            # logging.warning('Can not find element: %s' % loc[1])
            logger.warning('Can not find element: %s' %loc[1] )
            self.getScreenShot('找不到元素')
            raise

    def click_element(self, *loc):
        '''
            封装点击操作函数
        '''
        self.find_element(*loc).click()

    def input_text(self,text,*loc):
        '''
            封装输入操作函数
        '''
        self.fm = self.find_element(*loc)
        self.fm.clear()  # 需要先清空输入框，防止有默认内容
        self.fm = self.find_element(*loc)
        self.fm.send_keys(text)


    def assert_ele_in(self,text,name,*loc):
        '''
            封装断言操作函数
        '''
        try:
            assert text in self.find_element(*loc).text
            assert 1
        except Exception:
            self.getScreenShot(name)
            assert 0




    def get_assert_text(self,*loc ):
        ele = self.find_element(*loc)
        return ele.text


        # 自定义截图函数
    def getScreenShot(self,name):
        '''
         自定义截图函数
        '''
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())) #获取当前系统时间
        imageName = img_path+'/'+now +name+'.png'#拼接截图的名称
        self.driver.get_screenshot_as_file(imageName)


    def swipe_elemen(self,starY,endY):
        '''
        封装滚动操作函数
        '''
        time.sleep(1)
        self.driver.swipe(450,starY,450,endY,duration=None)
        time.sleep(1)


    def swipe_elemen_max(self,starX,starY,endX,endY):
        '''
        封装滚动操作函数
        '''
        time.sleep(1)
        self.driver.swipe(starX,starY,endX,endY,duration=None)
        time.sleep(1)

    def ios_swipe_elemen_up(self):
        '''
        封装ios向上滚动操作函数
        收缩键盘
        '''
        time.sleep(1)
        self.driver.execute_script("mobile:swipe",{"direction":"up"})
        time.sleep(1)


    def ios_swipe_elemen_down(self):
        '''
        封装ios向下滚动操作函数
        收缩键盘
        '''
        time.sleep(1)
        self.driver.execute_script("mobile:swipe",{"direction":"down"})
        time.sleep(1)

    def TouchAction_elemen_perform(self):
        '''
        封装坐标轴点击操作函数
        收缩键盘
        '''
        time.sleep(1)
        TouchAction(self.driver).tap(x=170,y=1100).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(x=200,y=400).perform()
        time.sleep(1)




    # 暂时用不到
    # def take_screenShot(self):
    #     '''
    #     测试失败截图，并把截图展示到allure报告中
    #     '''
    #     tm = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    #     self.driver.get_screenshot_as_file(  os.getcwd() + os.sep + "image/%s.png" % tm)
    #
    #     allure.attach.file(os.getcwd() + os.sep + "image/%s.png" %
    #                        tm, attachment_type=allure.attachment_type.PNG)



#ios用不了
 # 自定义一个获取当前设备尺寸的功能
    def get_device_size(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return x, y

    # 自定义一个功能，可以实现向左滑屏操作。
    def swipe_left(self):
        start_x = self.get_device_size()[0] * 0.9
        start_y = self.get_device_size()[1] * 0.5
        end_x = self.get_device_size()[0] * 0.4
        end_y = self.get_device_size()[1] * 0.5
        self.driver.swipe(start_x, start_y, end_x, end_y)

    # 自定义一个功能，可以实现向上滑屏操作。
    def swipe_up(self):
        start_x = self.get_device_size()[0] * 1/2
        start_y = self.get_device_size()[1] * 1/2
        end_x = self.get_device_size()[0] * 1/2
        end_y = self.get_device_size()[1] * 1/7
        self.driver.swipe(start_x, start_y, end_x, end_y, 500)

    # 自定义随机生成11位手机号
    def create_phone(self):
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]
        # 最后八位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)
