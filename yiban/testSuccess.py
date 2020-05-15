from yiban import yb

if __name__ == '__main__':
    if yb.login() is None:
        print("帐号或密码错误")
    result_auth = yb.auth()
    completedList = yb.getCompletedList()
    print("已打卡的任务:")
    print(completedList.get('data')['list'][:3])
    UncompletedList = yb.getUncompletedList()
    print("未打卡的任务:")
    print(UncompletedList.get('data'))
