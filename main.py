# -*- coding = utf-8 -*-
# @Time: 2022/02/17 17:32
# @Author: 123
# @File: main.py
# @Software: VS Code
# @Software: PyCharm
# @Version: 0.3
# @Function: 实现家庭药品管理


# import
import json
import random


# class
class Afile:  # 文件类

    def d_save(self: str, data):  # 保存文件或是创造文件。

        file_save = open(self, "w")  # 打开XXX文件，如果没有就创建一个。
        file_save.write(data)  # 把page_data_download内容写入。
        file_save.close()  # 关闭文件。

    def d_read(self: str):  # 读取文件

        file_read = open(self, "r")  # 打开XXXX文件
        file_data = file_read.read()  # 读取文件内容
        file_read.close()  # 关闭文件
        return file_data  # 返回文件内容


class Bfile:  # 文件类

    def save_json(self: str, data):  # 保存文件或是创造文件。

        data_json = json.dumps(data)  # 将data转换为json格式
        Afile.d_save(self, data_json)  # 保存文件

    def read_json(self: str):  # 读取文件

        data_json = Afile.d_read(self)  # 读取文件
        file_data: dict = json.loads(data_json)  # 将文件内容转换为json格式
        return file_data  # 返回文件内容


# def
def drug_info_uid():  # 生成唯一id

    drug_uid: str  # 初始化d_uid
    str_abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"          # 定义字母ABC
    list_abc = list(str_abc)                        # 将字母ABC转换为列表

    random_drug_uid = random.randint(0, 25)         # 生成0-25的随机数
    drug_uid = list_abc[random_drug_uid]            # 将生成的随机数转换为字母

    for i in range(4):
        random_drug_uid = random.randint(0, 25)     # 生成0-25的随机数
        wi_drug_uid = list_abc[random_drug_uid]     # 将生成的随机数转换为字母
        drug_uid += wi_drug_uid                     # 将生成的随机数乘以10的i次方，然后加到d_uid上

    return drug_uid  # 返回 drug_uid


def drug_info_add():  # 添加药品

    drug_pharmacy_add_d: dict = Bfile.read_json("pharmacy.hpms")  # 读取drug_info.hpms文件
    drug_add_pre: dict = Bfile.read_json("drug_info.hpms")  # 读取drug_info.hpms文件
    drug_daily_set_d: dict = Bfile.read_json("daily_set.hpms")  # 读取drug_info.hpms文件

    is_random_drug_uid = input("是否随机生成药品uid？(y/n)")  # 输入是否随机生成药品uid

    uid_pre = "AAA00"

    if is_random_drug_uid == "y":  # 如果输入是y
        # uid_pre = drug_info_uid()                   # 调用drug_info_uid函数，生成药品uid
        is_not_sim: bool = True  # 初始化is_not_sim

        while is_not_sim:  # 检测是否重复，如果重复就重新生成。
            uid_pre_pre = drug_info_uid()  # 调用drug_info_uid函数，生成药品uid

            if uid_pre_pre not in drug_add_pre:  # 如果生成的药品uid不在drug_add_pre中
                is_not_sim = False  # 将is_not_sim设置为False
                uid_pre = uid_pre_pre

    elif is_random_drug_uid == "n":  # 如果输入是n
        uid_pre = input("请输入药品信息uid:")

    drug_add_pre[uid_pre] = {"trade_name": "", "generic_name": "", "manufacturer": "", "specification": 0,
                            "tablets_per_package": 0, "packages_pre_box": 0, "is_rx": "", "indications": "",
                            "note": ""}

    drug_pharmacy_add_d[uid_pre] = {"inbound": 0, "outbound": 0}

    drug_daily_set_d[uid_pre] = {"daily_set": 0,}

    drug_add_pre[uid_pre]["trade_name"] = input("请输入药品名称(str):")
    drug_add_pre[uid_pre]["generic_name"] = input("请输入药品通用名(str):")
    drug_add_pre[uid_pre]["manufacturer"] = input("请输入药品生产厂(str):")
    drug_add_pre[uid_pre]["specification"] = int(input("请输入单片药品规格(int,mg):"))
    drug_add_pre[uid_pre]["tablets_per_package"] = int(input("请输入药品每板药片数(int):"))
    drug_add_pre[uid_pre]["packages_pre_box"] = int(input("请输入药品每盒板数(int):"))
    drug_add_pre[uid_pre]["is_rx"] = input("请输入管制情况(str):")
    drug_add_pre[uid_pre]["indications"] = input("请输入适应症(str):")
    drug_add_pre[uid_pre]["note"] = input("请输入备注(str):")

    Bfile.save_json("drug_info.hpms", drug_add_pre)  # 将drug_add_pre存入drug_info.hpms文件
    Bfile.save_json("pharmacy.hpms", drug_pharmacy_add_d)  # 将drug_pharmacy_add存入drug_info.hpms文件
    Bfile.save_json("daily_set.hpms", drug_daily_set_d)  # 将drug_daily_set存入drug_info.hpms文件

    drug_info_print_all()


