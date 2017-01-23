#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: bymost
# email: bymost@yeah.net
# Bytime: @ 2017-01-13 11:10:29

def romanToInt(s):
    roman = s.upper()
    ro = {}
    ro['I'] = 1
    ro['V'] = 5 
    ro['X'] = 10
    ro['L'] = 50
    ro['C'] = 100
    ro['D'] = 500
    ro['M'] = 1000
    sum = ro[roman[len(roman) - 1]]
    for x in range(len(roman) - 1, 0, -1):
        print(roman[x])
        if ro[roman[x]] > ro[roman[x-1]]:
            sum = sum - ro[roman[x - 1]]
        else:
            sum = sum + ro[roman[x - 1]]
    print(sum)
    return sum


if __name__ == '__main__':
    romanToInt("MCMXCVI")
