#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: bymost
# email: bymost@yeah.net
# Bytime: @ 2017-05-22 20:13:39

import hashlib,sys

def checkMD5():
    md5 = hashlib.md5(open(sys.argv[2], 'rb').read()).hexdigest()
    print(md5)
    return md5

def checkSHA1():
    sha1 = hashlib.sha1(open(sys.argv[2], 'rb').read()).hexdigest()
    print(sha1)
    return sha1

def checkSHA256():
    sha256 = hashlib.sha256(open(sys.argv[2], 'rb').read()).hexdigest()
    print(sha256)
    return sha256

def checkSHA512():
    sha512 = hashlib.sha512(open(sys.argv[2], 'rb').read()).hexdigest()
    print(sha512)
    return sha512

if __name__ == '__main__':
    hashType = sys.argv[1]
    if hashType == 'md5':
       newHash = checkMD5()
    elif hashType == 'sha1':
       newHash = checkSHA1()
    elif hashType == 'sha256':
       newHash = checkSHA256()
    elif hashType == 'sha512':
      newHash = checkSHA512()
    
    if len(sys.argv) >= 4:
        print(newHash == sys.argv[3])

