# Portions copyright (c) 2014 ZMAN(ZhangNing)
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Name: WebZ
# Version: 0.0.3.141224
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
import sys
import os
import string
import keywords
import autoreport

class preprocess :
    def __init__(self) :
        print("Step.2 Run Test Cases...\n")
    
    def main_case(self, case, casecount) :
        browser, case = keywords.keywords().case_main(case)
        failcount, faillist = self.detail_case(browser, case, casecount)
        return(failcount, faillist)
            
            
    def detail_case(self,browser, case, casecount) :
        a = time.time()
        failcount  = 0
        faillist = []
        for item in range(len(case)) :
        
            if case[0] != '' :
                try :
                    c = case[0]
                    c = c.split('：')
                    c1 = keywords.keywords()


                    flag = c1.filter(browser, c[0])
                    if flag == 1 :
                        case.remove(case[0])

                    elif flag == 0 :
                        print("failed： %s" %(c[0]))
                        faillist.append("Test Case%02d：%s" %(casecount, c[0]))
                        case[0] = ''
                    
          
                except Exception as e :
                    print(e)
                    print("failed2222222 : %s：%s" %(c[0],c[1]))
                
        b = time.time()
        
        if flag == 1 :
            print("1 case pass, in %.3f s\n" %(b-a))
        elif flag == 0 :
            failcount += 1
            print("1 case failed, in %.3f s\n" %(b-a))
            
        time.sleep(1)
        browser.quit()
        
        return(failcount, faillist)


    def process(self, case, pathnow) :
        allcount = failcount = n = 0
        casecount = 1
        info = []
        faillist = []
        for item in range(len(case)) :
            if case[0] != '' :
                try :
                    if n == 0 :
                        info = case[0]
                        n += 1
                        case.remove(case[0])
                        continue
                    print("Test Case%02d：" %casecount)
                    allcount += 1
                    c = ctemp = case[0]
                    c = c.replace('，', ',')
                    c = c.split(',')
                    case.remove(case[0])
                    failtemp, faillisttemp = self.main_case(c, casecount)
                    if len(faillisttemp) !=0 :
                        faillist.append(faillisttemp[0])
                    if failtemp != 0 :
                        failcount += failtemp
                    casecount += 1
                except Exception as e :
                    print(e)
                    print("Error")
                    input()

        
        try :
            print("Step.3 generating test report...")
            try :
                autoreport.new_report().auto_chart(allcount, failcount, faillist, info, pathnow)
            except Exception as e:
                print(e)
                input()
            print("This test round has run %d test cases, %d failed!" %(allcount,failcount))
            print("END.")
            input()
        except Exception as e :
            print(e)
            print("Failed to generate test report!")

if __name__ == '__main__':
    input("You can not run me!")
