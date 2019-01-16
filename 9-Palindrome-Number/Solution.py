# -*- coding:utf-8 -*-


class Solution:
    @staticmethod
    def is_palindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        x_str_list = list(str(x))
        x_str_list_reverse = [x_str_list[i] for i in range(len(x_str_list) - 1, 0, -1)]
        for a, b in zip(x_str_list, x_str_list_reverse):
            if a != b:
                return False

        return True


if __name__ == '__main__':
    print(Solution.is_palindrome(121))
    print(Solution.is_palindrome(-121))
    print(Solution.is_palindrome(10))
