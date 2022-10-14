import os
import json

# 全局变量
_items = {}   # 保存物品库存的列表
_users = {}   # 保存用户信息的列表


def init():
    """从磁盘JSON格式文件中读取数据"""
    global _items, _users
    if os.path.exists("items.json"):
        f = open("items.json", "r", encoding='utf-8')
        _items = json.loads(f.read())
        f.close()
    if os.path.exists("users.json"):
        f = open("users.json", "r", encoding='utf-8')
        _users = json.loads(f.read())
        f.close()


def _save_items():
    """把物品信息数据_items以JSON格式保存到磁盘"""
    global _items
    f = open("items.json", "w", encoding='utf-8')
    f.write(json.dumps(_items, ensure_ascii=False))
    f.close()


def _save_users():
    """把用户信息数据_users以JSON格式保存到磁盘"""
    global _users
    f = open("users.json", "w", encoding='utf-8')
    f.write(json.dumps(_users, ensure_ascii=False))
    f.close()
    # print('_save_users已执行_users为：')
    # print(_users)


def get_items():
    """返回物品信息"""
    global _items
    return _items


def get_users():
    """返回用户信息"""
    global _users
    # print('_users is:')
    # print(_users)
    return _users


def add_items(sku_id, sku_type, sku_name, sku_num, sku_remark, sku_uid):
    """增加一个物品，type,id,name"""
    global _items
    sku_info = [sku_type, sku_name, sku_num, sku_remark, sku_uid]
    _items[sku_id] = sku_info
    _save_items()


def add_users(sku_uid, sku_pswd, sku_uname):
    """增加一个用户， uid,pswd,name"""
    global _users
    sku_uinfo = [sku_pswd, sku_uname]
    _users[sku_uid] = sku_uinfo
    # print('add_users已执行')
    _save_users()


def remove_item(sku_id, sku_num):
    """出库一个物品"""
    global _items
    num = _items[sku_id][2]
    print('您有该物品', num, '份')
    # print('num 的类型为', type(num))
    # print('sku_num的类型为', type(sku_num))
    sku_num = int(sku_num, 10)
    if sku_num > num:
        return 'DELETE FAULT'
    elif sku_num < num:
        remain = num-sku_num
        _items[sku_id][2] = num-sku_num
        _save_items()
        return remain
    else:
        del _items[sku_id]
        _save_items()
        return 0
