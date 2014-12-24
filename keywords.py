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

import time
import process


class keywords :
    def __init__(self) :
        return
    
    # Open your browser
    def case_main(self, case) :
        case2 = case[0].split('|')
        if case2[0] == "打开网页" :
            browser = process.process().openpage("http://%s" %case2[1])
            case.remove(case[0])
        return(browser, case)
        
    # main key words
    def filter(self, browser,case) :
        case = case.split('|')

        # click
        if case[0] == "点击" :
            case[1] = case[1].split('@@')
            flag2 = process.process().sendcase_click(browser,case[1][0],'click',case[1][1])

        # fill
        elif case[0] == "填写" :
            case[1] = case[1].split('@@')
            flag2 = process.process().sendcase_fill(browser,case[1][0],'fill',case[1][1],case[1][2])

        # back forward
        elif case[0] == "后退" :
            flag2 = process.process().sendcase_action(browser,'back')

        # click on the text link 
        elif case[0] == "点击文字" :
            flag2 = process.process().sendcase_click_text(browser,'click_text', case[1])

        # go forward
        elif case[0] == "前往" :
            flag2 = process.process().sendcase_click_text(browser,'visit',case[1])

        # refresh
        elif case[0] == "刷新" :
            flag2 = process.process().sendcase_action(browser,'refresh')

        # verify
        elif case[0] == "验证" :
            case[1] = case[1].split('@@')
            flag2 = process.process().sendcase_verify(browser,case[1][0], case[1][1])

        # screenshot
        elif case[0] == "截图" :
            flag2 = process.process().sendcase_action(browser, 'screenshot')

        # wait
        elif case[0] == "等待" :
            flag2 = process.process().sendcase_action(browser, 'wait')

        # move mouse to
        elif case[0] == "鼠标移至" :
            case[1] = case[1].split('@@')
            flag2 = process.process().mouse_move(browser, case[1][0],case[1][1])

        # alert
        elif case[0] == "处理警告" :
            flag2 = process.process().sendcase_action2(browser, 'alert', case[1])
        
        # switch window
        elif case[0] == "切换窗口" :
            flag2 = process.process().sendcase_action2(browser, 'switch', case[1])


        return(flag2)
            

        
    
if __name__ == '__main__':
    input("You can not run me")
