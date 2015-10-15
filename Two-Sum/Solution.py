#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def twoSum():
    numbers = []
    numbers = eval(input("Please enter an integer arrary: "))
    target = eval(input("Please enter the target: "))
    for x in numbers:
        for y in numbers:
            if x + y == target:
                index1 = numbers.index(x)
                index2 = numbers.index(y)
                return (index1, index2)

def main():
    index1, index2 = twoSum()
    print("The index1 is", index1+1, ",", "and index2 is", index2+1)

if __name__ == '__main__':
    main()
