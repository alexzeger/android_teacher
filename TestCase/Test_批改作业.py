import unittest
import time
import os
from Config import globalconfig
from BeautifulReport import BeautifulReport
from Public.Pages.complete import complete
from Public.common.DoExcel import ReadExcel
from Public.common.desired_caps import desired


mobileValue = int(ReadExcel("Data.xls","Sheet1").read_excel(1,0))

class Test_u0101(unittest.TestCase):

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
    def test_case_1(self):
        '''
        这是一个单个的单句作业
        需求：测试单句
        断言：打包作业测试

        '''

        self.complete = complete(self.driver)
        self.complete.intoObj()
        self.complete.details_1_Obj()
        self.complete.CorrectionObj("测 试 评 语","测 试 点 评")
        time.sleep(4)
        # 断言
        result = self.driver.find_element_by_ios_predicate('label == "已批阅" AND name == "已批阅" AND type == "XCUIElementTypeButton"')
        self.save_img("Test_u0101_test_case_1")
        self.assertEqual ('已批阅',result.text )
        #self.save_img("test_case_1")  # 没有报错也要截图的话，直接在这里调用方法就行了

    def test_case_2(self):
        '''
        这是一个单个的视频作业
        需求：测试单句
        断言：打包作业测试

        '''

        self.complete = complete(self.driver)
        self.complete.intoObj()
        self.complete.details_2_Obj()
        self.complete.CorrectionObj("测 试 评 语","测 试 点 评")
        time.sleep(4)
        # 断言
        result = self.driver.find_element_by_ios_predicate('label == "已批阅" AND name == "已批阅" AND type == "XCUIElementTypeButton"')
        self.save_img("Test_u0101_test_case_2")
        self.assertEqual ('已批阅',result.text )

    def test_case_3(self):
        '''
        这是一个单个动画配音的作业
        需求：测试单句
        断言：打包作业测试

        '''

        self.complete = complete(self.driver)
        self.complete.intoObj()
        self.complete.details_3_Obj()
        self.complete.CorrectionObj("测 试 评 语", "测 试 点 评")
        time.sleep(4)
        # 断言
        result = self.driver.find_element_by_ios_predicate(
            'label == "已批阅" AND name == "已批阅" AND type == "XCUIElementTypeButton"')
        self.save_img("Test_u0101_test_case_3")
        self.assertEqual('已批阅', result.text)
        # 没有报错也要截图的话，直接在这里调用方法就行了
    def tearDown(self):

        self.driver.quit()

