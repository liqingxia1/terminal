# -*- coding:utf-8 -*-
import os
import threading
import Collocations

class AppiumServer():
    def killTask(self):
        Command = "taskkill /F /im node.exe"
        a = AppiumServer()
        a.runCommand(Command)

    def runAppiumServer(self, port, udid):
        bpport = int(port) + 1
        chromeport = int(port) + 4792
        Command = "appium.cmd -p " + str(port) + " -bp " + str(bpport) + " --session-override --chromedriver-port " + str(chromeport) + " -U "+ udid + " >c://" + port + ".txt"
        print(Command)

        a = AppiumServer()
        a.runCommand(Command)

    def runCommand(self,command):
        os.system(command)


    def appiumServerThread(self, list, list1):
        a = AppiumServer()
        threads = []
        files = range(len(list))

        # 创建线程
        for i in files:
            t = threading.Thread(target=a.runAppiumServer, args=(list[i], list1[i]))
            print(list[i], list1[i])
            threads.append(t)
        for i in files:
            threads[i].start()
        for i in files:
            threads[i].join()



if __name__ == '__main__':
    a = AppiumServer()
    a.appiumServerThread(Collocations.ports, Collocations.udids)
