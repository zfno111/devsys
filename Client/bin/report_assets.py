#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

import urllib.request
import urllib.parse

import os
import sys

BASE_DIR = os.path.dirname(os.getcwd())
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)
from conf import settings

def update_test(data):
    """
    创建测试用例
    :return:
    """
    # 将数据打包到一个字典内，并转换为json格式
    data = {"asset_data": json.dumps(data)}
    # 根据settings中的配置，构造url
    url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
    print('正在将数据发送至： [%s]  ......' % url)
    try:
        # 使用Python内置的urllib.request库，发送post请求。
        # 需要先将数据进行封装，并转换成bytes类型
        data_encode = urllib.parse.urlencode(data).encode()
        response = urllib.request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
        print("\033[31;1m发送完毕！\033[0m ")
        message = response.read().decode()
        print("返回结果：%s" % message)
    except Exception as e:
        message = "发送失败"
        print("\033[31;1m发送失败，%s\033[0m" % e)


if __name__ == '__main__':
    windows_data = {
        "os_type": "Windows",
        "os_release": "7 64bit  6.1.7601 ",
        "os_distribution": "Microsoft",
        "asset_type": "server",
        "cpu_count": 2,
        "cpu_model": "Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz",
        "cpu_core_count": 8,
        "ram": [
            {
                "slot": "A1",
                "capacity": 8,
                "model": "Physical Memory",
                "manufacturer": "kingstone ",
                "sn": "456"
            },
            {
                "slot": "A2",
                "capacity": 16,
                "model": "Physical Memory",
                "manufacturer": "kingstone ",
                "sn": "345"
            },

        ],
        "manufacturer": "Intel",
        "model": "P67X-UD3R-B3",
        "wake_up_type": 6,
        "sn": "20426-OEM-8992662-121111",
        "physical_disk_driver": [
            {
                "iface_type": "unknown",
                "slot": 0,
                "sn": "3830414130423230343234362020202020202020",
                "model": "KINGSTON SV100S264G ATA Device",
                "manufacturer": "(标准磁盘驱动器)",
                "capacity": 128
            },
            {
                "iface_type": "SATA",
                "slot": 1,
                "sn": "383041413042323023234362020102020202020",
                "model": "KINGSTON SV100S264G ATA Device",
                "manufacturer": "(标准磁盘驱动器)",
                "capacity": 2048
            },

        ],
        "nic": [
            {
                "mac": "14:CF:22:FF:48:34",
                "model": "[00000011] Realtek RTL8192CU Wireless LAN 802.11n USB 2.0 Network Adapter",
                "name": 11,
                "ip_address": "192.168.1.110",
                "net_mask": [
                    "255.255.255.0",
                    "64"
                ]
            },
            {
                "mac": "0A:01:27:00:00:00",
                "model": "[00000013] VirtualBox Host-Only Ethernet Adapter",
                "name": 13,
                "ip_address": "192.168.56.1",
                "net_mask": [
                    "255.255.255.0",
                    "64"
                ]
            },
            {
                "mac": "14:CF:22:FF:48:34",
                "model": "[00000017] Microsoft Virtual WiFi Miniport Adapter",
                "name": 17,
                "ip_address": "",
                "net_mask": ""
            },
            {
                "mac": "14:CF:22:FF:48:34",
                "model": "Intel Adapter",
                "name": 17,
                "ip_address": "192.1.1.1",
                "net_mask": ""
            },


        ]
    }

#必须要把null转化下，因为python 无法识别
    global null,true,false
    null = ''
    true=1
    false=0
    linux_data={"_id": {"$oid": "5d5514309b38edbb05992186"}, "Placement": {"Zone": "ap-guangzhou-4", "ProjectId": 1010937, "HostIds": null}, "InstanceId": "ins-4mjdz5u2", "InstanceType": "S2.2XLARGE16", "CPU": 8, "Memory": 16, "RestrictState": "NORMAL", "InstanceName": "\u672a\u547d\u540d3", "InstanceChargeType": "POSTPAID_BY_HOUR", "SystemDisk": {"DiskType": "CLOUD_PREMIUM", "DiskId": "disk-qt38uive", "DiskSize": 50}, "DataDisks": [{"DiskSize": 200, "DiskType": "CLOUD_PREMIUM", "DiskId": "disk-evaid2dg", "DeleteWithInstance": true, "SnapshotId": null}], "PrivateIpAddresses": ["10.8.6.5"], "PublicIpAddresses": null, "InternetAccessible": {"InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR", "InternetMaxBandwidthOut": 0, "PublicIpAssigned": null, "BandwidthPackageId": null}, "VirtualPrivateCloud": {"VpcId": "vpc-m4cwhr8p", "SubnetId": "subnet-pqxoyuae", "AsVpcGateway": false, "PrivateIpAddresses": null}, "ImageId": "img-9qabwvbn", "RenewFlag": null, "CreatedTime": "2019-08-14T08:15:42Z", "ExpiredTime": null, "OsName": "CentOS 7.6 64\u4f4d", "SecurityGroupIds": ["sg-fwknr3wh"], "LoginSettings": {"Password": null, "KeyIds": null, "KeepImageLogin": null}, "InstanceState": "RUNNING", "Tags": [], "StopChargingMode": "NOT_APPLICABLE", "asset_type": "server", "sn": "ins-4mjdz5u2", "os_distribution": "Linux", "os_type": "Linux", "os_release": "CentOS 7.6 64\u4f4d", "cpu_count": 1, "cpu_model": "inter", "cpu_core_count": 8, "ram": [{"slot": "A1", "capacity": 16}], "physical_disk_driver": [{"model": "FAST", "size": "666", "sn": "disk-evaid2dg"}], "idcname": "ap-guangzhou-4", "ip": ["10.8.6.5"]}

    update_test(linux_data)
    #update_test(windows_data)