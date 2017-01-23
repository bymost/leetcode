#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: bymost
# email: bymost@yeah.net
# Bytime: @ 2017-01-12 16:47:19

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype = {}
        for x in range(0, len(nums)):
            if target - nums[x] in rtype:
                return ([rtype[target - nums[x]], x ])
            rtype[nums[x]] = x 
            '''
            for y in range(x + 1, len(nums)):
                print('x = %d, y = %d' %(x, y)) 
                if nums[x] + nums[y] == target:
                    rtype.append(x)
                    rtype.append(y)
                    nums.extend
                    print(rtype)
                    #return rtype
            '''
if __name__ == '__main__':
    sol = Solution()
    sol.twoSum([3, 2, 4], 6)
