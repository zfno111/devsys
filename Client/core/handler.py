# -*- coding:utf-8 -*-

import json
import time
from core import info_collection
from conf import settings
import requests


class ArgvHandler(object):
    def __init__(self, args):
        self.args = args
        self.parse_args()

    def parse_args(self):
        """
       分析参数，如果有参数指定的方法，则执行该功能，如果没有，打印帮助说明。
       :return:
       """
        if len(self.args) > 1 and hasattr(self, self.args[1]):
            if self.args[1] == 'parse_args':
                exit(0)
            func = getattr(self, self.args[1])
            func()
        else:
            self.help()

    @staticmethod
    def help():
        """
        帮助说明
        :return:
        """
        msg = '''
                参数名               功能

                collect_data        测试收集硬件信息的功能

                report_data         收集硬件信息并汇报
                '''
        print(msg)

    @staticmethod
    def collect_data():
        """收集硬件信息,用于测试！"""
        #返回的是windows，或者linux
        info = info_collection.InfoCollection()
        asset_data = info.collect()
        print(asset_data)

    @staticmethod
    def report_data():
        """
        收集硬件信息，然后发送到服务器。
        :return:
        """

        info = info_collection.InfoCollection()
        asset_data = info.collect()

        data = {'asset_data': json.dumps(asset_data)}
        url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
        print('正在将数据发送至： [%s]  ......' % url)
        try:

            r = requests.post(url=url, data=data, timeout=settings.Params['request_timeout'])
            print("\033[31;1m发送完毕！\033[0m ")
            print(r.text)




        except Exception as e:
            message = '发送失败' + "   错误原因：  {}".format(e)
            print("\033[31;1m发送失败，错误原因： %s\033[0m" % e)
        # 记录发送日志
        with open(settings.PATH, 'ab') as f:  # 以byte的方式写入，防止出现编码错误
            log = '发送时间：%s \t 服务器地址：%s \t 返回结果：%s \n' % (time.strftime('%Y-%m-%d %H:%M:%S'), url, r.text)
            f.write(log.encode())
            print("日志记录成功！")
