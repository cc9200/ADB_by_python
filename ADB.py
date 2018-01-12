# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:39:34 2018

@author: github/cc9200
"""
##import matplot.pyplot as plt
import os
import cv2

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

def screen_shot(devices_index=0,phone_path='/sdcard/screen_shot_temp1.png',cpu_path='phone_screen_shot_temp1.png',_print=False,ratio=1.0):
    cmd='adb shell screencap -p '+phone_path
    os.system(cmd)
    cmd='adb pull '+phone_path+' '+cpu_path
    if os.system(cmd)!=0:
        cpu_path=None
    if cpu_path and _print:
        img=cv2.imread(cpu_path)
        height,width,chn=img.shape
        width=int(width*ratio)
        height=int(height*ratio)
        img=cv2.resize(img,(width,height))
        cv2.imshow('temp',img)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
    return cpu_path

def tap(x,y):
    cmd='adb shell input tap {0} {1}'.format(x,y)
    return os.system(cmd)

def get_screen_size():
    cmd='adb shell wm size'
    r=os.popen(cmd).read()
    r=r.split(' ')[-1].strip()
    width,height=tuple(r.split('x'))
    return width,height

def swipe(x1,y1,x2,y2,long=200)  :
    cmd='adb shell input swipe {0} {1} {2} {3} {4}'.format(x1,y1,x2,y2,long)
    return os.system(cmd)

def unlock(password=''):
    cmd='adb shell input keyevent 82'
    os.system(cmd)
    return input_text(password)

def media_play():
    cmd='adb shell input keyevent KEYCODE_MEDIA_PLAY'
    return os.system(cmd)

def media_stop():
    cmd='adb shell input keyevent KEYCODE_MEDIA_STOP'
    return os.system(cmd)

def media_next():
    cmd='adb shell input keyevent KEYCODE_MEDIA_NEXT'
    return os.system(cmd)

def input_text(text=''):
    cmd='adb shell input text {}'.format(text)
    return os.system(cmd)

if __name__=='__main__':
#    unlock('091297')
#    screen_shot(_print=True,ratio=0.3)
#    media_play()
#    media_stop()
    print(get_screen_size())
    