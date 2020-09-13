import time,image,sensor
from image import SEARCH_EX, SEARCH_DS
import math
import connect2
def templateMatch(sensor,model):
    # Template Matching Example - Normalized Cross Correlation (NCC)
    #
    # This example shows off how to use the NCC feature of your OpenMV Cam to match
    # image patches to parts of an image... expect for extremely controlled enviorments
    # NCC is not all to useful.
    #
    # WARNING: NCC supports needs to be reworked! As of right now this feature needs
    # a lot of work to be made into somethin useful. This script will reamin to show
    # that the functionality exists, but, in its current state is inadequate.
    #Something init from outsied of the main.py
    #Here are the model judge, but you may want to use another way to let it work.
    if model == "hand":
        templates = ["/hand/1.pgm", "/hand/2.pgm","/hand/3.pgm", "/hand/4.pgm", "/hand/5.pgm"]
    elif model == "object":
        templates = ["/object/1.pgm", "/object/2.pgm","/object/3.pgm" , "/object/4.pgm","/object/5.pgm"]
    elif model == "signs":
        templates = ["/signs/1.pgm", "/signs/2.pgm","/signs/3.pgm", "/signs/4.pgm", "/signs/5.pgm" ]
    else:
        print("Error module",model)
        templates = ["tmp/1.pgm"]
    #使用list引入模板图片

    a=True
    # Run template matching, and auto exit when finished.
    while (a):
        img = sensor.snapshot()

        # find_template(template, threshold, [roi, step, search])
        # ROI: The region of interest tuple (x, y, w, h).
        # Step: The loop step used (y+=step, x+=step) use a bigger step to make it faster.
        # Search is either image.SEARCH_EX for exhaustive search or image.SEARCH_DS for diamond search
        #
        # Note1: ROI has to be smaller than the image and bigger than the template.
        # Note2: In diamond search, step and ROI are both ignored.
        # , roi=(10, 0, 60, 60))
        for t in templates:
            template = image.Image(t)
        #对每个模板遍历进行模板匹配
        # , roi=(10, 0, 60, 60))
        r = img.find_template(template, 0.6, step=4, search=SEARCH_EX)
        #find_template(template, threshold, [roi, step, search]),threshold中
        #的0.7是相似度阈值,roi是进行匹配的区域（左上顶点为（10，0），长80宽60的矩形），
        #注意roi的大小要比模板图片大，比frambuffer小。
        #把匹配到的图像标记出来
        if r:
            img.draw_rectangle(r)
            print(t)  # 打印模板名字
            if t == "hand/1.pgm":
                connect2.handsfounction(1)
            elif t == "hand/2.pgm":
                connect2.handsfounction(2)
            elif t == "hand/3.pgm":
                connect2.handsfounction(3)
            elif t == "hand/4.pgm":
                connect2.handsfounction(4)
            elif t == "hand/5.pgm":
                connect2.handsfounction(5)
                a=False
            elif t == "tmp/1.pgm":
                connect2.sentdata(0,1)
                return


def QrCodeScan(sensor):
    #Something init from outsied of the main.py
    while(True):
        img = sensor.snapshot()
        img.lens_corr(1.8)  # strength of 1.8 is good for the 2.8mm lens.
        for code in img.find_qrcodes():
            return int(code.payload())
def ColorMatch(sensor):
    '''
    A founction to Match specific color.
    Such as Green Black or some other color.
    You may need a color bord to make it work propely.
    I'm not gonna to tell you it may make mistakes.
    @return is 001 010 100 or other things.
    '''
    # 为了使色彩追踪效果真的很好，你应该在一个非常受控制的照明环境中。
    template = [(0, 85, -68, -32, 19, 55),
                (56, 100, -128, 127, 42, 127),
                (45,   58,  69,   80,   42,   58),
                (21, 65, 0, 26, 21, 45)]
    green_threshold = (0,   80,  -70,   -10,   -0,   30)
    # 设置绿色的阈值，括号里面的数值分别是L A B 的最大值和最小值（minL, maxL, minA,
    # maxA, minB, maxB），LAB的值在图像左侧三个坐标图中选取。如果是灰度图，则只需
    # 设置（min, max）两个数字即可。
    px = False
    # 你可能需要调整上面的阈值来跟踪绿色的东西…
    # 在Framebuffer中选择一个区域来复制颜色设置。
    while(True):
        img = sensor.snapshot()  # 拍一张照片并返回图像。
        blobs = img.find_blobs(template)
        #find_blobs(thresholds, invert=False, roi=Auto),thresholds为颜色阈值，
        #是一个元组，需要用括号［ ］括起来。invert=1,反转颜色阈值，invert=False默认
        #不反转。roi设置颜色识别的视野区域，roi是一个元组， roi = (x, y, w, h)，代表
        #从左上顶点(x,y)开始的宽为w高为h的矩形区域，roi不设置的话默认为整个图像视野。
        #这个函数返回一个列表，[0]代表识别到的目标颜色区域左上顶点的x坐标，［1］代表
        #左上顶点y坐标，［2］代表目标区域的宽，［3］代表目标区域的高，［4］代表目标
        #区域像素点的个数，［5］代表目标区域的中心点x坐标，［6］代表目标区域中心点y坐标，
        #［7］代表目标颜色区域的旋转角度（是弧度值，浮点型，列表其他元素是整型），
        #［8］代表与此目标区域交叉的目标个数，［9］代表颜色的编号（它可以用来分辨这个
        #区域是用哪个颜色阈值threshold识别出来的）。
        c = []
        if blobs:
            #如果找到了目标颜色
            for b in blobs:
                #迭代找到的目标颜色区域
                # Draw a rect around the blob.
                img.draw_rectangle(b[0:4])  # rect
                #用矩形标记出目标颜色区域
                img.draw_cross(b[5], b[6])  # cx, cy
                #在目标颜色区域的中心画十字形标记
                c.append(b.code())
                if b.pixels() > 9000:
                    px = True
                    d=b.code()
                    if d ==4:
                        d=3
                    if d == 8:
                        d=4
            if (px):
                break
    return d

