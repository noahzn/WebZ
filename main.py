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

import preprocess
import getcase
import os


class main :

    def __init__(self) :
        self.main()

# the output folder is 'D:/WebZ'
# please put the test case 'case.xlsx' in 'D:/'

    def main(self) :
        pathnow = os.getcwd()
        try :
            os.mkdir("D:/WebZ")
        except Exception as e:
            pass
        case = getcase.case_format().case_in_xlsx("D:/case.xlsx")
        preprocess.preprocess().process(case, pathnow)
        
if __name__ == '__main__':
    input("You can not run me")


