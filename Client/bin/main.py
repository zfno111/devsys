#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  os
import  sys
BASE_DIR = os.path.dirname(os.getcwd())
#设置工作目录
sys.path.append(BASE_DIR)


#引入处理器
from core import  handler


if __name__=="__main__":
    print("OK")
    handler.ArgvHandler(sys.argv)

