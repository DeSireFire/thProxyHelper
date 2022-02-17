#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/2/17
# CreatTIME : 14:05 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'
# 东方登录
import json
import chardet
import requests
import base64
from config import *



class GetToken():
    """获取token"""

    def __init__(self):
        self.login_url = 'aHR0cHM6Ly9wb3J0YWwudG91aG91LnRlbC9hdXRoL2xvZ2lu'
        self.checkin_url = 'aHR0cHM6Ly9wb3J0YWwudG91aG91LnRlbC91c2VyL2NoZWNraW4='
        self.logout_url = 'aHR0cHM6Ly9wb3J0YWwudG91aG91LnRlbC91c2VyL2xvZ291dA=='
        self.login_data = {
          'email': email,
          'passwd': passwd,
          'code': '',
          'remember_me': 'hour'
        }
        self.timeout = 10.0
        self.headers = {
            'authority': 'portal.touhou.tel',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
            # 'origin': 'https://portal.touhou.tel',
            # 'referer': 'https://portal.touhou.tel/user',
        }
        self.cookies = None
        self.session = requests.session()

    def loginUser(self):
        """登录账户获取cookie"""
        session = self.session
        res = session.post(self.b2s(self.login_url), json=self.login_data, headers=self.headers, timeout=float(self.timeout))
        ck = res.cookies
        if not self.cookies:
            self.cookies = ck.get_dict()
        return res

    def checkInSignin(self):
        """签到"""
        session = self.session
        res = session.post(self.b2s(self.checkin_url), headers=self.headers, timeout=float(self.timeout))
        res = self.chartHandler(res)
        return res

    def loginOut(self):
        """退出登录状态"""
        session = self.session
        res = session.get(self.b2s(self.logout_url), headers=self.headers, timeout=float(self.timeout))
        # res = self.chartHandler(res)
        return res

    def chartHandler(self, requests_response):
        """
        自转码处理器
        若响应结果为json字符串，
        转码后还需要通过json.loads序列化，
        才能转换为中文。
        :param requests_response: obj, requests的response对象
        :return:
        """
        # 获取网页编码格式，并修改为request.text的解码类型
        requests_response.encoding = chardet.detect(requests_response.content)['encoding']
        if requests_response.encoding == "GB2312":
            requests_response.encoding = "GBK"
        return requests_response

    def b2s(self, bs):
        """
        防扫拐个弯
        :param bs: str, 暗送秋波
        :return:
        """
        return str(base64.b64decode(bs), "utf-8")


if __name__ == '__main__':
    gettoken = GetToken()
    loginUser = gettoken.loginUser()
    checkInSignin = gettoken.checkInSignin()
    res_json = json.loads(checkInSignin.text)
    loginOut = gettoken.loginOut()
    print(res_json)
    print("签到完成！")