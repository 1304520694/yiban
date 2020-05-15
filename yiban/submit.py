import json
import re

from yiban import yb
from yiban.utils import form_data

if __name__ == '__main__':
    if yb.login() is None:
        print("帐号或密码错误")
    result_auth = yb.auth()
    data_url = result_auth["data"].get("Data")
    if data_url is not None:  # 授权过期
        print("授权过期")
        print("访问授权网址")
        result_html = yb.session.get(url=data_url, headers=yb.HEADERS,
                                     cookies={"loginToken": yb.access_token}).text
        re_result = re.findall(r'input type="hidden" id="(.*?)" value="(.*?)"', result_html)
        print("输出待提交post data")
        print(re_result)
        post_data = {"scope": "1,2,3,"}
        for i in re_result:
            post_data[i[0]] = i[1]
        print("进行授权确认")
        usersure_result = yb.session.post(url="https://oauth.yiban.cn/code/usersure",
                                          data=post_data,
                                          headers=yb.HEADERS, cookies={"loginToken": yb.access_token})
        if usersure_result.json()["code"] == "s200":
            print("授权成功！")
        else:
            print("授权失败！")
        print("尝试重新二次登录")
        yb.auth()
    all_task = yb.getUncompletedList()
    if len(all_task["data"]) == 0:
        print("没有待完成的打卡任务")
    for i in all_task["data"]:
        task_detail = yb.getTaskDetail(i["TaskId"])["data"]
        if task_detail["WFId"] != yb.WFId:
            print("表单已更新,得更新程序了")
            exit()
        ex = {"TaskId": task_detail["Id"],
              "title": "任务信息",
              "content": [{"label": "任务名称", "value": task_detail["Title"]},
                          {"label": "发布机构", "value": task_detail["PubOrgName"]},
                          {"label": "发布人", "value": task_detail["PubPersonName"]}]}
        # print(ex)
        submit_result = yb.submit(form_data, json.dumps(ex, ensure_ascii=False))
        if submit_result.get('code') == '0':
            print(ex.get("title") + " 打卡成功")
