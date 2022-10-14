import data


def prompt_for_action1():
    """提示功能菜单1。返回用户输入选择"""
    while True:
        print('----欢迎来到你帮我助平台----')
        print('| 1: 登录')
        print('| 2: 注册')
        print('| 0: 退出平台')
        print('------------------------')

        choice = input('请选择功能菜单(0-2):')
        if choice == '0':
            return 'QUIT'
        elif choice == '1':
            return 'LOG_IN'
        elif choice == '2':
            return 'SIGN_IN'
        else:
            print("请您输入0-2间的一个整数，选择操作")
            continue


def prompt_for_action2():
    """提示功能菜单2。返回用户输入选择"""
    while True:
        print('-------你帮我助平台-------')
        print('| 1: 添加物品')
        print('| 2: 删除物品')
        print('| 3: 我的物品')
        print('| 4: 平台物品列表')
        print('| 5: 查找物品')
        print('| 0: 退出登录')
        print('------------------------')

        choice = input('请选择功能菜单(0-5):')
        if choice == '0':
            return 'LOG_OUT'
        elif choice == '1':
            return 'ADD_ITEMS'
        elif choice == '2':
            return 'DELETE_ITEMS'
        elif choice == '3':
            return 'VIEW_MY_ITEMS'
        elif choice == '4':
            return 'VIEW_ALL_ITEMS'
        elif choice == '5':
            return 'SEARCH_ITEMS'
        else:
            print("请您输入0-5间的一个整数，选择操作")
            continue


"""
用户信息的处理：登录
登陆时，需输入uid, 不存在时报错
    存在时，输入pswd, 错误时报错，正确时继续
"""


def prompt_for_old_sku_uid():
    while True:
        sku_uid = input("请输入您的账号（手机号码）:")
        if sku_uid not in data.get_users():
            print("该账号不存在")
            while True:
                print('-------请选择-------')
                print('| 1: 注册')
                print('| 2: 重新输入账号')
                print('| 0: 退出平台')
                print('-------------------')
                choice = input('请选择功能菜单(0-2):')
                if choice == '1':
                    return 'SIGN IN'
                elif choice == '0':
                    return 'QUIT'
                elif choice == '2':
                    break
                else:
                    print("请您输入0-2间的一个整数，选择操作")
                    continue
        # 当输入账号正确时
        else:
            return sku_uid


def prompt_for_old_sku_pswd(sku_uid):

    uinfo = data.get_users()[sku_uid]
    pswd = uinfo[0]
    # name = uinfo [1]
    while True:
        sku_pswd = input('请输入登录密码:')
        # 密码输入错误时
        if sku_pswd != pswd:
            print("密码输入错误")
            while True:
                print('-------请选择-------')
                print('| 1: 注册')
                print('| 2: 重新输入密码')
                print('| 0: 退出平台')
                print('-------------------')
                choice = input('请选择功能菜单(0-2):')
                if choice == '1':
                    return 'SIGN_IN'
                elif choice == '2':
                    break
                elif choice == '0':
                    return 'QUIT'
                else:
                    print("请您输入0-2间的一个整数，选择操作")
                    continue
        # 密码输入正确时
        else:
            return uinfo


"""
用户信息的处理：注册
注册时，需输入uid, 存在时报错
    不存在时，输入pswd, 错误时报错，正确时继续
    输入 uname
"""


def prompt_for_new_sku_uid():
    """提示用户输入新的账号sku_uid并返回新账号uid"""
    while True:
        sku_uid = input("请输入您的手机号码作为您的账号:")
        if sku_uid == "":
            print("请勿输入空值")
            continue
        elif sku_uid in data.get_users():
            print("该账号已经存在请重新输入")
        else:
            return sku_uid


def prompt_for_new_pswd():
    """提示账号注册成功的用户输入密码sku_pswd，并返回密码"""
    while True:
        sku_pswd = input("请输入您的密码:")
        if sku_pswd == "":
            print("请勿输入空值")
            continue
        else:
            return sku_pswd


def prompt_for_new_uname():
    """提示账号注册成功的用户输入密码sku_pswd，并返回密码"""
    while True:
        sku_uname = input("请输入您的用户名:")
        if sku_uname == "":
            print("请勿输入空值")
            continue
        else:
            return sku_uname


"""
物品信息的处理：
成功登陆后
    查看物品，需输入id, 返回不存在或返回有效ID
    添加物品，需输入ID，已存在重新输入，否则返回新ID
            继续添加 type, name, num, remark 等信息
    存在时，输入pswd, 错误时报错，正确时继续
"""


def prompt_for_old_sku_id():
    """提示用户输入有效的产品sku_id并返回有效产品ID, 或者返回None"""
    while True:
        sku_id = input("请输入产品ID(整数):")
        if sku_id == "":
            print("请不要输入空值")
            return 'FAIL'
        elif sku_id not in data.get_items():
            print("该物品编号不存在")
            return 'FAIL'
        else:
            return sku_id


