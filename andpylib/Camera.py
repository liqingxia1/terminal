import time

from andpylib.Mobile import Mobile

class Camera(Mobile):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def switchingCamera(self):
        Mobile.phone.find_element_by_id("org.codeaurora.snapcam:id/front_back_switcher").click()





def oneTest():
    C8_Device = Camera()

    C8_Device.android('6.0.1', 'org.codeaurora.snapcam', 'com.android.camera.CameraLauncher')
    i = 50
    while i > 0:
        C8_Device.switchingCamera()
        i = i - 1
        time.sleep(1)

    C8_Device.phone.close_app()

if __name__ == '__main__':
    # 进行代码调试
    oneTest()

