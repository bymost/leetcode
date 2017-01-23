#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: bymost
# email: bymost@yeah.net
# Bytime: @ 2017-01-13 14:59:34

def addTwoNum(l1,l2):
    split = ' -> '
    l1 = str.replace(l1, split, '')[::-1]
    l2 = str.replace(l2, split, '')[::-1]
    if l1.isalnum and l2.isalnum:
        l3 = str(int(l1) + int(l2))[::-1]
        print(split.join(l3))

if __name__ == '__main__':
    addTwoNum('2 -> 4 -> 3','5 -> 6 -> 4')
