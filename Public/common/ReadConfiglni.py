import configparser
import os

class ReadConfigIni():
    '''
    读取ini文件
    '''

    def __init__(self,filename):
        '''
        :param filename:ini文件名
        '''
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)
    def getConfigValue(self,config,name):
        value = self.cf.get(config,name)
        return value
        
# #############################################  
# 验证ReadConfigIni是否可以读取ini文件，且能够返回想要的值
# 该部分是测试代码，正式运行时，需要注释掉
# 注意：需要common途径下，创建一个config.ini文件，用于配合验证ReadConfigIni的作用      
# #############################################  
#file_path = os.path.split(os.path.realpath(__file__))[0]
#print(file_path)

#read_config = ReadConfigIni(os.path.join(file_path,"config.ini"))
#print(read_config)

#value = read_config.getConfigValue('project','project_path')
#print(value)