# 按物品名称查找
def search_by_name():
    """输入物品名称，若为空，返回None,非空，查找，未查找到，返回相应值"""
    while True:
        keyword = input("请输入您查找物品的名称:")
        if keyword == "":
            print("请不要输入空值")
            return 'FAIL'
        else:
            items = data.get_items()
            users = data.get_users()
            count = 0
            for id in items:
                if keyword in items[id][1]:
                    count = count+1
                    if count == 1:
                        print('物品编号', '物品种类', '物品名称', '物品份数', '备注', '拥有人昵称', '拥有人联系方式')
                    print(id, items[id][0], items[id][1], items[id][2], items[id][3], users[items[id][4]][1], items[id][4])
        if count == 0:
            print("您查找的物品名称不存在")
            return 'FAIL'
        else:
            return 'DONE'


# 查找自己的物品
def search_my_items(sku_uid):
    items = data.get_items()
    count = 0
    myIDlist = []
    for id in items:
        if sku_uid == items[id][-1]:
            count = count+1
            myIDlist.append(id)
            if count == 1:
                print('-------您的物品有-------')
                print('物品编号', '物品种类', '物品名称', '物品份数', '备注')
            print(id, items[id][0], items[id][1], items[id][2], items[id][3])
    if count == 0:
        print('您在你帮我助平台没有物品')
        return 'NO_ITEMS'
    else:
        print('------------------')
        return myIDlist


# 查看全部物品
def VIEW_ALL_ITEMS():
    items = data.get_items()
    if len(items) == 0:
        print('平台暂无物品')
        return 'EMPTY'
    else:
        print('物品编号', '物品种类', '物品名称', '物品份数', '备注', '拥有人昵称', '拥有人联系方式')
        users = data.get_users()
        for id in items:
            print(id, items[id][0], items[id][1], items[id][2], items[id][3], users[items[id][4]][1], items[id][4])



# add item_id
def prompt_for_new_sku_id():
    """提示用户输入新的产品sku_id并返回新产品ID, 或者返回None"""
    while True:
        sku_id = input("请输入新的产品ID:")
        if sku_id == "":
            print("请勿输入空值")
        elif sku_id in data.get_items():
            print("该产品已经存在，请重新输入")
        else:
            return sku_id


# add item 具体信息
def prompt_for_sku_type():
    """提示用户输入产品名称sku_name并返回产品名称，或者返回None"""
    while True:
        print('----请选择所添加物品的类型----')
        print('| 1: 食品')
        print('| 2: 洗漱用品')
        print('| 3: 其他')
        choice = input("请选择功能菜单(1-3):")
        if choice == '1':
            return '食品'
        elif choice == '2':
            return '洗漱用品'
        elif choice == '3':
            return '其他'
        else:
            print("请您输入0-2间的一个整数，选择类型")
            continue


def prompt_for_sku_name():
    """提示用户输入产品名称sku_name并返回产品名称，或者返回None"""
    while True:
        sku_name = input("请输入物品名称:")
        if sku_name == "":
            print("请勿输入空值")
        else:
            return sku_name


def prompt_for_sku_num():
    """提示用户输入产品名称sku_num并返回产品名称，或者返回None"""
    while True:
        sku_num = input("请输入物品份数(输入整数):")
        if sku_num == "":
            print("请勿输入空值")
        else:
            return int(sku_num,10)


def prompt_for_sku_remark():
    """提示用户输入产品备注sku_remark并返回产品名称，或者返回None"""
    while True:
        sku_remark = input("请输入物品备注:")
        if sku_remark == "":
            sku_remark = "无备注"
            return sku_remark
        else:
            return sku_remark


# main 中会使用到的函数列表
def LOG_IN():
    """登录"""
    res1 = prompt_for_old_sku_uid()
    if res1 == 'SIGN IN':
        return res1
    elif res1 == 'QUIT':
        return res1
    else:
        sku_uid = res1
        res2 = prompt_for_old_sku_pswd(sku_uid)
        if res2 == 'SIGN IN':
            return res2
        elif res2 == 'QUIT':
            return res2
        else:
            print('------注册成功------')
            print('欢迎你，' + res2[1] + '!')
            print('------------------')
            userinfo = [sku_uid, res2[0], res2[1]]
            return userinfo


def SIGN_IN():
    """注册"""
    uid = prompt_for_new_sku_uid()
    pswd = prompt_for_new_pswd()
    uname = prompt_for_new_uname()
    data.add_users(uid, pswd, uname)
    print('------注册成功------')
    print('欢迎你，'+uname+'!')
    print('------------------')
    userinfo = [uid, pswd, uname]
    return userinfo


