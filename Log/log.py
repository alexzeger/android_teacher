import logging
import os
import time 
from Config import globalconfig

log_path = globalconfig.log_path
print(log_path)

class Logger():
    def __init__(self,logger,Cmdlevel,Filelevel):
        '''
        :param logger：
        :param CmdLevel：
        :param Filelevel：
        '''
        self.logger =logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #设定日志文件的名称
        #存放在log类所在的当前目录
        #将日志存放在指定的日志路径下

        self.LogFileName = os.path.join(log_path,"{0}.Log".format(time.strftime("%Y-%m-%d")))

        #设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(Cmdlevel)

        #设置文件日志
        fh=logging.FileHandler(self.LogFileName)
        fh.setFormatter(fmt)
        fh.setLevel(Filelevel)


        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def warning(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.critical(message)

# ############################测试日志文件，在正式运行时，需要注释############################
#if __name__ == "__main__":
#    logger = Logger("bela",CmdLevel=logging.INFO,Filelevel=logging.ERROR)
#    logger.debug("debug message")
#    logger.info("info message")
#    logger.warning("warning message")
#    logger.error("error message")
#    logger.critical("critical message")