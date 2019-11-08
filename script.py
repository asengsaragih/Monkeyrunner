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
    device.touch(360, 1162, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang-form.png','png')
    MonkeyRunner.sleep(1)
    device.touch(49, 98, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)

    print "Setting Activity"
    device.touch(607, 1221, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang-setting.png','png')
    MonkeyRunner.sleep(1)

    print "Tentang Aplikasi"
    device.touch(321, 768, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang-tentang aplikasi.png','png')
    MonkeyRunner.sleep(1)

    #device.touch(607, 1221, 'DOWN_AND_UP')
    #MonkeyRunner.sleep(1)

    print "Tentang Developer"
    device.touch(652, 1218, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang-tentang developer.png','png')
    MonkeyRunner.sleep(1)
    device.touch(60, 1205, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    device.touch(60, 114, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    device.touch(65, 125, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)

    print "Chart Activity"
    device.touch(101, 1226, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    device.touch(384, 216, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    device.touch(546, 946, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang-chart.png','png')
    MonkeyRunner.sleep(1)
    device.touch(33, 114, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)

    print "History Activity"
    device.touch(668, 114, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang-history.png','png')
    MonkeyRunner.sleep(1)

    print "Main Activity"
    device.touch(54, 104, 'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('aseng\\ss\\utang-main.png','png')
    MonkeyRunner.sleep(1)

print "end monkey test"