import cv2 as cv
def template_demo():
    tpl = cv.imread("./p.png")
    target = cv.imread("./target.png")
    #methods = [cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]#各种匹配算法
    methods = [cv.TM_SQDIFF_NORMED]  # 各种匹配算法
    th,tw = tpl.shape[:2]#获取模板图像的高宽
    for md in methods:
        result = cv.matchTemplate(target,tpl,md)
        # result是我们各种算法下匹配后的图像
        # cv.imshow("%s"%md,result)
        #获取的是每种公式中计算出来的值，每个像素点都对应一个值
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc    #tl是左上角点
        else:
            tl = max_loc
        br = (tl[0]+tw,tl[1]+th)    #右下点
        #cv.rectangle(target,tl,br,(0,0,255),2)#画矩形
        #cv.namedWindow("match-%s"%md, 0);
        #cv.imshow("match-%s"%md,target)
        #cv.waitKey(500)  # 等待用户操作，里面等待参数是毫秒，我们填写0，代表是永远，等待用户操作
        #cv.destroyAllWindows()  # 销毁所有窗口
        return (tl,br)
#template_demo()
#cv.waitKey(1)   #等待用户操作，里面等待参数是毫秒，我们填写0，代表是永远，等待用户操作
#cv.destroyAllWindows()  #销毁所有窗口