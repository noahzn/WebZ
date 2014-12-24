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

class case_format :
    
    def __init__(self) :
        print("Step.1 Get Test Cases")

#if you write test cases in txt file, you can reference the following function        
    def case_in_txt(self, txt) :
        fr = open(txt, 'r')
        case = fr.readlines()
        fr.close()
        b =  []
        n = 1
        for a in case :
            a = a.rstrip('\n')
            if a != '' :
                b.append(a)
        return b

#you can modify the xlsx format

    def case_in_xlsx(self, xlsxfile) :
        import xlrd
        case = []
        fr = xlrd.open_workbook(xlsxfile)
        table = fr.sheets()[0]
        cols = table.ncols
        rows = table.nrows

        for m in range(8, rows) :
            a = ""
            for n in range(3, cols) :
                b = table.cell(m,n).value
                if b != '' :
                    b = b.strip(' ')
                    b = b.strip('\n')
                    a = a + "%s," %b
                    n += 1
                elif b == '' :
                    continue
            m += 1
            case.append(a)
  
        a = ""    
        for i in range(4) :
            j = table.cell(6,i).value
            j = j.strip('\n')
            a = a + "%s," %j
        a = a.strip(',')
        case[-1] = case[-1].strip(',')
        case.insert(0, a)
        
        return case

if __name__ == '__main__':
    input("You can not run me!")
