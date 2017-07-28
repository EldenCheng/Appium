# -*- coding; UTF-8 -*-
import os, time
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
#import HTMLTestRunner

class DragAndDrop(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '192.168.1.101:5555'
        desired_caps['appPackage'] = 'com.mobeta.android.demodslv'
        desired_caps['appActivity'] = 'com.mobeta.android.demodslv.Launcher'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_drag_and_drop(self):
        #Tap on Basic usage Playground.
        self.driver.find_element_by_name("Basic usage playground").click()
        #Locate 3rd element(Chick Corea) from list to drag.
        ele1 = self.driver.find_elements_by_id("com.mobeta.android.demodslv:id/drag_handle")
        print(ele1)
        #Perform drag and drop operation using TouchAction class.
        #It will hold tap on 3rd element and move to 5th position and then release tap.
        TouchAction(self.driver).long_press(ele1[2]).move_to(ele1[4]).release().perform()
        print("drag and drop successfully.")

if __name__ == '__main__':
    #suite = unittest.TestSuite()
    #suite.addTest(DragAndDrop('test_drag_and_drop'))
    suite = unittest.TestLoader().loadTestsFromTestCase(DragAndDrop)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #timestr = time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time()))
    #filename = "C:/Users/hardy.cao/PycharmProjects/TestDemo/Report/" + timestr + ".html"
    #fp = open(filename, 'wb')
    #runner = HTMLTestRunner.HTMLTestRunner(
        #stream=fp,
        #title='result',
        #description='report'
    #)
    #runner.run(suite)
    #fp.close()

    #a change for githug