#测试数据是在1行，0列里存放
import xlrd
import os
from Config import globalconfig 


data_path = globalconfig.data_path
print(data_path)


class ReadExcel():
    '''
    打开Excel，并读取1行0列的测试数据
    '''

    def __init__(self,filename,sheetname):
        '''
        :param filename：Data.xls
        :param sheetname：Sheet1
        '''
        datapath= os.path.join(data_path,filename)#获得Excel对象
        self.workbook = xlrd.open_workbook(datapath)
        self.sheetName = self.workbook.sheet_by_name(sheetname)

    def read_excel(self,rownum,colnum):
        '''
        :param rownum：行号
        :param colnum：列号

        '''
        value = self.sheetName.cell(rownum,colnum).value
        return value
# #################################################################
#如下为测试代码，运行框架时，需要注释掉
#测试代码用于验证ReadExcel类的正确性
# #################################################################

#mobileValue = int(ReadExcel("Data.xls","Sheet1").read_excel(1,0))d
#print(mobileValue)