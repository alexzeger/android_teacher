import unittest
import pytest

from Public.Pages.homework import Publish
from Public.common.DoExcel import ReadExcel
from Public.common.desired_caps import desired


mobileValue = int(ReadExcel("Data.xls","Sheet1").read_excel(1,0))

class Test_login(unittest.TestCase):

    def setUp(self):
        self.driver = desired()

    def test_login(self):
        self.teacher = Teacher(self.driver)
        self.teacher.waitActivity("com.teacher.boxfairy.mvp.ui.activity.login.LoginActivity",100)
        self.teacher.MobileTextObj(mobileValue)
        self.teacher.VerifyCodeTextObj()
        self.teacher.LoginBtnObj()

    def tearDown(self):
        self.driver.close_app()

# ################################################
# 如下为测试代码，正式运行时（run.py）,需要注释到
# ################################################

#if __name__ == "__main__":
#    unittest.main()