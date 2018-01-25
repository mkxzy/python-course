# -*- coding: utf-8 -*-
#!/usr/bin/env python

#第一题：判断是否是升序
def is_sorted(myList):
    return myList == sorted(myList)

myList = [3, 4, 12, 2]
myList2 = [1, 2, 3, 4]
print(is_sorted(myList))
print(is_sorted(myList2))


#第二题
def is_huiwen(s):
    reverse = s[::-1]
    return s == reverse

print(is_huiwen("abc"))
print(is_huiwen("abcba"))