def drug_info_print_all():  # 打印所有药品信息

    dpa_tag = Bfile.read_json("drug_info.hpms")  # 读取drug_info.hpms文件
    dpa_p_tag = Bfile.read_json("pharmacy.hpms")  # 读取pharmacy.hpms文件
    dpa_ds_tag = Bfile.read_json("daily_set.hpms")  # 读取daily_set.hpms文件

    for i in dpa_tag:  # 循环打印所有药品信息

        tcc:int = 0 
        pcc:int = 0
        ucc:int = 0

        print("药品代号:", i, end="\t")  # 打印药品代号
        print("商品名:", dpa_tag[i]["trade_name"], end="\t")  # 打印商品名
        print("通用名:", dpa_tag[i]["generic_name"], end="\t")  # 打印通用名
        # print("生产厂家:", dpa_tag[i]["manufacturer"], end="\t")
        # print("规格:", dpa_tag[i]["specification"], "毫克",  end="\t")
        # print("每板包含的粒数:", dpa_tag[i]["tablets_per_package"], "粒", end="\t")
        # print("每盒包含的板数:", dpa_tag[i]["packages_pre_box"], "板", end="\t")
        # print("是否为处方药:", dpa_tag[i]["is_rx"], end="\t")
        # print("备注:", dpa_tag[i]["note"])

        tcc = dpa_tag[i]["specification"] * dpa_tag[i]["tablets_per_package"] * dpa_tag[i]["packages_pre_box"]  # 计算总粒数

        if tcc < 1000:  # 如果总粒数小于1000
            print("每盒含量:", tcc, "毫克", end="\t")  # 打印每盒总含量

        else:
            print("每盒总含量:", tcc / 1000, "克", end="\t")  # 打印每盒总含量

        print("适应症:", dpa_tag[i]["indications"], end="\t")  # 打印适应症

        pcc = dpa_p_tag[i]["inbound"] - dpa_p_tag[i]["outbound"]
        
        print("库存量:", pcc , "盒", end="\t")  # 打印库存量

        if dpa_ds_tag[i]["daily_set"] == 0:  # 如果每日零售量不为0
            pass

        else:
            ucc = (tcc * pcc) / dpa_ds_tag[i]["daily_set"]
            print("库存可使用", ucc, "盒")


def drug_info_delete():  # 删除药品

    drug_info_print_all()  # 打印所有药品信息

    drug_delete_pre: dict = Bfile.read_json("drug_info.hpms")  # 读取drug_info.hpms文件

    print("请输入要删除的商品代号：", end="")  # 输入要删除的商品代号
    uid_pre = input()  # 获取输入的商品代号

    if uid_pre in drug_delete_pre:  # 如果输入的商品代号在drug_delete_pre字典中
        del drug_delete_pre[uid_pre]  # 删除药品
        Bfile.save_json("drug_info.hpms", drug_delete_pre)  # 将drug_delete_pre存入drug_info.hpms文件
        drug_info_print_all()

    else:  # 如果输入的商品代号不在drug_delete_pre字典中
        print("没有找到该商品代号，请重新输入")  # 提示没有找到该商品代号
        drug_info_delete()


