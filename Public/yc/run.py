from .start_appium_server import AppiumServer

def run(capabilitiesData):
    appium_server = AppiumServer("127.0.0.1", 4723, "udid")
    appium_server.start_appium_server()
    RemoteDriver(capabilitiesData).remoteDriver()

if __name__ == '__main__':
    capabilitiesData = {"platformName":"Android","platformVersion":"7.1",
                        "deviceName":"小米1","appPackage":"com.tencent.mm",
                        "appActivity":"com.tencent.mm.plugin.sns.ui.SnsTimeLineUI",
                        "udid":"SJE5T17619002517"}
    run(capabilitiesData)
