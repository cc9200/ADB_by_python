# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:39:34 2018

@author: github/cc9200
"""
##import matplot.pyplot as plt
import os
from PIL import Image
import matplotlib.pyplot as plt

def adb_connect(ip,port='5555'):
    cmd='adb connect '+ip+':'+port
    #cmd='ping 192.168.1.7'
    r=os.popen(cmd).read()
    return 'connected' in r

def adb_devices():
    r=os.popen('adb devices').read()
    ls=r.split('\n')[1:-2]

    ls2=[]
    for each in ls:
        ls2.append(each.strip('\tdevice'))
    return ls2

def select_app(device_index=0):
    dev=adb_devices()[device_index]
    cmd='adb -s {} shell pm list packages'.format(dev)
    return os.popen(cmd).read().split('\n')

def screen_shot(devices_index=0,phone_path='/sdcard/screen_shot_temp1.png',cpu_path='phone_screen_shot_temp1.png',_print=False):
    cmd='adb shell screencap -p '+phone_path
    os.system(cmd)
    cmd='adb pull '+phone_path+' '+cpu_path
    temp_path=None
    if os.system(cmd)==0:
        temp_path=cpu_path
    if temp_path and _print:
        img=Image.open(temp_path)
        plt.figure('temp')
        plt.imshow(img)
        plt.show()
    return temp_path
if __name__=='__main__':
    print(screen_shot(_print=True))
