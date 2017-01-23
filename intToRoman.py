#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: bymost
# email: bymost@yeah.net
# Bytime: @ 2017-01-13 14:09:17

def intToRoman(s):
    ro = {0:'', 1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    roman = ''
    for i in range(1,len(str(s)) + 1):
        temp = s % 10
        if (temp % 5) == 4:
            roman = ro[pow(10,i-1)] + ro[(int(temp / 5) + 1) * 5 * pow(10, i-1)] + roman
        else:
            roman = ro[int(temp / 5) * 5 * pow(10, i -1)] + (temp % 5) * ro[pow(10,i-1)] + roman
        s = int(s / 10)
    print(roman.strip())

if __name__ == '__main__':
    for i in range(3999):
       intToRoman(i)
