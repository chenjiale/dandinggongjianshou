import os
import getLocation
import datetime;  # 引入time模块
def getSwipeP():
    os.system("adb shell screencap /sdcard/target.png")
    os.system("adb pull  /sdcard/target.png C:\\Users\\Administrator\\PycharmProjects\\untitled")
    print(datetime.datetime.now())
    tl,br = getLocation.template_demo()
    print(tl , br)
    #取截取图标中心y轴 上调20 瞄小人的头
    x,y=(tl[0]+br[0])/2,(tl[1]+br[1])/2-20
    print(x,y)
    #求横轴比,值越大仰角约小test2.py
    c= (1700-x)/(800-y)
    c=round(c, 2)*0.7
    #延伸300像素，求增加的x y轴
    #将射箭的店1700，800设为原点，则x y变换为
    x,y=1700-x,800-y
    #根据抛物线公式求最大初始度v 1/c=tan
    #y=x/c-10x**/(2v*v/(c*c+1))
    g=10
    v=((g*x*x*(c*c+1))/(2*x/c-2*y))**0.5
    v = round(v)
    print("位置 {} {}力道值{},加速度{} tan {}".format(x,y,v,g,1/c))
    n=(v*v/(c*c+1))**0.5
    n=round(n)
    m=round(n*c)
    return (m,n)
def swipe(t,*args):
    print("adb shell input swipe {} {} {} {} {}".format(*args,t))
    os.system("adb shell input swipe {} {} {} {} {}".format(*args,t))
while 1:
    try:
        m,n=getSwipeP()
        swipe(40, 1700 -800, 800 - 800 * n / m, 1700, 800)
    except:
        pass