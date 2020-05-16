import re

import requests

from yiban.config import ACCOUNT, PASSWD

"""
author: wade
time: 2020-5-15 15:20
Reference project: 
- https://github.com/looyeagee/yiban_auto_submit 
- https://github.com/Avenshy/YibanCheckin
Reference link: 
- https://looyeagee.cn/software/yiban
"""


class YiBan:
    WFId = "ecac36c256540165ec2fd412a33f50f8"  # 疫情表单：固定表单值固定 每个大学可能不一样需要自行抓包 此处为长沙理工大学0512更新
    CSRF = "sui-bian-fang-dian-dong-xi"  # 随机值 随便填点东西
    COOKIES = {"csrf_token": CSRF}  # 固定cookie 无需更改
    HEADERS = {"Origin": "https://c.uyiban.com", "User-Agent": "yiban"}  # 固定头 无需更改

    def __init__(self, account, passwd):
        self.account = account
        self.passwd = passwd
        self.session = requests.session()

    def request(self, url, method="get", params=None, cookies=None):
        if method == "get":
            req = self.session.get(url, params=params, timeout=10, headers=self.HEADERS, cookies=cookies)
        else:
            req = self.session.post(url, data=params, timeout=10, headers=self.HEADERS, cookies=cookies)
        try:
            # print(req.json())
            return req.json()
        except:
            return None

    def login(self):
        params = {
            "account": self.account,
            "ct": 2,
            "identify": 0,
            "v": "4.7.4",
            "passwd": self.passwd
        }
        #         r = self.request(url="https://mobile.yiban.cn/api/v2/passport/login", params=params)
        r = self.request(url='https://mobile.yiban.cn/api/v2/passport/login', params=params)

        if r is not None and str(r["response"]) == "100":
            self.access_token = r["data"]["access_token"]
            self.name = r["data"]["user"]["name"]
            return r
        else:
            return None

    def auth(self):
        location = self.session.get("http://f.yiban.cn/iapp/index?act=iapp7463&v=%s" % self.access_token,
                                    allow_redirects=False).headers["Location"]
        verifyRequest = re.findall(r"verify_request=(.*?)&", location)[0]
        # print(verifyRequest)
        return self.request(
            "https://api.uyiban.com/base/c/auth/yiban?verifyRequest=%s&CSRF=%s" % (verifyRequest, self.CSRF),
            cookies=self.COOKIES)

    def getUncompletedList(self):
        return self.request("https://api.uyiban.com/officeTask/client/index/uncompletedList?CSRF=%s" % self.CSRF,
                            cookies=self.COOKIES)

    def getCompletedList(self):
        return self.request("https://api.uyiban.com/officeTask/client/index/completedList?CSRF=%s" % self.CSRF,
                            cookies=self.COOKIES)

    def getTaskDetail(self, taskId):
        return self.request(
            "https://api.uyiban.com/officeTask/client/index/detail?TaskId=%s&CSRF=%s" % (taskId, self.CSRF),
            cookies=self.COOKIES)

    def getForm(self):
        return self.request(
            "https://api.uyiban.com/workFlow/c/my/apply/%s?CSRF=%s" % (self.WFId, self.CSRF),
            cookies=self.COOKIES)

    def submit(self, data, extend):
        params = {
            "data": data,
            "extend": extend
        }
        return self.request(
            "https://api.uyiban.com/workFlow/c/my/apply/%s?CSRF=%s" % (self.WFId, self.CSRF), method="post",
            params=params,
            cookies=self.COOKIES)

    def getShareUrl(self, initiateId):
        return self.request(
            "https://api.uyiban.com/workFlow/c/work/share?InitiateId=%s&CSRF=%s" % (initiateId, self.CSRF),
            cookies=self.COOKIES)


yb = YiBan(ACCOUNT, PASSWD)
