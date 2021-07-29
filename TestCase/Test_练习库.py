import unittest
import pytest
import time
from Public.Pages.Practice import practive
from Public.common.DoExcel import ReadExcel
from Public.common.desired_caps import desired


mobileValue = int(ReadExcel("Data.xls","Sheet1").read_excel(1,0))

class Test_u0101(unittest.TestCase):

    def setUp(self):
        self.driver = desired()

    def test_practive_1(self):
        self.Publish = practive(self.driver)
        self.Publish.LoginBtnObj(mobileValue)
        self.Publish.intohomeworkObj()
        self.Publish.addpracticeObj("测试作业练习库")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

class Test_u0102(unittest.TestCase):

    def setUp(self):
        self.driver = desired()

    def test_practive_2(self):
        self.Publish = practive(self.driver)
        self.Publish.LoginBtnObj(mobileValue)
        self.Publish.intopracticeObj()
        self.Publish.contentObj("测试作业练习库（保存）")
        self.Publish.saveObj()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

class Test_u0103(unittest.TestCase):

    def setUp(self):
        self.driver = desired()

    def test_practive_3(self):
        self.Publish = practive(self.driver)
        self.Publish.LoginBtnObj(mobileValue)
        self.Publish.intopracticeObj()
        self.Publish.contentObj("测试作业练习库（另存为）")
        self.Publish.savenewObj()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

class Test_u0104(unittest.TestCase):

    def setUp(self):
        self.driver = desired()

    def test_practive_4(self):
        self.Publish = practive(self.driver)
        self.Publish.LoginBtnObj(mobileValue)
        self.Publish.intopracticeObj()
        self.Publish.assignmentObj()
        self.Publish.practivehomeworkObj("测试作业（练习库）")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

# ################################################
# 如下为测试代码，正式运行时（run.py）,需要注释到
# ################################################

#if __name__ == "__main__":
#    unittest.main()