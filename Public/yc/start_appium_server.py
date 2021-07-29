
import subprocess
import os
import time
import requests
import sys
import re


class AppiumServer(object):
    def __init__(self, host, port, udid, webDriver=None):
        self.host = host
        self.port = port
        self.udid = udid
        self.webDriver = webDriver

    def start_appium_server(self):
        """
        启动Appium Server
        :param host: 启动的本地ip
        :param port: 启动端口
        :param udid: 绑定的udid
        """
        bootStarpPort = str(self.port + 1)
        appium_log = os.path.join('.', str(self.port) + '.log')
        if os.path.exists(appium_log):
            os.remove(appium_log)

        cmd = " appium -a {0} -p {1} -bp {2} -U {3} --session-override -g {4}".format(
            self.host, self.port, bootStarpPort, self.udid, appium_log)
        if self.checkPort():
            self.stopPort()

        p = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
        flage = False
        checkCount = 0
        while not flage and checkCount < 7:
            time.sleep(1)
            flage = self.checkPort()
            if flage:
                print("端口：{0} Appium 系统服务启动成功".format(self.port))
            if not flage and checkCount == 6:
                print("端口：{0} Appium 系统服务启动成功".format(self.port))
            checkCount += 1

    def checkPort(self):
        """
        端口检查
        :return: check res
        """
        try:
            requests.get("http://{0}:{1}/wd/hub/status".format(self.host, self.port))
            res = True
        except:
            res = False
        return res

    def stopPort(self):
        """
        关闭appium server
        :param port:
        :return:
        """

        platform = sys.platform
        if "win" in platform:
            cmd = 'netstat -ano|findstr "{0}"'.format(self.port)
        else:
            cmd = "ps -ef | grep {0}".format(self.port) + "| awk '{print $2}'"
        pid_list = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        pattrn = re.compile(r"(\d+)")
        for pid in pid_list:
            if "win" in platform:
                cmd = "taskkill /pid   {0} /f".format(pattrn.findall(str(pid))[-1])
                print(cmd)
            else:
                cmd = 'kill -9 {0}'.format(pattrn.findall(str(pid))[0])
            os.system(cmd)
        print("端口:{0}退出成功".format(self.port))


if __name__ == '__main__':
    appium_server = AppiumServer("127.0.0.1", 4723, "udid")
    appium_server.start_appium_server()