def user_pick():  # 用户选择

    user_pick_input = input("请选择操作：(1.添加药品 2.删除药品 3.查看药品信息 4. 药品入库 5.药品出库 6.设置每日用量 7.退出)")
    user_pick_input = int(user_pick_input)  # 将user_pick转换为int类型

    if user_pick_input == 1:
        drug_info_add()

    elif user_pick_input == 2:
        drug_info_delete()

    elif user_pick_input == 3:
        drug_info_print_all()

    elif user_pick_input == 4:
        drug_pharmacy_add()

    elif user_pick_input == 5:
        drug_pharmacy_min()

    elif user_pick_input == 6:
        drug_daily_set()
    elif user_pick_input == 7:
        exit()


def drug_pharmacy_add():
    drug_pharmacy_add_d: dict = Bfile.read_json("pharmacy.hpms")  # 读取drug_info.hpms文件
    drug_info_add_d: dict = Bfile.read_json("drug_info.hpms")  # 读取drug_info.hpms文件

    drug_info_print_all()  # 打印所有药品信息

    print("请输入要入库的药品代号：", end="")  # 输入要添加的药品代号
    uid_pre = input()  # 获取输入的药品代号

    if uid_pre in drug_info_add_d:  # 如果输入的药品代号在drug_pharmacy_add字典中
        print("请输入要入库的药品数量：", end="")  # 输入要添加的药品数量
        drug_pharmacy_add_d[uid_pre]["inbound"] += int(input())  # 将输入的药品数量加入drug_pharmacy_add字典

        Bfile.save_json("pharmacy.hpms", drug_pharmacy_add_d)  # 将drug_pharmacy_add存入drug_info.hpms文件

        drug_info_print_all()

    else:  # 如果输入的药品代号不在drug_pharmacy_add字典中
        print("没有找到该商品代号，请重新输入")  # 提示没有找到该商品代号
        drug_pharmacy_add()


def drug_pharmacy_min():
    drug_pharmacy_min_d: dict = Bfile.read_json("pharmacy.hpms")  # 读取drug_info.hpms文件
    drug_info_add_d: dict = Bfile.read_json("drug_info.hpms")  # 读取drug_info.hpms文件

    drug_info_print_all()  # 打印所有药品信息

    print("请输入要出库的药品代号：", end="")  # 输入要减少的药品代号
    uid_pre = input()  # 获取输入的药品代号

    if uid_pre in drug_info_add_d:  # 如果输入的药品代号在drug_pharmacy_min字典中
        print("请输入要出库的药品数量：", end="")  # 输入要减少的药品数量
        drug_pharmacy_min_d[uid_pre]["outbound"] += int(input())  # 将输入的药品数量加入drug_pharmacy_min字典

        Bfile.save_json("pharmacy.hpms", drug_pharmacy_min_d)  # 将drug_pharmacy_min存入drug_info.hpms文件

        drug_info_print_all()

    else:  # 如果输入的药品代号不在drug_pharmacy_min字典中
        print("没有找到该商品代号，请重新输入")  # 提示没有找到该商品代号
        drug_pharmacy_min()


def drug_daily_set():  # 每日设置

    drug_info_print_all()

    drug_daily_set_d: dict = Bfile.read_json("daily_set.hpms")  # 读取drug_info.hpms文件

    print("请输入要设置的药品代号：", end="")  # 输入要设置的药品代号
    uid_pre = input()  # 获取输入的药品代号

    if uid_pre in drug_daily_set_d:  # 如果输入的药品代号在drug_daily_set字典中
        print("请输入每日摄入量：", end="")  # 输入要设置的药品数量
        drug_daily_set_d[uid_pre]["daily_set"] = int(input())  # 将输入的药品数量加入drug_daily_set字典

        Bfile.save_json("daily_set.hpms", drug_daily_set_d)  # 将drug_daily_set存入drug_info.hpms文件

        print("设置成功")

    else:  # 如果输入的药品代号不在drug_daily_set字典中
        print("没有找到该商品代号，请重新输入")  # 提示没有找到该商品代号
        drug_daily_set()



# main
if __name__ == "__main__":

    while True:
        user_pick()
        print("-" * 30)
