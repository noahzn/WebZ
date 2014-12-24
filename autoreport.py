# Portions copyright (c) 2014 ZMAN(ZhangNing)
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Name: WebZ
# Description: keyword-driven automated testing framework
# Author: ZMAN(ZhangNing)
#
# This project also used some third-party modules:
#
# selenium: Licensed under the Apache License, Version 2.0 (the "License");
# Copyright 2008-2013 Software Freedom Conservancy.
#
# splinter: Licensed under the BSD License;
# Copyright 2012 splinter authors. All rights reserved.
#
# reportlab: Licensed under the BSD License;
# Copyright ReportLab Europe Ltd. 2000-2014.
#
# xlrd: Licensed under the BSD License;
# Portions copyright 2005-2009, Stephen John Machin, Lingfo Pty Ltd. All rights reserved.
#


from reportlab.graphics.shapes import *
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.graphics.charts.textlabels import Label
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.lib import fonts
import os
import shutil


class new_report() :

    def __init__(self) :
        return

    
    def auto_chart(self, allcount, failcount, faillist, info, pathnow) :
        from reportlab.graphics.shapes import Drawing
        from reportlab.graphics import renderPDF
        from reportlab.graphics.charts.barcharts import VerticalBarChart
        from reportlab.lib import colors

        info = info.replace('，', ',')
        info = info.split(',')
        c = 0
        infolist = ['project name:','version:','test type:','tester:','results:']
        testtype = info[2]
        if failcount == 0 :
            info.append('pass')

        elif failcount != 0 :
            info.append('fail')
      
        drawing = Drawing(800,900)

        data = [(failcount,),((allcount - failcount),)]

        bc = VerticalBarChart()
        bc.x = 250
        bc.y = 110
        bc.height = 250
        bc.width = 300
        bc.groupSpacing = 25
        bc.data = data
        bc.strokeColor = colors.black

        bc.valueAxis.valueMin = 0
        bc.valueAxis.valueMax = 16
        bc.valueAxis.valueStep = 1

        bc.categoryAxis.labels.boxAnchor = 'ne'
        bc.categoryAxis.labels.dx = 4
        bc.categoryAxis.labels.dy = -2
        bc.categoryAxis.labels.angle = 30
        bc.categoryAxis.categoryNames = ['%s' %info[1],]
        bc.categoryAxis.style = 'stacked'
        drawing.add(bc)
        drawing.add(String(350,860,"Test Report!",fontSize=25, fillColor=colors.black))

        

        for i in infolist :
            xt = '%s%s' %(i,info[0])
            try:
                x_wid = self.get_width(xt, 14, 1)
            except Exception as e:
                print(e)

            x = 100 + x_wid/2
            y = 800 - c
            c += 25
            
            drawing.add(self.cn_process(i+info[0], x, y, pathnow))
            info.remove(info[0])

        xt2 = 100+(self.get_width("this %s has run %2d test case(s). pass: %2d, fail: %2d." %(testtype,allcount,(allcount-failcount),failcount),14,1)/2)

        drawing.add(self.cn_process("this %s has run %2d test case(s). pass: %2d, fail: %2d." %(testtype,allcount,(allcount-failcount),failcount), xt2, 650, pathnow))
        if failcount != 0 :
            xt3 = 100 +(self.get_width("failed details: ",14,1)/2)
            drawing.add(self.cn_process("failed details: ", xt3, 625, pathnow))
        drawing.add(self.cn_process("Dept.QA", 640, 80, pathnow))

        y2 = 625
        for m in faillist :
            y2 -= 25
            xt3 = 130 + (self.get_width(m,14,1)/2)
            if xt3 > 500 :
                m = m[:65] + '...'
                xt3 = 130 + (self.get_width(m,14,1)/2)
            drawing.add(self.cn_process(m, xt3, y2, pathnow))
            

        renderPDF.drawToFile(drawing, 'D:/WebZ/test report.pdf')


    def auto_log(self, allcount, failcount) :
        return


#the codes below can process Chinese character, you need a monospaced font.
    def cn_process(self, text, x, y, pathnow) :
        pdfmetrics.registerFont(ttfonts.TTFont("font1",'simsun.ttc'))
        title = Label()
        title.fontName = "font1"
        title.fontSize = 14
        title_text = text
        title._text = title_text
        title.x = x
        title.y = y

        return (title)

    def get_width(self, string, size, charspace) :
        pdfmetrics.registerFont(ttfonts.TTFont("font1",'simsun.ttc'))
        width = stringWidth(string, "font1", size)
        return width


if __name__ == '__main__':
    input("You can not run me")