def VIEW_MY_ITEMS(sku_uid):
    """查看我的物品"""
    search_my_items(sku_uid)


def ADD_ITEMS(uid):
    # 添加成功后返回 QUIT ADDING
    while True:
        sku_id = prompt_for_new_sku_id()
        sku_type = prompt_for_sku_type()
        sku_name = prompt_for_sku_name()
        sku_num = prompt_for_sku_num()
        sku_remark = prompt_for_sku_remark()
        data.add_items(sku_id, sku_type, sku_name, sku_num, sku_remark, uid)
        print("您已成功添加物品")
        VIEW_MY_ITEMS(uid)
        while True:
            print('----是否继续添加物品----')
            print('| 1: 继续添加物品')
            print('| 0: 退出添加物品')
            print('---------------------')
            choice = input('请选择功能菜单(0-1):')
            if choice == '0':
                return 'QUIT ADDING'
            elif choice == '1':
                break
            else:
                print("请您输入0-1间的一个整数，选择操作")
                continue

def DELETE_ITEMS(uid):
    flag1 = True
    while True:
        res1 = search_my_items(uid)
        # 无物品可删除时，直接退出本操作并返回 NO_ITEMS
        if res1 == 'NO_ITEMS':
            print("您无法删除物品")
            return res1
        # 有物品可删除时，删除结束、不选择删除，均返回 QUIT DELETING
        else:
            print('----请选择您是否要(继续)删除物品----')
            print('| 0: 退出删除物品')
            print('| 1: 继续删除物品')
            print('-------------------------------')
            choice = input('请选择功能菜单(0-1):')
            # 不选择继续删除物品
            if choice == '0':
                return 'QUIT DELETING'
            elif choice != '1':
                print("请您输入0-1间的一个整数，选择操作")
                continue
            # 选择继续删除物品
            else:
                flag1 = True
                IDlist = res1
                while flag1:
                    sku_id = input('请输入您想要删除商品的编号:')
                    if sku_id not in IDlist:
                        print('您输入的物品编号不存在')
                        continue
                    else:
                        while flag1:
                            sku_num = input('请输入您想要删除该物品的数目:')
                            res2 = data.remove_item(sku_id, sku_num)
                            if res2 == 'DELETE FAULT':
                                print('您输入的数目超过该物品原有数目，请重新输入')
                                continue
                            else:
                                print('删除成功')
                                flag1 = False
                                break


def ID_SEARCH():
    while True:
        res = prompt_for_old_sku_id()
        if res == 'FAIL':
            while True:
                print('---请选择是否继续查找---')
                print('| 0: 退出物品编号查找')
                print('| 1: 继续物品编号查找')
                print('--------------------')
                choice1 = input('请选择功能菜单(0-1):')
                if choice1 == '0':
                    return 'QUIT ID SEARCHING'
                elif choice1 == '1':
                    break
                else:
                    print("请您输入0-1间的一个整数，选择操作")
                    continue

        else:
            sku_id = res
            print('查找结果如下：')
            print('物品编号', '物品种类', '物品名称', '物品份数', '备注', '拥有人昵称', '拥有人联系方式')
            print(sku_id, data._items[sku_id][0], data._items[sku_id][1], data._items[sku_id][2], data._items[sku_id][3], data._users[data._items[sku_id][4]][1], data._items[sku_id][4])
            while True:
                print('---请选择是否继续查找---')
                print('| 0: 退出物品编号查找')
                print('| 1: 继续物品编号查找')
                print('--------------------')
                choice2 = input('请选择功能菜单(0-1):')
                if choice2 == '0':
                    return 'QUIT ID SEARCHING'
                elif choice2 == '1':
                    break
                else:
                    print("请您输入0-1间的一个整数，选择操作")
                    continue


def NAME_SEARCH():
    while True:
        res = search_by_name()
        print('---请选择是否继续查找---')
        print('| 0: 退出物品名称查找')
        print('| 1: 继续物品名称查找')
        print('--------------------')
        choice = input('请选择功能菜单(0-1):')
        if choice == '0':
            return 'QUIT NAME SEARCHING'
        elif choice == '1':
            continue
        else:
            print("请您输入0-1间的一个整数，选择操作")


def SEARCH_ITEMS():
    while True:
        print('------请选择查找类型------')
        print('| 1: 物品编号查找')
        print('| 2: 物品名称查找')
        print('| 0：退出查找')
        print('--------------------')
        choice = input('请选择功能菜单(0-2):')
        if choice == '0':
            return 'QUIT SEARCHING'
        elif choice == '1':
            res1 = ID_SEARCH()
        elif choice == '2':
            res2 = NAME_SEARCH()
        else:
            print("请您输入0-2间的一个整数，选择操作")
