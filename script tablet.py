#! /usr/bin/env monkeyrunner

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from random import randint

print "get device"
device = MonkeyRunner.waitForConnection()
package = 'org.d3ifcool.utang'
activity = 'org.d3ifcool.utang.MainActivity'
runComponent = package + '/' + activity
device.startActivity(component=runComponent)

MonkeyRunner.sleep(5)

device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

print "start monkey test"
for i in range(1, 2):
    MonkeyRunner.sleep(3)
    print "Form Activity"
    device.touch(628, 668, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang tablet-form.png','png')
    MonkeyRunner.sleep(1)
    device.touch(28, 33, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)

    print "Setting Activity Tablet"
    device.touch(1200, 716, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang tablet-setting.png','png')
    MonkeyRunner.sleep(1)

    print "Tentang Aplikasi Tablet"
    device.touch(628, 361, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang tablet-tentang aplikasi.png','png')
    MonkeyRunner.sleep(1)

    print "Tentang Developer Tablet"
    device.touch(1244, 723, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang tablet-tentang developer.png','png')
    MonkeyRunner.sleep(1)
    device.touch(36, 31, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    device.touch(32, 33, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)

    print "Chart Activity Tablet"
    device.touch(40, 716, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    device.touch(632, 90, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    device.touch(852, 518, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang tablet-chart.png','png')
    MonkeyRunner.sleep(1)
    device.touch(36, 30, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)

    print "History Activity Tablet"
    device.touch(1244, 33, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang tablet-history.png','png')
    MonkeyRunner.sleep(1)

    print "Main Activity Tablet"
    device.touch(32, 31, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang tablet-main.png','png')
    MonkeyRunner.sleep(1)

print "end monkey test"