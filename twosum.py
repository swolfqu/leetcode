#!/usr/bin/env python
# -*- coding:utf8 -*-
#
# Author  :  swolf.qu
# E-mail  :  swolf.qu@gmail.com
# Date    :  2018-04-13 18:17:47
"""
    https://leetcode.com/problems/two-sum/description/

    Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

    You may assume that each input would have exactly one solution, and you
may not use the same element twice.


Example:
ven nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum(nums, target):
    nmap = {x: nums.index(x) for x in nums}
    for value, index in nmap.items():
        another = target - value
        if another in nmap:
            return [index, nmap[another]]
    return None


if __name__ == "__main__":
    list_ = [1, 2, 3, 5, 4, 8]
    t = 7
    print("list: {}".format(list_))
    print("target: {}".format(t))
    ret = two_sum(list_, t)
    print("result: {}".format(ret))
