# -*- coding:utf-8 -*-


class Solution:
    @staticmethod
    def reverse_int(number):
        if number == 0:
            return 0

        if number > 0:
            num_str_list = list(str(number))
            num_str_list.reverse()
            return int(''.join(num_str_list))

        if number < 0:
            num_str_list = list(str(abs(number)))
            num_str_list.reverse()
            return 0 - int(''.join(num_str_list))


if __name__ == '__main__':
    print(Solution.reverse_int(123))
    print(Solution.reverse_int(-12566))
    print(Solution.reverse_int(120))
