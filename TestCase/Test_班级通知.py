import unittest
import time
import os
from Config import globalconfig
from BeautifulReport import BeautifulReport
from Public.Pages.Notice import notice
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
        self.Notice = notice(self.driver)
        self.Notice.LoginBtnObj(mobileValue)
    # @BeautifulReport.stop
    @BeautifulReport.add_test_img('test_Notice_case_1')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img()方法
    def test_Notice_case_1(self):
        '''
        班级通知
        '''

        self.Notice = notice(self.driver)
        self.Notice.intoObj()
        self.Notice.addObj("测试班级通知")
        self.Notice.addvideoObj()
        time.sleep(4)
        # 断言
        result = self.driver.find_element_by_id('com.teacher.boxfairy:id/tv_class_content')
        self.save_img("test_Notice_case_1")
        self.assertEqual ('测试班级通知',result.text )
        #self.save_img("test_case_1")  # 没有报错也要截图的话，直接在这里调用方法就行了


    def tearDown(self):

        self.driver.quit()


# ################################################
# 如下为测试代码，正式运行时（run.py）,需要注释到
# ################################################

#if __name__ == "__main__":
#    unittest.main()