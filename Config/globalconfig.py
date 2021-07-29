import os
from Public.common.ReadConfiglni import ReadConfigIni

#读取config目录下的ini配置文件，用于获得工程路径文件

#获取config.ini所在的路径
file_path = os.path.split(os.path.realpath(__file__))[0]
# print(file_path)

#获取config.ini对象
read_config = ReadConfigIni(os.path.join(file_path, "config.ini"))
# print(read_config)

#获取config.ini的工程路径
project_path = read_config.getConfigValue('project','project_path')
# print(project_path)

#日志路径
log_path = os.path.join(project_path,"Report","Log")
#print(log_path)
#错误截图路劲
img_path = os.path.join(project_path,"Report","Image")

#print(img_path)
#测试用例路径
TestCase_path = os.path.join(project_path,"TestCase")
#print(TestCase_path)
#测试报告路径
Report_path = os.path.join(project_path,"Report","TestReport")
#print(Report_path)
#测试数据路径
data_path = os.path.join(project_path,"Data")
#print(data_path)