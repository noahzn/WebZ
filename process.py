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

class process :
    
    def __init__(self) :
        return


    def openpage(self, url) :
        import splinter
        import selenium
        browser = splinter.Browser('chrome')
        browser.driver.maximize_window()
        browser.visit(url)
        time.sleep(2)
        return browser


    def sendcase_click(self, browser, widget, method, name) :
        if widget == 'id' and method == 'click' :
            cmethod = 'browser.find_by_id("%s").click()' %name
            flag2 = self.docase(browser,cmethod)
            
        elif widget == 'css' and method == 'click' :
            cmethod = 'browser.find_by_css("%s").click()' %name
            flag2 = self.docase(browser,cmethod)
            
        elif widget == 'xpath' and method == 'click' :
            cmethod = "browser.find_by_xpath('%s').click()" %name
            flag2 = self.docase(browser,cmethod)
            
        return(flag2)


    def sendcase_fill(self, browser, widget, method, name, attr) :
        if widget == 'id' and method == 'fill' :
            cmethod = 'browser.find_by_id("%s").fill("%s")' %(name, attr)

        elif widget == 'css' and method == 'fill' :
            cmethod = 'browser.find_by_css("%s").fill("%s")' %(name, attr)

        elif widget == 'xpath' and method == 'fill' :
            cmethod = "browser.find_by_xpath('%s').fill('%s')" %(name, attr)


        flag2 = self.docase(browser,cmethod)
        return(flag2)

    def sendcase_action2(self, browser, method, attr) :
        if method == 'alert' :
            if attr == '是' :
                cmethod = 'browser.get_alert().accept()'
            elif attr == '否' :
                cmethod = 'browser.get_alert().dismiss()'

        elif method == 'switch' :
            if attr == '最新' :
                cmethod = 'browser.switch_to_window(browser.windows[-1])'
            else :
                attr = int(attr)-1
                cmethod = 'browser.switch_to_window(browser.windows[%d])' %attr


        flag2 = self.docase(browser,cmethod)
        return(flag2)


    def sendcase_action(self, browser, method) :
        if method == 'back' :
            cmethod = 'browser.back()'

        elif method == 'refresh' :
            cmethod = 'browser.reload()'

        elif method == 'screenshot' :          
            cmethod = 'browser.screenshot(name="D:/WebZ/WebZ", suffix=".jpg")'

        elif method == 'wait' :
            cmethod = 'time.sleep(2)'


        flag2 = self.docase(browser,cmethod)
        return(flag2)


    def sendcase_click_text(self, browser, method, name) :
        if method == 'click_text' :
            cmethod = 'browser.click_link_by_text("%s")' %name

        elif method == 'visit' :
            if 'http://' not in name :
                name = 'http://%s' %name
            cmethod = 'browser.visit("%s")' %name


        flag2 = self.docase(browser,cmethod)  
        return(flag2)

    def mouse_move(self, browser, method, name) :
        if method == 'css' :
            cmethod = 'browser.find_by_css("%s").mouse_over()' %name

        elif method == 'xpath' :
            cmethod = 'browser.find_by_xpath("%s").mouse_over()' %name


        flag2 = self.docase(browser,cmethod)
        return(flag2)  


# try three times

    def sendcase_verify(self, browser, widget, attr) :
        i = flag2 = 0
        if widget == 'xpath' :
            for i in range(2) :
                try :
                    a = browser.find_by_xpath('%s' %attr)
                    if len(a) != 0 :
                        flag2 = 1
                        return(flag2)
                    elif len(a) == 0 :
                        time.sleep(0.5)
                        i += 1
                        if i == 2 :
                            return(flag2)
                except Exception as e :
                    print(e)
                        
        elif widget == 'css' :
            for i in range(2) :
                try :
                    a = browser.find_by_css('%s' %attr)
                    if len(a) != 0 :
                        flag2 = 1
                        return(flag2)
                    elif len(a) == 0 :
                        time.sleep(0.5)
                        i += 1
                        if i == 2 :
                            return(flag2)
                except Exception as e :
                    print(e)

        elif widget == 'url' :
            for i in range(2) :
                try :
                    a = browser.url
                    a = a.rstrip('/')
                    if "http://" + attr == a :
                        flag2 = 1
                        return(flag2)
                    elif "http://" + attr != a :
                        time.sleep(0.5)
                        i += 1
                        if i == 2 :
                            return(flag2)
                except Exception as e :
                    print(e)

        elif widget == 'text' :
            for i in range(2) :
                try :
                    a = browser.is_text_present('%s' %attr)
                    if a == True :
                        flag2 = 1
                        return(flag2)
                    elif a == False :
                        time.sleep(0.5)
                        i += 1
                        if i == 2 :
                            return(flag2)
                except Exception as e :
                    print(e)
    

    def docase(self, browser, cmethod) :
        i = flag2 = 0
        for i in range(3) :
            try :
                exec(cmethod)
                flag2 = 1
                return(flag2)
            except Exception as e:
                if "Element is not currently interactable" in str(e) :
                    print('something wrong with webdriver')
                    return(flag2)
                else :
                    print(e)
                    time.sleep(1.5)
                    i += 1
                    if i == 3 :
                        return(flag2)


if __name__ == '__main__':
    input("You can not run me!")
