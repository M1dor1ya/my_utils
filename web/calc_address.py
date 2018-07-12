# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 10:57
# @Author  : Zcs
# @File    : calc_address.py


def calc_address(ip, mask):
    """
    :param ip: IP地址 Exp: '202.112.14.137'
    :param mask:子网掩码 Exp: '255.255.255.224'
    :return: 网络地址 Exp: '202.112.14.128'
    """
    mask_list = mask.split('.')
    ip_list = ip.split('.')
    mask_bin = ''
    ip_bin = ''
    for i in mask_list:
        mask = bin(int(i))[2:]
        if len(mask) == 8:
            mask_bin = mask_bin + mask  # 子网掩码的二进制
        else:
            for j in range(8 - len(mask)):
                mask_bin = mask_bin + '0'
            mask_bin = mask_bin + mask

    for i in ip_list:
        ip = bin(int(i))[2:]
        if len(ip) == 8:
            ip_bin = ip_bin + ip  # IP地址的二进制
        else:
            for j in range(8 - len(ip)):
                ip_bin = ip_bin + '0'
            ip_bin = ip_bin + ip

    #  num_net = mask_bin.count('1')  # 网络号位数
    #  num_host = 32 - num_net  # 主机号位数
    result = ''  # 存放二进制的网络地址
    for i, j in zip(mask_bin, ip_bin):
        if i == '1' and j == '1':
            result = result + '1'
        else:
            result = result + '0'

    net_address = ''  # 存放十进制网络地址
    for i in range(4):
        if i != 3:
            net_address = net_address + str(int(result[i * 8:8 * (i + 1)], 2)) + '.'
        else:
            net_address = net_address + str(int(result[i * 8:8 * (i + 1)], 2))

    return net_address

if __name__ == '__main__':
    print(calc_address('202.112.14.137', '255.255.255.224'))
