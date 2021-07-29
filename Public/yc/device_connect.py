
from appium import webdriver


class RemoteDriver(object):

    def __init__(self,capabilitiesData):
        self.capabilitiesData = capabilitiesData
        platformName = capabilitiesData["platformName"]
        self.Capabilities = {}
        self.Capabilities["platformName"] = platformName
        self.Capabilities["platformVersion"] = capabilitiesData["platformVersion"]
        self.Capabilities["deviceName"] = capabilitiesData["deviceName"]
        if platformName.upper() =="ANDROID":
            self.Capabilities["appPackage"] = capabilitiesData["appPackage"]
            self.Capabilities["appActivity"] = capabilitiesData["appActivity"]
            self.Capabilities["automationName"] = "uiAutomator2"
            self.Capabilities["autoGrantPermissions"] = True # 自动获取需要哪些权限
            self.Capabilities["unicodeKeyboard"] = True # 使用Appium 自带的输入法
            self.Capabilities["resetKeyboard"] = True  # 输入法复位
        else:
            raise Exception("{0} 的手机类型不存在，只支持Android、iOS".format(platformName))

        self.Capabilities["udid"] = capabilitiesData["udid"]
        self.Capabilities["noReset"] = True
        self.Capabilities["newCommandTimeout"] = 72000

    def remoteDriver(self):
        """
        手机连接Appium server
        :return: Driver
        """
        remoteUrl = "http://{0}:{1}/wd/hub".format(str(self.capabilitiesData["host"]),str(self.capabilitiesData["port"]))
        driver = webdriver.Remote(remoteUrl,self.Capabilities)
        return driver
