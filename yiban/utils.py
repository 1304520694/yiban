import json

import requests
from yiban import yb

# 提交的基础表单数据
# 经纬度需要到小数点后六位
base_data = {"98ddd090dc2a7f5ac666daa41ef113f4": "XX姓名", "0735cf0a0b2ad4267ea2578da39a923a": "XX班级",
             "801a459c3503b1aebe54aef1540602ce": {"name": "XX地址名", "location": "XX经度(小数点后6位),XX纬度(小数点后6位)",
                                                  "address": "XX详细地址描述"},
             "18ad14fa5b723f437254f4dc8ed92ffc": {"name": "XX地址名", "location": "XX经度(小数点后6位),纬度(小数点后6位)",
                                                  "address": "XX详细地址描述"}, "1988af9823d6a9ad01e3f673106c6d59": "XX省",
             "62b5cbd69c8efddec63df6aa676cade2": "XX市", "5ca8c285360b059616fd9b706e06303e": "XX县（区）",
             "3cdc6f6669f7bafddbbdeaf04beca8c5": "XX体温", "88e831eb1f444f6447c7022c518e7de7": "无",
             "5e50acc9a4fd45fc578d7682ee8799a0": "无", "7d4a4f933e87ad84a323b9f893c23937": "无",
             "06e2393cb99c5324fbabd3561c32c723": "无", "9352c8ff9850b800eb2fa2453b65d846": "否",
             "eca39739507c9309e1f562b57541b3be": "否", "721478664a42a8c42563476e2452ff81": "否",
             "1f1b87c54d448f5eafc70c617f6ef357": "健康", "3a0e2ada22349c8b24c1ecd5e860f8e1": "健康",
             "e65b3d45a5a2298bac49ee67faf2e054": "否", "1f9d8ca37058562e088494e7cd07b372": "否",
             "4ac0e4c37925e2f307d4322aa02b400f": "否"}


def parse_data(url):
    """
    :param url
    将分享链接的数据解析出来生成表单数据字典
    """
    initiateId = url.split('=')[-1]
    # print(initiateId)
    share_url = 'https://api.uyiban.com/workFlow/c/share/index?InitiateId={}&CSRF={}'.format(initiateId, yb.CSRF)
    share_res = yb.request(share_url, cookies=yb.COOKIES)
    save_data_url = share_res.get('data')['uri']
    save_data_res = requests.get(save_data_url)
    save_data = save_data_res.json()
    FormDataJson = save_data.get('Initiate')['FormDataJson']
    dict_form = {i.get('id'): i.get("value") for i in FormDataJson}
    return dict_form


def get_from_data(url):
    # 将表单数据字典提取成需要填充表单的json
    dict_data = parse_data(url)
    form_data = {i: dict_data[i] for i in base_data.keys()}
    return json.dumps(form_data)


# 近几天的一次易班打卡登记表的转发审批表单的链接
# 需要替换此链接
url = 'https://app.uyiban.com/workflow/client/#/share?initiateId=xxxxxxxxxxxxxxxxxxxxxx'

# 最终提交的表单数据
form_data = get_from_data(url)

if __name__ == '__main__':
    # 打印表单提取的数据
    print(json.loads(form_data))
