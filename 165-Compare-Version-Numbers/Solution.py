# -*- coding:utf-8 -*-

import sys


def comp_version(version1, version2):
    v1_num_list = [int(num) for num in version1.split('.')]
    v2_num_list = [int(num) for num in version2.split('.')]
    v1_pos_list = [pos for pos in range(len(v1_num_list), 0, -1)]
    v2_pos_list = [pos for pos in range(len(v2_num_list), 0, -1)]
    v1_sum = sum([num * (10 ** pos) for num, pos in zip(v1_num_list, v1_pos_list)])
    v2_sum = sum([num * (10 ** pos) for num, pos in zip(v2_num_list, v2_pos_list)])
    print('v1_sum = {}, v2_sum = {}.'.format(v1_sum, v2_sum))
    if v1_sum > v2_sum:
        return 1
    if v1_sum == v2_sum:
        return 0
    if v1_sum < v2_sum:
        return -1


if __name__ == '__main__':
    v1 = sys.argv[1]
    v2 = sys.argv[2]
    print(comp_version(v1, v2))
