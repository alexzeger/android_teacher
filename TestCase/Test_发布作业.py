import unittest
import time
import os
from BeautifulReport import BeautifulReport
from Public.Pages.homework import Publish
from Public.common.DoExcel import ReadExcel
from Public.common.desired_caps import desired


mobileValue = int(ReadExcel("Data.xls","Sheet1").read_excel(1,0))

class Test_u0001(unittest.TestCase):

    def save_img(self, test_method):#失败截图方法（必须要定义在class中）

        """
        传入一个test_method, 并存储到默认的文件路径下
        :param test_method:
        :return:
        """
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path,test_method))

    def setUp(self):
        self.driver = desired()
        self.driver.implicitly_wait(30)


    @BeautifulReport.add_test_img('test_case_1')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img()方法
    def test_homework_case_0(self):
        self.Publish = Publish(self.driver)
        self.Publish.LoginBtnObj(mobileValue)
        time.sleep(4)
    def test_homework_case_1(self):
        '''
        单个 跟读练习 单句作业
        '''
        self.Publish = Publish(self.driver)
        self.Publish.intohomeworkObj()
        self.Publish.addhomeworkObj()
        self.Publish.sethomeworkObj1()
        self.Publish.simpleObj()
        self.Publish.requirementsObj("测试单句")
        self.Publish.publishhomeworkObj("测试单句")
        time.sleep(4)
        # 断言
        result = self.driver.find_element_by_id("com.teacher.boxfairy:id/tv_recent")
        self.save_img("test_homework_case_1")
        self.assertEqual ('最近发布:测试单句',result.text )
        #self.save_img("test_case_1")  # 没有报错也要截图的话，直接在这里调用方法就行了
        

    @BeautifulReport.add_test_img('test_homework_case_2')
    def test_homework_case_2(self):
        '''
         单个 跟读练习 多句作业
         '''

        self.Publish = Publish(self.driver)
        self.Publish.intohomeworkObj()
        self.Publish.addhomeworkObj()
        self.Publish.sethomeworkObj1()
        self.Publish.manyObj()
        self.Publish.requirementsObj("测试多句")
        self.Publish.publishhomeworkObj("测试多句")
        time.sleep(4)
        # 断言
        result = self.driver.find_element_by_id("com.teacher.boxfairy:id/tv_recent")
        self.save_img("test_homework_case_2")
        self.assertTrue(result.text == '最近发布:测试多句')
        
        # self.save_img("test_case_1")  # 没有报错也要截图的话，直接在这里调用方法就行了

    @BeautifulReport.add_test_img('test_homework_case_3')
    def test_homework_case_3(self):
        '''
         单个 照片视频 图片作业
         '''

        self.Publish = Publish(self.driver)
        self.Publish.intohomeworkObj()
        self.Publish.addhomeworkObj()
        self.Publish.sethomeworkObj1()
        self.Publish.pictureObj()
        self.Publish.requirementsObj("测试图片")
        self.Publish.publishhomeworkObj("测试图片")
        time.sleep(4)
        # 断言
        result = self.driver.find_element_by_id("com.teacher.boxfairy:id/tv_recent")
        self.save_img("test_homework_case_3")
        self.assertTrue(result.text == '最近发布:测试图片')
        
        # self.save_img("test_case_1")  # 没有报错也要截图的话，直接在这里调用方法就行了

    @BeautifulReport.add_test_img('test_homework_case_4')
    def test_homework_case_4(self):
        '''
        单个 动画配音 动画配音
        '''

        self.Publish = Publish(self.driver)
        self.Publish.intohomeworkObj()
        self.Publish.addhomeworkObj()
        self.Publish.sethomeworkObj1()
        self.Publish.animationObj()
        self.Publish.requirementsObj("测试动画配音")
        self.Publish.publishhomeworkObj("测试动画配音")
        time.sleep(4)
       # 断言
        result = self.driver.find_element_by_id("com.teacher.boxfairy:id/tv_recent")
        self.save_img("test_homework_case_4")
        self.assertTrue (result.text == '最近发布:测试动画配音')
        
        #self.save_img("test_case_1")  # 没有报错也要截图的话，直接在这里调用方法就行了


    @BeautifulReport.add_test_img('test_case_5')  # 失败后会有报错截图
    def test_homework_case_5(self):
        '''
        五个 打包作业
        '''
        self.Publish = Publish(self.driver)
        self.Publish.intohomeworkObj()
        self.Publish.addhomeworkObj()
        self.Publish.addhomeworkObj()
        self.Publish.addhomeworkObj()
        self.Publish.addhomeworkObj()
        self.Publish.addhomeworkObj()

        self.Publish.sethomeworkObj1()
        self.Publish.simpleObj()
        self.Publish.requirementsObj("测试单句")
        self.Publish.sethomeworkObj2()
        self.Publish.manyObj()
        self.Publish.requirementsObj("测试多句")
        self.Publish.sethomeworkObj3()
        self.Publish.pictureObj()
        self.Publish.requirementsObj("测试图片")
        self.Publish.sethomeworkObj4()
        self.Publish.animationObj()
        self.Publish.requirementsObj("测试动画配音")
        self.Publish.sethomeworkObj5()
        self.Publish.pictureObj()
        self.Publish.requirementsObj("测试图片")

        self.Publish.publishhomeworkObj("打包作业测试")

        time.sleep(4)
        # 断言
        result = self.driver.find_element_by_id("com.teacher.boxfairy:id/tv_recent")
        self.save_img("test_homework_case_5")
        self.assertTrue(result.text == '最近发布:打包作业测试')

        # self.save_img("test_case_5")  # 没有报错也要截图的话，直接在这里调用方法就行了

    def tearDown(self):
        self.driver.quit()




# ################################################
# 如下为测试代码，正式运行时（run.py）,需要注释到
# ################################################

#if __name__ == "__main__":
#    unittest.main()