from BeautifulReport import BeautifulReport
import unittest
import time
from Config import globalconfig
from Public.common import send_mail as cc


#测试报告的路径
report_path = globalconfig.Report_path
#测试用例的路径
TestCase_path = globalconfig.TestCase_path

def AutoRun(TestCaseName):
    '''
    :param TestCaseName:
    :return:
    '''
    discover = unittest.defaultTestLoader.discover(TestCase_path,pattern=TestCaseName)
    
    now = time.strftime("%Y-%m-%d %H_%M_%S") #获取当前系统时间

    filename = now +'result.html'#拼接测试报告的名称 如果不能打开这个文件，可能是now的格式，不支持：和空格
    filename1 =report_path+'//'+ now +'result.html'#拼接测试报告的名称

    suit=BeautifulReport(discover).report(filename=filename,
    description='测试deafult报告', report_dir=report_path, theme='theme_default')
    # 运行用例filename=报告名称，description=所有用例总的名称，report_path=报告路径,如果不填写默认当前执行文件目录，
    # theme=报告的主题，有四种可以选择：theme_default，theme_cyan，theme_candy，theme_memories  默认是第一种

    #fp=open(filename1,'wb')
    #runner = HTMLTestRunner(stream=fp,title='测试报告',description="测试用例执行情况")
    #runner.run(discover)
    #fp.close()

    new_report = cc.newReport(report_path) #在测试是报告目录下获取最新的测试报告
    # print(new_report)
    cc.sendReport(new_report)

if __name__ == "__main__":
    AutoRun("Test_班级通知.py")