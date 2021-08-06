from appium import webdriver


ServelUrl ='http://localhost:4723/wd/hub'
def desired():
    desired_caps ={ # 手机 系统信息
                    'platformName':'Android',
                    'platformVersion': '10',  # 华为真机
                    #'platforversion':'7.1.2',
                    # 设备号
                    'deviceName': 'D8H4C19A21002204',
                    # 'deviceName':'127.0.0.1:62001',
                    # 包名
                    'appPackage':'com.teacher.boxfairy',
                    # 启动名
                    #'appActivity':'com.teacher.boxfairy.mvp.ui.activity.login.LoginActivity',
                    'appActivity':'com.teacher.boxfairy.mvp.ui.activity.splash.SplashActivity',
                    'automationName':'Uiautomator2',
                    # 允许输入中文
                    'unicodeKeyboard':True, #使用unicode输入法
                    'resetKeyboard' : True,#重置输入法复位到初始状态
                    'autoGrantPermissions' : True ,# 自动获取需要哪些权限
                    'noReset':True,#启动app时，不要清除app里的原有数据
                    #'newCommandTimeout':600,#启动app时，命令的超时时间
                    }
    # 手机驱动对象
    driver = webdriver.Remote(ServelUrl,desired_caps)
    return driver
#测试打开，测试desired函数，能够被其他文件所调用；
#该测试代码，正式运行时，需要注释掉；
#if __name__ == '__main__':
#    desired()

