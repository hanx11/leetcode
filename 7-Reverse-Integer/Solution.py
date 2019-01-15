# -*- coding:utf-8 -*-


class Solution:
    @staticmethod
    def reverse(number):
        """
        :type number: int
        :rtype: int
        """
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
    print(Solution.reverse(123))
    print(Solution.reverse(-12566))
    print(Solution.reverse(120))
